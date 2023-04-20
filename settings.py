from pygame.math import Vector2 as vector

# window
WINDOW_SIZES = WIDTH, HEIGHT = 1920, 1080
H_WIDTH, H_HEIGHT = WIDTH//2, HEIGHT // 2
FPS = 0 # unlimited

# constants
ORIGINAL_TILE_SIZE = 16
TILE_SIZE = 64
SCALE_FACTOR = TILE_SIZE/ORIGINAL_TILE_SIZE
ANIMATION_SPEED = 8
TRANSITION_SPEED = 10
TRANSITION_THRESHOLD = 30

# maps
MAP_NAMES = [
    "DungeonFeatures"
]

# player
INVULNERABILITY_COOLDOWN = 600
P_SPEED = 400
ADD_FAIL_MESSAGES = {
    "space": "Inventory is full",
    "has": "Already has item",
    "ok": "You should be able to collect idk why not"
}

# ui
UI_HEART_SIZE = 45
BOSS_HEART_SIZE = 60
UI_SPACING = 8
UI_BG_COL = (20, 20, 20)
UI_SLOT_SIZE = 60
UI_INNER_SLOT_SIZE = 52
UI_SLOT_BG_COL = (30, 30, 30)
H_SLOT_SIZE = UI_SLOT_SIZE//2
UI_SLOT_SPACING = 5
UI_CORNER_W = 6
UI_COIN_SPEED = 10
MSG_DISAPPEAR_SPEED = 200
UI_DIALOGUE_BTN_COL = (35, 35, 35)
DIALOGUE_BTN_H = 40
DIALOGUE_OFFSET = 8
HEALTH_BAR_COL = (180,0,45)
HEALTH_OUTLINE_COL = (110,0,5)
DEBUG_S = 8
DEBUG_H = 30
DEBUG_SPACING = DEBUG_S+DEBUG_H
SLOT_SELECTED_COL = (205,130,0)

# dnc
DAY_DURATION = 10*1000*60
CYCLE_TRANSITION_SPEED = 10

# secondary room
SECONDARY_DIST = TILE_SIZE*5
SECONDARY_DOOR_DIST = TILE_SIZE*8
SECONDARY_ALPHA = 50
ONE_OVER_TILESIZE = 1/TILE_SIZE

# dungeon
SPIKE_ACTIVATION_DIST = TILE_SIZE*5
SPIKE_DAMAGE = 1
DROP_SCALE = 0.7
DROP_IDLE_SPEED, DROP_IDLE_OFFSET = 30, TILE_SIZE//6
END_ROOM_NAME = "Portal Room"
ENEMY_VISION_RANGE = TILE_SIZE*6
BOSS_VISION_RANGE = TILE_SIZE*10

# items
CAN_EQUIP = [
    "Sword",
    "Knight Sword",
    "Golden Sword",
    "Mace"
]
CAN_CONSUME = [
    "Healing Potion"
]
ITEM_STATS = {
    "Sword":{"damage": 3,"area":False},
    "Knight Sword":{"damage":8,"area":False},
    "Golden Sword":{"damage":12,"area":False},
    "Mace":{"damage":4,"area":True}
}

# generation
FLOOR_WEIGHTS = [
    50, 5, 10, 3, 50, 3, 3, 3
]
WALL_MID_ALTERNATIVES_ALL = [
    ("hole_1", 30), ("hole_2", 25),
    ("banner", 30),
    ("column", 5), ("fountain", 18), ("goo", 15)
]
WALL_MID_ALTERNATIVES_T = [
    ("hole_1", 30), ("hole_2", 25),
    ("banner", 30),
    ("column", 5)
]
FOUNTAIN_COLORS = ["blue", "red"]
BANNER_COLORS = ["blue", "green", "red", "yellow"]
OBJECT_ID_LOOKUP = {
    5: "crate",
    6: "spike",
    7: "room_name",
    8: "hero",
    9: "enemy",
    10: "portal"
}
WALL_NAMES_LOOKUP = mapping = {
    "mid": "wall_mid",
    "left": "wall_left",
    "right": "wall_right",
    "left_sided": "wall_inner_corner_mid_left",
    "right_sided": "wall_inner_corner_mid_rigth",
    "side_left": "wall_side_mid_left",
    "side_right": "wall_side_mid_right",
    "side_left_mid": "wall_side_front_left",
    "side_right_mid": "wall_side_front_right",
    "top_mid": "wall_top_mid",
    "top_left": "wall_top_left",
    "top_right": "wall_top_right",
    "top_corner_left": "wall_side_top_left",
    "top_corner_right": "wall_side_top_right",
    "hole_1": "wall_hole_1",
    "hole_2": "wall_hole_2",
    "goo": "wall_goo",
    "goo_base": "wall_goo_base",
    "column": "wall_column_mid",
    "column_top": "wall_column_top",
    "column_bottom": "wall_coulmn_base",
    "fountain_top": "wall_fountain_top",
    "edge": "edge",
    "none": "none",
}

# characters
HERO_NAMES = [
    "lizard_f",
    "lizard_m",
    "wizzard_f",
    "wizzard_m",
    "elf_f",
    "elf_m",
    "knight_f",
    "knight_m"
]
ENEMY_NAMES = [
    "chort",
    "goblin",
    "ice_zombie",
    "imp",
    "masked_orc",
    "muddy",
    "necromancer",
    "orc_shaman",
    "orc_warrior",
    "skelet",
    "swampy",
    "tiny_zombie",
    "wogol",
    "zombie"
]
BOSS_NAMES = [
    "big_demon",
    "big_zombie",
    "ogre"
]


# colors
BG_COL = (35, 29, 35)  # (20,20,20)
TRANSITION_COL = (20, 20, 20)
BG_DARK_COL = (35-3, 29-3, 35-3)
CYAN = (0,255,255)

# decorators
def internal(func): return func
def external(func): return func
def helper(func): return func
def static(func): return func
def singleton(func): return func
def once(func): return func
def extend(seg): 
    def dec(func): return func
    return dec
def override(func): return func
def runtime(func): return func
