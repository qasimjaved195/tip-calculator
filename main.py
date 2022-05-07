#Tip calculator

#Greetins
print("Welcome to the tip calculator.")

#Input for total bill
bill = float(input("What was the total bill?\n$"))

#input percentage tip
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))

#input number of people
num_of_people = int(input("How many people to split the bill?\n"))

#calculating percentage amount of tip
amount_of_tip = bill * percentage_tip / 100

#adding tip to the bill
total_bill = bill + amount_of_tip

#calculating total amount to pay by each person
bill_of_each_person = total_bill / num_of_people

#rounding the bill to 2 decimal points and printing amount to be paid by each person
print(f"Each person should pay: ${round(bill_of_each_person, 2)}")