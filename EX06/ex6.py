# x equals sentence, is replaced by.
# % formatter
x = "There are %d types of people." % 10
#? why first define
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
#prints x and y
print x
print y
#formatter stands for sentence x
print "I said: %r." % x

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
'? why percentage?'
print joke_evaluation % hilarious
w = "This is the left side of..."
e = "a string with a right side."

print w + e
