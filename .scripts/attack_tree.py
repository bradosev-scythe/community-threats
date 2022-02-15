#!/usr/bin/python

import json 
import argparse
import os
import re

flowchart = []

def parseJSOnFile(file,outfilename):
    js = open(file)
    data = json.load(js)
    module = None
    module_to_load= None
    request = None
    tags = [] 
    scripts = data["threat"]["script"]
    f = open(outfilename,"a")

    f.write("\n\n #Attack Graph\n")
    f.write("```mermaid\n")
    f.write("graph TD\n")
    for i in scripts:
        f.write(f'Step{i}["')
        if "ifelse" in scripts[i]:
            if scripts[i]['ifelse']["type"] == "decision":
                step = scripts[i]["ifelse"]["step"]
                nxt = scripts[i]["ifelse"]
                f.write(f"Step{step} --> Step{nxt}")
        if "delay" in scripts[i]["type"]:
            time = scripts[i]["time"]
        if 'module' in scripts[i]:
            module = f"{scripts[i]['module']}"
            f.write(f"<b> module: {module} </b> <br>")
        if 'module_to_load' in scripts[i]:
            module_to_load =f"{scripts[i]['module_to_load']}"
        if 'request' in scripts[i]:
            request = scripts[i]['request']
            request = request.replace("'","")
            request = request.replace('"',"")
            f.write(f"<h4> parameters: </h4> <i> {request} </i> <br>")
        if "depends_on" in scripts[i]:
            depends_on = f"{scripts[i]['depends_on']}"
        if 'rtags' in scripts[i]:
            stags = scripts[i]['rtags']
            tactic_matching = [s for s in stags if s.__contains__("att&ck-tactic:")]
            technique_matching = [s for s in stags if s.__contains__("att&ck-technique:")]
            
            for tm in tactic_matching:
                f.write(f"<a href='{mitreTactic(tm.split(':')[1])}'>{tm}</a><br>\n")
            
            for tm in technique_matching:
                f.write(f"<a href='{mitreTechnique(tm.split(':')[1])}'>{tm}</a><br>\n")
                
        f.write('"]\n')
    for i in scripts:
        if i == len(scripts)-1:
            break
        f.write(f"Step{i} --> Step{int(i)+1}\n")    
    f.write("```\n")
    f.close()
   
def mitreTechnique(tag):
    return f"https://attack.mitre.org/techniques/{tag}"

def mitreTactic(tag):
    return f"https://attack.mitre.org/tactics/{tag}"
    
    
def sequenceDiagram(filename):
    with open(filename,'w') as f:
        f.write('```mermaid\n')
        f.write('sequenceDiagram\n')
        for i in flowchart:
            f.write('C2-->>+Implant:"')
            c2_cmd = ""
            step,module,module_to_load,request,tags = i
            if module:
                c2_cmd = f"{module}"
            if request:
                request = request.replace('"',"")
                request = request.replace("'","")
                c2_cmd += f" {request}"
            f.write(c2_cmd)
            f.write('"\n')
            
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--file",
        help="JSON threat input file",
    )
    args = parser.parse_args()
    flowchart_name = os.path.basename(args.file)
    flowchart_name = flowchart_name.split(".")[0]
    readme_name = f"{os.path.dirname(args.file)}/README.md"
    parseJSOnFile(args.file,readme_name)

    
if __name__ == "__main__":
    main()
