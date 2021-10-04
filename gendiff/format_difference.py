from gendiff.search_difference import is_dictionary, decode_value


def format(diff):
    difference = ['{']

    def inner(diff, depth=0):
        if not is_dictionary(diff):
            return decode_value(diff)

        keys = sorted(diff.keys())
        depth += 1
        indent = "\t" * depth

        for key in keys:
            if diff[key]['condition'] == 'deleted':
                difference.append(f'{indent}- {key}: \
{inner(diff[key]["value"], depth)}')

            elif diff[key]['condition'] == 'added':
                difference.append(f'{indent}+ {key}: \
{inner(diff[key]["value"], depth)}')

            elif diff[key]['condition'] == 'equal':
                difference.append(f'{indent}  {key}: \
{inner(diff[key]["value"], depth)}')

            elif diff[key]['condition'] == 'replaced':
                difference.append(f'{indent}- {key}: \
{inner(diff[key]["value1"], depth)}')
                difference.append(f'{indent}+ {key}: \
{inner(diff[key]["value2"], depth)}')

            elif diff[key]['condition'] == 'changed':
                difference.append(f'{indent}  {key}: \
{inner(diff[key]["children"], depth)}')
        difference.append('}')
        return '\n'.join(difference)
    return inner(diff)
