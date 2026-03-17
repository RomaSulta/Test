import json
import sys
 
values = sys.argv[1]
tests = sys.argv[2]
report = sys.argv[3]
 
with open(values, encoding='utf-8') as f_values:
    values_data = json.load(f_values)['values']
 
with open(tests, encoding='utf-8') as f_tests:
    tests_data = json.load(f_tests)['tests']
 
values_dict = {item['id']: item['value'] for item in values_data}
 
def fill_test_values(tests):
    for test in tests:
        test_id = test.get('id')
        if test_id in values_dict:
            test['value'] = values_dict[test_id]
        if 'values' in test:
            fill_test_values(test['values'])
 
fill_test_values(tests_data)
 
with open(report, mode='w', encoding='utf-8') as f_output:
    json.dump({'tests': tests_data}, f_output, indent=2)
