to_do_list = []

def main_loop():
	if to_do_list:
		print ("To do:")
		for index, item in enumerate(to_do_list):
			print(f"{index + 1}. {item}")
		print("")
	user_input = input("Enter things you want to add, exit to quit and rm to remove an entry, use help to show this dialoge:")
	return user_input

if __name__ == "__main__":
	print("Welcome to the To do list!")

	while True:
		result = main_loop()

		if result.lower() == 'exit':
			print("Thanks for using the to do list!")
			break
		elif result.lower() == 'rm':
			user_input = input("Which entry Nr do you want to remove?")
			to_do_list.pop(int (user_input) -1)
		else:
			to_do_list.append(result)


