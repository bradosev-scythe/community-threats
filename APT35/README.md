# APT35 Adversary Emulation Plan


Adversary Emulation Plan based on CTI from: https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/ 

To emulate:

1. Download 'APT35_scythe_threat.json' and import the threat in JSON format to your SCYTHE instance
2. Download the Virtual File System (VFS) files under the 'VFS' folder
3. Upload the VFS files to your SCYTHE VFS in the following location: VFS:/shared/threats/APT35
4. Click "Create Campaign from Threat" to begin an emulation campaign


 #Attack Graph
```mermaid
graph TD
Step0["<b> module: https </b> <br>"]
Step1[""]
Step2["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load upsh </i> <br>"]
Step3["<b> module: upsh </b> <br><h4> parameters: </h4> <i> --vfs_filepath VFS:/shared/threats/APT35/Get-InstalledPrograms.ps1 </i> <br><a href='https://attack.mitre.org/techniques/T1059.001'>att&ck-technique:T1059.001</a><br>
"]
Step4["<b> module: upsh </b> <br><h4> parameters: </h4> <i> --cmd get-installedprograms </i> <br><a href='https://attack.mitre.org/techniques/T1059.001'>att&ck-technique:T1059.001</a><br>
<a href='https://attack.mitre.org/techniques/T1518'>att&ck-technique:T1518</a><br>
"]
Step5["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load run </i> <br>"]
Step6["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd.exe /c wmic product get name, InstallLocation, InstallDate, Version </i> <br><a href='https://attack.mitre.org/techniques/T1059.003'>att&ck-technique:T1059.003</a><br>
<a href='https://attack.mitre.org/techniques/T1518'>att&ck-technique:T1518</a><br>
<a href='https://attack.mitre.org/techniques/T1047'>att&ck-technique:T1047</a><br>
"]
Step7[""]
Step8["<b> module: upsh </b> <br><h4> parameters: </h4> <i> --vfs_filepath VFS:/shared/threats/APT35/screenshot.ps1 </i> <br><a href='https://attack.mitre.org/techniques/T1059.001'>att&ck-technique:T1059.001</a><br>
<a href='https://attack.mitre.org/techniques/T1113'>att&ck-technique:T1113</a><br>
"]
Step9[""]
Step10["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd.exe /c tasklist /v /FO csv > tasklist </i> <br><a href='https://attack.mitre.org/techniques/T1059.003'>att&ck-technique:T1059.003</a><br>
<a href='https://attack.mitre.org/techniques/T1057'>att&ck-technique:T1057</a><br>
<a href='https://attack.mitre.org/techniques/T1518'>att&ck-technique:T1518</a><br>
<a href='https://attack.mitre.org/techniques/T1007'>att&ck-technique:T1007</a><br>
"]
Step11[""]
Step12["<b> module: upsh </b> <br><h4> parameters: </h4> <i> --vfs_filepath VFS:/shared/threats/APT35/systeminfo.ps1 </i> <br><a href='https://attack.mitre.org/techniques/T1082'>att&ck-technique:T1082</a><br>
<a href='https://attack.mitre.org/techniques/T1059.001'>att&ck-technique:T1059.001</a><br>
"]
Step13[""]
Step14["<b> module: upsh </b> <br><h4> parameters: </h4> <i> --cmd cd C:/; ls; </i> <br><a href='https://attack.mitre.org/techniques/T1083'>att&ck-technique:T1083</a><br>
<a href='https://attack.mitre.org/techniques/T1059.001'>att&ck-technique:T1059.001</a><br>
"]
Step15["<b> module: upsh </b> <br><h4> parameters: </h4> <i> --vfs_filepath VFS:/shared/threats/APT35/wlan_enum.ps1 </i> <br><a href='https://attack.mitre.org/techniques/T1059.001'>att&ck-technique:T1059.001</a><br>
<a href='https://attack.mitre.org/techniques/T1016'>att&ck-technique:T1016</a><br>
"]
Step16["<b> module: upsh </b> <br><h4> parameters: </h4> <i> --cmd Get-PSDrive </i> <br><a href='https://attack.mitre.org/techniques/T1059.001'>att&ck-technique:T1059.001</a><br>
"]
Step17[""]
Step18["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c del info, tasklist, help.jpg </i> <br>"]
Step19["<b> module: controller </b> <br><h4> parameters: </h4> <i> --shutdown </i> <br><a href='https://attack.mitre.org/tactics/TA0011'>att&ck-tactic:TA0011</a><br>
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
```
