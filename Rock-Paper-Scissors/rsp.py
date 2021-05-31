from random import randint

t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,2)]

player = False

while player == False:
	player = raw_input("Rock, Paper, Scissors? ")
	#print type(player)
	if player == computer:
		print "Tie!"
	elif player == "Rock":
		if computer == "Paper":
			print "You lose! %s covers %s" % (computer, player)
		else:
			print "You win! %s smashes %s" % (player, computer)
	elif player == "Paper":
		if computer == "Scissors":
			print "You lose! %s cut %s" % (computer, player)
		else:
			print "You win! %s cover %s" % (player, computer)
	elif player == "Scissors":
		if computer == "Rock":
			print "You lose... %s smashes %s" %(computer,player)
		else:
			print "You win! %s cut %s" % (player, computer)
	else:
		print "That's not a valid play. Check your spelling"

	player = False
	computer = t[randint(0,2)]

		