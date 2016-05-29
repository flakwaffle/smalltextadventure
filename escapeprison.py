#Introduction#--------------/
print("You are stuck in a prison cell. Get out.")
print("To look around, enter 'N', 'S', 'E', or 'W'")

#stores items--------------/
inventory = []
#Current location----------/
current = []

def same_place():
	if current[-2] == 'n':
		print("You stare at the bars.")
	elif current[-2] == 's':
		print("You feel tired staring at the bed.")
	elif current[-2] == 'e':
		print("Dust on the walls? How old is this place?")
	elif current[-2] == 'w':
		print("You're thirsty. But not THAT thirsty.")

	
	
def game():
	while True:
		look = input("> ")
		if look == 'n':
			current.append('n')
			print("Thick, steel bars block your escape. A metal padlock hangs on the far right.")
			if 'key' in inventory:
				print("You found a key! Open the cell? y/n")
				affirm_open = input("> ")
				if affirm_open == "y":
					print("You're free!")
					print("Wow that was pretty easy")
					break
				else:
					print("You decide to look around some more.")
					continue
		elif look == 's':
			current.append('s')
			print("A dirty bed lies in the corner.")
			if 'key' not in inventory:
				print("A key rests on the pillow.")
				print("Take key? y/n")
				affirm_key = input("> ")
				if affirm_key == 'y':
					print("You pick up the key")
					inventory.append('key')
				elif affirm_key != 'y':
					print("You decide to not pick up the key.")
					continue
		elif look == 'e':
			current.append('e')
			print("A concrete wall solemnly greets you.")
		elif look == 'w':
			current.append('w')
			print("An empty toilet and a broken sink are plastered against the wall.")
		elif look != 'n' or 's' or 'e' or 'w': 
			print("Please enter a direction.")

# Find out how to see if player keeps looking at the same spot.
		
	
game()		
	