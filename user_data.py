#!/usr/bin/python36
import subprocess
import os
import cgi

print ("content-type: text/html")
print()

form =  cgi.FieldStorage()
docker_name = form.getvalue('n')
docker_image = form.getvalue('img')
a=subprocess.getoutput("sudo docker run --name {} {}".format(docker_name,docker_image))
aa=subprocess.getoutput("sudo docker ps -a")
print(aa)
print("Launched Docker {} Successfully".format(docker_name))
