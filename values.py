# Імпортуємо всі необхідні файли для роботи
from Image2 import Image
from character import Character
from text import Text
from ores import Ores
import pygame
import os
from enemies import Enemie, Static_Enemie, Chonky_enemie
from pygame import mixer

# лого гри
logo = Image(100, 250, 95*5, 23*5,'/image/logo.png')# Створення лого гри


#----------------------------Створення всіх об'єктів та гравця в грі-------------------------#
# Фони гри
background = Image(0,0,1080,720,"/image/phonee.png")# Створення заднього фону для стартового екрану
mainchar = Character(400, 550, 20, 27, 4, 5, 27*2+14, "/image/char1.png", 1, 2)# Створення головного героя
tavernabg = Image(0,0,1080,720,'/image/bg/tavernabg.png')# Створення заднього фону таверни
bgstart = Image(0,0,1080,720,'/image/bg/bgstart.png')# Створення Створення заднього фону для поверхні 
cavebg = Image(0,0,1080,720,'/image/bg/cavebg.png')# Створення заднього фону рівнів в кам'яному підземеллі
grassbg = Image(0,0,1080,720,'/image/bg/grassbg.png')# Створення заднього фону рівнів в підземеллі
deathbg = Image(0,0,1080,720,'/image/bg/dethbg.png')# Створення заднього фону після смерті

history1 = Image(0,0,1080,720,'/image/story/history1.png')# Створення фону історії
history2 = Image(0,0,1080,720,'/image/story/history2.png')# Створення фону історії
history3 = Image(0,0,1080,720,'/image/story/history3.png')# Створення фону історії
history4 = Image(0,0,1080,720,'/image/story/history4.png')# Створення фону історії
history5 = Image(0,0,1080,720,'/image/story/history5.png')# Створення фону історії
kywshbg = Image(0,0,1080,720,"/image/bg/kywshbg.png")# Створення заднього фону на рівні
help1 = Image(0,0,1080,720,"/image/help/help1.png")# Створення фону першої сторінки допомоги
help2 = Image(0,0,1080,720,"/image/help/help2.png")# Створення фону першої другої допомоги
#--------------------Кнопки гри--------------------#
# Кнопки меню
buttonplay = Image(690, 53, 180, 86, "/image/buttonplay1.png")# Створення кнопки для початку гри
buttonhelp = Image(690, 282, 180, 86, "/image/buttonhelp1.png")# Створення кнопки для допомоги
buttonexit = Image(690, 509, 180, 86, "/image/buttonexit1.png")# Створення кнопки для виходу з гри
# Кнопки таверни
buttonsell = Image(560, 400, 47*3,18*3,'/image/taverna/sell1.png')# Створення кнопки для для продажу
buttonbuy = Image(560+47*3+20,400,47*3,18*3,'/image/taverna/buy1.png')# Створення кнопки для купівлі
buttonselldiamond = Image(500, 60, 40*3,40*3,'/image/taverna/diamondsell.png')# Створення кнопки для продажу діамантів
buttonsellemeralds = Image(700, 60, 40*3,40*3,'/image/taverna/emeraldssell.png')# Створення кнопки для продаж емеральдів
buttonsellgold = Image(900, 60, 40*3,40*3,'/image/taverna/goldsell.png')# Створення кнопки для продажу золота
buttonselliron = Image(600, 230, 40*3,40*3,'/image/taverna/ironsell.png')# Створення кнопки для продажу заліза
buttonsellsilver = Image(800, 230, 40*3,40*3,'/image/taverna/silversell.png')# Створення кнопки для продажу срібла
heartupgrade = Image(620, 60,39*5,45*5,'/image/hearts/heartupgrade.png')# Створення кнопки для купівлі здоров'я
sellall = Image(buttonsellemeralds.X,0,40*3,20*3,'/image/taverna/sellall.png')# Створення кнопки для продажу всього
recover = Image(buttonsell.X-64*3-20,buttonsell.Y+3, 64*3,16*3,'/image/taverna/recoverybutton.png')# Створення кнопки для відновлення ХП
# Кнопки історії
buttonnext = Image(870,630,200,80,'/image/story/nextbutton.png')# Створення кнопки для переходу на наступну сторінку історії
buttonleave = Image(64,593,60*3,20*3,'/image/story/leavebutton.png')# Створення кнопки для переходу на минулу сторінку історії
buttontry = Image(64 +(60*3) +20,593,60*3,20*3,'/image/story/trybutton.png')# Створення кнопки для спроби
# Кнопки допомоги
backbutton = Image(10,670,100,40,"/image/help/backbutton.png")# Створення кнопки для переходу на минулу сторінку допомоги
buttonnext1 = Image(970,670,100,40,'/image/story/nextbutton.png')# Створення кнопки для переходу на наступну сторінку допомоги
# Текстури для рівнів
heart = Image(359,27,588,675,'/image/heart.png')# Створення заднього фону останнього рівня
taverna = Image(400,523,204,152,'/image/taverna1.png')# Створення таверни наповерхні
caveentertop = Image(1018,549,62,127,'/image/caveentertop.png')# Створення частини печери
caveenterbottom = Image(1018,608,25,68,'/image/caveenterbottom.png')# Створення частини печери

# Текстури кнопок

C = Image((heart.X + heart.WIDTH)-heart.WIDTH//2-15,heart.Y+100,40,40,'/image/C.png')# Створення кнопки C на екрані
X = Image(taverna.X + taverna.WIDTH/2-25, taverna.Y - 42,40,40,'/image/X.png')# Створення кнопки X на екрані
Esc = Image(10,10,40,40,'/image/Esc.png')# Створення кнопки Esc на екрані

# Всі монети

coin1 = Image(buttonselldiamond.X,buttonselldiamond.Y+buttonselldiamond.HEIGHT,27,27,'/image/taverna/coin.png')# Створення монети на екрані
coin2 = Image(buttonsellemeralds.X,buttonsellemeralds.Y+buttonsellemeralds.HEIGHT,27,27,'/image/taverna/coin.png')# Створення монети на екрані
coin3 = Image(buttonsellgold.X,buttonsellgold.Y+buttonsellgold.HEIGHT,27,27,'/image/taverna/coin.png')# Створення монети на екрані
coin4 = Image(buttonselliron.X,buttonselliron.Y+buttonselliron.HEIGHT,27,27,'/image/taverna/coin.png')# Створення монети на екрані
coin5 = Image(buttonsellsilver.X,buttonsellsilver.Y+buttonsellsilver.HEIGHT,27,27,'/image/taverna/coin.png')# Створення монети на екрані
coin6 = Image(buttonbuy.X + buttonbuy.WIDTH + 10, buttonbuy.Y + 12,27, 27,'/image/taverna/coin.png')# Створення монети на екрані
coin7 = Image(heartupgrade.X +20,heartupgrade.Y+heartupgrade.HEIGHT+20,27*2,27*2,'/image/taverna/coin.png')# Створення монети на екрані
list_coin = [coin1,coin2,coin3,coin4,coin5]# Створення списку монет
heartupgradeprice = Text(coin7.X + coin7.WIDTH + 5,coin7.Y -3,27*2,'arial','15',(0,0,0))# Створення ціни для апгрейду здоров'я
coin8 = Image(recover.X+recover.WIDTH//2-30,recover.Y-30,27,27,'/image/taverna/coin.png')# Створення монети на екрані

# Текстури для рівнів

rope = Image(50, 2,50,50,'/image/rope.png')# Створення кнопки на рівні

# Всі руди
oresiron1 = Ores(348,139,35,23,"/image/ores/iron.png",'iron')# Створення заліза на рівні
oresiron2 = Ores(899,193,35,23,"/image/ores/iron.png",'iron')# Створення заліза на рівні
oresiron3 = Ores(613,382,35,23,"/image/ores/iron.png",'iron')# Створення заліза на рівні
oresiron4 = Ores(106,490,35,23,"/image/ores/iron.png",'iron')# Створення заліза на рівні
oressilver1 = Ores(891,687,38,16,"/image/ores/silver.png",'silver')# Створення срібла на рівні
oressilver2 = Ores(180,227,38,16,"/image/ores/silver.png",'silver')# Створення срібла на рівні
oresgold1 = Ores(341,402,37,30,"/image/ores/gold.png",'gold')# Створення золота на рівні
oresgold2 = Ores(597,565,37,30,"/image/ores/gold.png",'gold')# Створення золота на рівні
list_ores1 = [oresiron1,oresiron2,oresiron3,oresiron4,oressilver1,oressilver2,oresgold1,oresgold2]# Створення списку руд на 1 рівні

oresiron5 = Ores(570,680,35,23,"/image/ores/iron.png",'iron')# Створення заліза на рівні
oresiron6 = Ores(468,436,35,23,"/image/ores/iron.png",'iron')# Створення заліза на рівні
oresiron7 = Ores(825,112,35,23,"/image/ores/iron.png",'iron')# Створення заліза на рівні
oressilver3 = Ores(293,92,38,16,"/image/ores/silver.png",'silver')# Створення срібла на рівні
oressilver4 = Ores(840,254,38,16,"/image/ores/silver.png",'silver')# Створення срібла на рівні
oressilver5 = Ores(193,524,38,16,"/image/ores/silver.png",'silver')# Створення срібла на рівні
oresgold3 = Ores(460,240,37,30,"/image/ores/gold.png",'gold')# Створення золота на рівні
oresgold4 = Ores(880,510,37,30,"/image/ores/gold.png",'gold')# Створення золота на рівні
oresgold5 = Ores(798,673,37,30,"/image/ores/gold.png",'gold')# Створення золота на рівні
oresdiamond1 = Ores(53,225,32,18,"/image/ores/diamond.png",'diamond')# Створення діамантівна рівні
oresdiamond2 = Ores(102,685,32,18,"/image/ores/diamond.png",'diamond')# Створення діамантів на рівні
list_ores2 = [oresiron5,oresiron6,oresiron7,oressilver3,oressilver4,oressilver5,oresgold3,oresgold4,oresgold5,oresdiamond1,oresdiamond2]# Створення списку руд на 2 рівні

oresiron8 = Ores(549,140,35,23,"/image/ores/iron.png",'iron')# Створення заліза на рівні
oresiron9 = Ores(275,599,35,23,"/image/ores/iron.png",'iron')# Створення заліза на рівні
oressilver6 = Ores(889,254,38,16,"/image/ores/silver.png",'silver')# Створення срібла на рівні
oressilver7 = Ores(289,281,38,16,"/image/ores/silver.png",'silver')# Створення срібла на рівні
oressilver8 = Ores(542,497,38,16,"/image/ores/silver.png",'silver')# Створення срібла на рівні
oresgold6 = Ores(502,294,37,30,"/image/ores/gold.png",'gold')# Створення золота на рівні
oresdiamond3 = Ores(1016,441,32,18,"/image/ores/diamond.png",'diamond')# Створення діамантів на рівні
list_ores3 = [oresiron8,oresiron9,oressilver6,oressilver7,oressilver8,oresgold6,oresdiamond3]# Створення списку руд на 3 рівні

oresiron10 = Ores(635,436,35,23,"/image/ores/iron.png",'iron')# Створення заліза на рівні
oressilver9 = Ores(587,687,38,16,"/image/ores/silver.png",'silver')# Створення срібла на рівні
oressilver10 = Ores(198,227,38,16,"/image/ores/silver.png",'silver')# Створення срібла на рівні
oresgold7 = Ores(706,240,37,30,"/image/ores/gold.png",'gold')# Створення золота на рівні
oresgold8 = Ores(1003,78,37,30,"/image/ores/gold.png",'gold')# Створення золота на рівні
oresdiamond4 = Ores(102,415,32,18,"/image/ores/diamond.png",'diamond')# Створення діамантів на рівні
oresemeralds1 = Ores(53,92,25,16,"/image/ores/emeralds.png",'emerald')# Створення емеральдів на рівні
list_ores4 = [oresiron10,oressilver9,oressilver10,oresgold7,oresgold8,oresdiamond4,oresemeralds1]# Створення списку руд на 4 рівні

oresiron11 = Ores(316,436,35,23,"/image/ores/iron.png",'iron')# Створення заліза на рівні
oresiron12 = Ores(1013,328,35,23,"/image/ores/iron.png",'iron')# Створення заліза на рівні
oressilver11 = Ores(617,497,38,16,"/image/ores/silver.png",'silver')# Створення срібла на рівні
oressilver12 = Ores(654,119,38,16,"/image/ores/silver.png",'silver')# Створення срібла на рівні
oressilver13 = Ores(231,280,38,16,"/image/ores/silver.png",'silver')# Створення срібла на рівні
oresgold9 = Ores(1002,429,37,30,"/image/ores/gold.png",'gold')# Створення золота на рівні
oresgold10 = Ores(441,105,37,30,"/image/ores/gold.png",'gold')# Створення золота на рівні
oresdiamond5 = Ores(784,252,32,18,"/image/ores/diamond.png",'diamond')# Створення діамантів на рівні
list_ores5 = [oresiron11,oresiron12,oressilver11,oressilver12,oressilver13,oresgold9,oresgold10,oresdiamond5]# Створення списку руд на 5 рівні

oresiron13 = Ores(741,166,35,23,"/image/ores/iron.png",'iron')# Створення заліза на рівні
oresiron14 = Ores(558,409,35,23,"/image/ores/iron.png",'iron')# Створення заліза на рівні
oressilver14 = Ores(389,227,38,16,"/image/ores/silver.png",'silver')# Створення срібла на рівні
oresgold11 = Ores(98,321,37,30,"/image/ores/gold.png",'gold')# Створення золота на рівні
oresgold12 = Ores(780,375,37,30,"/image/ores/gold.png",'gold')# Створення золота на рівні
oresdiamond6 = Ores(54,252,32,18,"/image/ores/diamond.png",'diamond')# Створення діамантів на рівні
oresemeralds2 = Ores(612,579,25,16,"/image/ores/emeralds.png",'emerald')# Створення емеральдів на рівні
oresemeralds3 = Ores(990,551,25,16,"/image/ores/emeralds.png",'emerald')# Створення емеральдів на рівні
list_ores6 = [oresiron13,oresiron14,oressilver14,oresgold11,oresgold12,oresdiamond6,oresemeralds2,oresemeralds3]# Створення списку руд на 6 рівні

oresiron15 = Ores(397,383,35,23,"/image/ores/iron.png",'iron')# Створення заліза на рівні
oresiron16 = Ores(739,220,35,23,"/image/ores/iron.png",'iron')# Створення заліза на рівні
oresgold13 = Ores(568,538,37,30,"/image/ores/gold.png",'gold')# Створення золота на рівні
oresgold14 = Ores(224,78,37,30,"/image/ores/gold.png",'gold')# Створення золота на рівні
oresdiamond7 = Ores(191,577,32,18,"/image/ores/diamond.png",'diamond')# Створення діамантів на рівні
oresdiamond8 = Ores(869,468,32,18,"/image/ores/diamond.png",'diamond')# Створення діамантів на рівні
oresdiamond9 = Ores(989,685,32,18,"/image/ores/diamond.png",'diamond')# Створення діамантів на рівні
oresemeralds4 = Ores(52,416,25,16,"/image/ores/emeralds.png",'emerald')# Створення емеральдів на рівні
oresemeralds5 = Ores(98,687,25,16,"/image/ores/emeralds.png",'emerald')# Створення емеральдів на рівні
oresemeralds6 = Ores(937,687,25,16,"/image/ores/emeralds.png",'emerald')# Створення емеральдів на рівні
list_ores7 = [oresiron15,oresiron16,oresgold13,oresgold14,oresdiamond7,oresdiamond8,oresdiamond9,oresemeralds4,oresemeralds5,oresemeralds6]# Створення списку руд на 7 рівні

# Всі звуки
buttonsound = pygame.mixer.Sound(os.path.abspath(__file__ + "/..") +'/sounds/buttonpressed.wav')# Створення звука натискання кнопки
walk_sound = pygame.mixer.Sound(os.path.abspath(__file__ + "/..") +'/sounds/step.wav')# Створення звука ходьби
walk_sound.set_volume(0.3)# Значення гучності звуку
orespickup = mixer.Sound(os.path.abspath(__file__ + '/..') + "/sounds/orespickup.wav")# Створення звука підняття руди
pageturn = mixer.Sound(os.path.abspath(__file__ + '/..') + "/sounds/pageturn.wav")# Створення звука перегортання сторінки
tavernaost = mixer.Sound(os.path.abspath(__file__ + '/..') + "/sounds/tavernaost.wav")# Створення фонової музики в таверні
caveost = mixer.Sound(os.path.abspath(__file__ + '/..') + "/sounds/caveost.wav")# Створення фонового звука в печері
# Весь текст
    # Таверна
        # Ціни
diamondprice = Text(coin2.X+coin2.WIDTH+5,coin2.Y,27,'arial','5',(0,0,0))# Створення тексту ціни діамантів
emeraldsprice = Text(coin1.X+coin1.WIDTH+5,coin1.Y,27,'arial','4',(0,0,0))# Створення тексту ціни емеральдів
goldprice = Text(coin3.X+coin3.WIDTH+5,coin3.Y,27,'arial','3',(0,0,0))# Створення тексту ціни золота
silverprice = Text(coin5.X+coin5.WIDTH+5,coin5.Y,27,'arial','2',(0,0,0))# Створення тексту ціни срібла
ironprice = Text(coin4.X+coin4.WIDTH+5,coin4.Y,27,'arial','1',(0,0,0))# Створення тексту ціни заліза
recoverprice = Text(coin8.X+coin8.WIDTH+5,coin8.Y,27,'arial','10',(0,0,0))# Створення тексту ціни відновлення
# Для показу таверни з середини
diamondcount = Text(buttonselldiamond.X+buttonselldiamond.WIDTH//2-10,buttonselldiamond.Y,27,'arial',str(mainchar.diamond),(0,0,0))# Створення тексту рахнка діамантів
emeraldscount = Text(buttonsellemeralds.X+buttonsellemeralds.WIDTH//2-10,buttonsellemeralds.Y,27,'arial',str(mainchar.emeralds),(0,0,0))# Створення тексту рахнка емеральдів
goldcount = Text(buttonsellgold.X+buttonsellgold.WIDTH//2-10,buttonsellgold.Y,27,'arial',str(mainchar.gold),(0,0,0))# Створення тексту рахнка золота
silvercount = Text(buttonsellsilver.X+buttonsellsilver.WIDTH//2-10,buttonsellsilver.Y,27,'arial',str(mainchar.silver),(0,0,0))# Створення тексту рахнка срібла
ironcount = Text(buttonselliron.X+buttonselliron.WIDTH//2-10,buttonselliron.Y,27,'arial',str(mainchar.iron),(0,0,0))# Створення тексту рахнка заліза
monyewehave = Text(coin6.X+coin6.WIDTH + 5,coin6.Y,27,'arial',str(mainchar.coin),(0,0,0))# Створення тексту рахнка монет

# вороги
"""-------------------------------------------Static_Enemys----------------------------------------------"""
# Статичні монстри на 1 рівні
chonky1_1 = Chonky_enemie(391, 137, 40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 1 рівні
chonky1_2 = Chonky_enemie(817, 81, 40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 1 рівні
chonky1_3 = Chonky_enemie(473, 379, 40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 1 рівні
chonky1_4 = Chonky_enemie(171, 486, 40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 1 рівні
# Статичні монстри на 2 рівні
chonky2_1 = Chonky_enemie(653, 191 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 2 рівні
chonky2_2 = Chonky_enemie(168, 433 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 2 рівні
chonky2_3 = Chonky_enemie(817, 433 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 2 рівні
chonky2_4 = Chonky_enemie(341, 649 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 2 рівні
# Статичні монстри на 3 рівні
chonky3_1 = Chonky_enemie(409, 109, 40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 3 рівні
chonky3_2 = Chonky_enemie(103, 163, 40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 3 рівні
chonky3_3 = Chonky_enemie(583, 407, 40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 3 рівні
chonky3_4 = Chonky_enemie(75, 569, 40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 3 рівні
# Статичні монстри на 4 рівні
chonky4_1 = Chonky_enemie(967, 299 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 4 рівні
chonky4_2 = Chonky_enemie(486, 325 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 4 рівні
chonky4_3 = Chonky_enemie(534, 460 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 4 рівні
chonky4_4 = Chonky_enemie(432, 650 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 4 рівні
# Статичні монстри на 5 рівні
chonky5_1 = Chonky_enemie(824, 245 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 5 рівні
chonky5_2 = Chonky_enemie(199, 434 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 5 рівні
chonky5_3 = Chonky_enemie(121, 677 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 5 рівні
chonky5_4 = Chonky_enemie(577, 677 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 5 рівні
# Статичні монстри на 6 рівні
chonky6_1 = Chonky_enemie(530, 136 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 6 рівні
chonky6_2 = Chonky_enemie(674, 433 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 6 рівні
chonky6_3 = Chonky_enemie(196, 460 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 6 рівні
chonky6_4 = Chonky_enemie(916, 569 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 6 рівні
# Статичні монстри на 7 рівні
chonky7_1 = Chonky_enemie(865, 216 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 7 рівні
chonky7_2 = Chonky_enemie(810, 460 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 7 рівні
chonky7_3 = Chonky_enemie(287, 677 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 7 рівні
chonky7_4 = Chonky_enemie(579, 677 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 7 рівні
# Статичні монстри на 8 рівні
chonky8_1 = Chonky_enemie(716, 189 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 8 рівні
chonky8_2 = Chonky_enemie(530, 406 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 8 рівні
chonky8_3 = Chonky_enemie(387, 677 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 8 рівні
chonky8_4 = Chonky_enemie(481, 677 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 8 рівні
# Статичні монстри на 9 рівні
chonky9_1 = Chonky_enemie(963, 244 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 9 рівні
chonky9_2 = Chonky_enemie(164, 406 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 9 рівні
chonky9_3 = Chonky_enemie(1012, 649 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 9 рівні
chonky9_4 = Chonky_enemie(869, 677 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 9 рівні
# Статичні монстри на 10 рівні
chonky10_1 = Chonky_enemie(248, 217 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 10 рівні
chonky10_2 = Chonky_enemie(410, 326 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 10 рівні
chonky10_3 = Chonky_enemie(746, 380 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 10 рівні
chonky10_4 = Chonky_enemie(195, 677 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 10 рівні
# Статичні монстри на 11 рівні
chonky11_1 = Chonky_enemie(504, 298 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 11 рівні
chonky11_2 = Chonky_enemie(247, 460 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 11 рівні
chonky11_3 = Chonky_enemie(722, 596 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 11 рівні
chonky11_4 = Chonky_enemie(51, 677 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 11 рівні
# Статичні монстри на 12 рівні
chonky12_1 = Chonky_enemie(626, 136 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 12 рівні
chonky12_2 = Chonky_enemie(387, 163 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 12 рівні
chonky12_3 = Chonky_enemie(385, 569 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 12 рівні
chonky12_4 = Chonky_enemie(213, 677 ,40, 26, 1, "/image/chonky.png", 0, 5)# Створення статичного монстра на 12 рівні
#Список статичних монстрів на 1 рівні
chonkys_1 = [
    chonky1_1, chonky1_2,
    chonky1_3, chonky1_4 
]
#Список статичних монстрів на 2 рівні
chonkys_2 = [
    chonky2_1, chonky2_2,
    chonky2_3, chonky2_4 
]
#Список статичних монстрів на 3 рівні
chonkys_3 = [
    chonky3_1, chonky3_2,
    chonky3_3, chonky3_4 
]
#Список статичних монстрів на 4 рівні
chonkys_4 = [
    chonky4_1, chonky4_2,
    chonky4_3, chonky4_4 
]
#Список статичних монстрів на 5 рівні
chonkys_5 = [
    chonky5_1, chonky5_2,
    chonky5_3, chonky5_4 
]
#Список статичних монстрів на 6 рівні
chonkys_6 = [
    chonky6_1, chonky6_2,
    chonky6_3, chonky6_4 
]
#Список статичних монстрів на 7 рівні
chonkys_7 = [
    chonky7_1, chonky7_2,
    chonky7_3, chonky7_4 
]
#Список статичних монстрів на 8 рівні
chonkys_8 = [
    chonky8_1, chonky8_2,
    chonky8_3, chonky8_4 
]
#Список статичних монстрів на 9 рівні
chonkys_9 = [
    chonky9_1, chonky9_2,
    chonky9_3, chonky9_4 
]
#Список статичних монстрів на 10 рівні
chonkys_10 = [
    chonky10_1, chonky10_2,
    chonky10_3, chonky10_4 
]
#Список статичних монстрів на 11 рівні
chonkys_11 = [
    chonky11_1, chonky11_2,
    chonky11_3, chonky11_4 
]
#Список статичних монстрів на 12 рівні
chonkys_12 = [
    chonky12_1, chonky12_2,
    chonky12_3, chonky12_4
]

"""------------------------------------------------------------------------------------------------------"""

"""--------------------------------------------MOVE_Enemys-----------------------------------------------"""
# Динамічні монстри на 1 рівні
zombie1_1 = Enemie(773, 215, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 220, 120)# Створення динамічного монстра на 1 рівні
zombie1_2 = Enemie(105, 243, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 200, 120)# Створення динамічного монстра на 1 рівні
zombie1_3 = Enemie(582, 405, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 110, 0)# Створення динамічного монстра на 1 рівні
zombie1_4 = Enemie(777, 702, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 250, 120)# Створення динамічного монстра на 1 рівні
zombie1_5 = Enemie(780, 702, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 250, -120)# Створення динамічного монстра на 1 рівні
zombie1_6 = Enemie(102, 702, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 400, -200)# Створення динамічного монстра на 1 рівні
zombie1_7 = Enemie(102, 702, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 400, 120)# Створення динамічного монстра на 1 рівні
zombie1_8 = Enemie(200, 702, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 200, 120)# Створення динамічного монстра на 1 рівні
zombie1_9 = Enemie(153, 620, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 160, 120)# Створення динамічного монстра на 1 рівні
zombie1_10 = Enemie(580, 702, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 120, 120)# Створення динамічного монстра на 1 рівні
zombie1_11 = Enemie(490, 487, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 160, 120)# Створення динамічного монстра на 1 рівні
zombie1_12 = Enemie(200, 325, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 120, 120)# Створення динамічного монстра на 1 рівні
# Динамічні монстри на 2 рівні
zombie2_1 = Enemie(250, 108, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 160, 0)# Створення динамічного монстра на 2 рівні
zombie2_2 = Enemie(490, 108, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 160, 120)# Створення динамічного монстра на 2 рівні
zombie2_3 = Enemie(732, 134, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 150, 80)# Створення динамічного монстра на 2 рівні
zombie2_4 = Enemie(116, 269, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 180, 60)# Створення динамічного монстра на 2 рівні
zombie2_5 = Enemie(394, 269, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 100, 100)# Створення динамічного монстра на 2 рівні
zombie2_6 = Enemie(782, 269, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 100, 120)# Створення динамічного монстра на 2 рівні
zombie2_7 = Enemie(455, 350, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 230, 60)# Створення динамічного монстра на 2 рівні
zombie2_8 = Enemie(355, 458, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 320, 120)# Створення динамічного монстра на 2 рівні
zombie2_9 = Enemie(500, 539, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 420, 120)# Створення динамічного монстра на 2 рівні
zombie2_10 = Enemie(500, 539, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 420, -210)# Створення динамічного монстра на 2 рівні
zombie2_11 = Enemie(400, 702, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 234, 60)# Створення динамічного монстра на 2 рівні
zombie2_12 = Enemie(783, 702, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 150, 120)# Створення динамічного монстра на 2 рівні
# Динамічні монстри на 3 рівні
zombie3_1 = Enemie(195, 136, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 112, 0)# Створення динамічного монстра на 3 рівні
zombie3_2 = Enemie(200, 298, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 104, 120)# Створення динамічного монстра на 3 рівні
zombie3_3 = Enemie(485, 325, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 110, 80)# Створення динамічного монстра на 3 рівні
zombie3_4 = Enemie(150, 433, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 110, 60)# Створення динамічного монстра на 3 рівні
zombie3_5 = Enemie(725, 460, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 110, 100)# Створення динамічного монстра на 3 рівні
zombie3_6 = Enemie(200, 541, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 150, 120)# Створення динамічного монстра на 3 рівні
zombie3_7 = Enemie(485, 514, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 154, 60)# Створення динамічного монстра на 3 рівні
zombie3_8 = Enemie(632, 595, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 200, 120)# Створення динамічного монстра на 3 рівні
zombie3_9 = Enemie(440, 703, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 200, 120)# Створення динамічного монстра на 3 рівні
zombie3_10 = Enemie(777, 703, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 250, 100)# Створення динамічного монстра на 3 рівні
# Динамічні монстри на 4 рівні
zombie4_1 = Enemie(585, 107, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 154, 0)# Створення динамічного монстра на 4 рівні
zombie4_2 = Enemie(680, 269, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 150, 120)# Створення динамічного монстра на 4 рівні
zombie4_3 = Enemie(150, 323, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 54, 80)# Створення динамічного монстра на 4 рівні
zombie4_4 = Enemie(340, 377 , 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 100, 60)# Створення динамічного монстра на 4 рівні
zombie4_5 = Enemie(585, 458, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 106, 100)# Створення динамічного монстра на 4 рівні
zombie4_6 = Enemie(150, 513, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 60, 120)# Створення динамічного монстра на 4 рівні
zombie4_7 = Enemie(293, 620, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 60, 60)# Створення динамічного монстра на 4 рівні
zombie4_8 = Enemie(55, 701, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 104, 120)# Створення динамічного монстра на 4 рівні
zombie4_9 = Enemie(490, 701, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right', 200, 120)# Створення динамічного монстра на 4 рівні
# Динамічні монстри на 5 рівні
zombie5_1 = Enemie(386, 134, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',120, 120)# Створення динамічного монстра на 5 рівні
zombie5_2 = Enemie(481, 215, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',60, 120)# Створення динамічного монстра на 5 рівні
zombie5_3 = Enemie(721, 269, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',80, 120)# Створення динамічного монстра на 5 рівні
zombie5_4 = Enemie(193, 296, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',110, 120)# Створення динамічного монстра на 5 рівні
zombie5_5 = Enemie(289, 458, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',110, 120)# Створення динамічного монстра на 5 рівні
zombie5_6 = Enemie(530, 512, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',150, 120)# Створення динамічного монстра на 5 рівні
zombie5_7 = Enemie(722, 621, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',110, 120)# Створення динамічного монстра на 5 рівні
zombie5_8 = Enemie(620, 702, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',240, 120)# Створення динамічного монстра на 5 рівні
zombie5_9 = Enemie(386, 702, 21, 30, 1, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',100, 120)# Створення динамічного монстра на 5 рівні
# Динамічні монстри на 6 рівні
zombie6_1 = Enemie(530, 323, 21, 30, 1.5, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',500, 120)# Створення динамічного монстра на 6 рівні
zombie6_2 = Enemie(534, 431, 21, 30, 1.5, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',130, 120)# Створення динамічного монстра на 6 рівні
zombie6_3 = Enemie(240, 351, 21, 30, 1.5, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',160, 120)# Створення динамічного монстра на 6 рівні
zombie6_4 = Enemie(338, 107, 21, 30, 1.5, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',170, 120)# Створення динамічного монстра на 6 рівні
zombie6_5 = Enemie(721, 594, 21, 30, 1.5, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',120, 120)# Створення динамічного монстра на 6 рівні
zombie6_6 = Enemie(290, 702, 21, 30, 1.5, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',350, 120)# Створення динамічного монстра на 6 рівні
zombie6_7 = Enemie(385, 485, 21, 30, 1.5, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',60, 120)# Створення динамічного монстра на 5 рівні
# Динамічні монстри на 7 рівні
zombie7_1 = Enemie(625, 242, 21, 30, 1.5, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',160, 120)# Створення динамічного монстра на 7 рівні
zombie7_2 = Enemie(914, 269, 21, 30, 1.5, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',120, 120)# Створення динамічного монстра на 7 рівні
zombie7_3 = Enemie(339, 405, 21, 30, 1.5, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',160, 120)# Створення динамічного монстра на 7 рівні
zombie7_4 = Enemie(529, 431, 21, 30, 1.5, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',160, 120)# Створення динамічного монстра на 7 рівні
zombie7_5 = Enemie(103, 594, 21, 30, 1.5, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',230, 120)# Створення динамічного монстра на 7 рівні
zombie7_6 = Enemie(483, 567, 21, 30, 1.5, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',150, 120)# Створення динамічного монстра на 7 рівні
# Динамічні монстри на 8 рівні
zombie8_1 = Enemie(386, 188, 21, 30, 2, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',120, 120)# Створення динамічного монстра на 8 рівні
zombie8_2 = Enemie(914, 269, 21, 30, 2, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',70, 120)# Створення динамічного монстра на 8 рівні
zombie8_3 = Enemie(144, 377, 21, 30, 2, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',150, 120)# Створення динамічного монстра на 8 рівні
zombie8_4 = Enemie(721, 512, 21, 30, 2, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',70, 120)# Створення динамічного монстра на 8 рівні
zombie8_5 = Enemie(626, 702, 21, 30, 2, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',310, 120)# Створення динамічного монстра на 8 рівні
zombie8_6 = Enemie(769, 404, 21, 30, 2, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',120, 120)# Створення динамічного монстра на 8 рівні
# Динамічні монстри на 9 рівні
zombie9_1 = Enemie(241, 214, 21, 30, 2, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',120, 120)# Створення динамічного монстра на 9 рівні
zombie9_2 = Enemie(528, 160, 21, 30, 2, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',120, 120)# Створення динамічного монстра на 9 рівні
zombie9_3 = Enemie(384, 323, 21, 30, 2, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',170, 120)# Створення динамічного монстра на 9 рівні
zombie9_4 = Enemie(673, 404, 21, 30, 2, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',110, 120)# Створення динамічного монстра на 9 рівні
zombie9_5 = Enemie(288, 702, 21, 30, 2, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',220, 120)# Створення динамічного монстра на 9 рівні
zombie9_6 = Enemie(578, 702, 21, 30, 2, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',210, 120)# Створення динамічного монстра на 9 рівні
# Динамічні монстри на 10 рівні
zombie10_1 = Enemie(533, 215, 21, 30, 2, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',120, 120)# Створення динамічного монстра на 10 рівні
zombie10_2 = Enemie(819, 188, 21, 30, 2, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',120, 120)# Створення динамічного монстра на 10 рівні
zombie10_3 = Enemie(192, 485, 21, 30, 2, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',120, 120)# Створення динамічного монстра на 10 рівні
zombie10_4 = Enemie(289, 702, 21, 30, 2, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',120, 120)# Створення динамічного монстра на 10 рівні
zombie10_5 = Enemie(530, 648, 21, 30, 2, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',120, 120)# Створення динамічного монстра на 10 рівні
# Динамічні монстри на 11 рівні
zombie11_1 = Enemie(243, 215, 21, 30, 2, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',170, 120)# Створення динамічного монстра на 11 рівні
zombie11_2 = Enemie(578, 161, 21, 30, 2, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',120, 120)# Створення динамічного монстра на 11 рівні
zombie11_3 = Enemie(387, 431, 21, 30, 2, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',130, 120)# Створення динамічного монстра на 11 рівні
zombie11_4 = Enemie(437, 539, 21, 30, 2, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',180, 120)# Створення динамічного монстра на 11 рівні
zombie11_5 = Enemie(199, 620, 21, 30, 2, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',120, 120)# Створення динамічного монстра на 11 рівні
zombie11_6 = Enemie(151, 700, 21, 30, 2, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',300, 120)# Створення динамічного монстра на 11 рівні
# Динамічні монстри на 12 рівні
zombie12_1 = Enemie(436, 702, 21, 30, 2, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',200, 120)# Створення динамічного монстра на 12 рівні
zombie12_2 = Enemie(778, 702, 21, 30, 2, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',260, 120)# Створення динамічного монстра на 12 рівні
zombie12_3 = Enemie(442, 594, 21, 30, 2, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',170, 120)# Створення динамічного монстра на 12 рівні
zombie12_4 = Enemie(200, 296, 21, 30, 2, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',120, 120)# Створення динамічного монстра на 12 рівні
zombie12_5 = Enemie(780, 296, 21, 30, 2, "/image/enemiewalk/walkingdude1.png", 0, 2, 2, 'Right',120, 120)# Створення динамічного монстра на 12 рівні
#Список динамічних монстрів на 1 рівні
enemys_1 = [
    zombie1_1, zombie1_2, zombie1_3,
    zombie1_4, zombie1_5, zombie1_6,
    zombie1_7, zombie1_8, zombie1_9,
    zombie1_10, zombie1_11, zombie1_12
]
#Список динамічних монстрів на 2 рівні
enemys_2 = [
    zombie2_1, zombie2_2, zombie2_3,
    zombie2_4, zombie2_5, zombie2_6,
    zombie2_7, zombie2_8, zombie2_9,
    zombie2_10, zombie2_11, zombie2_12
]
#Список динамічних монстрів на 3 рівні
enemys_3 = [
    zombie3_1, zombie3_2, zombie3_3,
    zombie3_4, zombie3_5, zombie3_6,
    zombie3_7, zombie3_8, zombie3_9,
    zombie3_10
]
#Список динамічних монстрів на 4 рівні
enemys_4 = [
    zombie4_1, zombie4_2, zombie4_3,
    zombie4_4, zombie4_5, zombie4_6,
    zombie4_7, zombie4_8, zombie4_9,
]
#Список динамічних монстрів на 5 рівні
enemys_5 = [
    zombie5_1, zombie5_2, zombie5_3,
    zombie5_4, zombie5_5, zombie5_6,
    zombie5_7, zombie5_8, zombie5_9 
]
#Список динамічних монстрів на 6 рівні
enemys_6 = [
    zombie6_1, zombie6_2, zombie6_3,
    zombie6_4, zombie6_5, zombie6_6,
    zombie6_7  
]
#Список динамічних монстрів на 7 рівні
enemys_7 = [
    zombie7_1, zombie7_2, zombie7_3,
    zombie7_4, zombie7_5, zombie7_6
]
#Список динамічних монстрів на 8 рівні
enemys_8 = [
    zombie8_1, zombie8_2, zombie8_3,
    zombie8_4, zombie8_5, zombie8_6
]
#Список динамічних монстрів на 9 рівні
enemys_9 = [
    zombie9_1, zombie9_2, zombie9_3,
    zombie9_4, zombie9_5, zombie9_6
]
#Список динамічних монстрів на 10 рівні
enemys_10 = [
    zombie10_1, zombie10_2, zombie10_3,
    zombie10_4, zombie10_5
]
#Список динамічних монстрів на 11 рівні
enemys_11 = [
    zombie11_1, zombie11_2, zombie11_3,
    zombie11_4, zombie11_5, zombie11_6
]
#Список динамічних монстрів на 12 рівні
enemys_12 = [
    zombie12_1, zombie12_2, zombie12_3,
    zombie12_4, zombie12_5
]
"""------------------------------------------------------------------------------------------------------"""

"""--------------------------------------------Shoot_Enemys----------------------------------------------"""
shooter1_1 = Static_Enemie(48, 433, 17, 27, 1, "/image/enemyshooting/right/enemyshootright1.png", 0, 1, 5, 'Left')# Створення монстра на 1 рівні з здатністю постріла
shooter1_2 = Static_Enemie(596, 510, 27, 17, 1, "/image/enemyshooting/left/enemyshootleft1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
shooter1_3 = Static_Enemie(1008, 240, 27, 17, 1, "/image/enemyshooting/up/enemyshootup1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
shooter1_4 = Static_Enemie(717, 134  , 27, 17, 1, "/image/enemyshooting/up/enemyshootup1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
#Список статичних монстрів з пострілом на 1 рівні
shoot_enemys_1 = [
    shooter1_1,
    shooter1_2,
    shooter1_3,
    shooter1_4
]

shooter2_1 = Static_Enemie(1040, 212, 17, 27, 1, "/image/enemyshooting/right/enemyshootleft1.png", 0, 1, 5, 'Right')# Створення монстра на 1 рівні з здатністю постріла
shooter2_2 = Static_Enemie(915, 25, 27, 17, 1, "/image/enemyshooting/left/enemyshootleft1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
shooter2_3 = Static_Enemie(729, 351, 27, 17, 1, "/image/enemyshooting/up/enemyshootup1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
shooter2_4 = Static_Enemie(1020, 402, 27, 17, 1, "/image/enemyshooting/up/enemyshootup1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
#Список статичних монстрів з пострілом на 1 рівні
shoot_enemys_2 = [
    shooter2_1,
    shooter2_2,
    shooter2_3,
    shooter2_4,
]

shooter3_1 = Static_Enemie(1038, 297, 17, 27, 1, "/image/enemyshooting/right/enemyshootleft1.png", 0, 1, 5, 'Right')# Створення монстра на 1 рівні з здатністю постріла
shooter3_2 = Static_Enemie(339, 25, 27, 17, 1, "/image/enemyshooting/left/enemyshootleft1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
shooter3_3 = Static_Enemie(194, 565, 27, 17, 1, "/image/enemyshooting/up/enemyshootup1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
shooter3_4 = Static_Enemie(1017, 593, 27, 17, 1, "/image/enemyshooting/up/enemyshootup1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
#Список статичних монстрів з пострілом на 1 рівні
shoot_enemys_3 = [
    shooter3_1,
    shooter3_2,
    shooter3_3,
    shooter3_4,
]

shooter4_1 = Static_Enemie(49, 380, 17, 27, 1, "/image/enemyshooting/right/enemyshootright1.png", 0, 1, 5, 'Left')# Створення монстра на 1 рівні з здатністю постріла
shooter4_2 = Static_Enemie(194, 539, 27, 17, 1, "/image/enemyshooting/left/enemyshootleft1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
shooter4_3 = Static_Enemie(724, 294, 27, 17, 1, "/image/enemyshooting/up/enemyshootup1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
shooter4_4 = Static_Enemie(724, 596, 27, 17, 1, "/image/enemyshooting/up/enemyshootup1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
#Список статичних монстрів з пострілом на 1 рівні
shoot_enemys_4 = [
    shooter4_1,
    shooter4_2,
    shooter4_3,
    shooter4_4,
]

shooter5_1 = Static_Enemie(433, 456, 17, 27, 1, "/image/enemyshooting/right/enemyshootright1.png", 0, 1, 5, 'Left')# Створення монстра на 1 рівні з здатністю постріла
shooter5_2 = Static_Enemie(1011, 378, 27, 17, 1, "/image/enemyshooting/left/enemyshootleft1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
shooter5_3 = Static_Enemie(862, 107, 27, 17, 1, "/image/enemyshooting/up/enemyshootup1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
shooter5_4 = Static_Enemie(242, 620, 27, 17, 1, "/image/enemyshooting/up/enemyshootup1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
#Список статичних монстрів з пострілом на 1 рівні
shoot_enemys_5 = [
    shooter5_1,
    shooter5_2,
    shooter5_3,
    shooter5_4,
]

shooter6_1 = Static_Enemie(577, 159, 17, 27, 1, "/image/enemyshooting/right/enemyshootright1.png", 0, 1, 5, 'Left')# Створення монстра на 1 рівні з здатністю постріла
shooter6_2 = Static_Enemie(99, 159, 27, 17, 1, "/image/enemyshooting/left/enemyshootleft1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
shooter6_3 = Static_Enemie(725, 619, 27, 17, 1, "/image/enemyshooting/up/enemyshootup1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
shooter6_4 = Static_Enemie(868, 512, 27, 17, 1, "/image/enemyshooting/up/enemyshootup1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
#Список статичних монстрів з пострілом на 1 рівні
shoot_enemys_6 = [
    shooter6_1,
    shooter6_2,
    shooter6_3,
    shooter6_4,
]

shooter7_1 = Static_Enemie(1037, 187, 17, 27, 1, "/image/enemyshooting/right/enemyshootleft1.png", 0, 1, 5, 'Right')# Створення монстра на 1 рівні з здатністю постріла
shooter7_2 = Static_Enemie(963, 483, 27, 17, 1, "/image/enemyshooting/left/enemyshootleft1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
shooter7_3 = Static_Enemie(438, 431, 27, 17, 1, "/image/enemyshooting/up/enemyshootup1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
shooter7_4 = Static_Enemie(100, 241, 27, 17, 1, "/image/enemyshooting/up/enemyshootup1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
#Список статичних монстрів з пострілом на 1 рівні
shoot_enemys_7 = [
    shooter7_1,
    shooter7_2,
    shooter7_3,
    shooter7_4,
]

shooter8_1 = Static_Enemie(385, 351, 17, 27, 1, "/image/enemyshooting/right/enemyshootright1.png", 0, 1, 5, 'Left')# Створення монстра на 1 рівні з здатністю постріла
shooter8_2 = Static_Enemie(871, 427, 27, 17, 1, "/image/enemyshooting/left/enemyshootleft1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
shooter8_3 = Static_Enemie(865, 133, 27, 17, 1, "/image/enemyshooting/up/enemyshootup1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
shooter8_4 = Static_Enemie(957, 568, 27, 17, 1, "/image/enemyshooting/up/enemyshootup1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
#Список статичних монстрів з пострілом на 1 рівні
shoot_enemys_8 = [
    shooter8_1,
    shooter8_2,
    shooter8_3,
    shooter8_4,
]

shooter9_1 = Static_Enemie(288, 405, 17, 27, 1, "/image/enemyshooting/right/enemyshootright1.png", 0, 1, 5, 'Left')# Створення монстра на 1 рівні з здатністю постріла
shooter9_2 = Static_Enemie(625, 190, 27, 17, 1, "/image/enemyshooting/left/enemyshootleft1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
shooter9_3 = Static_Enemie(909, 161, 27, 17, 1, "/image/enemyshooting/up/enemyshootup1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
shooter9_4 = Static_Enemie(959, 510, 27, 17, 1, "/image/enemyshooting/up/enemyshootup1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
#Список статичних монстрів з пострілом на 1 рівні
shoot_enemys_9 = [
    shooter9_1,
    shooter9_2,
    shooter9_3,
    shooter9_4,
]

shooter10_1 = Static_Enemie(125, 240, 17, 27, 1, "/image/enemyshooting/right/enemyshootleft1.png", 0, 1, 5, 'Right')# Створення монстра на 1 рівні з здатністю постріла
shooter10_2 = Static_Enemie(975, 26, 27, 17, 1, "/image/enemyshooting/left/enemyshootleft1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
shooter10_3 = Static_Enemie(147, 483, 27, 17, 1, "/image/enemyshooting/up/enemyshootup1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
shooter10_4 = Static_Enemie(817, 620, 27, 17, 1, "/image/enemyshooting/up/enemyshootup1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
#Список статичних монстрів з пострілом на 1 рівні
shoot_enemys_10 = [
    shooter10_1,
    shooter10_2,
    shooter10_3,
    shooter10_4,
]
shooter11_1 = Static_Enemie(148, 26, 27, 17, 1, "/image/enemyshooting/left/enemyshootleft1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
shooter11_2 = Static_Enemie(483, 566, 27, 17, 1, "/image/enemyshooting/left/enemyshootleft1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
shooter11_3 = Static_Enemie(103, 566, 27, 17, 1, "/image/enemyshooting/up/enemyshootup1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
shooter11_4 = Static_Enemie(379, 243, 27, 17, 1, "/image/enemyshooting/up/enemyshootup1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
#Список статичних монстрів з пострілом на 1 рівні
shoot_enemys_11 = [
    shooter11_1,
    shooter11_2,
    shooter11_3,
    shooter11_4,
]
shooter12_1 = Static_Enemie(673, 619, 17, 27, 1, "/image/enemyshooting/right/enemyshootright1.png", 0, 1, 5, 'Left')# Створення монстра на 1 рівні з здатністю постріла
shooter12_2 = Static_Enemie(336, 621, 27, 17, 1, "/image/enemyshooting/left/enemyshootleft1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
shooter12_3 = Static_Enemie(629, 458, 27, 17, 1, "/image/enemyshooting/up/enemyshootup1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
shooter12_4 = Static_Enemie(148, 537, 27, 17, 1, "/image/enemyshooting/up/enemyshootup1.png", 0, 1, 5, 'Top')# Створення монстра на 1 рівні з здатністю постріла
#Список статичних монстрів з пострілом на 1 рівні
shoot_enemys_12 = [
    shooter12_1,
    shooter12_2,
    shooter12_3,
    shooter12_4,
]
"""------------------------------------------------------------------------------------------------------"""
# Загружаємо всі текстури
all_list = [
    list_ores1, list_coin, list_ores2, list_ores3,
    list_ores4, list_ores5, list_ores6
]

list_all_enemie_1 = [enemys_1, shoot_enemys_1, chonkys_1]
list_all_enemie_2 = [enemys_2, shoot_enemys_2, chonkys_2]
list_all_enemie_3 = [enemys_3, shoot_enemys_3, chonkys_3]
list_all_enemie_4 = [enemys_4, shoot_enemys_4, chonkys_4]
list_all_enemie_5 = [enemys_5, shoot_enemys_5, chonkys_5]
list_all_enemie_6 = [enemys_6, shoot_enemys_6, chonkys_6]
list_all_enemie_7 = [enemys_7, shoot_enemys_7, chonkys_7]
list_all_enemie_8 = [enemys_8, shoot_enemys_8, chonkys_8]
list_all_enemie_9 = [enemys_9, shoot_enemys_9, chonkys_9]
list_all_enemie_10 = [enemys_10, shoot_enemys_10, chonkys_10]
list_all_enemie_11 = [enemys_11, shoot_enemys_11, chonkys_11]
list_all_enemie_12 = [enemys_12, shoot_enemys_12, chonkys_12]

for list in all_list:
    for obj in list:
        obj.load_image()

for_load_image = [
    rope, heart, deathbg, heartupgrade, coin6, cavebg, grassbg, caveenterbottom, caveentertop, 
    sellall, buttonsellemeralds, buttonselldiamond, buttonsellgold, buttonselliron, buttonsellsilver,
    buttonbuy, buttonsell, tavernabg, bgstart, taverna, Esc, buttonnext1, backbutton, help1, help2, C,
    coin8, recover, history1, history2, history3, history4, history5, buttonnext, buttonleave, buttontry,
    logo, kywshbg
]

for image in for_load_image:
    image.load_image()

for_load_text = [
    heartupgradeprice, diamondprice, emeraldsprice, goldprice, silverprice, ironprice, recoverprice,

]

for text in for_load_text:
    text.load_text()


all_enemy = [
    list_all_enemie_1,
    list_all_enemie_2 ,
    list_all_enemie_3 ,
    list_all_enemie_4 ,
    list_all_enemie_5 ,
    list_all_enemie_6 ,
    list_all_enemie_7 ,
    list_all_enemie_8 ,
    list_all_enemie_9 ,
    list_all_enemie_10,
    list_all_enemie_10,
    list_all_enemie_11,
]

all_ores = [
    list_ores1,
    list_ores2,
    list_ores3,
    list_ores4,
    list_ores5,
    list_ores6,
    list_ores7
]