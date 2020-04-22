#!/usr/bin/python
import subprocess
import cgi
import os

print "Content-type: text/html\n\n"
mydata =  cgi.FieldStorage()
docker_name = mydata.getvalue('name')
docker_image = mydata.getvalue('image')
#os.system('sshpass -p "redhat" ssh s@192.168.43.85 "mkdir ttt"')
os.system("docker run -d --name docker_name image_name")
