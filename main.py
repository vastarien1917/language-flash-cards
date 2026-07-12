import random

from catullus_63 import catullus_63
from neo_assyrian_signs import neo_assyrian_signs
from ur_III_signs import ur_III_signs
from classical_arabic_vocab import classical_arabic_vocab

lists = {
    "catullus 63" : catullus_63,
    "neo-assyrian signs": neo_assyrian_signs,
    "ur III signs": ur_III_signs,
    "classical arabic vocab": classical_arabic_vocab,
    }

should_quit = False

from weighted_sample import weighted_sample

def print_lists():
    out_string = ""
    for i, key in enumerate(lists):
        out_string += str(i+1) + ": " + key +"\n"
    return out_string

def total_elements(language_list):
    total_elements = 0
    for sublist in language_list:
        total_elements += len(sublist)
    return total_elements

def choose_list():
    global should_quit
    print_lists()

    while True:
        try:
            printed_lists = print_lists()
            num_lists = str(len(lists))
            #index = (int(input(f"\nThere are {num_lists} lists:\n{printed_lists}Which list would you like to study? press q to quit\n")) -1)
            index = (input(f"\nThere are {num_lists} lists:\n{printed_lists}\nWhich list would you like to study? press q to quit\n"))
            if index == "q":
                should_quit = True
                break
            elif 0 <= (int(index)-1) < len(lists):
                key = list(lists.keys())[(int(index)-1)]
                return key
            else:
                print("Input must correspond to a list\n")
        except ValueError:
            print("Input must be an integer.\n")

def choose_focus(list_key):
    global should_quit
    focus = False
    language_list = lists[list_key]
    if len(language_list) == 1:
        focus = False
    else:
        while True:
            user_input = input("Would you like to focus? y/n\n")
            if user_input == "y":
                focus = True
                break
            elif user_input == "n":
                focus = False
                break
            elif user_input == "q":
                should_quit = True
                break
            else:
                print("This is a yes or no question.")
    return focus

def choose_sublist_index(list_key):
    global should_quit
    language_list = lists[list_key]
    length = len(language_list)
    if length == 1:
        return None
    else:
        while True:
            try:
                #index = (int(input(f"{list_key} has {length} entries. Which one would you like to focus on?\n")) -1)
                index = (input(f"{list_key} has {length} entries. Which one would you like to focus on?\n"))
                if index == "q":
                    should_quit = True
                    break
                index = (int(index) - 1)
                if 0 <= index < len(language_list):
                    return index
                else:
                    print("Please type a number corresponding to an index")

            except ValueError:
                print("Please choose an integer.")

def choose_focused_element_number(list_key,sublist_index):
    global should_quit
    language_list = lists[list_key]
    max_number = len(language_list[sublist_index])
    focused_element_number = 0
    if max_number == 1:
        focused_element_number = max_number
    else:
        while True:
            try:
                #user_input = (int(input(f"Sublist {sublist_index + 1} of {list_key} has {max_number} elements. How many would you like to include?\n")))
                user_input = (input(f"Sublist {sublist_index + 1} of {list_key} has {max_number} elements. How many would you like to include?\n"))
                if user_input == "q":
                    should_quit = True
                    break
                user_input = int(user_input)
                if 0 < user_input <= max_number:
                    focused_element_number = user_input
                    break
                else:
                    print("Please type a number between 1 and the total elements in the sublist.")
            except ValueError:
                print("Please choose an integer.")
    return focused_element_number

def choose_unfocused_element_number(list_key,focus_index=None):
    global should_quit
    language_list = lists[list_key].copy()
    unfocused_string = ""
    unfocused_element_number = 0
    if focus_index:
        unfocused_string = " unfocused"
        language_list = language_list[:focus_index]
        
    max_elements = total_elements(language_list)
    while True:
        try:
            user_input = input(
                f"There are {max_elements}{unfocused_string} elements in earlier sublists. How many elements in them would you like to include?\n")
            if user_input == "q":
                should_quit = True
                break
            user_input = int(user_input)
            if 0 < user_input <= max_elements:
                unfocused_element_number = user_input
                break
            else:
                print("Please type a number between 1 and the total available elements.")
        except ValueError:
            print("Please choose an integer.")

    return unfocused_element_number

def go_again():
    global should_quit
    while True:
        user_input = input("Press enter to go again with the same parameters, press any other key to back out\n")
        if user_input == "":
            go_again = True
            break
        elif user_input == "q":
            go_again = False
            should_quit = True
            break
        else:
            go_again = False
            break
    return go_again

def should_i_quit():
    while True:
        user_input = input("Quit? y/n\n")
        if user_input == "y":
            should_i_quit = True
            break
        elif user_input == "n":
            should_i_quit = False
            break
        else:
            print("It's a yes or no question.")
    return should_i_quit

while True:

    list_key = choose_list()
    if should_quit == True:
        break
    language_list = lists[list_key]
    if should_quit == True:
        break
    focus = choose_focus(list_key)
    if should_quit == True:
        break
    focused_element_number = 0
    sublist_index = None
    if focus:
        sublist_index = choose_sublist_index(list_key)
        if should_quit == True:
            break
        focused_element_number = choose_focused_element_number(list_key,sublist_index)
        if should_quit == True:
            break

    unfocused_element_number = 0
    if sublist_index != 0:
        unfocused_element_number = choose_unfocused_element_number(list_key,sublist_index)
    if should_quit == True:
        break
    total_element_number = focused_element_number + unfocused_element_number
    if should_quit == True:
        break

    print("")
    if focus:
        weighted_sample(language_list,total_element_number,sublist_index,focused_element_number)
    else:
        weighted_sample(language_list,total_element_number)
    print("")
    while go_again():
        #print("")
        if focus:
            weighted_sample(language_list,total_element_number,sublist_index,focused_element_number)
        else:
            weighted_sample(language_list,total_element_number)
        print("")

        if should_quit == True:
            break

    if should_quit == True:
        break
