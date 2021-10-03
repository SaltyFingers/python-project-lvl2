import json


def is_dictionary(object):
    return isinstance(object, dict)

def decode_value(value):
  if value is None:
    return 'null'
  
  elif type(value) == bool:
    return str(value).lower()

  return str(value)



def get_keys(dict1, dict2):
  first_keys = list(dict1.keys())
  second_keys = list(dict2.keys())
  return first_keys if dict1 == dict2 else set(first_keys + second_keys)

def search_difference(dict1, dict2=None):
  if not is_dictionary(dict1):
    return dict1
  
  elif dict2 is None:
    dict2 = dict1

  keys = sorted(get_keys(dict1, dict2))

  difference = {}

  for key in keys:

    if key in dict1 and not key in dict2:
      difference[key] = {
      'condition': 'deleted',
      'children': None,
      'value': search_difference(dict1[key])}

    elif key in dict2 and not key in dict1:
      difference[key] = {
      'condition': 'added',
      'children': None,
      'value': search_difference(dict2[key])}
    
    else:

      if dict1[key] == dict2[key]:
        difference[key] = {
        'condition': 'equal',
        'children': None,
        'value': search_difference(dict1[key])}

      elif not is_dictionary(dict1[key]) or not is_dictionary(dict2[key]):
        difference[key] = {
        'condition': 'replaced',
        'children': None,
        'value1': search_difference(dict1[key]),
        'value2': search_difference(dict2[key]),}
        
      elif is_dictionary(dict1[key]) and is_dictionary(dict2[key]):
        difference[key] = {
      'condition': 'changed',
      'children': search_difference(dict1[key], search_difference(dict2[key])),
      'value': None}

  return difference

