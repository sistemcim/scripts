#!/usr/bin/python

import module1_user
import module2_operator

#print "Module1 namespace names"
#print dir(module1)

module1_user.greetUser()

userName=""
#userName=module1_user.getUser(userName)
#print "\nWelcome dear ", userName,"!"

userName=module1_user.changeUser(userName)
print "\nUser name changed!"
print "New username is:",userName
print "\n"

num1 = 15
num2 = 4

module2_operator.add(num1,num2)
module2_operator.subtract(num1,num2)
module2_operator.multiply(num1,num2)
module2_operator.devide(num1,num2)
module2_operator.mod(num1,num2)
module2_operator.floordiv(num1,num2)
module2_operator.exp(num1,num2)
