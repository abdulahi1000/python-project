alphabet = "abcdefghijklmnopqrstuvwxyz"

def histogram(s):
     d = dict()
     for c in s:
          if c not in d:
               d[c] = 1
          else:
               d[c] += 1
     return d
  
test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"]  
def missing_letters(s):
    missingAlphabets = ""
    global alphabet
    dic = histogram(s)
    value = ''

    for item, k in dic.items():
        value += item
  
    i = 0
    while i < len(alphabet):
        if alphabet[i] not in value:
            missingAlphabets += alphabet[i]
        i += 1

    
    return missingAlphabets
 
   

for i in test_miss:
    if missing_letters(i) == '':
        print('{} uses all the letters'.format(i))
    else:
        print('{} is missing letters {}'.format(i,missing_letters(i)))

