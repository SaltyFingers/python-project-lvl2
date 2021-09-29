import json

differense = []
prefixes = {
    'same': '    ',
    'add': '  + ',
    'del': '  - ',
    }

def is_dictionary(object):
    return isinstance(object, dict)

def get_encoded_bools(file):
    for key in file:
        if type(file[key]) == bool:
            file[key] = json.JSONEncoder().encode(file[key])

# def search_in_one(part_of_file, prefix, file):
#     for key in sorted(part_of_file):
#         if is_dictionary(key):
#             differense.append(f'{prefix}{key}: ')
#             part_of_file = part_of_file.get(key)
#             file = file.get(key)
#             search_in_one(key, prefix, file)
#         else:
#             for k in sorted(part_of_file):

#               differense.append(f'{part_of_file[k]}')
#     # return sorted(differense)


# def search_in_both(part_of_file ,first_file, second_file):
#     for key in sorted(part_of_file):
#         differense.append(f'{prefixes["same"]}{key}: ')
#         if is_dictionary(key):
#             first_file = first_file.get(key)
#             second_file = second_file.get(key)
#             in_both = first_file.keys() & second_file.keys()
#             search_in_both(in_both, first_file, second_file)
#         if first_file[key] == second_file[key]:
#             differense.append(f'{first_file[key]}')
#         else:
#             differense.append(f'{prefixes["del"]}{first_file[key]}')
#             differense.append(f'{prefixes["add"]}{second_file[key]}')

    # return sodifferense
 

#  def sort_difference(difference):
#     for key in difference:
#         differense = sorted(differense, key=lambda x: x[4])

def search_difference(first_file, second_file):
    in_first = first_file.keys()
    in_second = second_file.keys()
    for key in in_first, in_second:
        
        if key in list(in_first) and key not in list(in_second):
            differense.append(f'- {key}: {first_file[key]}')
       
        elif key not in list(in_first) and key in list(in_second):
            differense.append(f'+ {key}: {second_file[key]}')
        
        elif key in list(in_first) and key in list(in_second):
            if first_file[key] == second_file[key]:
                differense.append(f' {key}: {first_file[key]}')
            else:
                differense.append(f'- {key}: {first_file[key]}')
                differense.append(f'+ {key}: {second_file[key]}')
        if is_dictionary(key):
            first_file = first_file.get(key)
            second_file = second_file.get(key)
            search_difference(first_file, second_file)





# contains_only_in_first_file = first_file.keys() - second_file.keys()
# contains_only_in_second_file = second_file.keys() - first_file.keys()
# contains_in_both_files = first_file.keys() & second_file.keys()
# differense = []
# for key in contains_only_in_first_file:
#     differense.append(f'{prefixes["del"]}{key}: {first_file[key]}')
#     if is_dictionary(key):
# for key in contains_only_in_second_file:
#     differense.append(f'  + {key}: {second_file[key]}')
# for key in contains_in_both_files:
#     if first_file[key] == second_file[key]:
#         differense.append(f'    {key}: {first_file[key]}')
#     else:
#         differense.append(f'  - {key}: {first_file[key]}')
#         differense.append(f'  + {key}: {second_file[key]}')
