#Asking questions

print "How old are you?", #Comma is added so  it goes to the next new line
age = int(raw_input())
print "How tall are you?",
height = float(raw_input())
print "How much do you weigh?",
weight = float(raw_input())

print "So, you're {} old, {} tall and {} heavy.".format(age, height, weight)
