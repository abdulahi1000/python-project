
# part one
def histogram(s):
     d = dict()
     for c in s:
          if c not in d:
               d[c] = 1
          else:
               d[c] += 1
     return d 

# print(histogram('zzzbb'))

def has_duplicates(s):
    dic = histogram(s)
    # print(dic)
    for key, value in dic.items():
        if value >1:
            return True
        else:
            return False

# print(has_duplicates('ddeeu'))

test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"] 

for item in test_dups:
    if has_duplicates(item):
        print(item, 'has duplicates')
    else:
        print(item, 'has no duplicates')

