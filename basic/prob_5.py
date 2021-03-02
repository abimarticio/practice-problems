# Classic problem: Write a cashier register program which has at least 5 different items with different prices, 
# and takes in a list of the items purchased by the customer, 
# and computes the change. Account for senior citizens 
# and PWD discounts of 20% off the items. Sample run:

# 	>>> Choose items to purchase:
# 		[1] Burger (Php 30.00)
# 		[2] Fries (Php 25.00)
# 		[3] Chicken with rice (Php 70.00)
# 		[4] Spaghetti (Php 50.00)
# 		[5] Ice cream (Php 20.00)
# 	User input: 1
# 	>>> Is that all? (Y/N)

def user_input():
   
    list_items = []
    total_price = []

    while(True):
        user_input = int(input("Choose item to purchase:\n[1] Burger (Php 30.00)\n[2] Fries (Php 25.00)\n[3] Chicken with rice (Php 70.00)\n[4] Spaghetti (Php 50.00)\n[5] Ice cream (Php 20.00)\nUser input: "))

        if user_input == 1:
            item = "Burger"
            price = 30
            list_items.append(item)
            total_price.append(price)

        elif user_input == 2:
            item = "Fries"
            price = 25
            list_items.append(item)
            total_price.append(price)

        elif user_input == 3:
            item = "Chicken with rice"
            price = 70
            list_items.append(item)
            total_price.append(price)

        elif user_input == 4:
            item = "Spaghetti"
            price = 50
            list_items.append(item)
            total_price.append(price)

        elif user_input == 5:
            item = "Ice cream"
            price = 25
            list_items.append(item)
            total_price.append(price)


        addition = input("Is that all? ")
        if addition.upper() == "Y":
            break
            
        elif addition.upper() == "N":
            continue
    return total_price

def main():
    items = user_input()
    total = sum(items)
    print(f"Total amount: Php {total}")

    while True:
        cash_in = int(input("Enter cash: "))
        if cash_in >= total:
            discount = input("Do you have citizen/PWD discount? ")
            if discount.upper() == "Y":
                change = cash_in - (total - (total * .2))
                print(f"I have received Php {cash_in}, your change is Php{change}")
                
            elif discount.upper() == "N":
                change = cash_in - total
                print(f"I have received Php {cash_in}, your change is Php {change}")
            break
        else:
            print("Not enough cash. Try again.")
            continue
    
main()