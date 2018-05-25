"""
parses notes to be intrepreted as commands
"""
from constants import *

def tokenize(cmd):
  """
  tokenizes the command into atomic tokens
  input: cmd string
  output: list of string
  """
  return cmd.split(' ')
  
def canonicalize_command(tokens)
  """
  canonicalizes the command and returns it
  """
  command = tokens[0]
  canonical = NO_COMMAND_CANON
  for c in COMMANDS:
    if command in c:
      canonical = COMMANDS[c]
      break
  return canonical

def canonicalize_role(role):
  for r in ROLES:
    if role in r:
      return ROLES[r]
  return NO_ROLE_CANON
  
def canonicalize_summ(summ):
  for s in SUMMONERS:
    if summ in s:
      return SUMMONERS[s]
  return NO_SUMM_CANON
  
def canonicalize(tokens):
  """
  makes tokens canonical
  """
  type = canonicalize_command(tokens)
  tokens[0] = type
  
  if type == NO_COMMAND_CANON:
    return tokens
    
  if type == TRACK_CANON:
    if len(tokens) < 3:
      tokens[0] = NO_COMMAND_CANON
      return tokens
      
    tokens[1] = canonicalize_role(tokens[1])
    tokens[2] = canonicalize_summ(tokens[2])
    if len(tokens) >= 4:
      try:
        tokens[3] = int(tokens[3])
      except ValueError:
        tokens[3] = DEFAULT_OFFSET
    return tokens
    
  if type == CDR_CANON:
    if len(tokens) < 3:
      tokens[0] = NO_COMMAND_CANON
      return tokens
      
    tokens[1] = canonicalize_role(tokens[1])
    return tokens
    
  if type == SUMMS_CANON:
    if len(tokens) < 2:
      tokens[0] = NO_COMMAND_CANON
      return tokens
      
    tokens[1] = canonicalize_role(tokens[1])
    return tokens
    
  return tokens

def tokenize_and_canonicalize(cmd):
  tokens = tokenize(cmd)
  return canonicalize(tokens)
  