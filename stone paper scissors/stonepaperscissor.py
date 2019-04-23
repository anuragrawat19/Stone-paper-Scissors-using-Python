from random import randint
def win():
	print 'you win !'
def lose():
	print' you lose !'

while True:
	player_choice =raw_input("what do you pick ?  ( rock, paper,scissors)")
	player_choice.strip()
	random1=randint(0,2)
	moves=["rock","paper","scissors"]
	computer_choice=moves[random1]
	if player_choice==computer_choice:
		print "draw"
	elif player_choice =="rock" and computer_choice =="scissors":
		win()
	elif player_choice =="paper" and computer_choice =="scissors":
		lose()
	elif player_choice =="scissors" and computer_choice =="paper":
		win()
	elif player_choice =="scissors" and computer_choice =="rock":
		lose()
	elif player_choice =="paper" and computer_choice =="rock":
		win()
	elif player_choice =="rock" and computer_choice =="paper":
		lose()
	else:
		print "choose the correct option"
	again =raw_input("do you want to play again (y or n)").strip()
	if again == "n":
		break

