from random import randint
total=0 # start at 0
for i in range(10000): # start everything below te range
  wins=0 # set wins to 0
  if randint(1,100) <= 87: # random selection of number between 1-100. If number is between 1-87 then add 1 to the amount of wins
    wins=wins+1 # add 1 to amount of wins
  if randint(1,100) <= 65: # random selection of number between 1-100. If number is between 1-65 then add 1 to the amount of wins
    wins=wins+1 # add 1 to amount of wins
  if randint(1,100) <= 17: random selection of number between 1-100. If number is between 1-17 then add 1 to the amount of wins
    wins=wins+1 # add 1 to amount of wins
  if wins>=2 # compare amount of wins and see if its greater than or equal to 2
percentage = (total/float(10000)) * 100 # divide range of float to total wins
print "chances of winning are" + str(percentage) # print the possibilitiy of winning 
