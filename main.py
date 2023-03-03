# Налаштування гри та підгрузка класів
    # Підлкючення бібліотек
import pygame
from pygame import mixer
import os
from Image2 import Image
from character import Character
from level import *
from text import Text
from ores import Ores
from values import *

    # Ініціалізуємо pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()
    # Налаштування вікна
screen = pygame.display.set_mode((1080, 720))
font = pygame.font.SysFont('Comic Sans MS', 27)
pygame.display.set_caption('Unknown Depths')
    #Налаштування гри
mixer.music.load(os.path.abspath(__file__ + "/..") + '/sounds/mainmenuost.wav')
menu = None
clock = pygame.time.Clock()
mouse_position = 1
scene = 1
page = 1
helppage = 1
game = True
music = True
ost = True
save_key = pygame.key.get_pressed()

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        # Меню
        if scene == 1:
        #кнопки
            #кнопка play
            if  event.type == pygame.MOUSEMOTION:
                if event.pos[0] > buttonplay.X and event.pos[0] < buttonplay.X + buttonplay.WIDTH and event.pos[1] > buttonplay.Y and event.pos[1] < buttonplay.Y + buttonplay.HEIGHT:
                    buttonplay.PATH = "/image/buttonplay2.png"
                    buttonplay.load_image()
                else:
                    buttonplay.PATH = "/image/buttonplay1.png"
                    buttonplay.load_image()
            #кнопка help
                if event.pos[0] > buttonhelp.X and event.pos[0] < buttonhelp.X + buttonhelp.WIDTH and event.pos[1] > buttonhelp.Y and event.pos[1] < buttonhelp.Y + buttonhelp.HEIGHT:
                    buttonhelp.PATH = "/image/buttonhelp2.png"
                    buttonhelp.load_image()
                else:
                    buttonhelp.PATH = "/image/buttonhelp1.png"
                    buttonhelp.load_image()
            
            #кнопка exit
                if event.pos[0] > buttonexit.X and event.pos[0] < buttonexit.X + buttonexit.WIDTH and event.pos[1] > buttonexit.Y and event.pos[1] < buttonexit.Y + buttonexit.HEIGHT:
                    buttonexit.PATH = "/image/buttonexit2.png"
                    buttonexit.load_image()
                else:
                    buttonexit.PATH = "/image/buttonexit1.png"
                    buttonexit.load_image()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.pos[0] > buttonplay.X and event.pos[0] < buttonplay.X + buttonplay.WIDTH and event.pos[1] > buttonplay.Y and event.pos[1] < buttonplay.Y + buttonplay.HEIGHT:
                    scene = 18
                    mainchar.X_sprite = 20
                    mainchar.Y_sprite = 720 - 27 * 3
                    buttonsound.play(1)
                    mixer.music.set_volume(0.3)
                if event.pos[0] > buttonhelp.X and event.pos[0] < buttonhelp.X + buttonhelp.WIDTH and event.pos[1] > buttonhelp.Y and event.pos[1] < buttonhelp.Y + buttonhelp.HEIGHT:
                    scene = 21
                    buttonsound.play(1)
                if event.pos[0] > buttonexit.X and event.pos[0] < buttonexit.X + buttonexit.WIDTH and event.pos[1] > buttonexit.Y and event.pos[1] < buttonexit.Y + buttonexit.HEIGHT:
                    buttonsound.play(1)
                    game = False
            
            background.show_image(screen)
            buttonplay.show_image(screen)
            buttonhelp.show_image(screen)
            buttonexit.show_image(screen)
            logo.show_image(screen)
        # Таверна
        elif scene == 3:
            if ost:
                tavernaost.play(-1)
                ost = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.pos[0] > buttonsell.X and event.pos[0] < buttonsell.X + buttonsell.WIDTH and event.pos[1] > buttonsell.Y and event.pos[1] < buttonsell.Y + buttonsell.HEIGHT:
                    menu = 'sell'
                    buttonsound.play(1)
                if event.pos[0] > buttonbuy.X and event.pos[0] < buttonbuy.X + buttonbuy.WIDTH and event.pos[1] > buttonbuy.Y and event.pos[1] < buttonbuy.Y + buttonbuy.HEIGHT:
                    menu = 'buy'
                    buttonsound.play(1)
                if mainchar.hp != mainchar.hp_max:
                    if event.pos[0] > recover.X and event.pos[0] < recover.X + recover.WIDTH and event.pos[1] > recover.Y and event.pos[1] < recover.Y + recover.HEIGHT:
                        if mainchar.coin >= 10 and mainchar.hp != mainchar.hp_max:
                            mainchar.coin -= 10
                            mainchar.hp = mainchar.hp_max
            if mainchar.hp != mainchar.hp_max:
                if event.type == pygame.MOUSEMOTION:
                    if event.pos[0] > recover.X and event.pos[0] < recover.X + recover.WIDTH and event.pos[1] > recover.Y and event.pos[1] < recover.Y + recover.HEIGHT:
                        recover.PATH = '/image/taverna/recoverybutton2.png'
                        recover.load_image()
                    else:
                        recover.PATH = '/image/taverna/recoverybutton.png'
                        recover.load_image()
            # tavernaost.play(0)
            keys = pygame.key.get_pressed()
            tavernabg.show_image(screen)
            Esc.show_image(screen)
            buttonsell.show_image(screen)
            buttonbuy.show_image(screen)
            coin6.show_image(screen)
            if mainchar.hp != mainchar.hp_max:
                recover.show_image(screen)
                coin8.show_image(screen)
                recoverprice.show_text(screen)
            monyewehave.TEXT = str(mainchar.coin)
            monyewehave.load_text()
            monyewehave.show_text(screen)
            if menu == 'sell':
                sellall.show_image(screen)
                diamondcount.TEXT = str(mainchar.diamond)
                emeraldscount.TEXT = str(mainchar.emeralds)
                goldcount.TEXT = str(mainchar.gold)
                silvercount.TEXT = str(mainchar.silver)
                ironcount.TEXT = str(mainchar.iron)
                buttonsell.PATH = '/image/taverna/sell2.png'
                buttonbuy.PATH = '/image/taverna/buy1.png'
                buttonbuy.load_image()
                buttonsell.load_image()
                buttonsellemeralds.show_image(screen)
                buttonselldiamond.show_image(screen)
                buttonsellgold.show_image(screen)
                buttonselliron.show_image(screen)
                buttonsellsilver.show_image(screen)
                diamondprice.show_text(screen)
                emeraldsprice.show_text(screen)
                goldprice.show_text(screen)
                ironprice.show_text(screen)
                silverprice.show_text(screen)
                diamondcount.load_text()
                diamondcount.show_text(screen)
                emeraldscount.load_text()
                emeraldscount.show_text(screen)
                goldcount.load_text()
                goldcount.show_text(screen)
                silvercount.load_text()
                silvercount.show_text(screen)
                ironcount.load_text()
                ironcount.show_text(screen)
                
                for i in list_coin:
                    i.show_image(screen)
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.pos[0] > buttonselldiamond.X and event.pos[0] < buttonselldiamond.X + buttonselldiamond.WIDTH and event.pos[1] > buttonselldiamond.Y and event.pos[1] < buttonselldiamond.Y + buttonselldiamond.HEIGHT:
                        if mainchar.diamond > 0:
                            mainchar.diamond -= 1
                            mainchar.coin += 4
                            buttonsound.play(1)
                    if event.pos[0] > buttonsellemeralds.X and event.pos[0] < buttonsellemeralds.X + buttonsellemeralds.WIDTH and event.pos[1] > buttonsellemeralds.Y and event.pos[1] < buttonsellemeralds.Y + buttonsellemeralds.HEIGHT:
                        if mainchar.emeralds > 0:
                            mainchar.emeralds -= 1
                            mainchar.coin += 5
                            buttonsound.play(1)
                    if event.pos[0] > buttonsellgold.X and event.pos[0] < buttonsellgold.X + buttonsellgold.WIDTH and event.pos[1] > buttonsellgold.Y and event.pos[1] < buttonsellgold.Y + buttonsellgold.HEIGHT:
                        if mainchar.gold > 0:
                            mainchar.gold -= 1
                            mainchar.coin += 3
                            buttonsound.play(1)
                    if event.pos[0] > buttonsellsilver.X and event.pos[0] < buttonsellsilver.X + buttonsellsilver.WIDTH and event.pos[1] > buttonsellsilver.Y and event.pos[1] < buttonsellsilver.Y + buttonsellsilver.HEIGHT:
                        if mainchar.silver > 0:
                            mainchar.silver -= 1
                            mainchar.coin += 2
                            buttonsound.play(1)
                    if event.pos[0] > buttonselliron.X and event.pos[0] < buttonselliron.X + buttonselliron.WIDTH and event.pos[1] > buttonselliron.Y and event.pos[1] < buttonselliron.Y + buttonselliron.HEIGHT:
                        if mainchar.iron > 0:
                            mainchar.iron -= 1
                            mainchar.coin += 1
                            buttonsound.play(1)
                    if event.pos[0] > sellall.X and event.pos[0] < sellall.X + sellall.WIDTH and event.pos[1] > sellall.Y and event.pos[1] < sellall.Y + sellall.HEIGHT:
                        if mainchar.iron > 0:
                            mainchar.coin += 1 * mainchar.iron
                            mainchar.iron = 0
                        if mainchar.silver > 0:
                            mainchar.coin += 2 * mainchar.silver
                            mainchar.silver = 0
                        if mainchar.gold > 0:
                            mainchar.coin += 3 * mainchar.gold
                            mainchar.gold = 0
                        if mainchar.diamond > 0:
                            mainchar.coin += 4 * mainchar.diamond
                            mainchar.diamond = 0
                        if mainchar.emeralds > 0:
                            mainchar.coin += 5 * mainchar.emeralds
                            mainchar.emeralds = 0
                        buttonsound.play(1)
            if menu == 'buy':
                buttonsell.PATH = '/image/taverna/sell1.png'
                buttonbuy.PATH = '/image/taverna/buy2.png'
                buttonbuy.load_image()
                buttonsell.load_image()
                if mainchar.hp_max != 5:
                    heartupgrade.show_image(screen)
                    heartupgradeprice.show_text(screen)
                    coin7.show_image(screen)
                if mainchar.hp_max == 2:
                    heartupgradeprice.TEXT = '20'
                    heartupgradeprice.load_text()
                if mainchar.hp_max == 3:
                    heartupgradeprice.TEXT = '40'
                    heartupgradeprice.load_text()
                if mainchar.hp_max == 4:
                    heartupgradeprice.TEXT = '70'
                    heartupgradeprice.load_text()
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.pos[0] > heartupgrade.X and event.pos[0] < heartupgrade.X + heartupgrade.WIDTH and event.pos[1] > heartupgrade.Y and event.pos[1] < heartupgrade.Y + heartupgrade.HEIGHT:
                        if mainchar.hp_max == 2:
                            if mainchar.coin >= 20:
                                mainchar.hp_max = 3
                                mainchar.coin -= 20
                        elif mainchar.hp_max == 3:
                            if mainchar.coin >= 40:
                                mainchar.hp_max = 4
                                mainchar.coin -= 40
                        elif mainchar.hp_max == 4:
                            if mainchar.coin >= 50:
                                mainchar.hp_max = 5
                                mainchar.coin -= 70
                        buttonsound.play(1)
                
            mainchar.leave_taverna()
            if mainchar.can_entern_taverna != True:
                tavernaost.stop()
                ost = True
                scene = 2
        #Початкова заставка 1
        elif scene == 18:
            history1.show_image(screen)
            buttonnext.show_image(screen)
            if event.type == pygame.MOUSEBUTTONUP:
                if event.pos[0] > buttonnext.X and event.pos[0] < buttonnext.X + buttonnext.WIDTH and event.pos[1] > buttonnext.Y and event.pos[1] < buttonnext.Y + buttonnext.HEIGHT:
                    scene = 19
                    pageturn.play(0)
        #Початкова заставка 2
        elif scene == 19:
            history2.show_image(screen)
            buttonnext.show_image(screen)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] > buttonnext.X and event.pos[0] < buttonnext.X + buttonnext.WIDTH and event.pos[1] > buttonnext.Y and event.pos[1] < buttonnext.Y + buttonnext.HEIGHT:
                    scene = 2
                    pageturn.play(0)
                    mixer.music.stop()

        # Кінцева заставка 
        elif scene == 20:
            if page == 1:
                history3.show_image(screen)
                buttontry.show_image(screen)
                buttonleave.show_image(screen)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[0] > buttonleave.X and event.pos[0] < buttonleave.X + buttonleave.WIDTH and event.pos[1] > buttonleave.Y and event.pos[1] < buttonleave.Y + buttonnext.HEIGHT:
                        page = 2
                        pageturn.play(0)
                    if event.pos[0] > buttontry.X and event.pos[0] < buttontry.X + buttontry.WIDTH and event.pos[1] > buttontry.Y and event.pos[1] < buttontry.Y + buttontry.HEIGHT:
                        page = 3
                        pageturn.play(0)
            if page == 2:
                history4.show_image(screen)
            if page == 3:
                history5.show_image(screen)
        elif scene == 21:
            eys = pygame.key.get_pressed()
            mixer.music.set_volume(0.3)
            if helppage == 1:
                help1.show_image(screen)
                buttonnext1.show_image(screen)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[0] > buttonnext1.X and event.pos[0] < buttonnext1.X + buttonnext1.WIDTH and event.pos[1] > buttonnext1.Y and event.pos[1] < buttonnext1.Y + buttonnext1.HEIGHT:
                        pageturn.play()
                        helppage = 2
            if helppage == 2:
                help2.show_image(screen)
                backbutton.show_image(screen)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[0] > backbutton.X and event.pos[0] < backbutton.X + backbutton.WIDTH and event.pos[1] > backbutton.Y and event.pos[1] < backbutton.Y + backbutton.HEIGHT:
                        pageturn.play()
                        helppage = 1
            Esc.show_image(screen)
            if keys[pygame.K_ESCAPE]:
                mixer.music.set_volume(0.6)
                scene = 1
                helppage = 1
    keys = pygame.key.get_pressed()
    # Місто
    if scene == 2:
        bgstart.show_image(screen)
        for i in list_levelstart:
            i.show_image(screen)
        taverna.show_image(screen)
        caveenterbottom.show_image(screen)
        mainchar.move_character(list_levelstart,walk_sound)
        mainchar.taverna(X,taverna,screen)

        if mainchar.can_entern_taverna:
            scene = 3
        mainchar.show_image(screen)
        caveentertop.show_image(screen)
        if mainchar.X_sprite >= 1050:
            mainchar.X_sprite = 25
            mainchar.Y_sprite = 27*2
            scene = 4
    # Печера
        # 1 рівень
    elif scene == 4:
        if ost:
            caveost.play(-1)
            ost = False
        cavebg.show_image(screen)
        for i in list_level_1:
            i.show_image(screen)
        for i in list_ores1:
            if i.X > -100:
                i.show_image(screen)
        
        mainchar.move_character(list_level_1,walk_sound)
        mainchar.ores_collision(list_ores1,orespickup)
        mainchar.show_hp(screen)
        mainchar.damage(list_all_enemie_1)
        rope.show_image(screen)
        mainchar.show_image(screen)
        """--------------------------------------Stay_Enemys---------------------------------------------"""
        for stay_enemy in chonkys_1:
            stay_enemy.damage(mainchar)
            stay_enemy.show_image(screen)

        """----------------------------------------MOVE_Enemys-------------------------------------------"""
        for enemy in enemys_1:
            enemy.move()
            enemy.damage(mainchar)
            enemy.show_image(screen)

        """--------------------------------------Shoot_Enemys--------------------------------------------"""
        for shoot_enemy in shoot_enemys_1:
            shoot_enemy.animete_shoot(screen, mainchar, list_level_1)
            shoot_enemy.show_image(screen)
            
        
        """----------------------------------------Mainchar----------------------------------------------"""
        if mainchar.X_sprite >= 1050:
            mainchar.Y_sprite = 432
            mainchar.X_sprite = 20
            scene= 5
        if mainchar.X_sprite <= 20 and mainchar.Y_sprite <= 200:
            mainchar.X_sprite = 900
            mainchar.Y_sprite = 720 - 27*3
            scene = 2
        if mainchar.hp == 0:
            scene = 11
            ost = True
            caveost.stop()
        if keys[pygame.K_x] and mainchar.hp > 0:
            mainchar.X_sprite = 900
            mainchar.Y_sprite = 720 - 27*3
            scene = 2
            ost = True
            caveost.stop()
        # 2 рівень   
    elif scene == 5:
        cavebg.show_image(screen)
        for i in list_level_2:
            i.show_image(screen)
        for i in list_ores2:
            if i.X > -100:
                i.show_image(screen)
        """--------------------------------------Stay_Enemys---------------------------------------------"""
        for stay_enemy in chonkys_2:
            stay_enemy.damage(mainchar)
            stay_enemy.show_image(screen)

        """----------------------------------------MOVE_Enemys-------------------------------------------"""
        for enemy in enemys_2:
            enemy.move()
            enemy.damage(mainchar)
            enemy.show_image(screen)

        """--------------------------------------Shoot_Enemys--------------------------------------------"""
        for shoot_enemy in shoot_enemys_2:
            shoot_enemy.animete_shoot(screen, mainchar, list_level_2)
            shoot_enemy.show_image(screen)
            
        
        """----------------------------------------Mainchar----------------------------------------------"""
        mainchar.move_character(list_level_2,walk_sound)
        mainchar.ores_collision(list_ores2,orespickup)
        mainchar.show_hp(screen)
        mainchar.damage(list_all_enemie_2)
        rope.show_image(screen)
        mainchar.show_image(screen)
        if mainchar.X_sprite <= 15:
            mainchar.X_sprite = 1041
            mainchar.Y_sprite = 420
            scene = 4

        if mainchar.Y_sprite >= 720:
            scene = 6
            mainchar.X_sprite = 951
            mainchar.Y_sprite = 20
        if mainchar.X_sprite >= 1079:
            mainchar.X_sprite = 48
            mainchar.Y_sprite = 39
            scene = 8
        if mainchar.hp == 0:
            scene = 11
            ost = True
            caveost.stop()
        if keys[pygame.K_x] and mainchar.hp > 0:
            mainchar.X_sprite = 900
            mainchar.Y_sprite = 720 - 27*3
            scene = 2
            ost = True
            caveost.stop()
        # 3 рівень
    elif scene == 6:
        cavebg.show_image(screen)
        for i in list_level_3:
            i.show_image(screen)
        for i in list_ores3:
            if i.X > -100:
                i.show_image(screen)

        """--------------------------------------Stay_Enemys---------------------------------------------"""
        for stay_enemy in chonkys_3:
            stay_enemy.damage(mainchar)
            stay_enemy.show_image(screen)

        """----------------------------------------MOVE_Enemys-------------------------------------------"""
        for enemy in enemys_3:
            enemy.move()
            enemy.damage(mainchar)
            enemy.show_image(screen)

        """--------------------------------------Shoot_Enemys--------------------------------------------"""
        for shoot_enemy in shoot_enemys_3:
            shoot_enemy.animete_shoot(screen, mainchar, list_level_3)
            shoot_enemy.show_image(screen)
            

        """----------------------------------------Mainchar----------------------------------------------"""
        mainchar.move_character(list_level_3,walk_sound)
        mainchar.ores_collision(list_ores3,orespickup)
        mainchar.show_hp(screen)
        mainchar.damage(list_all_enemie_3)
        rope.show_image(screen)
        mainchar.show_image(screen)
        if mainchar.Y_sprite <= 14:
            mainchar.X_sprite = 930
            mainchar.Y_sprite = 663
            scene = 5
        if mainchar.X_sprite >= 1074:
            mainchar.X_sprite = 42
            mainchar.Y_sprite = 660
            scene = 7
        if mainchar.X_sprite <= 20:
            mainchar.X_sprite = 1047
            mainchar.Y_sprite = 150
            scene = 9
        if mainchar.hp == 0:
            scene = 11
            ost = True
            caveost.stop()
        if keys[pygame.K_x] and mainchar.hp > 0:
            mainchar.X_sprite = 900
            mainchar.Y_sprite = 720 - 27*3
            scene = 2
            ost = True
            caveost.stop()
        # 4 рівень
    elif scene == 7:
        cavebg.show_image(screen)
        for i in list_level_4:
            i.show_image(screen)
        for i in list_ores4:
            if i.X > -100:
                i.show_image(screen)

        
        """--------------------------------------Stay_Enemys---------------------------------------------"""
        for stay_enemy in chonkys_4:
            stay_enemy.damage(mainchar)
            stay_enemy.show_image(screen)

        """----------------------------------------MOVE_Enemys-------------------------------------------"""
        for enemy in enemys_4:
            enemy.move()
            enemy.damage(mainchar)
            enemy.show_image(screen)

        """--------------------------------------Shoot_Enemys--------------------------------------------"""
        for shoot_enemy in shoot_enemys_4:
            shoot_enemy.animete_shoot(screen, mainchar, list_level_4)
            shoot_enemy.show_image(screen)
            
        """----------------------------------------Mainchar----------------------------------------------"""
        mainchar.move_character(list_level_4,walk_sound)
        mainchar.ores_collision(list_ores4,orespickup)
        mainchar.show_hp(screen)
        mainchar.damage(list_all_enemie_4)
        rope.show_image(screen)
        mainchar.show_image(screen)
        if mainchar.X_sprite <= 12:
            mainchar.X_sprite = 1044
            mainchar.Y_sprite = 663
            scene = 6
        if mainchar.Y_sprite <= 14:
            mainchar.X_sprite = 405
            mainchar.Y_sprite = 666
            scene = 8
        if mainchar.hp == 0:
            scene = 11
            ost = True
            caveost.stop()
        if keys[pygame.K_x] and mainchar.hp > 0:
            mainchar.X_sprite = 900
            mainchar.Y_sprite = 720 - 27*3
            scene = 2
            ost = True
            caveost.stop()
        # 5 рівень
    elif scene == 8:
        cavebg.show_image(screen)
        for i in list_level_5:
            i.show_image(screen)
        for i in list_ores5:
            if i.X > -100:
                i.show_image(screen)
        """--------------------------------------Stay_Enemys---------------------------------------------"""
        for stay_enemy in chonkys_5:
            stay_enemy.damage(mainchar)
            stay_enemy.show_image(screen)

        """----------------------------------------MOVE_Enemys-------------------------------------------"""
        for enemy in enemys_5:
            enemy.move()
            enemy.damage(mainchar)
            enemy.show_image(screen)

        """--------------------------------------Shoot_Enemys--------------------------------------------"""
        for shoot_enemy in shoot_enemys_5:
            shoot_enemy.animete_shoot(screen, mainchar, list_level_5)
            shoot_enemy.show_image(screen)

        """----------------------------------------Mainchar----------------------------------------------"""
        mainchar.move_character(list_level_5,walk_sound)
        mainchar.ores_collision(list_ores5,orespickup)
        mainchar.show_hp(screen)
        mainchar.damage(list_all_enemie_5)
        rope.show_image(screen)
        mainchar.show_image(screen)
        if mainchar.X_sprite <=15:
            mainchar.X_sprite = 1059
            mainchar.Y_sprite = 30
            scene = 5
        if mainchar.Y_sprite >= 720:
            mainchar.X_sprite = 302
            mainchar.Y_sprite = 21
            scene = 7
        if mainchar.hp == 0:
            scene = 11
            ost = True
            caveost.stop()
        if keys[pygame.K_x] and mainchar.hp > 0:
            mainchar.X_sprite = 900
            mainchar.Y_sprite = 720 - 27*3
            scene = 2
            ost = True
            caveost.stop()
        # 6 рівень 
    elif scene == 9:
        grassbg.show_image(screen)
        for i in list_level_6:
            i.show_image(screen)
        for i in list_ores6:
            if i.X > -100:
                i.show_image(screen)
        """--------------------------------------Stay_Enemys---------------------------------------------"""
        for stay_enemy in chonkys_6:
            stay_enemy.damage(mainchar)
            stay_enemy.show_image(screen)

        """----------------------------------------MOVE_Enemys-------------------------------------------"""
        for enemy in enemys_6:
            enemy.move()
            enemy.damage(mainchar)
            enemy.show_image(screen)

        """--------------------------------------Shoot_Enemys--------------------------------------------"""
        for shoot_enemy in shoot_enemys_6:
            shoot_enemy.animete_shoot(screen, mainchar, list_level_6)
            shoot_enemy.show_image(screen)

        """----------------------------------------Mainchar----------------------------------------------"""
        mainchar.move_character(list_level_6,walk_sound)
        mainchar.ores_collision(list_ores6,orespickup)
        mainchar.show_hp(screen)
        mainchar.damage(list_all_enemie_6)
        rope.show_image(screen)
        mainchar.show_image(screen)
        if mainchar.X_sprite >= 1074:
            mainchar.X_sprite = 42
            mainchar.Y_sprite = 144
            scene = 6
        if mainchar.Y_sprite >= 720:
            mainchar.X_sprite = 828
            mainchar.Y_sprite = 61
            scene = 10
        if mainchar.hp == 0:
            scene = 11
            ost = True
            caveost.stop()
        if keys[pygame.K_x] and mainchar.hp > 0:
            mainchar.X_sprite = 900
            mainchar.Y_sprite = 720 - 27*3
            scene = 2
            ost = True
            caveost.stop()
        # 7 рівень
    elif scene == 10:
        grassbg.show_image(screen)
        for i in list_level_7:
            i.show_image(screen)
        for i in list_ores7:
            if i.X > -100:
                i.show_image(screen)
        
        """--------------------------------------Stay_Enemys---------------------------------------------"""
        for stay_enemy in chonkys_7:
            stay_enemy.damage(mainchar)
            stay_enemy.show_image(screen)

        """----------------------------------------MOVE_Enemys-------------------------------------------"""
        for enemy in enemys_7:
            enemy.move()
            enemy.damage(mainchar)
            enemy.show_image(screen)

        """--------------------------------------Shoot_Enemys--------------------------------------------"""
        for shoot_enemy in shoot_enemys_7:
            shoot_enemy.animete_shoot(screen, mainchar, list_level_7)
            shoot_enemy.show_image(screen)

        """----------------------------------------Mainchar----------------------------------------------"""
        mainchar.move_character(list_level_7,walk_sound)
        mainchar.ores_collision(list_ores7,orespickup)
        mainchar.show_hp(screen)
        mainchar.damage(list_all_enemie_7)
        rope.show_image(screen)
        mainchar.show_image(screen)
        if mainchar.Y_sprite <= 6:
            mainchar.X_sprite = 792
            mainchar.Y_sprite = 663
            scene = 9
            
        if mainchar.X_sprite>= 1075:
            mainchar.X_sprite = 50
            scene = 12
        if mainchar.hp == 0:
            scene = 11
            ost = True
            caveost.stop()
        if keys[pygame.K_x] and mainchar.hp > 0:
            mainchar.X_sprite = 900
            mainchar.Y_sprite = 720 - 27*3
            scene = 2
            ost = True
            caveost.stop()
        # кінцівка з сердцем не тепер це 8 рівень >:)
    elif scene == 12:
        kywshbg.show_image(screen)
        for i in list_level_8:
            i.show_image(screen)

        """--------------------------------------Stay_Enemys---------------------------------------------"""
        for stay_enemy in chonkys_8:
            stay_enemy.damage(mainchar)
            stay_enemy.show_image(screen)

        """----------------------------------------MOVE_Enemys-------------------------------------------"""
        for enemy in enemys_8:
            enemy.move()
            enemy.damage(mainchar)
            enemy.show_image(screen)

        """--------------------------------------Shoot_Enemys--------------------------------------------"""
        for shoot_enemy in shoot_enemys_8:
            shoot_enemy.animete_shoot(screen, mainchar, list_level_8)
            shoot_enemy.show_image(screen)

        """----------------------------------------Mainchar----------------------------------------------"""
        mainchar.move_character(list_level_8,walk_sound)
        mainchar.show_hp(screen)
        rope.show_image(screen)
        mainchar.damage(list_all_enemie_8)
        mainchar.show_image(screen)
        if mainchar.X_sprite <= 20:
            mainchar.X_sprite = 1050
            scene = 10
        if mainchar.X_sprite >= 1060:
            mainchar.X_sprite = 30
            scene = 13
        if keys[pygame.K_x] and mainchar.hp > 0:
            mainchar.X_sprite = 900
            mainchar.Y_sprite = 720 - 27*3
            scene = 2
            ost = True
            caveost.stop()
        if mainchar.hp == 0:
            scene = 11
            ost = True
            caveost.stop()
        # рівень 9 
    elif scene == 13:
        kywshbg.show_image(screen)
        for i in list_level_9:
            i.show_image(screen)

        """--------------------------------------Stay_Enemys---------------------------------------------"""
        for stay_enemy in chonkys_9:
            stay_enemy.damage(mainchar)
            stay_enemy.show_image(screen)

        """----------------------------------------MOVE_Enemys-------------------------------------------"""
        for enemy in enemys_9:
            enemy.move()
            enemy.damage(mainchar)
            enemy.show_image(screen)

        """--------------------------------------Shoot_Enemys--------------------------------------------"""
        for shoot_enemy in shoot_enemys_9:
            shoot_enemy.animete_shoot(screen, mainchar, list_level_9)
            shoot_enemy.show_image(screen)

        """----------------------------------------Mainchar----------------------------------------------"""
        mainchar.move_character(list_level_9,walk_sound)
        mainchar.show_hp(screen)
        mainchar.damage(list_all_enemie_9)
        rope.show_image(screen)
        mainchar.show_image(screen)
        if mainchar.X_sprite <= 20:
            mainchar.X_sprite = 1050
            scene = 12
        if mainchar.X_sprite >= 1060:
            mainchar.X_sprite = 30
            scene = 14
        if keys[pygame.K_x] and mainchar.hp > 0:
            mainchar.X_sprite = 900
            mainchar.Y_sprite = 720 - 27*3
            scene = 2
            ost = True
            caveost.stop()
        if mainchar.hp == 0:
            scene = 11
            ost = True
            caveost.stop()
        # рівень 10
    elif scene == 14:
        kywshbg.show_image(screen)
        for i in list_level_10:
            i.show_image(screen)
        
        """--------------------------------------Stay_Enemys---------------------------------------------"""
        for stay_enemy in chonkys_10:
            stay_enemy.damage(mainchar)
            stay_enemy.show_image(screen)

        """----------------------------------------MOVE_Enemys-------------------------------------------"""
        for enemy in enemys_10:
            enemy.move()
            enemy.damage(mainchar)
            enemy.show_image(screen)

        """--------------------------------------Shoot_Enemys--------------------------------------------"""
        for shoot_enemy in shoot_enemys_10:
            shoot_enemy.animete_shoot(screen, mainchar, list_level_1)
            shoot_enemy.show_image(screen)

        """----------------------------------------Mainchar----------------------------------------------"""
        mainchar.move_character(list_level_10,walk_sound)
        mainchar.show_hp(screen)
        mainchar.damage(list_all_enemie_10)
        rope.show_image(screen)
        mainchar.show_image(screen)
        if mainchar.X_sprite <= 20:
            mainchar.X_sprite = 1050
            scene = 13
        if mainchar.X_sprite >= 1060:
            mainchar.X_sprite = 30
            scene = 15
        if keys[pygame.K_x] and mainchar.hp > 0:
            mainchar.X_sprite = 900
            mainchar.Y_sprite = 720 - 27*3
            scene = 2
            ost = True
            caveost.stop()
        if mainchar.hp == 0:
            scene = 11
            ost = True
            caveost.stop()
    elif scene == 15:
        kywshbg.show_image(screen)
        for i in list_level_11:
            i.show_image(screen)
        
        """--------------------------------------Stay_Enemys---------------------------------------------"""
        for stay_enemy in chonkys_11:
            stay_enemy.damage(mainchar)
            stay_enemy.show_image(screen)

        """----------------------------------------MOVE_Enemys-------------------------------------------"""
        for enemy in enemys_11:
            enemy.move()
            enemy.damage(mainchar)
            enemy.show_image(screen)

        """--------------------------------------Shoot_Enemys--------------------------------------------"""
        for shoot_enemy in shoot_enemys_11:
            shoot_enemy.animete_shoot(screen, mainchar, list_level_11)
            shoot_enemy.show_image(screen)

        """----------------------------------------Mainchar----------------------------------------------"""
        mainchar.move_character(list_level_11,walk_sound)
        mainchar.show_hp(screen)
        mainchar.damage(list_all_enemie_11)
        rope.show_image(screen)
        mainchar.show_image(screen)
        if mainchar.X_sprite <= 20:
            mainchar.X_sprite = 1050
            scene = 14
        if mainchar.Y_sprite >= 720:
            mainchar.Y_sprite = 2
            scene = 16
        if keys[pygame.K_x] and mainchar.hp > 0:
            mainchar.X_sprite = 900
            mainchar.Y_sprite = 720 - 27*3
            scene = 2
            ost = True
            caveost.stop()
        if mainchar.hp == 0:
            scene = 11
            ost = True
            caveost.stop()
        # рівень 12
    elif scene == 16:
        kywshbg.show_image(screen)
        for i in list_level_12:
            i.show_image(screen)
        """--------------------------------------Stay_Enemys---------------------------------------------"""
        for stay_enemy in chonkys_12:
            stay_enemy.damage(mainchar)
            stay_enemy.show_image(screen)

        """----------------------------------------MOVE_Enemys-------------------------------------------"""
        for enemy in enemys_12:
            enemy.move()
            enemy.damage(mainchar)
            enemy.show_image(screen)

        """--------------------------------------Shoot_Enemys--------------------------------------------"""
        for shoot_enemy in shoot_enemys_12:
            shoot_enemy.animete_shoot(screen, mainchar, list_level_12)
            shoot_enemy.show_image(screen)

        """----------------------------------------Mainchar----------------------------------------------"""
        mainchar.move_character(list_level_12,walk_sound)
        mainchar.show_hp(screen)
        mainchar.damage(list_all_enemie_12)
        rope.show_image(screen)
        mainchar.show_image(screen)
        if mainchar.Y_sprite >= 720:
            mainchar.Y_sprite = 2
            scene = 17
        if keys[pygame.K_x] and mainchar.hp > 0:
            mainchar.X_sprite = 900
            mainchar.Y_sprite = 720 - 27*3
            scene = 2
            ost = True
            caveost.stop()
        if mainchar.hp == 0:
            scene = 11
            ost = True
            caveost.stop()
        # Фінал
    elif scene == 17:
        kywshbg.show_image(screen)
        for i in list_level_final:
            i.show_image(screen)
        heart.show_image(screen)
        mainchar.move_character(list_level_final,walk_sound)
        mainchar.show_image(screen)
        if mainchar.X_sprite + mainchar.Width_sprite >= heart.X and mainchar.X_sprite <= heart.X + heart.WIDTH:
            C.show_image(screen)
            if keys[pygame.K_c]:
                scene = 20
    # меню смерті
    elif scene == 11:
        buttonplay.X = 860
        buttonexit.X = 860
        buttonplay.Y = 230
        buttonexit.Y = 430
        deathbg.show_image(screen)
        for event in pygame.event.get():
            if  event.type == pygame.MOUSEMOTION:
                if event.pos[0] > buttonplay.X and event.pos[0] < buttonplay.X + buttonplay.WIDTH and event.pos[1] > buttonplay.Y and event.pos[1] < buttonplay.Y + buttonplay.HEIGHT:
                    buttonplay.PATH = "/image/buttonplay2.png"
                    buttonplay.load_image()
                else:
                    buttonplay.PATH = "/image/buttonplay1.png"
                    buttonplay.load_image()
                if event.pos[0] > buttonexit.X and event.pos[0] < buttonexit.X + buttonexit.WIDTH and event.pos[1] > buttonexit.Y and event.pos[1] < buttonexit.Y + buttonexit.HEIGHT:
                    buttonexit.PATH = "/image/buttonexit2.png"
                    buttonexit.load_image()
                else:
                    buttonexit.PATH = "/image/buttonexit1.png"
                    buttonexit.load_image()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.pos[0] > buttonplay.X and event.pos[0] < buttonplay.X + buttonplay.WIDTH and event.pos[1] > buttonplay.Y and event.pos[1] < buttonplay.Y + buttonplay.HEIGHT:
                    scene = 2
                    mainchar.hp = mainchar.hp_max
                    mainchar.X_sprite = 20
                    mainchar.Y_sprite = 720 - 27 * 3
                    mainchar.coin = 0
                    mainchar.diamond = 0
                    mainchar.emeralds = 0
                    mainchar.gold = 0
                    mainchar.silver = 0 
                    mainchar.iron = 0
                    buttonsound.play(1)
                if event.pos[0] > buttonexit.X and event.pos[0] < buttonexit.X + buttonexit.WIDTH and event.pos[1] > buttonexit.Y and event.pos[1] < buttonexit.Y + buttonexit.HEIGHT:
                    buttonsound.play(1)
                    game = False
        buttonplay.show_image(screen)
        buttonexit.show_image(screen)
    if music:
        mixer.music.play(-1)    
        music = False
    
    clock.tick(60)
    pygame.display.flip()