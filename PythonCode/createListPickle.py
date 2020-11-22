import SSH
from Person import Person as p

I = SSH.OnlineInterface()

p1 = p("George",10,20,30)
p2 = p("Bob",0,0,1)
p3 = p("Tamas",50,50,50)

I.putData([p1,p2,p3])

print(I.getData())
