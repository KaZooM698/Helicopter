#🌲🟩🚁🔥🌊🏥🗲🏆🧡🪣🏪☁️⚔️

from map import Map
import time
import os
from helicopter import Helicopter as Helico
from pynput import keyboard

TICK_SLEEP = 1
TREE_UPDATE = 50
FIRE_UPDATE = 100
MAP_W, MAP_H = 20, 10

field = Map(MAP_W, MAP_H)
field.generate_forest(3, 10)
field.generate_river(10)
field.generate_river(10)
field.add_fire()
field.add_fire()
field.add_fire()
field.add_fire()

helico = Helico(MAP_W, MAP_H)

MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}
def process_key(key):
    global helico
    c = key.char.lower()
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.move(dx, dy)
listener = keyboard.Listener(
    on_press=None,
    on_release=process_key,)
listener.start()

tick = 1

while True:
    os.system("cls") #cls
    print("TICK", tick)
    field.print_map(helico)
    tick += 1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UPDATE == 0):
        field.generate_tree()
    if (tick % FIRE_UPDATE == 0):
        field.update_fires()