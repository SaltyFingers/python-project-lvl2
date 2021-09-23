import json


def generate_diff(file_path1, file_path2):
    first_file = json.load(open(file_path1))
    second_file = json.load(open(file_path2))
    for key in first_file:
        if type(first_file[key]) == bool:
            first_file[key] = json.dumps(first_file[key])
    for key in second_file:
        if type(second_file[key]) == bool:
            second_file[key] = json.dumps(second_file[key])          
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
    sorted_differense = sorted(differense, key=lambda x: x[4])
    result = '{\n' + '\n'.join(sorted_differense) + '\n}'
    return result
