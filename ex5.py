#More variables and printing
#Format string

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

#Str formatting with %
#print "If I add %d, %d, and %d I get %d." % (
#my_age, my_height, my_weight, my_age + my_height + my_weight)

#Str formatting with {} as recommended in CF:G
print "If I add {}, {}, and {} I get {}.".format(
my_age, my_height, my_weight, my_age + my_height + my_weight)


#String Formatting own example
name = "Renata"
age = 21

description = "My name is {} and I'm {}.".format(name, age)
print description

#Indexing
description = "My name is {0} and I'm {1}.".format(name, age)
print description

#Argument specifiers
#%s - String (or any object with a string representation, like numbers)
#%d - Integers
#%f - Floating point numbers
#%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
#%x/%X - Integers in hex representation (lowercase/uppercase)
