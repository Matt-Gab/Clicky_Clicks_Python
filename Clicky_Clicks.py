import pygame
pygame.init()

# code variables

Black = (0, 0, 0)
Light_Blue = (173, 216, 230)
Blue = (0, 100, 250)
Display = pygame.display.set_mode([800, 600])
pygame.display.set_caption('clicky clicks')
Tick_Rate = pygame.time.Clock()

# clicker game variables

Coins = 50
Clicker_Amount = 1
Clicker_Cost = 50
Auto_Clicker_Amount = 0
Auto_Clicker_Cost = 50
Duration = 0
Use_Clicker = False
Use_Buy_Auto_Clicker = False
Use_Buy_Clicker = False

# clicker game functions

def Auto_Clicker():
    global Coins
    global Auto_Clicker_Amount
    global Duration
    
    if Duration < 60:
        Duration += 1
    elif Duration:
        Duration = 0
        Coins = Coins + (Auto_Clicker_Amount * 10)
    return Duration

def Clicker():
    global Coins
    global Use_Clicker
    
    if Use_Clicker == True:
        Coins += Clicker_Amount
        Use_Clicker = False
    Hitbox_Clicker = pygame.draw.circle(Display, Blue, [400, 260], 60)
    return Hitbox_Clicker

def Buy_Button(X_Coords, Y_Coords):
    global Coins
    global Auto_Clicker_Cost
    global Clicker_Cost
    global Auto_Clicker_Amount
    global Clicker_Amount
    global Use_Buy_Auto_Clicker
    global Use_Buy_Clicker
    
    if Use_Buy_Auto_Clicker and Coins >= Auto_Clicker_Cost:
        Coins -= Auto_Clicker_Cost
        Auto_Clicker_Cost = Auto_Clicker_Cost * 1.5
        Auto_Clicker_Amount = Auto_Clicker_Amount + 0.5
        Use_Buy_Auto_Clicker = False
    if Use_Buy_Clicker and Coins >= Clicker_Cost:
        Coins -= Clicker_Cost
        Clicker_Cost = Clicker_Cost * 1.5
        Clicker_Amount = Clicker_Amount * 1.1
        Use_Buy_Clicker = False
    Hitbox_Buy_Button = pygame.draw.rect(Display, Blue, (X_Coords, Y_Coords, 200, 300))
    return Hitbox_Buy_Button

def Text(Text, X_Center, Y_Center, Font_Size):
    Font = pygame.font.Font('freesansbold.ttf', Font_Size)
    Text = Font.render(Text, True, Black)
    Text_Box = Text.get_rect()
    Text_Box.center = (X_Center, Y_Center)
    Display.blit(Text, Text_Box)

Game_Running = True
while Game_Running:
    Auto_Clicker()
    Tick_Rate.tick(60)       # 1 sec / 30 ticks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game_Running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Clicked_On_Clicker.collidepoint(event.pos):
                Use_Clicker = True
            if Clicked_On_Buy_Auto_Clicker.collidepoint(event.pos):
                Use_Buy_Auto_Clicker = True
            if Clicked_On_Buy_Clicker.collidepoint(event.pos):
                Use_Buy_Clicker = True

# drawing of game

    Display.fill(Light_Blue)
    
    Clicked_On_Clicker = Clicker()
    
    Clicked_On_Buy_Auto_Clicker = Buy_Button(50, 400)
    
    Clicked_On_Buy_Clicker = Buy_Button(600, 317)
    
    Text('you have ' + f'{Coins:.2f}' + ' coins', 100, 50, 20)
    Text('Version: Beta 0.1.6.3', 650, 50, 20)
    Text('Clicky Clicks', 400, 100, 50)
    Text('buy auto miner ' + str(Auto_Clicker_Cost), 150, 370, 20)
    Text('upgrade clicker ' + str(Clicker_Cost), 700, 300, 20)

    pygame.display.update()
    
pygame.quit()