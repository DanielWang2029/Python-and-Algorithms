
# import sys
# sys.path.append('/1/Desktop/...')
# The above code is used if the import module/packages is not in the same directory with this file

from Python_Intro import Functions as fn
from Python_Intro.Functions import another_func, courses as cs  # only give access to the function/variable, do not need to use 'fn.'
print()
print('Imported file\'s output')
print(fn.input_func('Hi', 'Daniel'))
print(another_func())
print(cs)

import random

random_course = random.choice(['History', 'Math', 'Stat','Communication'])
print(random_course)

import math

rads = math.radians(90)
print(math.sin(rads))

import datetime
import calendar

today = datetime.date.today()
print(today)
print(calendar.isleap(2020))

import os

print(os.getcwd())

print(os.__file__)

# import antigravity
