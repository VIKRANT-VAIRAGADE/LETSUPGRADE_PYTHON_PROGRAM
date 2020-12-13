a = open("letsupgrade.txt",'w')
a.write("I love letsupgrade.\n")
a.close()

a=open("letsupgrade.txt",'r+')
print(a.read())
a.close()

a=open("letsupgrade.txt",'a')
a.write("It provide best learning ever.")
a.close()

a=open("letsupgrade.txt",'r')
print(a.read())
a.close()
