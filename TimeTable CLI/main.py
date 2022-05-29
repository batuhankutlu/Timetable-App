import os, sys

p = os.path.abspath('..')
sys.path.insert(1, p)

from timetable import getNewActivity

print(getNewActivity())