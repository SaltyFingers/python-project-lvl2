from gendiff.search_difference import is_dictionary, decode_value
    

def format(diff):

    def inner(diff, depth=0):
        if not is_dictionary(diff):
            return decode_value(diff)

        keys = sorted(diff.keys())
        indent = " " * depth
        difference = ['{']
        depth += 4
        for key in keys:
            if diff[key]['condition'] == 'deleted':
                obj = (f'{indent}  - {key}: \
{inner(diff[key]["value"], depth)}')

            elif diff[key]['condition'] == 'added':
                obj = (f'{indent}  + {key}: \
{inner(diff[key]["value"], depth)}')

            elif diff[key]['condition'] == 'equal':
                obj = (f'{indent}    {key}: \
{inner(diff[key]["value"], depth)}')

            elif diff[key]['condition'] == 'replaced':
                obj = (
                f'{indent}  - {key}: \
{inner(diff[key]["value1"], depth)}\n'
                f'{indent}  + {key}: \
{inner(diff[key]["value2"], depth)}')

            elif diff[key]['children']:
                obj = (f'{indent}    {key}: \
{inner(diff[key]["children"], depth)}')

            difference.append(obj)
        difference.append(f'{indent}}}')
        return '\n'.join(difference)
    return inner(diff)
