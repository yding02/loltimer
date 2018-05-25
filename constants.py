"""
ROLES
"""
TOP = ('top', 't')
MID = ('mid', 'm', 'middle')
JG = ('jungle', 'jg', 'j')
BOT = ('bot', 'ad', 'adc', 'a', 'b')
SUPP = ('supp', 'support', 's', 'sup')
ALL_ROLE = ('all', )

TOP_CANON = 'top'
MID_CANON = 'mid'
JG_CANON = 'jg'
BOT_CANON = 'bot'
SUPP_CANON = 'supp'
NO_ROLE_CANON = 'norole'
ALL_ROLE_CANON = 'allrole'

ROLES = { TOP : TOP_CANON,
          JG : JG_CANON,
          MID : MID_CANON,
          BOT : BOT_CANON,
          SUPP : SUPP_CANON,
          ALL_ROLE : ALL_ROLE_CANON
        }
        
"""
SUMMONERS
"""
HEAL = ('heal', 'h')
GHOST = ('ghost', 'g', 'gh')
BARRIER = ('b', 'barrier', 'shield')
EXHAUST = ('e', 'exhaust', 'ex', 'exh')
FLASH = ('f', 'flash', 'fl', 'fla')
TELEPORT = ('tp', 'teleport', 't')
SMITE = ('smite', 's')
CLENSE = ('clense', 'c', 'cl')
IGNITE = ('ignite', 'i', 'fire', 'ig')

HEAL_CANON = 'heal'
GHOST_CANON = 'ghost'
BARRIER_CANON = 'barrier'
EXHAUST_CANON = 'exhaust'
FLASH_CANON = 'flash'
TELEPORT_CANON = 'teleport'
SMITE_CANON = 'smite'
CLENSE_CANON = 'clense'
IGNITE_CANON = 'ignite'
NO_SUMM_CANON = 'nosumm'

SUMMONERS = { HEAL : HEAL_CANON,
              GHOST : GHOST_CANON,
              BARRIER : BARRIER_CANON,
              EXHAUST : EXHAUST_CANON,
              FLASH : FLASH_CANON,
              TELEPORT : TELEPORT_CANON,
              SMITE : SMITE_CANON,
              CLENSE : CLENSE_CANON,
              IGNITE : IGNITE_CANON,
            }

"""
COOLDOWNS
"""
COOLDOWNS = { HEAL_CANON : 270, 
              GHOST_CANON : 180,
              BARRIER_CANON : 180,
              EXHAUST_CANON : 210,
              FLASH_CANON : 300,
              TELEPORT_CANON : 300,
              SMITE_CANON : 90,
              CLENSE_CANON : 210,
              IGNITE_CANON : 210,
              NO_SUMM_CANON : 0,
            }
            
"""
COMMANDS
"""  
TRACK = ('track', 't')
CDR = ('cdr', 'cooldown', 'cd')
SUMMS = ('summs', 'summ', 's')

TRACK_CANON = 'track'
CDR_CANON = 'cdr'
SUMMS_CANON = 'summs'
NO_COMMAND_CANON = 'nocommand'

COMMANDS = {TRACK : TRACK_CANON, 
            CDR : CDR_CANON, 
            SUMMS : SUMMS_CANON
           }

"""
MISC
"""
DEFAULT_OFFSET = 10
