"""Example 33."""
numbers = []
i = int(raw_input("Count from what number? \n > "))
t = int(raw_input("To what number? \n > "))


def numPrint(i, t):
    """Feed integer to print until."""
    while i <= t:
        print "At the top i is %d" % i
        numbers.append(i)

        i += 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


numPrint(i, t)

print "The numbers: "

for num in numbers:
    print num
