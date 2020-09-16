import sys
from datetime import datetime


sf = '%d/%m/%Y'
a = datetime.strptime('03/11/2020', sf)
b = datetime.strptime('02/11/2020', sf)
print(b >= a)

"""
from DB to python
f = '%Y-%m-%d %H:%M:%S.%f'
a = datetime.strptime('2020-09-01 13:09:41.4196', f)
"""
