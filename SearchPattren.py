#search a pattren in the str

import re

girl = 'she has a black hair'
pattren = r'black'

result = re.search(gril,pattren)
print(result)

if result:
    print('found')
else:
    print('Not found')