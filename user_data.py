#!/usr/bin/python36
import subprocess
import os
import cgi

print("content-type: text/html")
print()

form =  cgi.FieldStorage()
docker_name = form.getvalue('n')
docker_image = form.getvalue('img')
docker_in_system=subprocess.getoutput("sudo docker ps -a --format '{{.Names}}'")
if (docker_name in docker_in_system):
  print("Docker already exist please choose another name.")
  exit()
else:
  output=subprocess.getoutput("sudo docker run --name {} {}".format(docker_name,docker_image))
  print("Docker {} launched successfully".format(docker_name))
  docker_in_system=subprocess.getoutput("sudo docker ps -a --format '{{.Names}}'")
  a=docker_in_system.split()
  <p>print("Total docker present in system are: {}".format(len(a)))</p>
  for i in range(0,len(a)):
    print(a[i])<br>
