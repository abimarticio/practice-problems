# Write a program that can add, update, delete a list based on user input

my_list = []

while True:
    mode = input("Do you want to add, update or delete text on your list? ")
    if mode.lower() == "add":
        user_input = input("Enter the text you want to add: ")
        my_list.append(user_input)
        
    elif mode.lower() == "update":
        user_input = input("Enter the text you want to update: ")
        new_text = input("Enter the new text: ")
        for index in range(len(my_list)):
            if my_list[index] == user_input:
                my_list[index] = new_text
                break
        
    elif mode.lower() == "delete":
        user_input = input("Enter the text you want to delete: ")
        my_list.remove(user_input)

    else:
        break

    print("Success!")