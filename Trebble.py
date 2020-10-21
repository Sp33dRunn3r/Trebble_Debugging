# debugging

# 1: Linting
# 2: ide/ editor
# 3: read errors
# pdb

import pdb

def add(num1, num2):
    pdb.set_trace()
    return num1 + num2

add(4, 'agdasfasdf')
