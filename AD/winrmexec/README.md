# winrmexec
Impacket-based WinRM client with support for NTLM and Kerberos authentication over HTTP and HTTPS in the spirit of `smbexec.py` and `psexec.py`. You can run a single command with `-X 'whoami /all'`, or use the "shell" mode to issue multiple commands. It depends on `impacket`, `requests`, and optionally `prompt_toolkit` python packages. If `prompt_toolkit` is not installed on your system, it defaults to the built-in `readline` module.

(Experimental) `evil_winrmexec.py` adds a custom shell to replicate some of the features of `evil-winrm` like AMSI bypasses ability to download and upload files, run scripts/.NET executables from remote http, etc.

## Examples:
In the following examples impacket's "target" format will be used: `[[domain/]username[:password]@]<target>`.

### NTLM:
```bash
$ winrmexec.py 'box.htb/username:password@dc.box.htb'
$ winrmexec.py 'username:password@dc.box.htb'
$ winrmexec.py -hashes 'LM:NT' 'username@dc.box.htb'
$ winrmexec.py -hashes ':NT' 'username@dc.box.htb'
```
If `password` or `-hashes` are not specified, it will prompt for password:
```bash
$ winrmexec.py username@dc.box.htb
Password:
```

If `-target-ip` is specified, `target` will be ignored (still needs `@` after `username[:password]`)
```bash
$ winrmexec.py -target-ip '10.10.11.xx' 'username:password@whatever'
$ winrmexec.py -target-ip '10.10.11.xx' 'username:password@'
```

If `-target-ip` is not specified, then `-target-ip=target`. If `-ssl` is specified, it will use 5986 port and https:
```bash
$ winrmexec.py -ssl 'username:password@dc01.box.htb'
```
If `-port` is specified, it will use that instead of 5985. If `-ssl` is also specified it will use https:
```bash
$ winrmexec.py -ssl -port 8443 'username:password@dc01.box.htb'
```
If `-url` is specified, `target`, `-target-ip` and `-port` will be ignored:
```bash
$ winrmexec.py -url 'http://dc.box.htb:8888/endpoint' 'username:password@whatever'
```
If `-url` is not specified it will be constructed as `http(s)://target_ip:port/wsman`

### Kerberos:
```bash
$ winrmexec.py -k 'box.htb/username:password@dc.box.htb'
$ winrmexec.py -k -hashes 'LM:NT' 'box.htb/username@dc.box.htb'
$ winrmexec.py -k -aesKey 'AESHEX' 'box.htb/username@dc.box.htb'
```

If `KRB5CCACHE` is set as env variable, it will use `domain` and `username` from there:
```bash
$ KRB5CCNAME=ticket.ccache winrmexec.py -k -no-pass 'dc.box.htb'
```
It doesn't hurt if you also specify `domain/username`, but they will be ignored:
```bash
$ KRB5CCNAME=ticket.ccache winrmexec.py -k -no-pass 'box.htb/username@dc.box.htb'
```
If `target` does not resolve to an ip, you have to specify `-target-ip`:
```bash
$ winrmexec.py -k -no-pass -target-ip '10.10.11.xx' 'box.htb/username:password@DC'
$ KRB5CCNAME=ticket.ccache winrmexec.py -k -no-pass -target-ip '10.10.11.xx' DC
```
For Kerbros it is important that `target` is a host or FQDN, as it will be used to construct SPN as `HTTP/{target}@{domain}`. Or you can specify `-spn` yourself, in which case `target` will be ignored (or used only as `-target-ip`):
```bash
$ winrmexec.py -k -spn 'http/dc' 'box.htb/username:password@dc.box.htb'
$ winrmexec.py -k -target-ip '10.10.11.xx' -spn 'http/dc' box.htb/username:password@whatever
$ KRB5CCNAME=ticket.ccache winrmexec.py -k -no-pass -target-ip '10.10.11.xx' -spn 'http/dc' 'whatever'
```
If you have a TGS for SPN other than HTTP (for example CIFS) it still works (at least from what i tried). If you have a TGT, then it will request TGS for `HTTP/target@domain` (or your custom `-spn`)

If `-dc-ip` is not specified then `-dc-ip=domain`. For `-url` / `-port` / `-ssl` same rules apply as for NTLM.

### Basic Auth:
Not likely to be enabled, but if it is, same rules as for NTLM (but no `-hashes`)
```bash
winrmexec.py -basic username:password@dc.box.htb
winrmexec.py -basic -target-ip '10.10.11.xx' 'username:password@whatever'
winrmexec.py -basic -target-ip '10.10.11.xx' -ssl 'username:password@whatever'
winrmexec.py -basic -url 'http://10.10.11.xx/endpoint' 'username:password@whatever'
```

### Client Certificate:
You need to specify a certificate and a corresponding private key:
```console
winrmexec.py -cert-pem 'user.pem' -cert-key 'user.key' 'dc01.box.htb'
```

### CredSSP:
Authenticate using CredSSP:
```bash
$ winrmexec.py 'box.htb/username:password@dc.box.htb' -credssp
$ winrmexec.py 'username:password@dc.box.htb' -credssp
```
If `-k` is specified it will use Kerberos during SPNEGO phase, but here plaintext credentials
are needed anyway. Using `KRB5CCNAME` is not really usefull unless you can't connect to
kerberos service on `:88` port but somehow got TGS  anyway:
```bash
$ winrmexec.py 'box.htb/username:password@dc.box.htb' -k -credssp
```

# Setup WinRM for testing

I have two test boxes here, one Windows Server 2022 running as a DC in AD environment and
a standalone Windows 10 machine. Domain for AD is `test.lab` and domain controller is `DC01`.
Either way start WinRM with
```console
PS> winrm quickconfig
```
this should also set up firewall rule for 5985 port, but check just in case as this sometimes
fails if your network is set to public. By default NTLM auth will be enabled for both and
Kerberos for `DC01`:
```console
PS> Get-ChildItem WSMan:\localhost\Service\Auth
Type            Name                           SourceOfValue   Value
----            ----                           -------------   -----
System.String   Basic                                          false
System.String   Kerberos                                       true
System.String   Negotiate                                      true
System.String   Certificate                                    false
System.String   CredSSP                                        false
System.String   CbtHardeningLevel                              Relaxed
```
Windows 10:
```console
PS> Get-ChildItem WSMan:\localhost\Service\Auth
Type            Name                           SourceOfValue   Value
----            ----                           -------------   -----
System.String   Basic                                          false
System.String   Kerberos                                       false
System.String   Negotiate                                      true
System.String   Certificate                                    false
System.String   CredSSP                                        false
System.String   CbtHardeningLevel                              Relaxed
```

## WinrRM over https

Remove any existing HTTPS listeners to start over (not needed if you're running this for the
first time):
```console
PS> Get-ChildItem WSMan:\localhost\Listener\ | ? -Property Keys -like "*HTTPS" | Remove-Item -Recurse
```

Generate a new self-signed certificate. For testing purposes `-DnsName` can be anything in this
case because `winrmexec.py` will not verify server certificates anyway:
```console
PS> $cert = New-SelfSignedCertificate -DnsName dc01.test.lab,dc01 -CertStoreLocation Cert:\LocalMachine\My
```

Now create a HTTPS listner for WinRM:
```console
PS> New-Item -Path WSMan:\localhost\Listener\ -Transport HTTPS -Address * -CertificateThumbPrint $cert.Thumbprint -Force
```

Add a firewall rule to allow incomming connections on 5986 port:
```console
PS> New-NetFirewallRule -Displayname 'WinRM - Powershell remoting HTTPS-In' -Name 'WinRM - Powershell remoting HTTPS-In' -Profile Any -LocalPort 5986 -Protocol TCP
```

## Other auth methods
### Basic
This sends credentials in `Authorization: Basic <b64 encoded username:password>` header over
http(s). By default unencrypted channels are not enabled:
```console
PS> Get-Item WSMan:\localhost\Service\AllowUnencrypted
Type            Name                           SourceOfValue   Value
----            ----                           -------------   -----
System.String   AllowUnencrypted                               false
```
so this will only work over https at first:
```console
PS> Set-Item WSMan:\localhost\Service\Auth\Basic $true
```
but let's enable it over http too:
```console
PS> Set-Item WSMan:\localhost\Service\AllowUnencrypted $true
```
this is unrealistic in practice, but it makes it easy to debug the protocol in wireshark.

### CredSSP
Enable CredSSP on the server:
```console
PS> Enable-WSManCredSSP -Role Server -Force
```

Set WinRM CertificateThumbprint, this can be the same as the one we used for HTTPS listner:
```console
PS> Get-ChildItem WSMan:\localhost\Listener\*\CertificateThumbprint
Type           Name                   SourceOfValue   Value
----           ----                   -------------   -----
...
System.String  CertificateThumbprint                  1AC6B4AE1E2231928BE953A50BD74F9E18C5C209
...

PS> Set-Item WSMan:\localhost\Service\CertificateThumbprint '1AC6B4AE1E2231928BE953A50BD74F9E18C5C209'
```
or create a new one
```console
PS> $cert = New-SelfSignedCertificate -DnsName XXX -CertStoreLocation Cert:\LocalMachine\My
PS> echo $cert.Thumbprint
FD8CDF253942B6744EA75C2E2428B34DF99A5FA7
```

`NETWORK SERVICE` account must be able to read private key of this certificate. Doing this
in powershell is a bit of chore, but using `mmc.exe`:
1. File > Add/Remove Snap-In
2. Select "Certificates" and click "Add >"
3. Choose "Computer Account", click "Next"
4. Choose "Local Computer", click "Finish"
5. In main window expand "Certificates (Local Computer) > Personal > Certificates"
6. Select that self-signed certificate we created earlier (double click, select details tab
   and make sure Thumbprint is the same)
7. Right-click on that certificate, "All-Tasks > Manage Private Keys"
8. Add `NETWORK SERVICE` to "Group or user names" list and click on it
9. Uncheck "Full Control", check "Read"


### CbtHardeningLevel
This is not really a diffrent authentication method, but if set to `Strict`, connections
over https require [channel bindings for TLS](https://www.ietf.org/rfc/rfc9266.html)
to be added during Kerberos and NTLM auth. Set this to `Strict` to make sure `winrmexec.py`
can deal with this. If set to `Relaxed`, the server will ignore those anyway:
```console
Set-Item WSMan:\localhost\Service\Auth\CbtHardeningLevel Strict
```

### Certificate
This uses client certificates to authorize clients when connecting over https:
```console
PS> Set-Item WSMan:\localhost\Service\Auth\Certificate $true
```

We'll do this two different ways. If your DC has "Active Directory Certificate Services"
(`ADCS` for short) role, then we can reuse some of the functionality provided by it to
help us create user certificates that have just the right format for this. On a standalone
Windows 10 box or a DC where ADCS are not enabled we can do the same thing ourselves
though it is a little bit more involved.

### `ADCS`
Find the thumbprint of Certificate Authority certificate:
```console
PS> Get-ChildItem Cert:\LocalMachine\Root
Thumbprint                                Subject
----------                                -------
...
E7696CC893A778B8E4437522D9751B1DC23AACC8  CN=test-DC01-CA, DC=test, DC=lab
...
```
Now pick a user you want to use for Client Certificate auth:
```console
PS> $pass = ConvertTo-SecureString -Force 'hunter2' -AsPlain
PS> $cred = [PSCredential]::new("target_user", $pass)
```
Now add this to WSMan:
```console
PS> New-Item -Path 'WSMan:\localhost\ClientCertificate' -Subject 'target_user@test.lab' -Issuer 'E7696CC893A778B8E4437522D9751B1DC23AACC8' -Credential $cred -Force
```
Now back in linux land you can use a tool like `certipy` to request a certificate with `User`
template from `ADCS`:
```console
$ certipy req -ca test-DC01-CA -template 'User' -u 'target_user@test.lab' -p 'hunter2' -target dc01.test.lab
...
[*] Saved certificate and private key to 'target_user.pfx'
```
Convert it to `.pem` and `.key`:
```console
$ openssl pkcs12 -in target_user.pfx -passin pass: -nokeys -out target_user.pem
$ openssl pkcs12 -in target_user.pfx -passin pass: -nocerts -noenc -out target_user.key
```
and use this to connect to WinRM:
```console
$ winrmexec.py -cert-pem 'target_user.pem' -cert-key 'target_user.key' 'dc01.test.lab'
```
Like I said before, `ADCS` here is sort of unrelated, we just use the fact that `CA` cert is
already in `Cert:\LocalMachine\Root` and that `User` template issues a certificate with a
required format. You might as well use that certificate with PKINIT to request a TGT and then
use Kerberos auth if it is enabled.

### "We have ADCS at home"
If `ADCS` is not running this can be done manually. I'll do this for Windows 10 box, but this
also works for DC. First create a certificate for our own Certificate Authority:
```console
$ cat << EOF > win10_ca.conf
distinguished_name = req_distinguished_name
[req_distinguished_name]
[v3_ca]
subjectKeyIdentifier = hash
basicConstraints = critical, CA:true
keyUsage = critical, keyCertSign
EOF

$ openssl req -new -config win10_ca.conf -sha256 -subj "/CN=WinRM CA" -newkey rsa:2048 -reqexts v3_ca -noenc -keyout win10_ca.key -out win10_ca.csr
$ openssl x509 -req -in win10_ca.csr -key win10_ca.key -sha256 -days 365 -extfile win10_ca.conf -extensions v3_ca -outform DER -out win10_ca.cer
```
Upload `win10_ca.cer` file to windows and add it to certificate root:
```console
PS> certutil.exe -addstore "Root" win10_ca.cer
```
Remember it's thumbprint either with
```console
PS> Get-ChildItem Cert:\LocalMachine\Root | ? -Property Subject -eq "CN=WinRM CA"
Thumbprint                                Subject
----------                                -------
1373F536BDF18C54DD7A86962BF113E7E2B415B0  CN=WinRM CA
```
or
```console
$ sha1sum win10_ca.cer
1373f536bdf18c54dd7a86962bf113e7e2b415b0  win10_ca.cer
```

Unlike last time, let's do this a bit differently. We'll use `Administrator` for user, but
set `-Subject` to some unrelated name that is not a user on the system:
```console
PS> $pass = ConvertTo-SecureString -Force 'hunter2' -AsPlain
PS> $cred = [PSCredential]::new("Administrator", $pass)
PS> New-Item -Path 'WSMan:\localhost\ClientCertificate' -Subject 'admin@other.domain' -Issuer '1373F536BDF18C54DD7A86962BF113E7E2B415B0' -Credential $cred -Force
```
Now create a certificate with UPN set to `admin@other.domain` and sign it with CA certificate:
```console
$ cat << EOF > admin.conf
distinguished_name = req_distinguished_name
[req_distinguished_name]
[v3_req_client]
extendedKeyUsage = clientAuth
subjectAltName = otherName:1.3.6.1.4.1.311.20.2.3;UTF8:admin@other.domain
EOF

$ openssl req -config admin.conf -new -sha256 -subj '/CN=admin' -newkey rsa:2048 -keyout admin.key -noenc -reqexts v3_req_client -out admin.csr
$ openssl x509 -req -extfile admin.conf -in admin.csr -sha256 -days 365 -extensions v3_req_client -CA win10_ca.cer -CAkey win10_ca.key -CAcreateserial -out admin.pem
```
And then
```console
winrmexec.py -cert-pem 'admin.pem' -cert-key 'admin.key' dc01.test.lab
```

