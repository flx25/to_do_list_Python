to_do_list = []

def read_in_list():
	with open("todo.txt", "r") as file:
		for line in file:
			to_do_list.append(line.strip())
	if to_do_list:
		print("List has been loaded.")

def main_loop():
	if to_do_list:
		print ("To do:")
		for index, item in enumerate(to_do_list):
			print(f"{index + 1}. {item}")
		print("")
	user_input = input("Enter things you want to add, exit to quit and rm to remove an entry, use clear to clear the list:")
	return user_input

if __name__ == "__main__":
	print("Welcome to the To do list!")
	read_in_list()
	while True:
		result = main_loop()

		if result.lower() == 'exit':
			print("\nThanks for using the to do list, your list has been saved!")
			file_path = "todo.txt"
			with open(file_path, "w") as file:
				for item in to_do_list:
					file.write(item + "\n")
			break
		elif result.lower() == 'rm':
			user_input = input("Which entry Nr do you want to remove?")
			to_do_list.pop(int (user_input) -1)
		elif result.lower() == 'clear':
			to_do_list.clear()
			print("Your list has been cleared.")
		else:
			to_do_list.append(result)


