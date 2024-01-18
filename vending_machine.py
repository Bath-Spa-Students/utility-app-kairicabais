

#                                            Kairi's Vending Machine Program


bubble_tea=[
{"code":"A1",                                                      # code of product
 "name": "black sugar boba + pearl coffee latte",                  # name of product
 "price": 18.50 ,                                                  # price of product
 "stock" : 8,},                                                    # stock left of product

{"code":"A2",                                                      # code of product
 "name": "mango sago bubble tea",                                  # name of product
 "price": 12.75 ,                                                  # price of product
 "stock" : 17,},                                                   # stock left of product

{"code":"A3",                                                      # code of product
 "name": "matcha black sugar boba milk with cream mousse",         # name of product
 "price": 14.00 ,                                                  # price of product
 "stock" : 12,},                                                   # stock left of product

{"code":"A4",                                                      # code of product
 "name": "strawberry mochi with cream mousse",                     # name of product
 "price": 20.50 ,                                                  # price of product
 "stock" : 6,},                                                    # stock left of product

{"code":"A5",                                                      # code of product
 "name": "taro + taro pudding black sugar boba milk",              # name of product
 "price": 15.75 ,                                                  # price of product
 "stock" : 6,},                                                    # stock left of product

]




# list of pastries to go with the bubble teas

Pâtisserie=[

{"code":"B1",                                                     # code of product
 "name": "Taiwanese Brown Sugar Cake",                            # name of product
 "price": 6 ,                                                     # price of product
 "stock" : 17,},                                                  # stock left of product
   
{"code":"B2",                                                     # code of product
 "name": "Bubble waffles + nutella and pistachio",                # name of product
 "price": 8 ,                                                     # price of product
 "stock" : 12,},                                                  # stock left of product

{"code":"B3",                                                     # code of product
 "name": "Strawberry Melon Cake",                                 # name of product
 "price": 10 ,                                                    # price of product
 "stock" : 12,},                                                  # stock left of product

{"code":"B4",                                                     # code of product
 "name": "Mango Bear Muffins",                                    # name of product
 "price": 8 ,                                                     # price of product
 "stock" : 6,},                                                   # stock left of product

{"code":"B5",                                                    # code of product
 "name": "taro with sticky rice",                                # name of product
 "price": 5 ,                                                    # price of product
 "stock" : 6,},                                                  # stock left of product

]






# print the title of my vending machine using text art 
print("\n\t\t\tｔｈｅ   ｃａｆｅ    ｖｅｎｄｉｎｇ     ｍａｃｈｉｎｅ\n")


print ("\n\tToday, on our bubble tea menu, we have...")

# Vending machine items and prices
print ('''\n 
         Bubble Teas 🧋                                                Price             Code             Stock\n
       black sugar boba + pearl coffee latte                           AED 18.50           A1                2
       mango sago bubble tea                                           AED 12.75           A2                17
       matcha black sugar boba milk with cream mousse                  AED 14.00           A3                12
       strawberry mochi with cream mousse                              AED 20.50           A4                6
       taro + taro pudding black sugar boba milk                       AED 15.75           A5                6
       ''')


print ('''\n 
         Pâtisserie  🍨                                                 Price             Code             Stock\n
       Taiwanese Brown Sugar Cake                                       AED 6              B1                2
       Mango Bear Muffins                                               AED 6              B2                1
       Bubble waffles + nutella and pistachio                           AED 6              B3                3
       Strawberry Melon Cake                                            AED 7              B4                1
       taro with sticky rice                                            AED 6              B5                0
       ''')


purchased_item = []                                          # An empty list to purchased item
total = []                                                   # An empty list to put total amount calculations
anykey = input("\n Press any key to proceed...\n")           # The user will press any key to continue
print("\npress q to quit and proceed with payment\n")        # The user can proceed to payment by entering q


# This code manages the number of products in stocks. 
# If the number goes below 0, the user will be informed that the product is sold out.
   
 # Stock for bubble_tea drinks
A1_stock = 2
A2_stock = 2
A3_stock = 3
A4_stock = 1
A5_stock = 0


 # stock for Pâtisserie 
B1_stock = 12
B2_stock = 17
B3_stock = 12
B4_stock = 6
B5_stock = 6


# This code manages the price of products. 
# For calculating the change, it was easier for me to use this data through this assigning of price variables.

# price for bubble_tea
A1_price = 18.50
A2_price = 12.75
A3_price = 14.00
A4_price = 20.50
A5_price = 15.75

# price for bubble_tea
B1_price = 6
B2_price = 6
B3_price = 6
B4_price = 7
B5_price = 6



# My vending Machine's main function for managing user money and accepting orders.

def main():
    
    balance = float(input("\nInsert your budget: \n"))
    balance 


# a while loop that will keep on repeating until the user enters 'q'
while True: 

# ask user for the product code of the product they want to purchase.
    buy = input("\nEnter the code ")


# to quit buying, user can type q
    if buy == "q":                                
         print("Thank you for choosing the cafe vending machine. Have a good day! \n")
         break


# An if-elif-else chain that process the code, smart suggests a complementary product, balance-handling, and stock recording. 
    
    elif buy == "A1" :
     print("\nYou have selected the black sugar boba + pearl coffee latte 18.50 AED \n")
     balance = float(input("\nInsert your budget: \n"))
    if balance == 0 or balance < 18.50:                   # ternary operator
        print("insufficient balance")
        balance = float(input("\nEnter the valid amount 18.50 AED or more: "))
        balance += A1_price
    else:
        balance -= A1_price
        print("\nYour black sugar boba + pearl coffee latte has been dispensed. Enjoy!")
        print("Your change " , balance, "AED has been dispensed\n")
        suggestion = input("\nTaiwanese Brown Sugar Cake goes well with your order. Would you like to pair it with your drink?\n yes or no\n")
        if suggestion == "yes" :    # smart suggestion option, which allows user to pair their current order with a complementary dessert
            print("\n Enter only 6 AED to add Taiwanese Brown Sugar Cake\n")
            secondary_purchase = float(input("\nAdd 6 AED here: "))
            if secondary_purchase == 6 :
                print("Item has been dispensed. Thank you for trying the Taiwanese Brown Sugar Cake!") 
        else:
# Display menu 
                print("\n\t\t\tｔｈｅ   ｃａｆｅ    ｖｅｎｄｉｎｇ     ｍａｃｈｉｎｅ\n")

        print ("\n\tToday, on our bubble tea menu, we have...")

# Vending machine items and prices
        print ('''\n 
         Bubble Teas 🧋                                                Price             Code             Stock\n
       black sugar boba + pearl coffee latte                           AED 18.50           A1                2
       mango sago bubble tea                                           AED 12.75           A2                17
       matcha black sugar boba milk with cream mousse                  AED 14.00           A3                12
       strawberry mochi with cream mousse                              AED 20.50           A4                6
       taro + taro pudding black sugar boba milk                       AED 15.75           A5                6
       ''')


        print ('''\n 
         Pâtisserie  🍨                                                 Price             Code             Stock\n
       Taiwanese Brown Sugar Cake                                       AED 6              B1                2
       Mango Bear Muffins                                               AED 6              B2                1
       Bubble waffles + nutella and pistachio                           AED 6              B3                3
       Strawberry Melon Cake                                            AED 7              B4                1
       taro with sticky rice                                            AED 6              B5                0
       ''')
        
        pass

        balance = 0                                  # this subtracts the price to the budget the user had entered
        purchased_item.append("black sugar boba + pearl coffee latte       18.50 AED")
        total.append(6.00)                                # this adds the new amount of balance to the total
        A1_stock -= 1
        if A1_stock == 0:                                 # This controls the stock count a user is able to buy
            print("\n Sorry, we ran out of the black sugar boba + pearl coffee latte! Proceed with payment.\n")
            break                                         # this stops the chain for this smart suggestion
        
        


        elif buy == "A2":
         balance = float(input("\nInsert your budget: \n"))
    if balance == 0 or balance <= 12.75:
        print("insufficient balance")
        balance = float(input("\nEnter the valid amount 12.75 AED or more: "))
        balance += balance
    else:
        balance -= balance
        print("\nYour mango sago bubble tea has been dispensed. Enjoy!")
        print("Your change ", balance, "AED has been dispensed\n")
        suggestion = input("\n Would you like to try the Mango Bear Muffins with your order for 6 AED?\n [1] Yes [2] No\n")
        if suggestion == "1" :                          # smart suggestion option, which allows user to pair their current order with a complementary dessert
            print("\n Enter B2 to add Mango Bear Muffins for 6 AED\n")
            secondary_purchase = float(input("\nAdd 6 AED here: "))
            if secondary_purchase == 6 :
                print("Item has been dispensed. Thank you for trying the Mango Bear Muffins!")
            else: 
                balance -= 6
            pass                                         # this repeats the loop so that the vending machine is still running, and can get more orders
    
        purchased_item.append("mango sago bubble tea       6 AED")
        total.append(6.00)                               # this adds the new amount of balance to the total
        A2_stock -= 1
        if A2_stock == 0:                                # This controls the stock count a user is able to buy
            print("\n Sorry, we ran out of the mango sago bubble tea! Proceed with payment.\n")
            break                                        # this stops the chain for this smart suggestion

        
    
        elif buy == "A3":
          print("\nYou have selected the matcha black sugar boba milk with cream mousse 14.00 AED \n")
          balance = float(input("\nInsert your budget: \n"))
    if balance == 0 or balance <= 14.00:
        print("insufficient balance")
        insufficient = (input("\nEnter the valid amount 14.00 AED or more: "))
        if insufficient == 'yes' :
         balance = float(input("\nEnter the valid amount 14.00 AED or more: "))
         balance += balance
        else:
         print("\nYour matcha black sugar boba milk with cream mousse has been dispensed. Enjoy!")
         suggestion = input("\nBubble waffles + nutella and pistachio goes well with your order. Would you like to add to your cart?\n  yes or no\n")
        if suggestion == "yes" :                        # smart suggestion option, which allows user to pair their current order with a complementary dessert
            print("\n Add 6 AED to avail Bubble waffles + nutella and pistachio\n")
            secondary_purchase = float(input("\nAdd 6 AED here: "))
        if secondary_purchase < 6 :
                print("Thank you for trying the Bubble waffles + nutella and pistachio!")
                balance -= 6
        else:
            pass                                        # this repeats the loop so that the vending machine is still running, and can get more orders
        balance -= 12.75                                # this subtracts the price to the budget the user had entered
        purchased_item.append("mango sago bubble tea       12.75 AED")
        total.append(12.75)                             # this adds the new amount of balance to the total
        A3_stock -= 1
        if A3_stock < 0:                                # This controls the stock count a user is able to buy
            print("\n Sorry, we ran out of the mango sago bubble tea! Proceed with payment.\n")
            break                                       # this stops the chain for this smart suggestion



# elif statement to test multiple conditions smoothly 
        elif buy == "A4":
         print("\nYou have selected the strawberry mochi with cream mousse 20.50 AED\n")
         balance = float(input("\nInsert your budget: \n"))
    if balance == 0 or balance <= 20.50:
        print("insufficient balance")
        balance = float(input("\nEnter the valid amount 20.50 AED or more: "))
        balance += balance
    else:
        balance -= balance
        print("\nYour strawberry mochi with cream mousse has been dispensed. Enjoy!")
        print("Your change ", balance, "AED has been dispensed\n")
        suggestion = input("\nStrawberry Melon Cake goes well with your order. Would you like to add to your cart?\n [1] Yes [2] No\n")
        if suggestion == "1" :    # smart suggestion option, which allows user to pair their current order with a complementary dessert
            print("\n Enter B2 to add Strawberry Melon Cake for 6 AED\n")
            secondary_purchase = float(input("\nAdd 6 AED here: "))
            if secondary_purchase == 6 :
                print("Item has been dispensed. Thank you for trying the Strawberry Melon Cake!")
            else: 
                balance -= 6
            pass                                           # this repeats the loop so that the vending machine is still running, and can get more orders
        balance -= 20.50                                   # this subtracts the price to the budget the user had entered
        purchased_item.append("strawberry mochi with cream mousse       20.50 AED")
        total.append(6.00)                                 # this adds the new amount of balance to the total
        A4_stock -= 1
        if A4_stock == 0:                                  # This controls the stock count a user is able to buy
            print("\n Sorry, we ran out of the strawberry mochi with cream mousse! Proceed with payment.\n")
            break                                          # this stops the chain for this smart suggestion


        
        elif buy == "A5":
         print("\nYou have selected the taro + taro pudding black sugar boba milk \n")
         balance = float(input("\nInsert your budget: \n"))
    if balance == 0 or balance <= 12.75:
        print("insufficient balance")
        balance = float(input("\nEnter the valid amount 12.75 AED or more: "))
        balance += balance
    else:
        balance -= balance
        print("\nYour taro + taro pudding black sugar boba milk has been dispensed. Enjoy!")
        print("Your change ", balance, "AED has been dispensed\n")
        suggestion = input("\ntaro with sticky rice goes well with your order. Would you like to add to your cart?\n [1] Yes [2] No\n")
        if suggestion == "1" :    # smart suggestion option, which allows user to pair their current order with a complementary dessert
            print("\n Enter B2 to add taro with sticky rice for 6 AED\n")
            secondary_purchase = float(input("\nAdd 6 AED here: "))
            if secondary_purchase == 6 :
                print("Item has been dispensed. Thank you for trying the taro with sticky rice !")
            else: 
                balance -= 6
            pass                                           # this repeats the loop so that the vending machine is still running, and can get more orders
        balance -= 18.50                                   # this subtracts the price to the budget the user had entered
        purchased_item.append("taro + taro pudding black sugar boba milk       6 AED")
        total.append(6.00)                                 # this adds the new amount of balance to the total
        A5_stock -= 1
        if A5_stock == 0:                                  # This controls the stock count a user is able to buy
            print("\n Sorry, we ran out of the taro + taro pudding black sugar boba milk! Proceed with payment.\n")
            break                                          # this stops the chain for this smart suggestion



        
        elif buy == "B1" :
           print ("\nYou chose the Taiwanese Brown Sugar Cake 6 AED \n")
        balance = float(input("\nInsert your budget: \n"))
    if balance < 6:                                               
        print("insufficient balance")
        balance = float(input("\nEnter the valid amount 6 AED or more: "))
        balance += B1_price
    else:
        balance -= B1_price
        print("\nYour Taiwanese Brown Sugar Cake has been dispensed. Enjoy!")
        print("Your change " , balance, "AED has been dispensed\n")
        balance -= 18.50                                       # this subtracts the price to the budget the user had entered
        purchased_item.append("Taiwanese Brown Sugar Cake         6 AED")
        total.append(6.00)                                     # this adds the new amount of balance to the total
        B1_stock -= 1
        if B1_stock == 0:                                      # This controls the stock count a user is able to buy
            print("\n Sorry, we ran out of the Taiwanese Brown Sugar Cake! Proceed with payment.\n")
            break                                                        



        elif buy == "B2" :
           print ("\nYou chose the Mango Bear Muffins  6 AED\n")
        balance = float(input("\nInsert your budget: \n"))
    if balance < 6:                                                     # ternary operator
        print("insufficient balance")
        balance = float(input("\nEnter the valid amount 6 AED or more: "))
        balance += B2_price
    else:
        balance -= B2_price
        print("\nYour Mango Bear Muffins has been dispensed. Enjoy!")
        print("Your change " , balance, "AED has been dispensed\n")
        balance -= 18.50                                               # this subtracts the price to the budget the user had entered
        purchased_item.append(" Mango Bear Muffins        6 AED")
        total.append(6.00)                                             # this adds the new amount of balance to the total
        B2_stock -= 1
        if B2_stock == 0:                                              # This controls the stock count a user is able to buy
            print("\n Sorry, we ran out of the Mango Bear Muffins! Proceed with payment.\n")
            break                                                     




        elif buy == "B3" :
           print ("\nYou chose the Bubble waffles + nutella and pistachio 6 AED \n")
        balance = float(input("\nInsert your budget: \n"))
    if balance < 6:                                                    # ternary operator
        print("insufficient balance")
        balance = float(input("\nEnter the valid amount 6 AED or more: "))
        balance += B3_price
    else:
        balance -= B3_price
        print("\nYour Bubble waffles + nutella and pistachio has been dispensed. Enjoy!")
        print("Your change " , balance, "AED has been dispensed\n")
        balance -= 6                                                   # this subtracts the price to the budget the user had entered
        purchased_item.append("Bubble waffles + nutella and pistachio      6 AED")
        total.append(6.00)                                             # this adds the new amount of balance to the total
        B3_stock -= 1
        if B3_stock == 0:                                              # This controls the stock count a user is able to buy
            print("\n Sorry, we ran out of the Bubble waffles + nutella and pistachio! Proceed with payment.\n")
            break    




        elif buy == "B4" :
           print ("\nYou chose the Strawberry Melon Cake 7 AED \n")
        balance = float(input("\nInsert your budget: \n"))
    if balance < 7:                                                    # ternary operator
        print("insufficient balance")
        balance = float(input("\nEnter the valid amount 7 AED or more: "))
        balance += B4_price
    else:
        balance -= B4_price
        print("\nYour Strawberry Melon Cake has been dispensed. Enjoy!")
        print("Your change " , balance, "AED has been dispensed\n")
        balance -= 7                                                   # this subtracts the price to the budget the user had entered
        purchased_item.append("Strawberry Melon Cake       7 AED")
        total.append(7.00)                                             # this adds the new amount of balance to the total
        B4_stock -= 1
        if B4_stock == 0:                                              # This controls the stock count a user is able to buy
            print("\n Sorry, we ran out of the Strawberry Melon Cake! Proceed with payment.\n")
            break    




        elif buy == "B5" :
           print ("\nYou chose the taro with sticky rice 6 AED \n")
        balance = float(input("\nInsert your budget: \n"))
    if balance < 6:                   #ternary operator
        print("insufficient balance")
        balance = float(input("\nEnter the valid amount 6 AED or more: "))
        balance += B5_price
    else:
        balance -= B5_price
        print("\nYour taro with sticky rice has been dispensed. Enjoy!")
        print("Your change " , balance, "AED has been dispensed\n")
        balance -= 6                                  # this subtracts the price to the budget the user had entered
        purchased_item.append("taro with sticky rice       6 AED")
        total.append(6.00)                                # this adds the new amount of balance to the total
        B5_stock -= 1
        if B5_stock == 0:                                 # This controls the stock count a user is able to buy
            print("\n Sorry, we ran out of the taro with sticky rice! Proceed with payment.\n")
            break    



 # anything that is not listed as a code above, will inform the user that it is an invalid code
        else:                                      # else statement     
          print("Your change " , balance, "AED has been dispensed\n")
        break



# calling the main function
main()                                               


# end of my vending machine