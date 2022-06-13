import json

data = {
    # 'myset': set([1, 2, 3]),        # TypeError: {1, 2, 3} is not JSON serializable
    'mytuple': tuple([1, 2, 3]),      # Attention: tuple will became list!
    'mylist': list([1, 2, 3]),
    'mystr': '123'
}

print(data)
# {'mystr': '123', 'mytuple': (1, 2, 3), 'mylist': [1, 2, 3]}

# write json to file
with open("json_dump.json", "w") as wf:
    json.dump(data, wf)

# load json from file
with open("json_dump.json", "r") as rf:
    print(json.load(rf))
    # {'mystr': '123', 'mytuple': [1, 2, 3], 'mylist': [1, 2, 3]}
