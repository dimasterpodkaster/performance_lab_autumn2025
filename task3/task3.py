import sys
import json
import copy

filename1 = sys.argv[1]
filename2 = sys.argv[2]
filename3 = sys.argv[3]

with open(filename1, "r") as file_values, open(filename2, "r") as file_tests, open(filename3, "w") as file_report:
    data1 = json.load(file_values)
    data2 = json.load(file_tests)
    result = copy.deepcopy(data2)

    values_info = dict()

    for item in data1['values']:
        values_info[item['id']] = item['value']

    # print(values_info)

    def add_info(current_level):
        if current_level.get('id') in values_info:
            current_level['value'] = values_info[current_level['id']]
        if current_level.get('values'):
            for item_ in current_level['values']:
                add_info(item_)

    for item in result['tests']:
        add_info(item)

    json.dump(result, file_report, indent=2)
