while True:
	num1 = int(input("Enter first number: "))
	num2 = int(input("Enter second number: "))
	operation = input("Enter what operation you want to do: ")

	if operation == "+":
		print(num1 + num2)
	elif operation == "-":
		print(num1 - num2)
	elif operation == "*":
		print(num1 * num2)
	elif operation == "/":
		if num2 != 0:
			print(num1 / num2)
		else:
			print("Num2 shouldn't be 0")
	else:
		print("Invalid operation")
	again = input("Do you want to calculate again? (yes/no): ")
	if again == "no":
    		break
	elif again == "yes":
    		pass
	else:
    		print("Invalid Answer")