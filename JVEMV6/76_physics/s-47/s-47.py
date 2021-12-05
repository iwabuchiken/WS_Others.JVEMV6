######################
# C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\76_physics\s-47\s-47.py
#pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\76_physics\s-47 && python s-47.py

#ref
#https://www.digitalocean.com/community/tutorials/how-to-use-subprocess-to-run-external-programs-in-python-3
#ref exec
#https://stackoverflow.com/questions/1027714/how-to-execute-a-file-within-the-python-interpreter
######################

print("this file is --> C:\\WORKS_2\\WS\\WS_Others.JVEMV6\\JVEMV6\\76_physics\\s-47\\s-47.py")

import math

#n = 3
n = 5
x = (1/2)

sumOf = 0

for i in range(n) :
	print ("i is : %d" % (i))
	print ("sin(i*(1/2)*pi) is : %d" % (math.sin(i*(1/2)*math.pi)))


