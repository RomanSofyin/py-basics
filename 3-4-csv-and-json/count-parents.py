import json

json_test1 = r'[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]'
json_test2 = r'['                                      \
             r'  { "name":"B", "parents":["A","C"] },' \
             r'  { "name":"C", "parents":["A"]     },' \
             r'  { "name":"A", "parents":[]        },' \
             r'  { "name":"D", "parents":["C","F"] },' \
             r'  { "name":"E", "parents":["D"]     },' \
             r'  { "name":"F", "parents":[]        }'  \
             r']'

data = json.loads(str(json_test2))
print(data)

my_dict = {}

for cls in data:
    parents = cls['parents']
    for parent in parents:
        if parent not in my_dict.keys():
            my_dict[parents[0]] = 1
        else:
            my_dict[parents[0]] += 1

print(my_dict)
