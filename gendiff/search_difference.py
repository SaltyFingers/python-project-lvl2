differense = []
prefixes = {
    'same': '    ',
    'add': '  + ',
    'del': '  - ',
    }


def search(file, prefix):
    key = file.keys()
    
    if type(file) is dict:
      
      file = key
 
 

def search_difference(first_file, second_file):

    def get_difference(first_file, second_file):
        contains_only_in_first_file = first_file.keys() - second_file.keys()
        contains_only_in_second_file = second_file.keys() - first_file.keys()
        contains_in_both_files = first_file.keys() & second_file.keys()
        search(contains_only_in_first_file, prefixes['del'])
        search(contains_only_in_second_file, prefixes['add'])
        search(contains_in_both_files, prefixes['same'])
        files = first_file, second_file
        diff = map(get_difference, files)
        return sorted(diff)
    return get_difference(first_file, second_file)
