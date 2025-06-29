# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
PINS = [board.D3, board.D4, board.D2, board.D1]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Soccer-themed keymap with 4 buttons
# Button 1: Pass/Shoot (W key - common in soccer games)
# Button 2: Tackle/Defend (S key - defensive action)
# Button 3: Sprint/Dribble (SHIFT key - speed boost)
# Button 4: Tactical View (TAB key - switch camera/view)

keyboard.keymap = [
    [
        # Button 1: Pass/Shoot - W key
        KC.W,
        
        # Button 2: Tackle/Defend - S key  
        KC.S,
        
        # Button 3: Sprint/Dribble - SHIFT key
        KC.LSHIFT,
        
        # Button 4: Tactical View - TAB key
        KC.TAB,
    ]
]

# Alternative keymap with soccer macros (uncomment to use)
# keyboard.keymap = [
#     [
#         # Button 1: "GOAL!" macro
#         KC.MACRO("GOAL! ⚽"),
#         
#         # Button 2: "Nice pass!" macro
#         KC.MACRO("Nice pass! 👏"),
#         
#         # Button 3: "Foul!" macro
#         KC.MACRO("Foul! 🟨"),
#         
#         # Button 4: "Substitution" macro
#         KC.MACRO("Substitution 🔄"),
#     ]
# ]

# Advanced soccer keymap with game controls (uncomment to use)
# keyboard.keymap = [
#     [
#         # Button 1: Pass (W) + Sprint (SHIFT) combo
#         KC.Macro(Press(KC.W), Tap(KC.LSHIFT), Release(KC.W)),
#         
#         # Button 2: Tackle (S) + Tactical view (TAB) combo
#         KC.Macro(Press(KC.S), Tap(KC.TAB), Release(KC.S)),
#         
#         # Button 3: "Kickoff!" macro
#         KC.MACRO("Kickoff! 🏟️"),
#         
#         # Button 4: "Full time!" macro
#         KC.MACRO("Full time! ⏰"),
#     ]
# ]

# Start kmk!
if __name__ == '__main__':
    keyboard.go() 