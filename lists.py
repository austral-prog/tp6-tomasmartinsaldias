# Replace the "ANSWER HERE" with your answer

#def remove_elements(list_to_remove_elements):
#    len_list = len(list_to_remove_elements)
#    if len_list == 0:
#        list_to_remove_elements = []
#    elif len_list >= 1 and len_list <= 4:
#        del list_to_remove_elements[0]
#    elif len_list == 5:
#        del list_to_remove_elements[4]
#        del list_to_remove_elements[0]
#    else:
#        del list_to_remove_elements[5]
#        del list_to_remove_elements[4]
#        del list_to_remove_elements[0]
#    return list_to_remove_elements

def remove_elements(list_to_remove_elements):
    len_list = len(list_to_remove_elements)
    if len_list >= 5:
        del list_to_remove_elements[5]
        del list_to_remove_elements[4]
    if len_list == 5:
        del list_to_remove_elements[4]
    if len_list >= 1:
        del list_to_remove_elements[0]
    return list_to_remove_elements

def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0, "Pink")
    list_to_add_elements.append("Yellow")
    return list_to_add_elements

def is_empty(list_to_check):
    check = False
    if list_to_check == []:
        check = True
    return check

def check_lists(list_to_compare1, list_to_compare2):
    check = False 
    if len(list_to_compare1) >= 3 and len(list_to_compare2) >= 3 and list_to_compare1[2] == list_to_compare2[2]:
        check = True
    return check

def list_of_lists(list_of_lists_to_modify):
    parte_1 = list_of_lists_to_modify[0][0:2]
    parte_2 = list_of_lists_to_modify[1][1:4]
    parte_3 = list_of_lists_to_modify[2][-2:]
    new_list = [parte_1, parte_2, parte_3]
    return new_list