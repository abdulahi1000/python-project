dic = {
    'name':['Daniel', 'Ifeoluwa', 'Opeyemi', 'Joe'],
    'state': ['Oyo', 'Lagos', 'oklahoma', 'Texas'],
    'age': [30,40, 50, 60],
    'food':['Amala', 'Rice', 'semo','Beans'],
}
dic1 = {
    'name':'Daniel',
    'state': 'Texas',
    'age': 30,
    'food':'Beans',
    'good':'Beans'
}
# print(dict['name'][3])

# def inverse_dict(dic):
#     inverse = dict()
#     for key in dic:
#         print(dic[key])
#         print('key', key)
#         value = dic[key]
#         if value in inverse:
#             inverse[value].append(key)
#         else:
#             inverse[value] = [key]

#     print(inverse)

# inverse_dict(dic1)
def inverse_dict(dic):
    inverse = dict()
    for key in dic:
        print(dic[key])
        print('key', key)
        value = dic[key]
        for v in value:
            print(v)
            if v in inverse:
                inverse[v].append(key)
            else:
                inverse[v] = [key]

    print(inverse)

inverse_dict(dic)