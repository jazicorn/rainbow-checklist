checklist = list()


def create(item):
    checklist.append(item)


def read(index):
    return checklist[index]
    # int(index)
    # item = checklist[index]
    # return item


def update(index, item):
    checklist[index] = item


def destroy(index):
    checklist.pop(index)


def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1


def mark_completed(index, list_item):
    # solution to adding checkmark without error
    # https://stackoverflow.com/questions/16676101/print-the-approval-sign-check-mark-u2713-in-python
    print('√' + "{} {}".format(index, list_item))
    #checklist[index] = '√' + checklist[index]
    # print(checklist)


def select(function_code, index):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    # Read item
    elif function_code == "R":
        read(index)

    # Print all items
    elif function_code == "P":
        if len(checklist) > 0:
            list_all_items()
        else:
            print("Empty List")

    elif function_code == "D":
        destroy(index)

    elif function_code == "M":
        index = len(input(
            "Using the number paired to the item, which item do you want to check off?\n"))
        # if index == 0 | index > 1:
        #print("Error, one number please")
        # elif index is not index.isdigit():
        #    print("Error, no letters please")
        if index == 1:
            mark_completed(index)
            print(checklist)
        else:
            "unknown error"

    elif function_code == "Q":
        return

    # Catch all
    else:
        print("Unknown Option")

    return True


def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input


def test():

    create("purple sox")
    create("red cloak")
    create("red sox")

    print(read(0))

    if 0 <= len(checklist):
        for test_list in checklist:
            print(test_list)

    update(0, "purple socks")
    destroy(1)

    print(read(0))

    list_all_items()

    select("C")
    # View the results
    list_all_items()
    # Call function with new value
    select("R")
    # View results
    list_all_items()
    # Continue until all code is run


# test()


running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, P to display list,\nU to update list, D to remove list item, M to mark item as finished and Q to quit:\n")
    if len(selection) > 1:
        print("can only choose 1 action at a time")
    elif selection.isalpha():
        running = select(selection.upper())
    elif selection.isdigit():
        running = select(selection)
    else:
        print("Error Try Again")
