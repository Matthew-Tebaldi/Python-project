import re
import zipfile
import os
import time
import smtplib

from collections import defaultdict
from email.mime.multipart import MIMEMultipart 
from email.mime.base import MIMEBase 
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate 
from email import encoders


def createHtmlFile():
    
    filename = "csc344/links_to_projects.html"
    target = open(filename, 'w')
    
    filewords =  "<!DOCTYPE html><html><head> <meta http-equiv=\"content-type\"content=\"text/html; charset=utf-8\" /> <title>CSC344 FINAL PROJECT!!! </title></head>"
    filewords = filewords + "<style>body {background-color:#434444;}</style>"
    filewords = filewords + "<body text=#2ec8f7 vlink=\"pink\" link=#2ef7a0><h1>Final Project</h1>"
    filewords = filewords + " <h2><u>Course Work</u></h2><br><ol><li> <b>Projects' source code:</b><br><br>C: <a href=\"project1.c\">source code</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Clojure: <a href=\"project2.clj\">source code</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
    filewords = filewords + "Haskell: <a href=\"project3.hs\">source code</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Prolog: <a href=\"project4.pl\">source code</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Python: <a href=\"project5.py\">source code</a><br><br><br><br><br><br>"
    filewords = filewords + "<li> <b>Symbols File: </b><br><br> Symbols: <a href=\"SymbolsFile.txt\">text file</a></ol></body></html>"
   
    target.write(filewords)
    target.close()
    
    
    

def createSymbolsFile():
    
    
    f = open('csc344/a1/project1.c','r')
    ctxt = ""
    while 1:
        line = f.readline()
        if not line:break
        ctxt += line

    f.close()
    
    
    output = "\n ----Symbols File----\n\n Symbols for C:\n\n"   
    r = re.compile(r'(?<=void\s)\w+ | (?<=int\s)\w+ | (?<=char\s)\w+' , flags=re.I | re.X )
    iterator = r.finditer(ctxt)
    for match in iterator:
   
        name =  re.compile(r'(?P<word>\b\w+\b)' , flags=re.I | re.X ).match(match.group()).group()
      
        matchObj = re.search('\s('+name+')', output, re.M|re.I)
        if matchObj:
            something = ""
        else:
            output = output + "[Project 1, " + name + "]\n"  
        
        
 ####Clojure####

    f = open('csc344/a2/project2.clj','r')
    clojuretxt = ""
    while 1:
        line = f.readline()
        if not line:break
        clojuretxt += line

    f.close()
    
    clojureOutput = "\n Symbols for Clojure:\n\n"   
    r = re.compile('(?<=[(]defn\s)\w+ | (?<=[(]def\s)\w+' , flags=re.I | re.X )
    iterator = r.finditer(clojuretxt)
    for match in iterator:
   
        name =  re.compile(r'(?P<word>\b\w+\b)' , flags=re.I | re.X ).match(match.group()).group()
      
        matchObj = re.search('\s('+name+')', clojureOutput, re.M|re.I)
        if matchObj:
            something = ""
        else:
            clojureOutput = clojureOutput + "[Project 2, " + name + "]\n"  
    
    output = output + clojureOutput
    
    
    ####Haskell####

    f = open('csc344/a3/project3.hs','r')
    txt = ""
    while 1:
        line = f.readline()
        if not line:break
        txt += line

    f.close()
    
    haskellOutput = "\n Symbols for Haskell:\n\n"   
    r = re.compile(r'(?P<word>\w+\b\s[::]) | (?P<words>\w+\b\s[=])' , flags=re.I | re.X )
    iterator = r.finditer(txt)
    for match in iterator:
   
        name =  re.compile(r'(?P<word>\b\w+\b)' , flags=re.I | re.X ).match(match.group()).group()
      
        matchObj = re.search('\s('+name+')', haskellOutput, re.M|re.I)
        if matchObj:
            something = ""
        else:
            haskellOutput = haskellOutput + "[Project 3, " + name + "]\n"  
          
    output = output + haskellOutput
    
    ####Prolog####

    f = open('csc344/a4/project4.pl','r')
    txt = ""
    while 1:
        line = f.readline()
        if not line:break
        txt += line

    f.close()
    
    prologOutput = "\n Symbols for Prolog:\n\n"   
    r = re.compile(r'(?P<word>\b\w+\b[(]) | \b[A-Z]+_[A-Z]+\b | \b[A-Z]+\b' , flags=re.I | re.X )
    iterator = r.finditer(txt)
    for match in iterator:
   
        name =  re.compile(r'(?P<word>\b\w+\b)' , flags=re.I | re.X ).match(match.group()).group()
      
        matchObj = re.search('\s('+name+')', prologOutput, re.M|re.I)
        if matchObj:
            something = ""
        else:
            if name != "not":
                prologOutput = prologOutput + "[Project 4, " + name + "]\n"  
          
    output = output + prologOutput
    print(prologOutput)
    
    
    ####Python####
    
    f = open('csc344/a5/project5.py','r')
    txt = ""
    while 1:
        line = f.readline()
        if not line:break
        txt += line

    f.close()
    
    pythonOutput = "\n Symbols for Python:\n\n"   
    r = re.compile(r'(?P<word>\b\w+\b\s[=]) | (?<=def\s)\w+' , flags=re.I | re.X )
    iterator = r.finditer(txt)
    for match in iterator:
   
        name =  re.compile(r'(?P<word>\b\w+\b)' , flags=re.I | re.X ).match(match.group()).group()
      
        matchObj = re.search('\s('+name+')', pythonOutput, re.M|re.I)
        if matchObj:
            something = ""
        else:
            if name != "not":
                pythonOutput = pythonOutput + "[Project 5, " + name + "]\n"  
          
    output = output + pythonOutput
    
    symbolsFile = open("csc344/SymbolsFile.txt", "w")
    symbolsFile.truncate()
    symbolsFile.write(output)
    symbolsFile.close()
    
    

    
def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), file)
            
            
            
def sendEmail(address):
    
    user = "email goes here"
    pwd = "pass word goes here"
    FROM = "email goes here "
    TO = address
    SUBJECT = 'Final Project'
    textMessage = 'Here is a zip file containing all the projects so far.'


   
    zipf = zipfile.ZipFile("csc344.zip", 'w', zipfile.ZIP_DEFLATED)
    zipdir("csc344", zipf)
    zipf.close()  
    
    zf = open("csc344.zip")
    
    msg = MIMEMultipart()
    msg['From'] = FROM
    msg['To'] = TO
    msg['Date'] = formatdate(localtime = True)
    msg['Subject'] = SUBJECT
    msg.attach (MIMEText(textMessage))
    part = MIMEBase('application', "octet-stream")
    part.set_payload(zf.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="csc344_final_project.zip"')
    msg.attach(part)
    
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    server.login(user, pwd)
    server.sendmail(FROM, TO, str(msg))
    server.close()
    print( 'Project was successfully sent to: ' + address)

def main():
  
    
      
    emailAddress = raw_input("Enter your email:")
    
    createHtmlFile()
    
    createSymbolsFile()

    sendEmail(emailAddress)




if __name__ == '__main__':
    main()
