import json
import collections


def account_class(class_name):
    if class_name not in my_dict.keys():
        my_dict[class_name] = 1     # add new class to dict
    else:
        my_dict[class_name] += 1    # bump class in dict


def account_classes(class_name_list):
    for class_name in class_name_list:
        account_class(class_name)


def build_parent_list(class_name):
    lst = [class_name]
    for cls_dict in list_from_json:
        if cls_dict['name'] == class_name:
            for parent in cls_dict['parents']:
                lst += build_parent_list(parent)
            return list(dict.fromkeys(lst))     # return a list without duplicates
    return None


json_test1 = r'[ {"name":"A", "parents":[]         },' \
             r'  {"name":"B", "parents":["A","C"]  },' \
             r'  {"name":"C", "parents":["A"]      }'  \
             r']'   # A : 3;   B : 1;   C : 2
json_test2 = r'['                                      \
             r'  { "name":"B", "parents":["A","C"] },' \
             r'  { "name":"C", "parents":["A"]     },' \
             r'  { "name":"A", "parents":[]        },' \
             r'  { "name":"D", "parents":["C","F"] },' \
             r'  { "name":"E", "parents":["D"]     },' \
             r'  { "name":"F", "parents":[]        }'  \
             r']'   # A : 5;   B : 1;   C : 4;   D : 2;   E : 1;   F : 3
my_dict = {}
list_from_json = json.loads(str(json_test2))

for cls_dict in list_from_json:
    class_name = cls_dict['name']
    lst = build_parent_list(class_name)
    account_classes(lst)

od = collections.OrderedDict(sorted(my_dict.items()))

for k, v in od.items():
    print(k, ':', v)
