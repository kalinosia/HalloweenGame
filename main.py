import pygame
import random
from pygame import mixer
import math
#from pygame.time import Clock
import time

'''
Pająki kąsają, chyba, że rzucisz im piwo - klawisz "m"
Miotłę i widły trzba wziać, ale można użwać jednego na raz
zmienia się za pomocą "l"
Szczory gryzą, zabijaj je dźganiem widłami za pomocą "spacji"
koty są spoko, nie dźaj bo gryzną, pet them
widły oznaczją dla pająków koniec przyjaźni
zmiana wideł na miotłę tylko na ziemi

nietoperze gryzą, 
'''
##Icons made by href="https://www.flaticon.com/authors/freepik"
## backgroung   https://www.freepik.com/vectors/poster - Poster vector created by kjpargeter
## background2  Background vector created by pikisuperstar - www.freepik.com
##

pygame.init()
timer = pygame.time.Clock()

# SCREEN
screenX = 800
screenY = 600
screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption("Halloween Party")
icon = pygame.image.load("image/skull.png")
pygame.display.set_icon(icon)
# BACKGROUND
background = pygame.image.load('image/background2.jpg')
background = pygame.transform.scale(background, (screenX, screenY))
background_info = pygame.image.load('image/background.jpg')
background_info = pygame.transform.scale(background_info, (screenX, screenY))
#BACKGROUND SOUND
mixer.music.load('sounds/background.mp3')
mixer.music.play(-1)


# PLAYER (witch.png czy wybór??)
playerOneImg = pygame.image.load("image/witch.png")
playerTwoImg = pygame.image.load("image/vampire.png")
playerThreeImg = pygame.image.load("image/ghost.png")
playerFourImg = pygame.image.load("image/womancat.png")
playerFiveImg = pygame.image.load("image/werewolf.png")
playerSixImg = pygame.image.load("image/monster.png")
################################################################################################################
playerImg=playerOneImg
#playerImg = pygame.image.load("image/witch.png")
playerWidth = playerOneImg.get_width()
playerHeight = playerOneImg.get_height()
playerX = screenX / 2 - playerWidth / 2
playerY = screenY - playerHeight
playerXChange = 0
playerYChange = 0
speed = 0.7
jump = False
jumpCount=250   #(...)

def player(x, y):
    screen.blit(playerImg, (x, y))

#CANDIES
candies = pygame.image.load('image/candies.png')
cookie = pygame.image.load('image/cookie.png')
lollipop = pygame.image.load('image/lollipop.png')
punch = pygame.image.load('image/punch-bowl.png')
carmelized = pygame.image.load('image/caramelized-apple.png')
sweets=[candies, cookie, lollipop, punch, carmelized]

candiesWidth = candies.get_width()
candiesHeight = candies.get_height() #check if every is the same?? i do not know
candiesX = random.randint(0, screenX - candiesWidth)
candiesY = random.randint(20, screenY - candiesWidth)

how_many_sweets=0 #player have
how_many_candies=0  #not need?on screeen
random_time_candies = 1000

candiesImg=[]
candyX=[]
candyY=[]
candyTime=[]
def new_candies(current_time):
    sweets_random = random.randrange(0, len(sweets))
    candiesImg.append(sweets[sweets_random])
    candyX.append(random.randint(0, screenX - candiesWidth))
    candyY.append(random.randint(20, screenY - candiesWidth))
    candyTime.append(current_time+random.randint(5000, 10000))   #random time every sweet have

def collision_player_candies(candyX, candyY, playerX, playerY):
    if playerX < candyX and playerX+playerWidth>candyX+candiesWidth and playerY<candyY and playerY+playerHeight>candyY+candiesHeight:
        return True
    else:
        return False


# TREE BAD THING                                opacity0.5??? time???
treeImg = pygame.image.load('image/tree.png')
treeWidth = treeImg.get_width()
treeHeight = treeImg.get_height()
treeX = random.randint(0, screenX - treeWidth)
treeY = screenY - treeHeight

tree_appear = False
random_time_tree = 10000
tree_time = 20000

bite_time_on_tree = False
bite_time_tree = 0


def random_time_tree_function(current_time, random_time_tree):
    random_time_tree_new = random.randint(random_time_tree + tree_time, random_time_tree + tree_time + 10000)  # change ???????
    treeX = random.randint(0, (screenX - treeWidth))
    return random_time_tree_new, treeX

def new_tree(treeX):
    screen.blit(treeImg, (treeX, treeY))

def collision_tree_player(treeX, treeY, playerX, playerY):
    if treeX+10 <= playerX + playerWidth and treeX + treeWidth-10 >= playerX and playerY + playerHeight >= treeY+20: ##dificult
        return True
    else:
        return False


# BAT
batImgL = pygame.image.load('image/bat.png')
batImgR = pygame.transform.flip(batImgL, True, False)
batWidth = batImgR.get_width()
batHeight = batImgR.get_height()
numbers_of_bat = 0
bat_speed=0.5
new_bat_time=1000
batImg = []
batX = []
batY = []
batX_change = []

def new_bat():
    bat_side = random.randrange(0, 2)
    if bat_side==0:
        batImg.append(batImgL)
        batX.append(-batWidth)#   batX.append(random.randint(-screenX, -batWidth))
        batX_change.append(bat_speed)
    if bat_side==1:
        batImg.append(batImgR)
        batX.append(screenX)#   batX.append(random.randint(screenX, 2*screenX))
        batX_change.append(-bat_speed)
    batY.append(random.randint(20, screenY - batHeight-2*playerHeight))

def collision_bat_player(batX, batY, playerX, playerY):
    if playerX < batX+batWidth/2 < playerX+playerWidth and playerY < batY + batHeight / 2 < playerY + playerHeight:
        return True
    else:
        return False

# SPIDER -one spider drop from random x
spiderImg = pygame.image.load('image/spider.png')
spiderWidth = spiderImg.get_width()
spiderHeight = spiderImg.get_height()
spiderX = random.randint(0, screenX - spiderWidth)
spiderY = - spiderHeight + 10  #########
spiderY_change = 0.5  # speed spider drop
spiderDrop = random.randint(0, screenY - spiderHeight)

bite_time_spider = 0
bite_time_on_spider = False

def new_spider():
    spiderX = random.randint(0, (screenX - spiderWidth))
    spiderY = - spiderHeight + 10
    spiderY_change = 0.5
    spiderDrop = random.randint(screenY - spiderHeight, screenY - spiderHeight)
    return [spiderX, spiderY, spiderY_change, spiderDrop]

def spider(x, y):
    screen.blit(spiderImg, (x, y))


# BULLET FOOD SPIDER LOVE
bulletImg = pygame.image.load('image/beer.png')
bulletWidth = bulletImg.get_width()
bulletHeight = bulletImg.get_height()
bulletX = 0
bulletY = playerY
bulletY_change = 1
bullet_state = "ready"

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + playerWidth / 2 - bulletWidth / 2, y))


# COLISION SPIDER BULLET
def collision_spider_bullet(spiderX, spiderY, bulletX, bulletY):
    '''
    distance = math.sqrt((math.pow((spiderX+spiderWidth)-(bulletX+bulletWidth), 2))+(math.pow((spiderY+spiderHeight)-(bulletY+bulletHeihgt), 2)))
    if distance <= 57.69:
    #if distance < bulletHeihgt / 2 + spiderHeight / 2:
    # if spiderY + (spiderHeight/2) - bulletY >= 0 and spiderY - bulletY <= 0 :
    #if spiderX+spiderWidth-bulletX >= 0 and 0 > spiderX-bulletX:
    if distance <= 57.69:
    '''
    if spiderY + spiderHeight > bulletY:
        if (spiderX - spiderWidth < bulletX) and (
                spiderX) > bulletX:  ##WTF?????????????????????????????????????????????????????????????????
            return True
        else:
            return False
    else:
        return False


spider_love = False
font = pygame.font.Font('freesansbold.ttf', 12)
# textX=10 textY=10                      NAPISY
# def show_spider_love():
#    score=font.render("Score: " + str(spider_love), True, (255,255,0))
#    screen.blit(score, (10, 10))
spider_love_img = pygame.image.load('image/spiderlove.png')


def spider_love_draw(x, y):
    screen.blit(spider_love_img, (x, y))


# COLLISION SPIDER PLAYER - poison                                                               FLY REPAIR!!!!!!
def collision_spider_player(spiderX, spiderY, playerX, playerY):
    if playerX - spiderWidth / 2 <= spiderX and playerX + playerWidth + spiderWidth / 2 >= spiderX + spiderWidth and playerY - playerHeight / 2 <= spiderY < playerY + playerHeight:
        return True
    else:
        return False


# CAT
catImgR = pygame.image.load('image/cat.png')
catImgL = pygame.transform.flip(catImgR, True, False)
catImgList = [catImgR, catImgL]
catWidth = catImgR.get_width()
catHeight = catImgR.get_height()
catXList = [screenX + catWidth, -catWidth]
catY = screenY - catHeight+5 # +5 because not on ground was
catXChangeList = [-0.2, 0.2]
cat_appear = False
catLove = False

bite_time_cat = 0
bite_time_on_cat = False

random_time_cat = 1000
i = 0
catX = catXList[i]
catXChange = catXChangeList[i]
catImg = catImgList[i]


def new_cat(current_time, random_time_cat):
    i = random.randrange(0, 2)
    catX = catXList[i]
    catXChange = catXChangeList[i]
    catImg = catImgList[i]
    cat_go_from_screen = current_time + random_time_cat + 3000  # enough to random
    random_time_cat_new = random.randint(cat_go_from_screen, cat_go_from_screen + random_time_cat)
    return catXChange, catX, catImg, random_time_cat_new


def cat(catX):
    screen.blit(catImg, (catX, catY))


def collision_cat_player(catX, catY, playerX, playerY):
    if playerX <= catX + catWidth / 2 <= playerX + playerWidth and playerY + playerHeight > catY:
        return True
    else:
        return False


# RAT
ratImgL = pygame.image.load('image/rat.png')
ratImgR = pygame.transform.flip(ratImgL, True, False)
ratImgList = [ratImgR, ratImgL]
ratWidth = ratImgR.get_width()
ratHeight = ratImgR.get_height()
ratXList = [screenX + ratWidth, -ratWidth]
ratY = screenY - 0.8 * ratHeight
ratXChangeList = [-0.2, 0.2]
rat_appear = False
ratLove = False

random_time_rat = 25000 #good time???
i = 0
ratX = ratXList[i]
ratXChange = ratXChangeList[i]
ratImg = ratImgList[i]

bite_time_on_rat = False
bite_time_rat = 0


def new_rat(current_time, random_time_rat):
    i = random.randrange(0, 2)
    ratX = ratXList[i]
    ratXChange = ratXChangeList[i]
    ratImg = ratImgList[i]
    rat_go_from_screen = current_time + random_time_rat + 3000
    random_time_rat_new = random.randint(rat_go_from_screen, rat_go_from_screen + random_time_rat)
    return ratXChange, ratX, ratImg, random_time_rat_new


def rat(ratX):
    screen.blit(ratImg, (ratX, ratY))


def collision_rat_player(ratX, ratY, playerX, playerY):
    if playerX <= ratX + ratWidth / 2 and playerX + playerWidth >= ratX + ratWidth / 2 and playerY + playerHeight > ratY:
        return True
    else:
        return False
'''
def show_kill_rat(ratX,ratY):
    killed=font.render("Killed rat!", True, (255,255,255))
    screen.blit(killed, (ratX, ratY))
    add time
'''

# BROOM -if new rule to lost broom change time and draw...
broomImg = pygame.image.load("image/broom.png")
broomWidth = broomImg.get_width()
broomHeight = broomImg.get_height()
broomX = -broomWidth
broomY = screenY - broomHeight
broom_appear = False
broom_witch = False
broom_draw = False
broom_witch_now = False
random_time_broom_old = 10   # 1000ms=1s
random_time_broom = 10
broom_time = 3


def random_time_broom_function(current_time):
    random_time_broom_return = int(
        random.randint(current_time + random_time_broom * 1000, current_time + random_time_broom * 1000 * 2) / 1000)    #??????more random
    return random_time_broom_return


def broomXRandom():
    broomX = random.randint(0, screenX - broomWidth)
    return broomX


def collision_broom_player(broomX, broomY, playerX, playerY):
    if broomX + broomWidth/2 >= playerX and playerX+playerWidth>broomX+batWidth/2:  # broom lay always on ground but player fly
        if playerY + playerHeight >= broomY:
            return True
        else:
            return False
    else:
        return False


def broom_player_draw(playerX, playerY):
    screen.blit(broomImg, (playerX, playerY))


# TRIDENT
tridentImg = pygame.image.load("image/trident.png")
tridentImgL = pygame.transform.flip(tridentImg, True, False)
tridentWidth = tridentImg.get_width()
tridentHeight = tridentImg.get_height()
tridentX = -tridentWidth
tridentY = screenY - tridentHeight
trident_appear = False
trident_draw = False
trident_witch = False
trident_witch_now = False
random_time_trident_old = 5
random_time_trident = 5
trident_time = 3
stab = False
stab_step = 0.1
stab_step_change = 2


def random_time_trident_function(current_time):
    random_time_trident_return = int(
        random.randint(current_time + random_time_trident * 1000, current_time + random_time_trident * 1000 * 2) / 1000)
    return random_time_trident_return


def tridentXRandom():
    tridentX = random.randint(0, screenX - tridentWidth)
    return tridentX


def collision_trident_player(tridentX, tridentY, playerX, playerY):
    if playerX <= tridentX + tridentWidth/2 <= playerX + playerWidth:  # trident lay always on ground
        if playerY + playerHeight >= tridentY:
            return True
        else:
            return False
    else:
        return False


def trident_player_draw(playerX, playerY):
    screen.blit(tridentImg, (playerX, playerY))


def collision_trident_rat(ratX, ratY, playerX, playerY, trident_witch_now):
    if trident_witch_now:
        if ratX + ratWidth >= playerX and playerX + playerWidth >= ratX and ratY <= playerY + playerHeight:
            return True
        else:
            return False
    else:
        return False


def collision_trident_cat(catX, catY, playerX, playerY, trident_witch_now, stab):
    if trident_witch_now and stab:
        if catX + catWidth >= playerX and playerX + playerWidth >= catX and catY <= playerY + playerHeight:
            return True
        else:
            return False
    else:
        return False


def collision_trident_spider(spiderX, spiderY, playerX, playerY, trident_witch_now):
    if trident_witch_now:
        if playerX <= spiderX + spiderWidth / 2 <= playerX + playerWidth and spiderY + spiderHeight >= playerY:
            return True
        else:
            return False
    else:
        return False


# HEALTH
health = 100


def change_health(health, x):
    health += x
    if health <= 0:
        health = 0
    elif health >= 100:
        health = 100
    return health


def draw_health(health):
    color = (0, 0, 0)
    long = screenX / 10 / 100 * health
    if 100 >= health >= 50:
        color = color_health_max = (0, 204, 0)
    elif 30 <= health < 50:
        color = color_health_half = (255, 255, 0)
    elif 15 <= health < 30:
        color = color_health_small = (255, 128, 0)
    elif 0 <= health < 15:
        color = color_health_red = (255, 0, 0)

    x = screenX - screenX / 10 - 20  # right corner screen , 1/10screen long, 20px space from right
    y = 20  # 20px space from top
    width = screenX / 10  # 1/10 screen long
    height = screenX / 50  # 1/5 * width

    pygame.draw.rect(screen, (50, 50, 50), pygame.Rect(x, y, width, height))
    pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(x - 1, y - 1, width + 2, height + 2), 1)
    pygame.draw.rect(screen, color, pygame.Rect(x, y, long, height))

    text = font.render("Health: " + str(health), True, (255, 255, 255))
    text_width = text.get_width()
    text_height = text.get_height()
    screen.blit(text, (x + width / 2 - text_width / 2, y + height / 2 - text_height / 2))


energy = 100


def draw_energy(energy):
    color = (0, 0, 0)
    long = screenX / 10 / 100 * energy
    if 100 >= energy >= 50:
        color = (0, 204, 0)
    elif 30 <= energy < 50:
        color = (255, 255, 0)
    elif 15 <= energy < 30:
        color = (255, 128, 0)
    elif 0 <= energy < 15:
        color = (255, 0, 0)

    width = screenX / 10  # 1/10 screen long
    height = screenX / 50  # 1/5 * width
    x = screenX - screenX / 10 - 20  # right corner screen , 1/10screen long, 20px space from right
    y = 20 + 20 + height  # 20px space from top

    pygame.draw.rect(screen, (50, 50, 50), pygame.Rect(x, y, width, height))
    pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(x - 1, y - 1, width + 2, height + 2), 1)
    pygame.draw.rect(screen, color, pygame.Rect(x, y, long, height))

    text = font.render("Energy: " + str(energy), True, (255, 255, 255))
    text_width = text.get_width()
    text_height = text.get_height()
    screen.blit(text, (x + width / 2 - text_width / 2, y + height / 2 - text_height / 2))

def draw_score(how_many_sweets):
    font = pygame.font.Font('freesansbold.ttf', 20)
    x = screenX - screenX / 10 - 20  # right corner screen , 1/10screen long, 20px space from right
    y = 20 + 20 + screenX / 50   # 20px space from top
    text = font.render("Score: " + str(how_many_sweets), True, (255, 255, 255))
    text_width = text.get_width()
    text_height = text.get_height()
    screen.blit(text, (x + screenX / 10 / 2 - text_width / 2, y + screenX / 50 / 2 - text_height / 2))


def paused():
    pauseImg=pygame.image.load('image/pause.png')
    pauseWidth = pauseImg.get_width()
    pauseHeight = pauseImg.get_height()
    pauseX = screenX/2-pauseWidth/2
    pauseY = screenY/2-pauseHeight/2
    screen.blit(pauseImg, (pauseX, pauseY))

    #screen.blit(pygame.font.Font('freesansbold.ttf', 150).render("Pause", True, (0,0,0)), ((screenX/2),(screenY/2)))

def info():
    #screen.blit(background_info, (0, 0))
    screen.fill((255,255,255))
    font_info=pygame.font.Font('Lacquer-Regular.ttf', 32)

    text1=font_info.render("Click 'm' to give ", True, (255,0,0))
    text1_width=text1.get_width()
    screen.blit(text1,  (20, 20))
    bulletImg_info = pygame.transform.scale(bulletImg, (32, 32))
    screen.blit(bulletImg_info, (20+text1_width, 20))
    text2 = font_info.render(" to ", True, (255, 0, 0))
    text2_width = text2.get_width()
    screen.blit(text2, (20+text1_width+32, 20))
    spiderImg_info=pygame.transform.scale(spiderImg, (32,32))
    screen.blit(spiderImg_info, (20 + text1_width+32+text2_width, 20))
    text3=font_info.render(" to have 'spider love'  ", True, (255,0,0))
    text3_width = text3.get_width()
    screen.blit(text3, (20+text1_width+text2_width+32+32, 20))
    spider_love_info = pygame.transform.scale(spider_love_img, (32, 32))
    screen.blit(spider_love_info, (20+text1_width+text2_width+32+32+text3_width, 20))

    y_2=20+32+20
    text4=font_info.render("Now spider don't bite. Spider bite = health - 3", True,(255,0,0))
    text4_width = text4.get_width()
    screen.blit(text4, (20, y_2))

    y_3=20+32+20+32+20
    text5=font_info.render("Pick up ", True,(255,0,0))
    screen.blit(text5, (20, y_3))
    tridentImg_info = pygame.transform.scale(tridentImg, (32, 32))
    screen.blit(tridentImg_info, (20 + text5.get_width(), y_3))
    text6 = font_info.render(" and stab ('space') to kill ", True, (255, 0, 0))
    screen.blit(text6, (20+text5.get_width()+32, y_3))
    ratImg_info=pygame.transform.scale(ratImg, (32, 32))
    screen.blit(ratImg_info, (20+text5.get_width()+32+text6.get_width(), y_3))
    text7 = font_info.render(" because ", True, (255, 0, 0))
    screen.blit(text7, (20 + text5.get_width() + 32 + text6.get_width() + 32, y_3))

    y_4=y_3+32+20
    text8 = font_info.render("they bite (health - 5). Don't stab ", True, (255, 0, 0))
    screen.blit(text8, (20, y_4))
    catImg_info = pygame.transform.scale(catImg, (32, 32))
    screen.blit(catImg_info, (20 + text8.get_width(), y_4))
    text9 = font_info.render(" . If stab they ", True, (255, 0, 0))
    screen.blit(text9, (20 + text8.get_width() + 32 , y_4))

    y_5=y_4+32+20
    text10 = font_info.render("bite (health - 2). Also avoid ", True, (255, 0, 0))
    screen.blit(text10, (20, y_5))
    screen.blit(spiderImg_info, (20 + text10.get_width(), y_5))
    text11 = font_info.render(" when have ", True, (255, 0, 0))
    screen.blit(text11, (20+text10.get_width()+32, y_5))
    screen.blit(tridentImg_info, (20+text10.get_width()+32+text11.get_width(), y_5))

    y_6=y_5+32+20
    text12 = font_info.render("Pick up  ", True, (255, 0, 0))
    screen.blit(text12, (20, y_6))
    broomImg_info=pygame.transform.scale(broomImg, (32, 32))
    screen.blit(broomImg_info, (20+ text12.get_width(), y_6))
    text13 = font_info.render(" to fly. Avoid ", True, (255, 0, 0))
    screen.blit(text13, (20+ text12.get_width()+32, y_6))
    batImg_info = pygame.transform.scale(batImgR, (32, 32))
    screen.blit(batImg_info, (20+ text12.get_width()+32+text13.get_width(), y_6))
    text14 = font_info.render("(health -1). Change ", True, (255, 0, 0))
    screen.blit(text14, (20+ text12.get_width()+32+text13.get_width()+32, y_6))

    y_7=y_6+32+20
    screen.blit(broomImg_info, (20, y_7))
    text15 = font_info.render(" to ", True, (255, 0, 0))
    screen.blit(text15, (20+32, y_7))
    screen.blit(tridentImg_info, (20+32+text15.get_width(), y_7))
    text16 = font_info.render(" or ", True, (255, 0, 0))
    screen.blit(text16, (20+32+text15.get_width()+32, y_7))
    screen.blit(tridentImg_info, (20+32+text15.get_width()+32+text16.get_width(), y_7))
    screen.blit(text15, (20+32+text15.get_width()+32+text16.get_width()+32, y_7))
    screen.blit(broomImg_info, (20+32+2*text15.get_width()+32+text16.get_width()+32, y_7))
    text17 = font_info.render(" by clicking 'l'. ", True, (255, 0, 0))
    screen.blit(text17, (20 + 32 + 2 * text15.get_width() + 32 + text16.get_width() + 32+32, y_7))

    y_8=y_7+32+20
    text18 = font_info.render("Avoid ", True, (255, 0, 0))
    screen.blit(text18, (20, y_8))
    treeImg_info = pygame.transform.scale(treeImg, (32, 32))
    screen.blit(treeImg_info, (20 + text18.get_width(), y_8))
    text19 = font_info.render(" (health - 10 !). Jump over or fly. ", True, (255, 0, 0))
    screen.blit(text19, (20+text18.get_width()+32, y_8))

    y_9=y_8+32+20
    text20= font_info.render("Collect sweets (cookies, candies, lollipops, ...).", True, (255, 0, 0))
    screen.blit(text20, (20, y_9))

    y_10 = y_9 + 32 + 20
    text21 = font_info.render("Info click 'i'. Pause click 'p'. Now click 'i' to go.",True, (255, 0, 0))
    screen.blit(text21, (20, y_10))

def GameOver():
    '''
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
    gameSurf = gameOverFont.render('Game', True, (0,0,0))
    overSurf = gameOverFont.render('Over', True, (0,0,0))
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (screenX / 2, 10)
    overRect.midtop = (screenX / 2, gameRect.height + 10 + 25)

    screen.blit(gameSurf, gameRect)
    screen.blit(overSurf, overRect)
    #drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(50000)
    #checkForKeyPress()  # clear out any key presses in the event queue
    '''
    gameoverImg = pygame.image.load('image/game-over.png')
    gameoverWidth = gameoverImg.get_width()
    gameoverHeight = gameoverImg.get_height()
    gameoverX = screenX / 2 - gameoverWidth / 2
    gameoverY = screenY / 2 - gameoverHeight / 2
    screen.blit(gameoverImg, (gameoverX, gameoverY))
    #screen.blit(font.render("You have: "+str(how_many_sweets)+" sweets!", True, (255,255,255)), ((20),(screenY/2))) yes or no?


# LOOP RUNING SCREEN

running = True
character = True
informations = True
pause=False
current_time = 0
char_time=0
info_time=0
pause_time=0
char_time_start=0
char_time_end=0
info_time_start=0
info_time_end=0
pause_time_start=0
pause_time_end=0
while running:

    while character:#############################################################################
        font_character = pygame.font.SysFont('Bauhaus 93', 36)
        text_char = font_character.render("SELECT CHARACTER", True, (255, 255, 0))
        text_char_width=text_char.get_width()
        text_char_height = text_char.get_height()+40
        screen.blit(text_char, (screenX/2-text_char_width/2, 40))

        distanceX=(screenX-3*playerWidth)/4 #tree picture in x line so 4 distance
        distanceY=((screenY-text_char_height)-2*playerHeight)/3 #two picture in y line

        oneXY=(distanceX, distanceY+text_char_height)
        twoXY=(2*distanceX+playerWidth, distanceY+text_char_height)
        threeXY=(3*distanceX+2*playerWidth, distanceY+text_char_height)
        fourXY=(distanceX, 2*distanceY+playerHeight+text_char_height)
        fiveXY=(2*distanceX+playerWidth, 2*distanceY+playerHeight+text_char_height)
        sixXY=(3*distanceX+2*playerWidth, 2*distanceY+playerHeight+text_char_height)

        screen.blit(playerOneImg, oneXY)
        screen.blit(playerTwoImg, (twoXY))
        screen.blit(playerThreeImg, (threeXY))
        screen.blit(playerFourImg, (fourXY))
        screen.blit(playerFiveImg, (fiveXY))
        screen.blit(playerSixImg, (sixXY))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):#??not working? ???????????????????????????@@@@@@@@@@@@@@@@@@@@@@@@@@
                character = False
                running = False
                informations = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_v:
                    character=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                x, y = event.pos
                #print(x,y)
                if oneXY[0]+playerWidth>x>oneXY[0] and oneXY[1]+playerHeight>y>oneXY[1]:
                    playerImg=playerOneImg
                    character=False
                if twoXY[0]+playerWidth>x>twoXY[0] and twoXY[1]+playerHeight>y>twoXY[1]:
                    playerImg=playerTwoImg
                    character=False
                if threeXY[0]+playerWidth>x>threeXY[0] and threeXY[1]+playerHeight>y>threeXY[1]:
                    playerImg=playerThreeImg
                    character=False
                if fourXY[0]+playerWidth>x>fourXY[0] and fourXY[1]+playerHeight>y>fourXY[1]:
                    playerImg=playerFourImg
                    character=False
                if fiveXY[0]+playerWidth>x>fiveXY[0] and fiveXY[1]+playerHeight>y>fiveXY[1]:
                    playerImg=playerFiveImg
                    character=False
                if sixXY[0]+playerWidth>x>sixXY[0] and sixXY[1]+playerHeight>y>sixXY[1]:
                    playerImg=playerSixImg
                    character=False
            if character==False:
                char_time_end = pygame.time.get_ticks()
                char_time+=char_time_end+char_time_start
                info_time_start=char_time_end
        pygame.display.update()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # player left right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if not pause:
                    pause = True
                    pasue_time_start=pygame.time.get_ticks()
                elif pause:
                    pause=False
            if event.key == pygame.K_LEFT:
                if broom_witch_now:
                    playerXChange = -0.8 * speed
                else:
                    playerXChange = -speed
            if event.key == pygame.K_RIGHT:
                if broom_witch_now:
                    playerXChange = 0.8 * speed
                else:
                    playerXChange = speed
            if event.key == pygame.K_UP:
                if broom_witch_now:
                    playerYChange = -0.8 * speed
                elif not jump:
                    jump = True
                    #playerYChange = -0.8 * speed  #################3grawitacja
            if event.key == pygame.K_DOWN:
                if broom_witch_now:
                    playerYChange = 0.8 * speed

            if event.key == pygame.K_m:
                if bullet_state == "ready":
                    bulletX = playerX
                    bullet_sound=mixer.Sound('sounds/drinkspider.wav')
                    bullet_sound.play()
                    fire_bullet(playerX, bulletY)

            if event.key == pygame.K_l:
                # TRIDENT OR BROOM ONE OF TWO
                if trident_witch and broom_witch:
                    if trident_witch_now:
                        trident_witch_now = False  # TU TEŻ ZMIENI???????????????
                        broom_witch_now = True
                        switch_sound = mixer.Sound('sounds/switch.mp3')
                        switch_sound.play()
                    elif broom_witch_now:
                        if playerY >= screenY - 2*playerHeight:
                            broom_witch_now = False
                            trident_witch_now = True
                            switch_sound = mixer.Sound('sounds/switch.mp3')
                            switch_sound.play()
                            if playerYChange<0:
                                playerYChange=-playerYChange
                        else:
                            print("You should be on ground to change")

            if event.key == pygame.K_SPACE and trident_witch_now:
                stab_step = 0.1
                stab = True
                trident_sound = mixer.Sound('sounds/trident.wav')
                trident_sound.play()

            if event.key == pygame.K_i:
                informations=True
                info_time_start=pygame.time.get_ticks()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerXChange = 0
                # playerYChange = 0
    paused_time_to_subtract=0
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = False
                    pause_time_end=pygame.time.get_ticks()
                    pause_time+=pause_time_end-pasue_time_start
        paused()
    

    while informations:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i or event.key == pygame.K_KP_ENTER:
                    informations = False
                    info_time_end=pygame.time.get_ticks()
                    info_time=info_time+(info_time_end-info_time_start)
        info()


        pygame.display.update()

                # UPDATE SCREEN
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    current_time = pygame.time.get_ticks()
    current_time-=(pause_time+info_time+char_time)
    #print(current_time)##########################################
    # PLAYER
    playerX = playerX + playerXChange
    if playerX <= 0:
        playerX = 0
    elif playerX >= screenX - playerWidth:
        playerX = screenX - playerWidth
    playerY = playerY + playerYChange
    if playerY <= 20:
        playerY = 20
        playerYChange = -playerYChange
    elif playerY >= screenY - playerHeight:
        playerY = screenY - playerHeight

    jump_height = playerHeight
    if jump:
        #F = (1 / 2) * m * (v ** 2)
        #playerY -= F        # change in the y co-ordinate
        if jumpCount>= -250:
            playerY -= (jumpCount * abs(jumpCount))*0.00003
            jumpCount -= 1
        else:
            jumpCount=250
            jump=False
        '''
        playerY = playerY + playerYChange
        if playerY < screenY / 2:
            playerYChange = -playerYChange

            print("pdwrót")
        if playerY >= screenY - playerHeight:
            jump = False
            playerY = screenY + playerHeight
        '''
    player(playerX, playerY)

    #CANDIES
    if current_time>random_time_candies:
        new_candies(current_time)
        how_many_candies+=1
        random_time_candies=random.randint(current_time, current_time+4000)
    #print(how_many_candies, len(candiesImg))
    kill=[] #list of index candy to kill (time out or collision)
    for candy in range(len(candiesImg)):
        screen.blit(candiesImg[candy], (candyX[candy], candyY[candy]))
        #print("candy:", candy)
        if current_time>candyTime[candy]:
            kill.append(candy)
        if collision_player_candies(candyX[candy], candyY[candy], playerX, playerY):
            kill.append(candy)
            how_many_sweets+=1
            #print("collision")
    if len(kill)>0: #check if list to kill is no empty
        J=set(kill) #change list to set to avoid repeat
        K=list(J)   #change to list again
        kill=(K[::-1]) #list from the largest number to kill from end of list candies
    for k in range(len(kill)): #kill candies from list
        del candiesImg[k]
        del candyX[k]
        del candyY[k]
        del candyTime[k]
        how_many_candies -= 1


    # TREE
    if current_time > random_time_tree and not tree_appear:
        tree_appear = True
    if tree_appear:
        new_tree(treeX)
    if current_time > random_time_tree + tree_time:
        random_time_tree, treeX = random_time_tree_function(current_time, random_time_tree)
        tree_appear = False

    if collision_tree_player(treeX, treeY, playerX, playerY) and tree_appear:
        if playerX + playerWidth / 2 < treeX + treeWidth / 2:
            playerX -= 20
        elif playerX + playerWidth / 2 > treeX + treeWidth / 2:
            playerX += 20
        if not bite_time_on_tree:
            tree_sound = mixer.Sound('sounds/zombie.wav')
            tree_sound.play()
            health = change_health(health, -10)
            bite_time_on_tree = True
            bite_time_tree = pygame.time.get_ticks()
    if bite_time_on_tree and current_time - bite_time_tree > 1000:
        bite_time_on_tree = False

    # BAT
    #print(numbers_of_bat)
    if current_time>new_bat_time:
        new_bat()
        numbers_of_bat+=1
        #print(new_bat_time)
        new_bat_time=random.randint(current_time+2000, current_time+4000)

    for bat in range(numbers_of_bat):
        batX[bat] += batX_change[bat]
        screen.blit(batImg[bat], (batX[bat], batY[bat]))
    #print(numbers_of_bat)
    for bat in range(numbers_of_bat):
        if bat>numbers_of_bat-1:
            break
        if batX[bat] > screenX or batX[bat] < -batWidth:
            del batImg[bat]
            del batX[bat]
            del batY[bat]
            del batX_change[bat]
            numbers_of_bat -= 1
    for bat in range(numbers_of_bat):
        if collision_bat_player(batX[bat], batY[bat], playerX, playerY):
            health = change_health(health, -1)
            bat_sound = mixer.Sound('sounds/bat.wav')
            bat_sound.play()
            if playerX+playerWidth/2<batX[bat]+batWidth/2:
                playerX-=20
            elif playerX+playerWidth/2>=batX[bat]+batWidth/2:
                playerX+=20
            if playerY+playerHeight/2<batY[bat]+batHeight/2:
                playerY-=20
            elif playerY + playerHeight / 2 >= batY[bat] + batHeight / 2:
                playerY += 20
    '''
    for bat in range(numbers_of_bat):
        batX[bat]+=batX_change[bat]
        if batX[bat]>2*screenX or batX[bat]<-screenX:
            batX_change[bat] = -batX_change[bat]
            batImg[bat]=pygame.transform.flip(batImg[bat], True, False)
            batY[bat]=(random.randint(20, screenY - playerHeight))
        screen.blit(batImg[bat], (batX[bat], batY[bat]))
    '''
    # SPIDER
    spiderY = spiderY + spiderY_change
    if spiderY >= spiderDrop:
        spiderY_change = -spiderY_change
    elif spiderY < - spiderHeight:
        spiderX, spiderY, spiderY_change, spiderDrop = new_spider()
    spider(spiderX, spiderY)

    # bullet movment
    if bulletY <= 0:
        bulletY = playerY
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    collision = False
    # Collision Spider bullet
    if bullet_state == "fire":
        collision = collision_spider_bullet(spiderX, spiderY, bulletX, bulletY)
    if collision:
        if bulletY == playerY:
            continue
        bulletY = playerY
        bullet_state = "ready"
        spider_love = True
        if spiderY_change > 0:
            spiderY_change = -spiderY_change
    if spider_love == True:
        spider_love_draw(0, 0)
        # show_spider_love()
        # spiderDrop -= playerHeight#################dodać to przy malowaniu?? czy czasowo będzie czy wcale

    # Colision spider player - POISON - SPIDER BITE
    bite = collision_spider_player(spiderX, spiderY, playerX, playerY)
    if bite:
        if bite_time_on_spider == False and spider_love == False:
            spider_sound = mixer.Sound('sounds/bite.wav')
            spider_sound.play()
            health = change_health(health, -3)
            bite_time_on_spider = True
            bite_time_spider = pygame.time.get_ticks()
    if current_time - bite_time_spider > 2000:
        bite_time_on_spider = False

    # BROOM
    if current_time > 1000 * random_time_broom and not broom_appear and not broom_witch:  # can change to more clear but no
        broom_draw = True
        broom_appear = True

    if broom_draw:
        broomX = broomXRandom()
        random_time_broom_old = random_time_broom
        random_time_broom = random_time_broom_function(current_time)
        broom_draw = False

    if broom_appear:
        screen.blit(broomImg, (broomX, screenY - broomWidth))

    if random_time_broom_old * 1000 + broom_time * 1000 < current_time and broom_appear:
        broom_appear = False

    if collision_broom_player(broomX, broomY, playerX, playerY) and broom_appear:
        if not broom_witch:
            broom_appear = False
            broom_witch = True
            broom_witch_now = True
            # screen.blit(broomImg, (screenX/2, screenY))###

    if broom_witch:
        if broom_witch_now:
            trident_witch_now = False
            broom_player_draw(playerX + playerWidth / 2 - broomWidth / 2,
                              playerY + playerHeight - broomHeight / 2)  # is good that level broom?
        if trident_witch and broom_witch_now:
            trident_player_draw(screenX-20-tridentWidth, 100)

    # TRIDENT

    if current_time > 1000 * random_time_trident and not trident_appear and not trident_witch:  # after minute or random??
        trident_draw = True
        trident_appear = True

    if trident_draw:
        tridentX = tridentXRandom()
        random_time_trident_old = random_time_trident
        random_time_trident = random_time_trident_function(current_time)
        trident_draw = False

    if trident_appear:
        screen.blit(tridentImg, (tridentX, screenY - tridentWidth))

    if random_time_trident_old * 1000 + trident_time * 1000 < current_time and trident_appear:
        trident_appear = False

    if collision_trident_player(tridentX, tridentY, playerX, playerY) and trident_appear:
        if not trident_witch:
            trident_appear = False
            trident_witch = True
            trident_witch_now = True

    if trident_witch:
        if trident_witch_now:

            distance = screenX / 2
            side = "right"
            animalWidth = catWidth  ##because catWidth=ratWidth and this is neccessery to x
            for animal in {ratX, catX, treeX}:
                if animal + animalWidth / 2 >= playerX + playerWidth / 2:
                    x = animal + animalWidth / 2 - playerX + playerWidth / 2
                    if x < distance:
                        distance = x
                        side = "right"
                elif animal + animalWidth / 2 < playerX + playerWidth / 2:
                    x = abs(animal + animalWidth / 2 - playerX + playerWidth / 2)
                    if x < distance:
                        distance = x
                        side = "left"
            # print(side)
            if distance > screenX / 4:
                side = "right"
            if side == "right" and not stab:
                trident_player_draw(playerX + playerWidth / 2 - tridentWidth / 2,
                                    playerY + playerHeight - tridentHeight)  # is good that level trident?
            elif side == "left" and not stab and (rat_appear or cat_appear):
                screen.blit(tridentImgL, (playerX + playerWidth / 2 - tridentWidth / 2,
                                          playerY + playerHeight - tridentHeight))
            elif stab:  # STAB STAB STAB is good??????????????????????????????????
                stab_step += stab_step_change
                if stab_step >= playerWidth / 2:
                    stab_step_change = -stab_step_change
                elif stab_step < 0:
                    stab_step = 0
                    stab_step_change = abs(stab_step_change)
                    stab = False
                    #print("Stabend")
                if side == "left" and (rat_appear or cat_appear):
                    screen.blit(tridentImgL, (playerX + playerWidth / 2 - tridentWidth / 2 - stab_step,
                                              playerY + playerHeight - tridentHeight))
                else:
                    trident_player_draw(playerX + playerWidth / 2 - tridentWidth / 2 + stab_step,
                                        playerY + playerHeight - tridentHeight)
            else:
                trident_player_draw(playerX + playerWidth / 2 - tridentWidth / 2,
                                    playerY + playerHeight - tridentHeight)

            broom_witch_now = False
        if broom_witch and trident_witch_now:
            broom_player_draw(screenX-20-broomWidth, 100)

    if collision_trident_rat(ratX, ratY, playerX, playerY, trident_witch_now) and rat_appear and stab:
        rat_sound = mixer.Sound('sounds/rat.wav')
        rat_sound.play()
        #show_kill_rat(ratX,ratY)
        rat_appear = False
        ratX = -ratWidth

    if collision_trident_cat(catX, catY, playerX, playerY, trident_witch_now, stab) and cat_appear and stab:
        #    cat_love=False
        if bite_time_on_cat == False:
            cat_sound = mixer.Sound('sounds/cat.wav')
            cat_sound.play()
            health = change_health(health, -2)
            bite_time_on_cat = True
            bite_time_cat = pygame.time.get_ticks()
    if current_time - bite_time_cat > 2000:
        bite_time_on_cat = False

    if collision_trident_spider(spiderX, spiderY, playerX, playerY, trident_witch_now) and spider_love:
        spider_love = False  # or if stab also???

    # CAT
    if current_time > random_time_cat and not cat_appear:  # after minute or random??
        cat_appear = True
        catXChange, catX, catImg, random_time_cat = new_cat(current_time, random_time_cat)
        #print(random_time_cat)
    if cat_appear:
        cat(catX)
    catX = catX + catXChange
    if catX < -catWidth or catX > screenX + catWidth:
        cat_appear = False

    # if collision_cat_player(catX, catY, playerX, playerY) and cat_appear:

    # RAT
    if current_time > random_time_rat and not rat_appear:  # after minute or random??
        rat_appear = True
        ratXChange, ratX, ratImg, random_time_rat = new_rat(current_time, random_time_rat)
        #print(random_time_rat)
    if rat_appear:
        rat(ratX)
    ratX = ratX + ratXChange
    if ratX < -ratWidth or ratX > screenX + ratWidth:
        rat_appear = False

    if collision_rat_player(ratX, ratY, playerX, playerY) and rat_appear:
        if bite_time_on_rat == False:  # and trident == False:
            health = change_health(health, -5)
            ratbite_sound = mixer.Sound('sounds/ratbite.wav')
            ratbite_sound.play()
            bite_time_on_rat = True
            bite_time_rat = pygame.time.get_ticks()
    if current_time - bite_time_rat > 2000:
        bite_time_on_rat = False

    draw_health(health)
    #draw_energy(energy)
    draw_score(how_many_sweets)

    if health<=0:
        GameOver()



    pygame.display.update()
