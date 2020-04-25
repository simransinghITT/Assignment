#!/usr/bin/python36
import subprocess
import os
import cgi

print("content-type: text/html")
print()

form =  cgi.FieldStorage()
docker_name = form.getvalue('n')
docker_image = form.getvalue('img')
dockers_in_system=subprocess.getoutput("sudo docker ps -a --format '{{.Names}}'")
if(docker_name in dockers_in_system):
  print("""
  <H1>Docker already exist please choose another name.</H1>
  """)
  exit()
else:
  output=subprocess.getoutput("sudo docker run --name {} {}".format(docker_name,docker_image))
  print("""
  <H1>print("Docker {} launched successfully".format(docker_name))</H1>
  """)
  docker_in_system=subprocess.getoutput("sudo docker ps -a --format '{{.Names}}'")
  a=docker_in_system.split()
  print("Total docker present in system are: {}".format(len(a)))
  for i in range(0,len(a)):
    print(a[i])
