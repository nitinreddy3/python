# Define a function which takes two parameters

def cheese_and_crackers(cheese_count, cracker_count):
    print "You have %r cheeses!" % cheese_count
    print "You have %r crackers" % cracker_count

print "We can just give the function numbers directly:"

# Calling a function with parameters passed
cheese_and_crackers(20, 30)

# Variables storing cheeses' and crackers' count
amount_of_cheeses = 10
amount_of_crackers = 20

# Passing the variables as params on a calling function
cheese_and_crackers(amount_of_cheeses, amount_of_crackers)

print "We can even do math inside too:"

# Directly passing values to the function
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"

# Passing values along with variables storing the values
cheese_and_crackers(amount_of_cheeses + 100, amount_of_crackers + 1000)
