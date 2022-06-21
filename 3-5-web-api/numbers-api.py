import requests

# city = input('City? - ')
cs_nums = ''
lines = ''

###
# >>> the code below joins all the input numbers,
# >>> I ended up with a different approach querying numbers one by one
# with open('dataset_24476_3.txt', 'r') as f:
#     lines = [line.strip() for line in f]
#     cs_nums = ','.join(lines)
# api_url = 'http://numbersapi.com/{2}/math?json=true'.format(None, None, cs_nums, None)  # just an example
# api_url = f'http://numbersapi.com/{cs_nums}/math'  # f-string usage
###

with open('dataset_24476_3.txt', 'r') as f:
    for line in f:
        num = line.strip()
        api_url = f'http://numbersapi.com/{num}/math?json=true'
        res = requests.get(api_url)
        res_dict = res.json()
        # print(res_dict)
        if res_dict['found']:
            print('Interesting')
        else:
            print('Boring')
