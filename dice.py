for i in range(1,7):
	r = input("Press r to roll and q to quit ")
	if r=="r":
		if i==1 or i==3 or i==4:
			print("You go ",6)
		elif i==2 or i==5:
			print("You got ", 2)
		else:
			print("You got ", 3)	
	elif r == "q":
		print("You lose")
		exit()
print("You won!!")