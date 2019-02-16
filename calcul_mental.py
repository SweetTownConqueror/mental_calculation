import Addition
import Soustraction
import Multiplication
import Division
import sys
import random
import time
import _thread
# first arg : operation
# 1 addition 2 soustraction 3 multiplication 4 division
# 5 all 

# second arg : number of digits of first number
number_one = 0
number_two = 0
def generate_number_one():
	if sys.argv[2]=="1":
		number_one = random.randint(0, 9)
	if sys.argv[2]=="2":
		number_one = random.randint(0, 99)
	if sys.argv[2]=="3":
		number_one = random.randint(0, 999)
	return number_one

# third arg : number of digits of second number
def generate_number_two():
	if sys.argv[3]=="1":
		number_two = random.randint(1, 9)
	if sys.argv[3]=="2":
		number_two = random.randint(1, 99)
	if sys.argv[3]=="3":
		number_two = random.randint(1, 999)
	return number_two

#temps en sec
#timee = 5

nb_repet = 20
good_response = 0
for i in range(nb_repet):
	number_one = generate_number_one()
	number_two = generate_number_two()

	if sys.argv[1]=="1":
		a = Addition.Addition(number_one,number_two)
		user_input = input ("Enter result : ")
		try:
			val = int(user_input)
			#print("Yes input string is an Integer.")
			print("Input number value is: ", val)
			if val == a.getResult():
				good_response = good_response+1
				print("Good job!")
			else:
				print("Wrong ! Answer is : "+str(a.getResult()))
		except ValueError:
		   print("Error :  not an integer")

	if sys.argv[1]=="2":
		a = Soustraction.Soustraction(number_one,number_two)
		user_input = input ("Enter result : ")
		try:
			val = int(user_input)
			#print("Yes input string is an Integer.")
			print("Input number value is: ", val)
			if val == a.getResult():
				good_response = good_response+1
				print("Good job!")
			else:
				print("Wrong ! Answer is : "+str(a.getResult()))
		except ValueError:
		   print("Error :  not an integer")

	if sys.argv[1]=="3":
		a = Multiplication.Multiplication(number_one,number_two)
		user_input = input ("Enter result : ")
		try:
			val = int(user_input)
			#print("Yes input string is an Integer.")
			print("Input number value is: ", val)
			if val == a.getResult():
				good_response = good_response+1
				print("Good job!")
			else:
				print("Wrong ! Answer is : "+str(a.getResult()))
		except ValueError:
		   print("Error :  not an integer")

	if sys.argv[1]=="4":
		while number_one%number_two!=0:
			number_one = generate_number_one()
			number_two = generate_number_two()	
		a = Division.Division(number_one,number_two)
		user_input = input ("Enter result : ")
		try:
			val = int(user_input)
			#print("Yes input string is an Integer.")
			print("Input number value is: ", val)
			if val == a.getResult():
				good_response = good_response+1
				print("Good job!")
			else:
				print("Wrong ! Answer is : "+str(a.getResult()))
		except ValueError:
		   print("Error :  not an integer")
print("The end! your score : "+str(good_response)+"/"+str(nb_repet))


#a = Addition.Addition(2, 2)