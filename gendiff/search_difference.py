def search_difference(first_file, second_file):
    contains_only_in_first_file = first_file.keys() - second_file.keys()
    contains_only_in_second_file = second_file.keys() - first_file.keys()
    contains_in_both_files = first_file.keys() & second_file.keys()
    differense = []
    for key in contains_only_in_first_file:
        differense.append(f'  - {key}: {first_file[key]}')
    for key in contains_only_in_second_file:
        differense.append(f'  + {key}: {second_file[key]}')
    for key in contains_in_both_files:
        if first_file[key] == second_file[key]:
            differense.append(f'    {key}: {first_file[key]}')
        else:
            differense.append(f'  - {key}: {first_file[key]}')
            differense.append(f'  + {key}: {second_file[key]}')
    return differense
