# Imports
import sys
# from termcolor import colored
from os import system, name

#Create our checklist
checklist = list()

#Define Functions
def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

#helper functions
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item.title()))
        index += 1

def mark_completed(index):
    checklist[index] = '√ ' + checklist[index]
    return checklist[index]

def uncheck(index):
    checklist[index][int(index)] = checklist[int(index)].replace('√', '')
    return checklist[index]

def user_input(prompt):
    user_input = input(prompt).upper()
    return user_input;

# Clear terminal between user selection for readability
def clear():
    if name == 'nt':
        _=system('cls')
    else:
        _=system('clear')

#Select
def select(function_code):
    # Create list_item
    if function_code =='C':
        input_item = user_input("Add item to your list: ")
        create(input_item);
        return True
        clear()

    # Read list_item
    elif function_code == 'R':
        item_index = user_input("Enter index of item you'd like to view: ")
        # Remember that item_index must actually exist or our program will crash.
        print(read(int(item_index)))
        return True

    # Print all items
    elif function_code =='P':
        list_all_items()
        print('\n')
        return True

    elif function_code == 'U':
        item_index = user_input("Enter index of item you want to update: ")
        input_item = user_input("Enter replacement item: ")
        update(int(item_index), input_item)
        return True

    elif function_code == "M" :
        item_index = user_input("Enter index of item you'd like to check off: ")
        mark_completed(int(item_index))
        list_all_items()
        return True

    elif function_code == "UM" :
        item_index = user_input("Enter index of item you want to uncheck: ")
        uncheck(int(item_index))
        list_all_items()
        return True

    elif function_code == "D":
        input_item = int(user_input("What is the index number of the item you want to destroy?"))
        destroy(input_item)
        return True

    elif function_code == "Q":
        return False

    # Catch all
    else:
        print("Unknown Option")
        return True


running = True

while running:
    print("\nWelcome to Rainbow Checklist!")
    selection = user_input(
      "\nPress 'C' to add an item to your list.\nPress 'R' to read one particular item from your list.\nPress 'P' to view all list items.\nPress 'U' to update your list.\nPress 'M' to check an item off your list.\nPress 'UM' if you want to uncheck an item from the list. \nPress 'D' to delete an item from your list.\nPress 'Q' to quit!\n\n")

    # if selection != str('P') or :
    #     running = select(selection)
    #     clear()
    # else:
    running = select(selection)




# #test function
# def test():
#     create("purple sox)")
#     create("red cloak")
#
#     print(read(0))
#     print(read(1))
#
#     update(0, "purple socks")
#
#     destroy(1)
#
#     print(read(0))
#
#     select('C')
#
#     select('R')
#
#     list_all_items()
#
#     user_value = user_input("Please Enter a value:")
#     print(user_value)
#
# test();
