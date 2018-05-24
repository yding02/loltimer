"""
ROLES
"""
TOP = ('top',)
MID = ('mid', 'm', 'middle')
JG = ('jungle', 'jg', 'j')
BOT = ('bot', 'ad', 'adc', 'a', 'b')
SUPP = ('supp', 'support', 's', 'sup')

TOP_CANON = 'top'
MID_CANON = 'mid'
JG_CANON = 'jg'
BOT_CANON = 'bot'
SUPP_CANON = 'supp'

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
            }
            
"""
COMMANDS
"""  
TRACK = ('track', 't')
CDR = ('cdr', 'cooldown', 'cd')
SUMMS = ('summs', 'summ', 's')          