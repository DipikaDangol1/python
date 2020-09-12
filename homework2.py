def guessNumber(start_num, last_num,guess_tries): 
	if start_num > last_num: 
		return True
	mid = (start_num + last_num)//2 #to find the middle of the range	
	while True:
		print("Is the number is ", mid, "? (yes/no)") #asking the user about the number guess by the computer
		user = input() 
		guess=guess_tries+1
		if user == "Yes" or user == "yes": #Condition to check if the guess number is correct or not
			print("I Successfully guessed your number in" ,guess, "tries")
			play=input("Do you wanna continue the game(yes/no)??")
			if play=="yes":
				play_again=guessNumber(start_num=1,last_num=100,guess_tries=0)
				return True
			else:
				print("bye bye")
				return False			
		else: 
			print("Actual number is greater than", mid, "?", end = " ") 
			user = input() 
			if user == "Yes" or user == "yes": 
				return guessNumber(mid+1, last_num,guess) 
			else: 
				return guessNumber(start_num, mid-1,guess)  			
if __name__ == "__main__": 
	name=input("Enter your name : ")
	print("hello, "+ name +"! Let us play the game") 
	print('Think of random number from 1 to 100, and I will try to guess it!')
	out=guessNumber(start_num=1,last_num=100,guess_tries=0)
	