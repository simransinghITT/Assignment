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
print(type((docker_in_system))
output=subprocess.getoutput("sudo docker run --name {} {}".format(docker_name,docker_image))
print(output)
print("Launched Docker {} Successfully".format(docker_name))
