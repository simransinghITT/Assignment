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
print("Docker present in system are:")
a=docker_in_system.split()
for i in len(a):
  print(a[i],sep="\n")
print("\n")
output=subprocess.getoutput("sudo docker run --name {} {}".format(docker_name,docker_image))
