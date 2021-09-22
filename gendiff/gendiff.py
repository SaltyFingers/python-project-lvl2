import json


def generate_diff(file_path1, file_path2):
    first_file = json.load(open(file_path1))
    second_file = json.load(open(file_path2))
    contains_only_in_first = first_file.keys() - second_file.keys()
    contains_only_in_second = second_file.keys() - first_file.keys()
    contains_in_both_files = first_file.keys() & second_file.keys()
    differense = []
    for key in contains_only_in_first:
        differense.append(f'  - {key}: {first_file[key]}')
    for key in contains_only_in_second:
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
