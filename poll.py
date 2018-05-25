import os
from constants import PATH

prev_stamp = 0
def poll():
  global prev_stamp
  stamp = os.stat(PATH).st_mtime
  if stamp != prev_stamp:
    prev_stamp = stamp
    f = open(PATH)
    s = f.read()
    f.close()
    command = s.split('\n')[-2]
    return command
  return ''
