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
  print("<H1>Docker already exist please choose another name.</H1>")
  exit()
else:
  output=subprocess.getoutput("sudo docker run --name {} {}".format(docker_name,docker_image))
  print("<H1>Docker '{}' launched successfully</H1>".format(docker_name))
  docker_in_system=subprocess.getoutput("sudo docker ps -a --format '{{.Names}}'")
  docker_in_system_list=docker_in_system.split()
  print("<H3>Total docker present in system are: {}</H3>".format(len(a)))
  for i in docker_in_system_list:
    print(i)
