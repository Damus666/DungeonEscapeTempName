import pygame
from settings import *
from support import *
from sprites.sprites import FloatingUI

class UIState:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
    
    def draw(self):
        pass
    
class UIDNC(UIState):
    def __init__(self, assets, day_night):
        super().__init__()
        self.day_night = day_night
        
        self.dnc_bg_rect = pygame.Rect(0,0,150,80)
        self.dnc_bg_rect.topright = (WIDTH,0)
        self.dnc_font1 = pygame.font.Font("assets/fonts/main.ttf",50)
        self.dnc_time_h = 27
        self.dnc_time_surf = pygame.Surface((130,25))
        self.dnc_time_rect = self.dnc_time_surf.get_rect(topright=(WIDTH-5,10))
        dncscale = 0.6; self.dnc_sun = pygame.transform.scale(assets["sun"],(int(TILE_SIZE*dncscale),int(TILE_SIZE*dncscale)))
        dncscale = 0.5; self.dnc_moon = pygame.transform.scale(assets["moon"],(int(TILE_SIZE*dncscale),int(TILE_SIZE*dncscale)))
        self.dnc_lil_moon = pygame.transform.scale(self.dnc_moon,(int(self.dnc_moon.get_width()*0.68),int(self.dnc_moon.get_height()*0.68)))
        dnc_img_pos = (self.dnc_time_rect.left-8,self.dnc_time_rect.centery)
        self.dnc_sun_r, self.dnc_moon_r = self.dnc_sun.get_rect(midright=dnc_img_pos), self.dnc_moon.get_rect(midright=dnc_img_pos)
        self.dnc_lil_moon_r = self.dnc_lil_moon.get_rect(topleft=self.dnc_sun_r.center)
        self.dnc_timepos_r = pygame.Rect(0,0,4,self.dnc_time_rect.h+6)
        self.dnc_timepos_r.centery = self.dnc_time_rect.centery
        self.dnc_timepos_inf = self.dnc_timepos_r.inflate(4,4)
        self.form_dnc_gradient()
        self.update_dnc()
        
    def update_dnc(self):
        self.day_count_surf = self.dnc_font1.render(f"DAY  {self.day_night.day_counter}",True,"white")
        self.day_count_rect = self.day_count_surf.get_rect(topright = (WIDTH-5,5+self.dnc_time_h))
        self.day_night.ui_changed = False
        
    def draw(self):
        # update
        if self.day_night.ui_changed: self.update_dnc()
        # time bar
        if self.day_night.status == 0 and not self.day_night.in_transition:
            if not self.day_night.black_transition:
                ratio = (pygame.time.get_ticks()-self.day_night.start_time)/DAY_DURATION; w = self.dnc_time_rect.w*ratio
                self.dnc_timepos_r.centerx = self.dnc_time_rect.left + w; self.dnc_timepos_inf.centerx = self.dnc_timepos_r.centerx
            else: self.dnc_timepos_r.centerx = self.dnc_time_rect.left; self.dnc_timepos_inf.centerx = self.dnc_timepos_r.centerx
        else: self.dnc_timepos_r.centerx = self.dnc_time_rect.right; self.dnc_timepos_inf.centerx = self.dnc_timepos_r.centerx
        # choose sun, moon
        also_t = False
        if self.day_night.status == 0:
            if self.day_night.in_transition: also_t = True
            img_touse, r_touse = self.dnc_sun,self.dnc_sun_r
        else: img_touse, r_touse = self.dnc_moon,self.dnc_moon_r
        # draw bg
        pygame.draw.rect(self.display_surface,UI_BG_COL,self.dnc_bg_rect)
        pygame.draw.polygon(self.display_surface,UI_BG_COL,[ (self.dnc_bg_rect.x-85,self.dnc_bg_rect.y), self.dnc_bg_rect.topleft, self.dnc_bg_rect.bottomleft])
        # draw gradient, count, sun/moon, lil moon
        self.display_surface.blit(self.dnc_time_surf,self.dnc_time_rect)
        self.display_surface.blit(self.day_count_surf,self.day_count_rect)
        self.display_surface.blit(img_touse,r_touse)
        if also_t: self.display_surface.blit(self.dnc_lil_moon,self.dnc_lil_moon_r)
        # draw time bar
        pygame.draw.rect(self.display_surface,"white",self.dnc_timepos_inf)
        pygame.draw.rect(self.display_surface,"red",self.dnc_timepos_r)
        
    @extend(__init__)
    def form_dnc_gradient(self):
        pixels = pygame.PixelArray(self.dnc_time_surf)
        color1 = (255, 150, 0); color2 = (0, 0, 100)
        for x in range(self.dnc_time_surf.get_width()):
            color = (
                int((color2[0] - color1[0]) * (x / self.dnc_time_surf.get_width())) + color1[0],
                int((color2[1] - color1[1]) * (x / self.dnc_time_surf.get_width())) + color1[1],
                int((color2[2] - color1[2]) * (x / self.dnc_time_surf.get_width())) + color1[2],
            )
            for y in range(self.dnc_time_surf.get_height()): pixels[x][y] = color
        del pixels
        
class UIHealth(UIState):
    def __init__(self, assets, stats, bg_bottom=60):
        super().__init__()
        self.stats = stats
        
        self.heart_empty = assets["ui_heart_empty"]
        self.heart_full = assets["ui_heart_full"]
        self.heart_half = assets["ui_heart_half"]
        self.heart_empty, self.heart_full, self.heart_half = pygame.transform.scale(self.heart_empty,(UI_HEART_SIZE,UI_HEART_SIZE)),\
            pygame.transform.scale(self.heart_full,(UI_HEART_SIZE,UI_HEART_SIZE)),\
            pygame.transform.scale(self.heart_half,(UI_HEART_SIZE,UI_HEART_SIZE))
        self.heart_spacing = UI_SPACING/2
        self.range_5 = range(5)
        self.hearts_bg_r = pygame.Rect(0,0,200,bg_bottom)
        
    def draw(self):
        # draw bg
        pygame.draw.rect(self.display_surface,UI_BG_COL,self.hearts_bg_r)
        pygame.draw.polygon(self.display_surface,UI_BG_COL,(self.hearts_bg_r.topright,self.hearts_bg_r.bottomright,(self.hearts_bg_r.right+50,0)))
        # empty hearts
        for i in self.range_5: self.display_surface.blit(self.heart_empty,(self.heart_spacing+(-self.heart_spacing/2)*(i)+UI_HEART_SIZE*i,self.heart_spacing))
        # fill hearts
        last_i = 0
        for i in range(self.stats.health //2):
            self.display_surface.blit(self.heart_full,(self.heart_spacing+(-self.heart_spacing/2)*(i)+UI_HEART_SIZE*i,self.heart_spacing/2))
            last_i = i+1
        # half heart
        if self.stats.health % 2 != 0: self.display_surface.blit(self.heart_half,(self.heart_spacing+(-self.heart_spacing/2)*(last_i)+UI_HEART_SIZE*last_i,self.heart_spacing/2))
                  
class UICoins(UIState):
    def __init__(self, inventory, coin_img, bg_bottom=60):
        super().__init__()
        self.inventory = inventory
        
        self.coins_bg_r = pygame.Rect(0,bg_bottom,120,32)
        cs = 1.5
        self.coin_img = pygame.transform.scale(coin_img,(int(coin_img.get_width()*cs),int(coin_img.get_height()*cs)))
        self.coin_rect = self.coin_img.get_rect(topleft=(self.coins_bg_r.left-2,self.coins_bg_r.top-16))
        self.coins_font = pygame.font.Font("assets/fonts/main.ttf",40)
        self.update_coins()
        
        self.floating_img = pygame.transform.scale(self.coin_img,(int(self.coin_img.get_width()*0.8),int(self.coin_img.get_height()*0.8)))
        self.floating_coins = pygame.sprite.Group()
        self.inventory.add_floating_coin = self.add_floating_coin
        self.floating_end_rect = pygame.Rect(0,bg_bottom,self.coins_bg_r.w,self.coins_bg_r.h)
    
    @external
    def add_floating_coin(self):
        self.floating_coins.add(FloatingUI(self.floating_end_rect,self.floating_img))
    
    @runtime
    def update(self, dt):
        self.floating_coins.update(dt)
    
    @override
    def draw(self):
        # draw bg
        pygame.draw.rect(self.display_surface,UI_BG_COL,self.coins_bg_r)
        pygame.draw.polygon(self.display_surface,UI_BG_COL,(self.coins_bg_r.topright,self.coins_bg_r.bottomright,(self.coins_bg_r.right+30,self.coins_bg_r.top)))
        # update
        if self.inventory.ui_changed: self.update_coins()
        # draw coin, count
        self.display_surface.blit(self.coin_img,self.coin_rect)
        self.display_surface.blit(self.coin_amount_surf,self.coin_amount_rect)
        # floating
        self.floating_coins.draw(self.display_surface)
        
    def update_coins(self):
        self.coin_amount_surf = self.coins_font.render(f"{self.inventory.coins}",True,"white")
        self.coin_amount_rect = self.coin_amount_surf.get_rect(topleft=(self.coin_rect.right+3,0))
        self.coin_amount_rect.centery = self.coin_rect.centery+4
        self.inventory.ui_changed = False
        
class UIInventory(UIState):
    def __init__(self, inventory, player):
        super().__init__()
        self.inventory = inventory
        self.player = player
        self.inventory.add_floating_item = self.add_floating_item
        
        self.bg_rect = pygame.Rect(0,0,320,72)
        self.bg_rect.centerx = WIDTH//2
        self.poly_offset = 40
        
        middle_slot = pygame.Rect(H_WIDTH-H_SLOT_SIZE,UI_SLOT_SPACING,UI_SLOT_SIZE,UI_SLOT_SIZE)
        rects = [middle_slot]
        for i in range(1,3):
            rect = middle_slot.copy()
            rect.x += UI_SLOT_SPACING*i+UI_SLOT_SIZE*i
            lrect = middle_slot.copy()
            lrect.x -= UI_SLOT_SPACING*i+UI_SLOT_SIZE*i
            rects.append(rect); rects.append(lrect)
            
        rects = sorted(rects,key=lambda r: r.centerx)
        self.slot_rects = [CornerRect(rect,UI_CORNER_W,UI_SLOT_BG_COL) for rect in rects]
        
        self.item_font = pygame.font.Font("assets/fonts/main.ttf",30)
        
        self.floating_items = pygame.sprite.Group()
        self.floating_end_rect = self.bg_rect
    
    @external
    def add_floating_item(self, name):
        surf = self.inventory.get_item_surf_only(name)
        w,h = surf.get_size(); scale = DROP_SCALE
        surf = pygame.transform.scale(surf,(int(w*scale),int(h*scale)))
        self.floating_items.add(FloatingUI(self.floating_end_rect,surf,True))
    
    @runtime
    def update(self, dt):
        self.floating_items.update(dt)
    
    @override
    def draw(self):
        pos = pygame.mouse.get_pos()
        # bg
        pygame.draw.rect(self.display_surface,UI_BG_COL,self.bg_rect)
        pygame.draw.polygon(self.display_surface,UI_BG_COL,(self.bg_rect.bottomleft,self.bg_rect.topleft,(self.bg_rect.left-self.poly_offset,self.bg_rect.top)))
        pygame.draw.polygon(self.display_surface,UI_BG_COL,(self.bg_rect.bottomright,self.bg_rect.topright,(self.bg_rect.right+self.poly_offset,self.bg_rect.top)))
        # slots
        for i,slot_r in enumerate(self.slot_rects):
            slot_r.draw()
            slot = self.inventory.slots[i]
            if not slot.is_empty():
                surf,r = self.inventory.get_item_surf(slot.item.name)
                r.center = slot_r.center
                self.display_surface.blit(surf,r)
                if slot_r.original.collidepoint(pos):
                    txt = f"{slot.item.name},  Drop [Q]"
                    name_surf = self.item_font.render(txt,False,"white")
                    name_rect = name_surf.get_rect(midtop=(slot_r.center[0],self.bg_rect.bottom+UI_SLOT_SPACING))
                    pygame.draw.rect(self.display_surface,UI_BG_COL,name_rect.inflate(10,0),0,4)
                    self.display_surface.blit(name_surf,name_rect)
                    if self.player.key_data["q"]: self.drop_item(slot.item)
        # items
        self.floating_items.draw(self.display_surface)
    
    @internal
    def drop_item(self, item): self.player.drop_item(item)
        
class UIOverlay(UIState):
    def __init__(self, ui_assets):
        super().__init__()