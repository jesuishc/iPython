# -*- coding: utf-8 -*-
"""printing recursive function by jesuishc"""

# building recursive function

def print_lol(the_list, level):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            for tab_stop in range(level):
                print("\t")
            print(each_item)
