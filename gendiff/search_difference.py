differense = []
prefixes = {
    'same': '    ',
    'add': '  + ',
    'del': '  - ',
    }


def search_in_one(part_of_file, prefix, file):
    for key in part_of_file:
        differense.append(f'{prefix}{key}: {file}')


def search_in_both(part_of_file, prefix, first_file, second_file):
    for key in part_of_file:
        if first_file[key] == second_file[key]:
            differense.append(f'{prefix}{key}: {first_file[key]}')
        else:
            differense.append(f'{prefixes["del"]}{key}: {first_file[key]}')
            differense.append(f'{prefixes["add"]}{key}: {second_file[key]}')
 

def search_difference(first_file, second_file):
    first_file = sorted(first_file)
    second_file = sorted(second_file)
    def get_difference(first_file, second_file):
        first_file_only = first_file.keys() - second_file.keys()
        second_file_only = second_file.keys() - first_file.keys()
        both_files = first_file.keys() & second_file.keys()
        search_in_one(first_file_only, prefixes['del'], first_file)
        search_in_one(second_file_only, prefixes['add'], second_file)
        search_in_both(both_files, prefixes['same'], first_file, second_file)
        for key in first_file.keys():
            if type(key) is dict:
                first_file = key
        for key in second_file.keys():
            if type(key) is dict:
                second_file = key  
    diff = map(get_difference, first_file, second_file)
    return diff
