#!/usr/bin/python3
import subprocess
import os
import cgi

print ("content-type: text/html")
print()

form =  cgi.FieldStorage()
docker_name = form.getvalue('n')
docker_image = form.getvalue('img')
#os.system('sshpass -p "redhat" ssh s@192.168.43.85 "mkdir ttt"')
a=subprocess.getoutput("sudo docker -it run --name {} {}".format(docker_name,docker_image))
print(a)
