import pygame
from settings import *
from support import *
from graphics.spritesheet import SingleSpriteSheet

@singleton
@helper
@once
class AssetLoader:
    def __init__(self):
        self.assets = {}
        self.load()
    
    @extend(__init__)
    def load(self):
        # dungeon
        self.assets["floor"] = import_folder("dungeon/floor",False)
        self.assets["hole"] = load("dungeon/hole",False)
        self.assets["wall"] = import_folder_dict("dungeon/wall",True)
        self.assets["wall"]["edge"] = load("dungeon/edge")
        self.assets["column"] = import_folder_dict("dungeon/column",True)
        self.assets["spikes"] = import_folder("dungeon/spikes",True)
        self.assets["door"] = import_folder_dict("dungeon/door",True)
        self.assets["crack"] = load_scale("dungeon/crack",3)
        # flasks
        self.assets["flasks"] = import_folder_dict("flasks")
        # ui
        self.assets["ui"] = import_folder_dict("ui",True,False)
        self.assets["ui"]["emark"] = load_scale("ui/emark",SCALE_FACTOR/1.5)
        # weapons
        self.assets["weapons"] = import_folder_dict("weapons")
        # objects
        self.assets["chest_empty"] = [load("objects/chest_empty/chest_empty"),import_folder("objects/chest_empty/animation")]
        self.assets["chest_full"] = [load("objects/chest_full/chest_full"),import_folder("objects/chest_full/animation")]
        self.assets["chest_mimic"] = [load("objects/chest_mimic/chest_mimic"),import_folder("objects/chest_mimic/animation")]
        self.assets["crate"] = load("objects/crate")
        self.assets["skull"] = load("objects/skull")
        # heros
        for hero in HERO_NAMES: self.import_hero_assets(hero)
        # enemies
        for enemy in ENEMY_NAMES: self.import_enemy_assets("enemies",enemy)
        for boss in BOSS_NAMES: self.import_enemy_assets("bosses", boss)
        # effect
        self.assets["fx_sheet"] = import_dict_fx("fx",3)
        self.assets["fx"] = self.parse_sheets(self.assets["fx_sheet"])
        # coin
        self.import_multiple_assets("coin","coin",["anim","particle"],True,False)
        # smoke
        self.import_multiple_assets("smoke","smoke",["slide","explosion","particles"])
        # items
        self.assets["items"] = import_folder_dict("items",True,False)
    
    @internal
    def import_multiple_assets(self,name,pathname,names,convert_alpha=True,scale_factor=True):
        self.assets[name] = {}
        for n in names: self.assets[name][n] = import_folder(f"{pathname}/{n}",convert_alpha,scale_factor)
    
    @internal
    def parse_sheets(self, sheet_dict):
        new_dict = {}
        for name, sheet in sheet_dict.items():
            spritesheet = SingleSpriteSheet(sheet)
            frames = spritesheet.frames()
            new_dict[name] = frames
        return new_dict
    
    @internal
    def import_hero_assets(self, name):
        self.assets[name] = {
            "idle": import_folder(f"heros/{name}/idle"),
            "run": import_folder(f"heros/{name}/run"),
            "hit": import_folder(f"heros/{name}/hit")
        }
    
    @internal
    def import_enemy_assets(self, folder_name, name):
        self.assets[name] = {
            "idle":import_folder(f"{folder_name}/{name}/idle"),
            "run":import_folder(f"{folder_name}/{name}/run")
        }
        
    def __getitem__(self,name):
        return self.assets[name]
