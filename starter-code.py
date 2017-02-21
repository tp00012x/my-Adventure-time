
import random

def msg(room):
	if room['msg'] == '': #There is no custom message
		return 'You have entered the ' + room['name'] + "\n"
	else:
		return room['msg']

def help():
	print("Type N,S,E,W to move a direction \n \
	       Type 'QUIT' to quit.\
		   Type 'HELP' for help")

def get_choice(room,dir):
	if dir=="HELP":
		help()
		return -2
	if dir=="QUIT":
		return -3
	elif dir == 'N':
		choice = 0
	elif dir == 'E':
		choice = 1
	elif dir == 'S':
		choice = 2
	elif dir == 'W':
		choice = 3
	else:
		return -1

	if room['directions'][choice] == -1:
		print("You cannot go in that direction!")
		return -2
	else:
		return room['directions'][choice]

def statusupdate(bunny):
	if not bunny["basket"]:
		print("You do not have the basket")
	else:
		print("You have the basket! Now you can collect eggs")
		eggmessage = "You have ", bunny['eggs'], "egg(s) in your basket."
		print(eggmessage)

def basketeggplacement(rooms):
	myrooms = random.sample(rooms,4)
	myrooms[0]["basket"] = True
	myrooms[1]["egg"] = True
	myrooms[2]["egg"] = True
	myrooms[3]["egg"] = True

def main():
	rooms = [{"name":"entranceway", "msg":"","egg":False,"basket":False,"directions":[2,4,-1,-1]},
	         {"name":"hallway", "msg":"", "egg":False, "basket":False,"directions":[-1,2,-1,-1]},
	         {"name":"kitchen","msg":"", "egg":False, "basket":False, "directions":[-1,3,0,1]},
	         {"name":"diningroom", "msg":"", "egg":False, "basket":False, "directions":[-1,-1,4,2]},
	         {"name":"livingroom", "msg":"", "egg":False, "basket":False, "directions":[3,-1,-1,0]}]
	basketeggplacement(rooms)

	bunny = {"location":0,"basket":False,"eggs":0}
	gameover = False
	help()
	while(not gameover):
		userinput = input("Pick a direction. Type 'HELP' for help.\n")
		new_room = get_choice(rooms[bunny["location"]], userinput)
		if new_room == -1:
			print("Invalid input, try again\n")
		elif new_room == -2:
			continue
		elif new_room == -3:
			print("You quit the game! Quitter!")
			gameover = True
		else:
			print(msg(rooms[new_room]))
			bunny["location"] = new_room
			if rooms[new_room]["basket"]:
				print("You got the basket")
				bunny["basket"] = True
				rooms[new_room]["basket"] = False
			if rooms[new_room]["egg"]:
				if bunny["basket"]:
					print("There is an egg in this room! You picked it up")
					bunny["eggs"] += 1
					rooms[new_room]["egg"] = False
				else:
					print("There is an egg here, but you need the basket! Go find it!")
		if bunny["eggs"] == 3:
			print("You win! You stole all the eggs!")
			gameover = True

main()
