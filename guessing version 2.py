import random 

x = random.randint(1,10)
	

while True:
	num=int(input(f"guess a number between 1 and 10 \n"))
	if num > x:
		print("****nope, its a smaller number****")
	elif num < x:
	    print("****nope, its a larger number****")
	elif num == "":
		print("enter a number dumbass")
	else:
	    print("correct, you guessed it right****")

	    playagain = input(f"DO YOU WANT TO PLAY AGAIN? (y/n) \n") 
	    if playagain == "y" or playagain == "Y":
	        x = random.randint(1,10)
	        num = ""
	    elif playagain == "":
	    	print("y or n ??")
	    else:	
	        print("thankyou for playing") 
	        break     	