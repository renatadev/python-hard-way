#Else and if

people = 30
cars = 40
buses = 15

if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We shouldnt"
else:
    print "We cant decide"

if buses > cars:
    print "Thats too many buses"
elif buses < cars:
    print "Maybe we could take them"
else:
    print "We still cant decide"

if people > buses:
    print "Alright, lets just take the buses"
else:
    print "Fine, lets stay at home then"
