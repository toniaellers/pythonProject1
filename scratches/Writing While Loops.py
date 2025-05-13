#i =1
#while i <= 5:
#    print (i)
#    i += 1


#x = 2
#while x < 12:
   # print (x)
   # x+=3

#y = -10
#while y <=0:
 #   print (y, end=" ")
  #  y += 2
   # print ()

#z = 0
#while z < 4:
 #   print (4 * "*")
  #  z += 1

#string = "CSCI 150"
#i = 0
#while i < len(string) :
 #   print (string[i])
  #  i += 1

#list = []
#prompt = "Please enter a number ('0' to finish)"
#response = eval (input (prompt))
#while response != 0:
 #   list.append(response)
  #  response = eval(input (prompt))
   # print (sorted(list))
    #print (sum(list))
    #print (sum(list) / len (list))

import random
from random import choice

questions = ["why is the sky blue?: ", "where do babies come from?: ", "how can birds fly?: "]

question = choice(questions)
answer = input (question).strip().lower()

while answer != "just because":
    answer = input("why?: ").strip().lower()
