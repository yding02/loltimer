import os
PATH = 'C:/Riot Games/League of Legends/RADS/solutions/lol_game_client_sln/releases/0.0.1.217/MyNotes.txt'

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
