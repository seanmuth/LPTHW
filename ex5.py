name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

lbs_kilos_conv = 0.45359237
weight_kilos = weight * lbs_kilos_conv

inches_cm_conv = 2.54
height_cm = height * inches_cm_conv

print "Let's talk about %s." % name
print "He's %d inches tall. (That's %.2f centimeters)" % (height, height_cm)
print "He's %d pounds heavy. (That's %.3f kilograms)" % (weight, weight_kilos)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight
)
