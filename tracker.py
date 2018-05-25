import win32clipboard
import sys
from constants import *
from t_parser import tokenize_and_canonicalize as tokenize
from time import time, sleep
from poll import poll

players = {}

class Player:
  def __init__(self, role):
    self.role = role
    self.summs = {}
    self.cdr = 1
    return
    
def init_players():
  players[TOP_CANON]  = Player(TOP_CANON)
  players[JG_CANON]   = Player(JG_CANON)
  players[MID_CANON]  = Player(MID_CANON)
  players[BOT_CANON]  = Player(BOT_CANON)
  players[SUPP_CANON] = Player(SUPP_CANON)

def clipboard(s):
  win32clipboard.OpenClipboard()
  win32clipboard.EmptyClipboard()
  win32clipboard.SetClipboardText(s)
  win32clipboard.CloseClipboard()
  
def set_summ(player, summ, offset):
  player.summs[summ] = time() - offset + COOLDOWNS[summ] * player.cdr
  
def get_summ_timer(player):
  t = time()
  s = '{:6} '
  s = s.format(player.role)
  for summ in player.summs:
    template = '{:8} {:3}    '
    diff = round(player.summs[summ] - t)
    if diff > 0:
      s += template.format(summ, diff)
  return s
  
def eval_summs(role):
  s = ''
  if role == NO_ROLE_CANON:
    return
  if role == ALL_ROLE_CANON:
    for player_key in players:
      player = players[player_key]
      s += get_summ_timer(player) + ' \n\n '
  else:
    player = players[role]
    s += get_summ_timer(player)
  clipboard(s)
  print(s)
  return
  
def eval_track(role, spell, offset):
  if role == NO_ROLE_CANON or role == ALL_ROLE_CANON:
    return
  player = players[role]
  set_summ(player, spell, offset)
  return
  
def eval_cdr(role, percent):
  if role == NO_ROLE_CANON:
    return
  player = players[role]
  player.cdr = (1 - percent / 100)
  return

def evaluate(tokens):
  command = tokens[0]
  if command == NO_COMMAND_CANON:
    return
  print('recieved command ' + str(tokens))
  if command == SUMMS_CANON:
    eval_summs(tokens[1])
  if command == TRACK_CANON:
    eval_track(tokens[1], tokens[2], tokens[3])
  if command == CDR_CANON:
    eval_cdr(tokens[1], tokens[2])
  return

def main():
  init_players()
  print("players initialized")
  sys.stdout.flush()
  poll()
  while True:
    sleep(0.1)
    cmd = poll()
    evaluate(tokenize(cmd))
    sys.stdout.flush()

if __name__ == '__main__':
  main()
  