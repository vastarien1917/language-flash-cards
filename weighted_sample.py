import random

def weighted_sample(language_list,total_element_number,sublist_index=None,focused_element_number=None):        

    sample = []
    if sublist_index == None:
        big_boy = []
        for sublist in language_list:
            big_boy += sublist
        sample = random.sample(big_boy,total_element_number)
    else:
        focused_list = language_list[sublist_index]
        clipped_list = language_list.copy()
        clipped_list = clipped_list[:sublist_index]
        unfocused_list = []
        for sublist in clipped_list:
            unfocused_list += sublist
        unfocused_element_number = total_element_number - focused_element_number
        focused_sample = random.sample(focused_list,focused_element_number)
        unfocused_sample = random.sample(unfocused_list,unfocused_element_number)
        sample = focused_sample + unfocused_sample
        random.shuffle(sample)
    

    for element in sample:
        print(element)
