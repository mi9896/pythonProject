import random
from poldeptopFL import *
import json
import os


def remesting():
    print("Таблица лидеров: ")
    if emeralds > em1:
        print(mes1, playname, vin1, "❇️ кол.изумрудов:", emeralds, "❇️ ID:", IdifendIp)
        print(mes2, MEST1, vin2, MEST1_1)
        print(mes3, MEST2, vin3, MEST2_2)
    elif emeralds > em2:
        print(mes1, MEST1, vin1, MEST1_1)
        print(mes2, playname, vin2, "❇️ кол.изумрудов:", emeralds, "❇️ ID:", IdifendIp)
        print(mes3, MEST2, vin3, MEST2_2)
    elif emeralds > em3:
        print(mes1, MEST1, vin1, MEST1_1)
        print(mes2, MEST2, vin2, MEST2_2)
        print(mes3, playname, vin3, "❇️ кол.изумрудов:", emeralds, "❇️ ID:", IdifendIp)
    else:
        print(mes1, MEST1, vin1, MEST1_1)
        print(mes2, MEST2, vin2, MEST2_2)
        print(mes3, MEST3, vin3, MEST3_3)


def remestingpy():
    print("Таблица лидеров: ")
    if yrprof > yp1:
        print(mes1, playname, vin1, "🎓 Уровень профиля:", yrprof, "🎓 ID:", IdifendIp)
        print(mes2, MESTPY1, vin2, MESTPY1_1)
        print(mes3, MESTPY2, vin3, MESTPY2_2)
    elif yrprof > yp2:
        print(mes1, MESTPY1, vin1, MESTPY1_1)
        print(mes2, playname, vin2, "🎓 Уровень профиля:", yrprof, "🎓 ID:", IdifendIp)
        print(mes3, MESTPY2, vin3, MESTPY2_2)
    elif yrprof > yp3:
        print(mes1, MESTPY1, vin1, MESTPY1_1)
        print(mes2, MESTPY2, vin2, MESTPY2_2)
        print(mes3, playname, vin3, "🎓 Уровень профиля:", yrprof, "🎓 ID:", IdifendIp)
    else:
        print(mes1, MESTPY1, vin1, MESTPY1_1)
        print(mes2, MESTPY2, vin2, MESTPY2_2)
        print(mes3, MESTPY3, vin3, MESTPY3_3)


def remestingpt():
    print("Таблица лидеров: ")
    if trophei > tr1:
        print(mes1, playname, vin1, "🏆 Количество трофеев:", trophei, "🏆 ID:", IdifendIp)
        print(mes2, MESTPT1, vin2, MESTPT1_1)
        print(mes3, MESTPT2, vin3, MESTPT2_2)
    elif trophei > tr2:
        print(mes1, MESTPT1, vin1, MESTPT1_1)
        print(mes2, playname, vin2, "🏆 Количество трофеев:", trophei, "🏆 ID:", IdifendIp)
        print(mes3, MESTPT2, vin3, MESTPT2_2)
    elif trophei > tr3:
        print(mes1, MESTPT1, vin1, MESTPT1_1)
        print(mes2, MESTPT2, vin2, MESTPT2_2)
        print(mes3, playname, vin3, "🏆 Количество трофеев:", trophei, "🏆 ID:", IdifendIp)
    else:
        print(mes1, MESTPT1, vin1, MESTPT1_1)
        print(mes2, MESTPT2, vin2, MESTPT2_2)
        print(mes3, MESTPT3, vin3, MESTPT3_3)


print("1")
if omer == 0:
    I1 = ['w', 'D', 'F', 'g', 'H', 'u', 'Y', 't', 'I', 'P', 'o', 'm', 'M', 'u', 'q', 'c', 'J', 'E', 'x', 'L']
    I2 = ['1', '0', '2', '3', '4', '5', '6', '7', '8', '9']
    Id1 = random.choice(I1)
    Id2 = random.choice(I1)
    Id3 = random.choice(I2)
    Id4 = random.choice(I1)
    Id5 = random.choice(I2)
    Id6 = random.choice(I2)
    Id7 = random.choice(I2)
    Id8 = random.choice(I1)
    Id9 = random.choice(I1)
    Id10 = random.choice(I1)
    Id11 = random.choice(I1)
    Id12 = random.choice(I1)
    Id13 = random.choice(I1)
    Id14 = random.choice(I2)
    IdifendIp = Id1 + Id2 + Id3 + "-" + Id4 + Id5 + Id6 + "-" + Id7 + Id8 + Id9 + Id10 + "-" + Id11 + Id12 + Id13 + "-" + Id14
    omer += 1
print("2")

if omer == 1:
    print("3")
    Id3Id = {"1": "9", "0": "8", "2": "7", "3": "6", "4": "5", "5": "4", "6": "3", "7": "2", "8": "0", "9": "1"}
    for i in Id3Id:
        if Id3 == i:
            kode_mini_plysh1 = Id3Id[i]
    if Id5 == "1":
        kode_mini_plysh2 = "P"
    elif Id5 == "0":
        kode_mini_plysh2 = "D"
    elif Id5 == "2":
        kode_mini_plysh2 = "O"
    elif Id5 == "3":
        kode_mini_plysh2 = "F"
    elif Id5 == "4":
        kode_mini_plysh2 = "I"
    elif Id5 == "5":
        kode_mini_plysh2 = "G"
    elif Id5 == "6":
        kode_mini_plysh2 = "U"
    elif Id5 == "7":
        kode_mini_plysh2 = "H"
    elif Id5 == "8":
        kode_mini_plysh2 = "U"
    elif Id5 == "9":
        kode_mini_plysh2 = "H"
    if Id6 == "1":
        kode_mini_plysh3 = "l"
    elif Id6 == "0":
        kode_mini_plysh3 = "l"
    elif Id6 == "2":
        kode_mini_plysh3 = "s"
    elif Id6 == "3":
        kode_mini_plysh3 = "f"
    elif Id6 == "4":
        kode_mini_plysh3 = "i"
    elif Id6 == "5":
        kode_mini_plysh3 = "h"
    elif Id6 == "6":
        kode_mini_plysh3 = "d"
    elif Id6 == "7":
        kode_mini_plysh3 = "l"
    elif Id6 == "8":
        kode_mini_plysh3 = "u"
    elif Id6 == "9":
        kode_mini_plysh3 = "u"
    if Id7 == "1":
        kode_mini_plysh4 = "u"
    elif Id7 == "0":
        kode_mini_plysh4 = "u"
    elif Id7 == "2":
        kode_mini_plysh4 = "s"
    elif Id7 == "3":
        kode_mini_plysh4 = "h"
    elif Id7 == "4":
        kode_mini_plysh4 = "i"
    elif Id7 == "5":
        kode_mini_plysh4 = "h"
    elif Id7 == "6":
        kode_mini_plysh4 = "i"
    elif Id7 == "7":
        kode_mini_plysh4 = "l"
    elif Id7 == "8":
        kode_mini_plysh4 = "u"
    elif Id7 == "9":
        kode_mini_plysh4 = "u"
    if Id14 == "1":
        kode_mini_plysh5 = "s"
    elif Id14 == "0":
        kode_mini_plysh5 = "s"
    elif Id14 == "2":
        kode_mini_plysh5 = "s"
    elif Id14 == "3":
        kode_mini_plysh5 = "h"
    elif Id14 == "4":
        kode_mini_plysh5 = "h"
    elif Id14 == "5":
        kode_mini_plysh5 = "h"
    elif Id14 == "6":
        kode_mini_plysh5 = "s"
    elif Id14 == "7":
        kode_mini_plysh5 = "s"
    elif Id14 == "8":
        kode_mini_plysh5 = "h"
    elif Id14 == "9":
        kode_mini_plysh5 = "h"
    if Id14 == "1":
        kode_mini_plysh6 = "h"
    elif Id14 == "0":
        kode_mini_plysh6 = "h"
    elif Id14 == "2":
        kode_mini_plysh6 = "h"
    elif Id14 == "3":
        kode_mini_plysh6 = "s"
    elif Id14 == "4":
        kode_mini_plysh6 = "s"
    elif Id14 == "5":
        kode_mini_plysh6 = "s"
    elif Id14 == "6":
        kode_mini_plysh6 = "h"
    elif Id14 == "7":
        kode_mini_plysh6 = "h"
    elif Id14 == "8":
        kode_mini_plysh6 = "s"
    elif Id14 == "9":
        kode_mini_plysh6 = "s"
    kode_mini_plysh = kode_mini_plysh1 + "-" + kode_mini_plysh2 + kode_mini_plysh3 + kode_mini_plysh4 + kode_mini_plysh5 + kode_mini_plysh6
    omer += 1
print("kode_mini_plysh6 =", kode_mini_plysh6)
print("kode_mini_plysh5 =", kode_mini_plysh5)
print("kode_mini_plysh4 =", kode_mini_plysh4)
print("kode_mini_plysh3 =", kode_mini_plysh3)
print("kode_mini_plysh2 =", kode_mini_plysh2)
print("kode_mini_plysh1 =", kode_mini_plysh1)
print("kode_mini_plysh =", kode_mini_plysh)


def pervkart():
    go_player_minimap_ob = codrdinite
    if go_player_minimap_ob == 6:
        go_player_minimap_ob_st6 = "🟦"
        go_player_minimap_ob_st11 = "🟩"
        go_player_minimap_ob_st12 = "🟩"
        go_player_minimap_ob_st13 = "🟩"
        go_player_minimap_ob_st8 = "🟥"
    elif go_player_minimap_ob == 11:
        go_player_minimap_ob_st6 = "🟩"
        go_player_minimap_ob_st11 = "🟦"
        go_player_minimap_ob_st12 = "🟩"
        go_player_minimap_ob_st13 = "🟩"
        go_player_minimap_ob_st8 = "🟥"
    elif go_player_minimap_ob == 12:
        go_player_minimap_ob_st6 = "🟩"
        go_player_minimap_ob_st11 = "🟩"
        go_player_minimap_ob_st12 = "🟦"
        go_player_minimap_ob_st13 = "🟩"
        go_player_minimap_ob_st8 = "🟥"
    elif go_player_minimap_ob == 13:
        go_player_minimap_ob_st6 = "🟩"
        go_player_minimap_ob_st11 = "🟩"
        go_player_minimap_ob_st12 = "🟩"
        go_player_minimap_ob_st13 = "🟦"
        go_player_minimap_ob_st8 = "🟥"
    elif go_player_minimap_ob == 14:
        go_player_minimap_ob_st6 = "🟩"
        go_player_minimap_ob_st11 = "🟩"
        go_player_minimap_ob_st12 = "🟩"
        go_player_minimap_ob_st13 = "🟩"
        go_player_minimap_ob_st8 = "🟦"
    print("🟫🟫🟫🟫")
    print("🟫" + go_player_minimap_ob_st8 + go_player_minimap_ob_st13 + "🟫")
    print("🟫🟫" + go_player_minimap_ob_st12 + "🟫")
    print("🟫" + go_player_minimap_ob_st6 + go_player_minimap_ob_st11 + "🟫")
    print("🟫🟫🟫🟫")


def shops(magz, mcikl, loc1, loc2, loc3, magpok1, magpok2, magpok3, emeralds, PBox, LBox):
    if magz > 5:
        magz = 0
    print("Добропожаловать в магазин!")
    while mcikl:
        print("Что-бы выйти из магазина напишите: 'выход'")
        if magz == 0:
            print("Асортимент:")
            sort = ['AD1', 'Структурный', 'Структурная']
            if 'Структурная' in DostPersone:
                if loc1 == 1:
                    if loc2 == 1:
                        del sort[0]
                        magpok3 = 0
                    elif loc2 == 0:
                        del sort[1]
                        magpok3 = 0
                elif loc1 == 0:
                    if loc2 == 1:
                        del sort[1]
                        magpok3 = 0
                    elif loc2 == 0:
                        del sort[2]
                        magpok3 = 0
            if 'Структурный' in DostPersone:
                if loc1 == 1:
                    if loc3 == 1:
                        del sort[0]
                        magpok2 = 0
                    elif loc3 == 0:
                        del sort[0]
                        magpok2 = 0
                elif loc1 == 0:
                    if loc3 == 1:
                        del sort[1]
                        magpok2 = 0
                    elif loc3 == 0:
                        del sort[1]
                        magpok2 = 0
            if 'AD1' in DostPersone:
                if loc2 == 1:
                    if loc3 == 1:
                        del sort[0]
                        magpok1 = 0
                    elif loc3 == 0:
                        del sort[0]
                        magpok1 = 0
                elif loc2 == 0:
                    if loc3 == 1:
                        del sort[0]
                        magpok1 = 0
                    elif loc3 == 0:
                        del sort[0]
                        magpok1 = 0
            magBox = ['простой', 'легаси']
            print("Персонажи:", sort)
            print("Ящики:", magBox)
            sobp = input()
            if sobp == 'AD1':
                if magpok1 == 1:
                    print("Выбран:", sobp)
                    print("Тип персонаж")
                    print("Цена: ❇️ 230 изумрудов ❇️")
                    print("Вы покупаете?")
                    sobp = input()
                    if sobp == "да":
                        if emeralds >= 230:
                            emeralds -= 230
                            loc1 = 1
                            DostPersone.append('AD1')
                            print("Покупка прошла успешно!")
                            print("Ваше количество изумрудов:", emeralds)
                        else:
                            print("У вас недостатачно изумрудов!")
                    else:
                        print("Ок")
            elif sobp == 'Структурный':
                if magpok2 == 1:
                    print("Выбран:", sobp)
                    print("Тип персонаж")
                    print("Цена: ❇️ 160 изумрудов ❇️")
                    print("Вы покупаете?")
                    sobp = input()
                    if sobp == "да":
                        if emeralds >= 160:
                            emeralds -= 160
                            loc2 = 1
                            DostPersone.append('Структурный')
                            print("Покупка прошла успешно!")
                            print("Ваше количество изумрудов:", emeralds)
                        else:
                            print("У вас недостатачно изумрудов!")
                    else:
                        print("Ок")
            elif sobp == 'Структурная':
                if magpok3 == 1:
                    print("Выбрана:", sobp)
                    print("Тип персонаж")
                    print("Цена: ❇️ 180 изумрудов ❇️")
                    print("Вы покупаете?")
                    sobp = input()
                    if sobp == "да":
                        if emeralds >= 180:
                            emeralds -= 180
                            loc3 = 1
                            DostPersone.append('Структурная')
                            print("Покупка прошла успешно!")
                            print("Ваше количество изумрудов:", emeralds)
                        else:
                            print("У вас недостатачно изумрудов!")
                    else:
                        print("Ок")
            elif sobp == "простой":
                print("Выбран:", sobp)
                print("Тип ящик")
                kola = int(input("Количество: "))
                bzen = 160
                bzen2 = bzen * kola
                print("Цена: ❇️", bzen2, "изумрудов ❇️")
                print("Вы покупаете?")
                sobp = input()
                if sobp == "да":
                    if emeralds >= bzen2:
                        emeralds -= bzen2
                        PBox += kola
                        print("Покупка прошла успешно!")
                        print("Ваше количество изумрудов:", emeralds)
                    else:
                        print("У вас недостатачно изумрудов!")
                else:
                    print("Ок")
            elif sobp == "легаси":
                print("Выбран:", sobp)
                print("Тип ящик")
                kola = int(input("Количество: "))
                bzen = 200
                bzen2 = bzen * kola
                print("Цена: ❇️", bzen2, "изумрудов ❇️")
                print("Вы покупаете?")
                sobp = input()
                if sobp == "да":
                    if emeralds >= bzen2:
                        emeralds -= bzen2
                        LBox += kola
                        print("Покупка прошла успешно!")
                        print("Ваше количество изумрудов:", emeralds)
                    else:
                        print("У вас недостатачно изумрудов!")
                else:
                    print("Ок")
            elif sobp == "выход":
                mcikl = False

def liga(MAXtrophei, trophei):
    print("Ваше наивысшее количество трофеев:", MAXtrophei)
    print("Ваше нынешнее количество трофеев:", trophei)
    print("Напишите 'список' чтобы увидеть список ступеней или 'ступень' чтобы увидеть свою ступень")
    ligovapyt = input()
    if ligovapyt == "список":
        print("Список ступеней:")
        print("Ржавая I [0 трофеев]")
        print("Ржавая II [100 трофеев]")
        print("Ржавая III [200 трофеев]")
        print("Ржавая IV [300 трофеев]")
        print("Ржавая V [400 трофеев]")
        print("Деревянная I [500 трофеев]")
        print("Деревянная II [700 трофеев]")
        print("Деревянная III [900 трофеев]")
        print("Деревянная IV [1100 трофеев]")
        print("Деревянная V [1300 трофеев]")
        print("Каменная I [1500 трофеев]")
        print("Каменная II [1700 трофеев]")
        print("Каменная III [2000 трофеев]")
        print("Каменная IV [2300 трофеев]")
        print("Каменная V [2600 трофеев]")
        print("Медная I [2900 трофеев]")
        print("Медная II [3300 трофеев]")
        print("Медная III [3700 трофеев]")
        print("Медная IV [4100 трофеев]")
        print("Медная V [4500 трофеев]")
        print("Стальная I [4900 трофеев]")
        print("Стальная II [5400 трофеев]")
        print("Стальная III [5900 трофеев]")
        print("Стальная IV [6400 трофеев]")
        print("Стальная V [6900 трофеев]")
    elif ligovapyt == "ступень":
        if 100 > trophei >= 0:
            print("Ваша ступень: Ржавая I")
        elif 200 > trophei >= 100:
            print("Ваша ступень: Ржавая II")
        elif 300 > trophei >= 200:
            print("Ваша ступень: Ржавая III")
        elif 400 > trophei >= 300:
            print("Ваша ступень: Ржавая IV")
        elif 500 > trophei >= 400:
            print("Ваша ступень: Ржавая V")
        elif 700 > trophei >= 500:
            print("Ваша ступень: Деревянная I")
        elif 900 > trophei >= 700:
            print("Ваша ступень: Деревянная II")
        elif 1100 > trophei >= 900:
            print("Ваша ступень: Деревянная III")
        elif 1300 > trophei >= 1100:
            print("Ваша ступень: Деревянная IV")
        elif 1500 > trophei >= 1300:
            print("Ваша ступень: Деревянная V")
        elif 1700 > trophei >= 1500:
            print("Ваша ступень: Каменная I")
        elif 2000 > trophei >= 1700:
            print("Ваша ступень: Каменная II")
        elif 2300 > trophei >= 2000:
            print("Ваша ступень: Каменная III")
        elif 2600 > trophei >= 2300:
            print("Ваша ступень: Каменная IV")
        elif 2900 > trophei >= 2600:
            print("Ваша ступень: Каменная V")
        elif 3300 > trophei >= 2900:
            print("Ваша ступень: Медная I")
        elif 3700 > trophei >= 3300:
            print("Ваша ступень: Медная II")
        elif 4100 > trophei >= 3700:
            print("Ваша ступень: Медная III")
        elif 4500 > trophei >= 4100:
            print("Ваша ступень: Медная IV")
        elif 4900 > trophei >= 4500:
            print("Ваша ступень: Медная V")
        elif 5400 > trophei >= 4900:
            print("Ваша ступень: Стальная I")
        elif 5900 > trophei >= 5400:
            print("Ваша ступень: Стальная II")
        elif 6400 > trophei >= 5900:
            print("Ваша ступень: Стальная III")
        elif 6900 > trophei >= 6400:
            print("Ваша ступень: Стальная IV")
        elif 7400 > trophei >= 6900:
            print("Ваша ступень: Стальная V")
def wonekart():
    print("🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫")
    print("🟫🟥🟩🟩🟩🟩🟩🟫🟩🟫")
    print("🟫🟫🟫🟫🟩🟩🟩🟩🟩🟫")
    print("🟫🟩🟩🟩🟫🟥🟩🟩🟩🟫")
    print("🟫🟩🟩🟩🟫🟩🟩🟩🟫🟫")
    print("🟫🟩🟫🟩🟩🟩🟩🟩🟫🟫")
    print("🟫🟩🟫🟩🟩🟩🟩🟩🟩🟫")
    print("🟫🟩🟫🟫🟩🟩🟥🟩🟩🟫")
    print("🟫🟦🟩🟩🟩🟩🟫🟩🟩🟫")
    print("🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫")


def name_simvl(playname, nam_sim):
    b = nam_sim
    nam_sim = len(playname)
    return nam_sim


def clear():
    return os.system('cls')


print("Welcome to Cloudcore")
print(" version:", version)
# if omer == 1:
#     playname = input("Введите свой никнейм:")
#     omer += 1
#     if omerdos == 1:
#         if playname == "mi9896":
#             signature = "mi97-98lo-g011-rim6"
#     elif omerdos == 1:
#         if playname == "AD1":
#             signature = "mi97-98lo-g011-rim6"
#     elif omerdos == 1:
#         if playname == "pixplay":
#             signature = "mi97-98lo-g011-rim6"
#     else:
#         signature = "be84-13lo-g890-zer7"
# if omer == 2:
#     omer += 1
#     while polol:
#         if playname == "mi9896":
#             parolpyt = input()
#             if parolpyt == poroli1:
#                 signature = "mi97-98lo-g011-rim6"
#             elif parolpyt != poroli1:
#                 pololv -= 1
#                 if pololv == 0:
#                     polol = False
#         elif playname == "AD1":
#             parolpyt = input()
#             if parolpyt == poroli2:
#                 signature = "mi97-98lo-g011-rim6"
#             elif parolpyt != poroli2:
#                 pololv -= 1
#                 if pololv == 0:
#                     polol = False
#         elif playname == "pixplay":
#             parolpyt = input()
#             if parolpyt == poroli3:
#                 signature = "mi97-98lo-g011-rim6"
#             elif parolpyt != poroli3:
#                 pololv -= 1
#                 if pololv == 0:
#                     polol = False
# if signature != "mi97-98lo-g011-rim6":
#     while True:
#         signdost = random.choice(dost)
#         if signdost == 1:
#             print("Неверная сигнатура!")
#             heldost = input()
#         elif signdost == 0:
#             print("Нет доступа!")
#             heldost = input()
if signature == "mi97-98lo-g011-rim6":
    if namnem == 0:
        while name_reg:
            playname = input("Введите свой никнейм:")
            nam_sim = name_simvl(playname, nam_sim)
            if nam_sim > 3 and nam_sim < 12:
                namnem += 1
                name_reg = False
            elif nam_sim <= 2:
                print("Ваше имя пользователя недопустимо!"
                      "\nВедь оно состоит из:", nam_sim, "символов \nИ противоречит правилам: "
                                                         "имя пользователя недолжно превышать 12 символов и быть меньше"
                                                         "3 символов!")
                print("Так что пожалуйста введите имя пользователя заново! :)")
            elif nam_sim > 12:
                print("Ваше имя пользователя недопустимо!"
                      "\nВедь оно состоит из:", nam_sim, "символов \nИ противоречит правилам: "
                                                         "имя пользователя недолжно превышать 12 символов и быть меньше"
                                                         "3 символов!")
                print("Так что пожалуйста введите имя пользователя заново")
    while True:
        mcikl = True
        lives = pervonahallives
        Weapon = pervonahalWeapon
        if trophei >= 550:
            if yrprof >= 20:
                dorstkvazvaniy = 1
                print("🗡️Теперь вам доступно выживание!🗡️")
        if yrproff >= 1:
            yrproff -= 1
            yrprof += 1
            print("🆙Уровень повышен!🆙")
        if mtik1 < 1:
            mtik10 -= 5
        if mtik1 <= 0:
            mtik1 = 10
            if mtik10 <= 0:
                mtik10 = 10
                magz += 1
        if trophei == trophei:
            if trophei < 0:
                trophei = 0
            elif trophei > MAXtrophei:
                MAXtrophei = trophei
        print("Ваши изумруды: ❇️", emeralds, "❇️")
        print("'профиль','лидеры','персонажи','магазин','ящики','промокоды','лига','играть'.")
        if dorstkvazvaniy == 1:
            print("'выживание'")
        menu = input()
        if menu == "/akvadevida":
            if ADMINPRAV == 0:
                ADMINPRAV += 9896
            elif ADMINPRAV == 9896:
                ADMINPRAV -= 9896
        elif menu == "персонажи":
            print("Доступные персонажи:", DostPersone)
            print("Персонажи которые есть в игре:", NeDostPersone)
            persolv = input()
            if persolv == "Путник":
                if persona == 1:
                    print("У вас уже выбран этот персонаж!")
                elif persona != 1:
                    print("Персонаж выбран")
                    persona = 1
                    Weapon = 5
                    lives = 12
                    print("Характеристики:")
                    print("Урон:", Weapon)
                    print("Жизни:", lives)
            elif persolv == "AD1":
                if loc1 == 1:
                    if persona == 2:
                        print("У вас уже выбран этот персонаж!")
                    elif persona != 2:
                        print("Персонаж выбран")
                        persona = 2
                        Weapon = 8
                        lives = 17
                        print("Характеристики:")
                        print("Урон:", Weapon)
                        print("Жизни:", lives)
                else:
                    print("У вас нет данного персонажа!")
            elif persolv == "Структурный":
                if loc2 == 1:
                    if persona == 3:
                        print("У вас уже выбран этот персонаж!")
                    elif persona != 3:
                        print("Персонаж выбран")
                        persona = 3
                        Weapon = 6
                        lives = 19
                        print("Характеристики:")
                        print("Урон:", Weapon)
                        print("Жизни:", lives)
                else:
                    print("У вас нет данного персонажа!")
            elif persolv == "Структурная":
                if loc3 == 1:
                    if persona == 4:
                        print("У вас уже выбран этот персонаж!")
                    elif persona != 4:
                        print("Персонаж выбран")
                        persona = 4
                        Weapon = 5
                        lives = 20
                        print("Характеристики:")
                        print("Урон:", Weapon)
                        print("Жизни:", lives)
                else:
                    print("У вас нет данного персонажа!")
            elif persolv == "Механический":
                if loc4 == 1:
                    if persona == 5:
                        print("У вас уже выбран этот персонаж!")
                    elif persona != 5:
                        print("Персонаж выбран")
                        persona = 5
                        Weapon = 8
                        lives = 15
                        print("Характеристики:")
                        print("Урон:", Weapon)
                        print("Жизни:", lives)
                else:
                    print("У вас нет данного персонажа!")
            elif persolv == "Нулевой":
                if loc5 == 1:
                    if persona == 6:
                        print("У вас уже выбран этот персонаж!")
                    elif persona != 6:
                        print("Персонаж выбран")
                        persona = 6
                        Weapon = 10
                        lives = 13
                        print("Характеристики:")
                        print("Урон:", Weapon)
                        print("Жизни:", lives)
                else:
                    print("У вас нет данного персонажа!")
            elif persolv == "Тень":
                if loc6 == 1:
                    if persona == 7:
                        print("У вас уже выбран этот персонаж!")
                    elif persona != 7:
                        print("Персонаж выбран")
                        persona = 7
                        Weapon = 6
                        lives = 22
                        print("Характеристики:")
                        print("Урон:", Weapon)
                        print("Жизни:", lives)
                else:
                    print("У вас нет данного персонажа!")
            elif persolv == "Кубер":
                if loc7 == 1:
                    if persona == 8:
                        print("У вас уже выбран этот персонаж!")
                    elif persona != 8:
                        print("Персонаж выбран")
                        persona = 8
                        Weapon = 12
                        lives = 28
                        print("Характеристики:")
                        print("Урон:", Weapon)
                        print("Жизни:", lives)
                else:
                    print("У вас нет данного персонажа!")
            if persolv == persolv:
                pervonahallives = lives
                pervonahalWeapon = Weapon
        elif menu == "магазин":
            shops(magz, mcikl, loc1, loc2, loc3, magpok1, magpok2, magpok3, emeralds, PBox, LBox)
        elif menu == "лига":
            liga(MAXtrophei, trophei)

        elif menu == "ящики":
            print("Количество ваших простых ящиков:", PBox)
            print("Количество ваших легаси ящиков:", LBox)
            print("Будете что-то открывать?")
            openBox = input()
            if openBox == "да":
                print("Что вы будете открывать: 'легаси' ящик или 'простой' ящик?")
                openBox = input()
                if openBox == "простой":
                    if PBox > 0:
                        print("Начинаем открытие!")
                        PBox -= 1
                        rrenPBox = random.choice(renPBox)
                        if rrenPBox == 1:
                            print("Вам выпало: ❇️ 30 изумрудов ❇️")
                            emeralds += 30
                        elif rrenPBox == 2:
                            print("Вам выпало: ❇️ 95 изумрудов ❇️")
                            emeralds += 95
                        elif rrenPBox == 3:
                            print("Вам выпало: ❇️ 120 изумрудов ❇️")
                            emeralds += 120
                        elif rrenPBox == 4:
                            print("Вам выпало: ❇️ 160 изумрудов ❇️")
                            emeralds += 160
                        elif rrenPBox == 5:
                            print("Вам выпало: ❇️ 240 изумрудов ❇️")
                            emeralds += 240
                        elif rrenPBox == 6:
                            print("Вам выпало: ❇️ 400 изумрудов ❇️")
                            emeralds += 400
                        elif rrenPBox == 7:
                            print("Вам выпало: ❇️ 30 изумрудов ❇️")
                            emeralds += 30
                        elif rrenPBox == 8:
                            print("Вам выпало: ❇️ 95 изумрудов ❇️")
                            emeralds += 95
                        elif emeralds == 9:
                            print("Вам выпало: ❇️ 30 изумрудов ❇️")
                            emeralds += 30
                        elif rrenPBox == 10:
                            print("Вам выпало: ❇️ 15 изумрудов ❇️")
                            emeralds += 15
                        elif rrenPBox == 11:
                            if loc1 == 1:
                                if loc2 == 1:
                                    print("Вам выпало: ❇️ 360 изумрудов ❇️")
                                    emeralds += 360
                                elif loc2 == 0:
                                    print("Вам выпал: Структурный")
                                    loc2 = 1
                                    DostPersone.append('Структурный')
                                    magpok2 = 0
                            elif loc1 == 0:
                                print("Вам выпал: AD1")
                                loc1 = 1
                                DostPersone.append('AD1')
                                magpok1 = 0
                        elif rrenPBox == 12:
                            print("Вам выпало: ❇️ 240 изумрудов ❇️")
                            emeralds += 240
                        else:
                            print("ошибка")
                            emeralds += 160
                    else:
                        print("У вас нету этих ящиков")
                elif openBox == "легаси":
                    if LBox > 0:
                        print("Начинаем открытие!")
                        LBox -= 1
                        rrenLBox = random.choice(renLBox)
                        if rrenLBox == 1:
                            print("Вам выпало: ❇️ 100 изумрудов ❇️")
                            emeralds += 100
                        elif rrenLBox == 2:
                            print("Вам выпало: ❇️ 240 изумрудов ❇️")
                            emeralds += 240
                        elif rrenLBox == 3:
                            print("Вам выпало: ❇️ 100 изумрудов ❇️")
                            emeralds += 100
                        elif rrenLBox == 4:
                            if loc1 == 1:
                                if loc2 == 1:
                                    if loc3 == 1:
                                        if loc4 == 1:
                                            if loc5 == 1:
                                                if loc6 == 1:
                                                    if loc7 == 1:
                                                        print("Вам выпало: ❇️ 360 изумрудов ❇️")
                                                        emeralds += 360
                                                    elif loc7 == 0:
                                                        print("Вам выпал: Кубер")
                                                        loc7 = 1
                                                        DostPersone.append('Кубер')
                                                elif loc6 == 0:
                                                    print("Вам выпал: Тень")
                                                    loc6 = 1
                                                    DostPersone.append('Тень')
                                            elif loc5 == 0:
                                                print("Вам выпал: Нулевой")
                                                loc5 = 1
                                                DostPersone.append('Нулевой')
                                        elif loc4 == 0:
                                            print("Вам выпал: Механический")
                                            loc4 = 1
                                            DostPersone.append('Механический')
                                    elif loc3 == 0:
                                        print("Вам выпала: Структурная")
                                        loc3 = 1
                                        DostPersone.append('Структурная')
                                        magpok3 = 0
                                elif loc2 == 0:
                                    print("Вам выпал: Структурный")
                                    loc2 = 1
                                    DostPersone.append('Структурный')
                                    magpok2 = 0
                            elif loc1 == 0:
                                print("Вам выпал: AD1")
                                loc1 = 1
                                DostPersone.append('AD1')
                                magpok1 = 0
                        elif rrenLBox == 5:
                            if loc1 == 1:
                                if loc2 == 1:
                                    if loc3 == 1:
                                        if loc4 == 1:
                                            if loc5 == 1:
                                                if loc6 == 1:
                                                    if loc7 == 1:
                                                        print("Вам выпало: ❇️ 420 изумрудов ❇️")
                                                        emeralds += 420
                                                    elif loc7 == 0:
                                                        print("Вам выпал: Кубер")
                                                        loc7 = 1
                                                        DostPersone.append('Кубер')
                                                elif loc6 == 0:
                                                    print("Вам выпал: Тень")
                                                    loc6 = 1
                                                    DostPersone.append('Тень')
                                            elif loc5 == 0:
                                                print("Вам выпал: Нулевой")
                                                loc5 = 1
                                                DostPersone.append('Нулевой')
                                        elif loc4 == 0:
                                            print("Вам выпал: Механический")
                                            loc4 = 1
                                            DostPersone.append('Механический')
                                    elif loc3 == 0:
                                        print("Вам выпала: Структурная")
                                        loc3 = 1
                                        DostPersone.append('Структурная')
                                        magpok3 = 0
                                elif loc2 == 0:
                                    print("Вам выпал: Структурный")
                                    loc2 = 1
                                    DostPersone.append('Структурный')
                                    magpok2 = 0
                            elif loc1 == 0:
                                print("Вам выпал: AD1")
                                loc1 = 1
                                DostPersone.append('AD1')
                                magpok1 = 0
                        elif rrenLBox == 6:
                            if loc1 == 1:
                                if loc2 == 1:
                                    if loc3 == 1:
                                        if loc4 == 1:
                                            if loc5 == 1:
                                                if loc6 == 1:
                                                    if loc7 == 1:
                                                        print("Вам выпало: ❇️ 480 изумрудов ❇️")
                                                        emeralds += 480
                                                    elif loc7 == 0:
                                                        print("Вам выпал: Кубер")
                                                        loc7 = 1
                                                        DostPersone.append('Кубер')
                                                elif loc6 == 0:
                                                    print("Вам выпал: Тень")
                                                    loc6 = 1
                                                    DostPersone.append('Тень')
                                            elif loc5 == 0:
                                                print("Вам выпал: Нулевой")
                                                loc5 = 1
                                                DostPersone.append('Нулевой')
                                        elif loc4 == 0:
                                            print("Вам выпал: Механический")
                                            loc4 = 1
                                            DostPersone.append('Механический')
                                    elif loc3 == 0:
                                        print("Вам выпала: Структурная")
                                        loc3 = 1
                                        DostPersone.append('Структурная')
                                        magpok3 = 0
                                elif loc2 == 0:
                                    print("Вам выпал: Структурный")
                                    loc2 = 1
                                    DostPersone.append('Структурный')
                                    magpok2 = 0
                            elif loc1 == 0:
                                print("Вам выпал: AD1")
                                loc1 = 1
                                DostPersone.append('AD1')
                                magpok1 = 0
                        elif rrenLBox == 7:
                            if loc1 == 1:
                                if loc2 == 1:
                                    if loc3 == 1:
                                        if loc4 == 1:
                                            if loc5 == 1:
                                                if loc6 == 1:
                                                    if loc7 == 1:
                                                        print("Вам выпало: ❇️ 675 изумрудов ❇️")
                                                        emeralds += 675
                                                    elif loc7 == 0:
                                                        print("Вам выпал: Кубер")
                                                        loc7 = 1
                                                        DostPersone.append('Кубер')
                                                elif loc6 == 0:
                                                    print("Вам выпал: Тень")
                                                    loc6 = 1
                                                    DostPersone.append('Тень')
                                            elif loc5 == 0:
                                                print("Вам выпал: Нулевой")
                                                loc5 = 1
                                                DostPersone.append('Нулевой')
                                        elif loc4 == 0:
                                            print("Вам выпал: Механический")
                                            loc4 = 1
                                            DostPersone.append('Механический')
                                    elif loc3 == 0:
                                        print("Вам выпала: Структурная")
                                        loc3 = 1
                                        DostPersone.append('Структурная')
                                        magpok3 = 0
                                elif loc2 == 0:
                                    print("Вам выпал: Структурный")
                                    loc2 = 1
                                    DostPersone.append('Структурный')
                                    magpok2 = 0
                            elif loc1 == 0:
                                print("Вам выпал: AD1")
                                loc1 = 1
                                DostPersone.append('AD1')
                                magpok1 = 0
                        elif rrenLBox == 8:
                            print("Вам выпало: ❇️ 100 изумрудов ❇️")
                            emeralds += 100
                        elif rrenLBox == 9:
                            print("Вам выпало: ❇️ 240 изумрудов ❇️")
                            emeralds += 240
                        elif rrenLBox == 10:
                            print("Вам выпало: ❇️ 1375 изумрудов ❇️")
                            emeralds += 1375
                        elif rrenLBox == 11:
                            print("Вам выпало: ❇️ 240 изумрудов ❇️")
                            emeralds += 240
                        elif rrenLBox == 12:
                            print("Вам выпало: ❇️ 160 изумрудов ❇️")
                            emeralds += 160
                        elif rrenLBox == 13:
                            print("Вам выпало: ❇️ 400 изумрудов ❇️")
                            emeralds += 400
                        elif rrenLBox == 14:
                            print("Вам выпало: ❇️ 240 изумрудов ❇️")
                            emeralds += 240
                        elif rrenLBox == 15:
                            if loc1 == 1:
                                if loc2 == 1:
                                    if loc3 == 1:
                                        if loc4 == 1:
                                            if loc5 == 1:
                                                if loc6 == 1:
                                                    if loc7 == 1:
                                                        print("Вам выпало: ❇️ 985 изумрудов ❇️")
                                                        emeralds += 985
                                                    elif loc7 == 0:
                                                        print("Вам выпал: Кубер")
                                                        loc7 = 1
                                                        DostPersone.append('Кубер')
                                                elif loc6 == 0:
                                                    print("Вам выпал: Тень")
                                                    loc6 = 1
                                                    DostPersone.append('Тень')
                                            elif loc5 == 0:
                                                print("Вам выпал: Нулевой")
                                                loc5 = 1
                                                DostPersone.append('Нулевой')
                                        elif loc4 == 0:
                                            print("Вам выпал: Механический")
                                            loc4 = 1
                                            DostPersone.append('Механический')
                                    elif loc3 == 0:
                                        print("Вам выпала: Структурная")
                                        loc3 = 1
                                        DostPersone.append('Структурная')
                                        magpok3 = 0
                                elif loc2 == 0:
                                    print("Вам выпал: Структурный")
                                    loc2 = 1
                                    DostPersone.append('Структурный')
                                    magpok2 = 0
                            elif loc1 == 0:
                                print("Вам выпал: AD1")
                                loc1 = 1
                                DostPersone.append('AD1')
                                magpok1 = 0
                        else:
                            print("ошибка")
                            emeralds += 200
                    else:
                        print("У вас нету этих ящиков")
            elif openBox == "нет":
                print("Ок")
        elif menu == "промокоды":
            print("Введите промокод если он у вас есть:")
            prom = input()
            if prom == "free23":
                if free23 == 0:
                    print("Вы получили: ❇️ 2023 изумруда ❇️")
                    emeralds += 2023
                    free23 += 1
                else:
                    print("Вы уже активировали данный промокод!")
            elif prom == "HALVA_VC":
                if HALVA_VC == 0:
                    print("Вы получили: ❇️ 500 изумрудов ❇️")
                    emeralds += 500
                    HALVA_VC += 1
                else:
                    print("Вы уже активировали данный промокод!")
            elif prom == "lapota":
                if lapota == 0:
                    print("Вы получили: ❇️ 5000 изумрудов ❇️")
                    emeralds += 5000
                    lapota += 1
                else:
                    print("Вы уже активировали данный промокод!")
            elif prom == kode_mini_plysh:
                print("Вы успешно активировали данный ключ!")
            else:
                print("Данного промокода несуществует!")
        elif menu == "лидеры":
            print("Какой из списков лидеров вы хотите увидеть: по 'изумрудам', 'уровню' профиля, количеству 'трофеев'?")
            lidspv = input()
            if lidspv == "изумрудам":
                remesting()
            elif lidspv == "уровню":
                remestingpy()
            elif lidspv == "трофеев":
                remestingpt()
        elif menu == "/":
            if ADMINPRAV == 9896:
                print("Все команды: /em [set, add, dell] [5, 7, 10, 20, 50, 100, 200, 500, 1000, 5000],"
                      " /lbox , /pbox , /yp , /trof , /nam , /plysh")
                comandexpi = input()
                print("comandexpi =", comandexpi)
                if comandexpi == "/plysh":
                    print(kode_mini_plysh)
                elif comandexpi == "/em set 5":
                    emeralds = 5
                elif comandexpi == "/em set 7":
                    emeralds = 7
                elif comandexpi == "/em set 10":
                    emeralds = 10
                elif comandexpi == "/em set 20":
                    emeralds = 20
                elif comandexpi == "/em set 50":
                    emeralds = 50
                elif comandexpi == "/em set 100":
                    emeralds = 100
                elif comandexpi == "/em set 200":
                    emeralds = 200
                elif comandexpi == "/em set 500":
                    emeralds = 500
                elif comandexpi == "/em set 1000":
                    emeralds = 1000
                elif comandexpi == "/em set 5000":
                    emeralds = 5000
                elif comandexpi == "/em add 5":
                    emeralds += 5
                elif comandexpi == "/em add 7":
                    emeralds += 7
                elif comandexpi == "/em add 10":
                    emeralds += 10
                elif comandexpi == "/em add 20":
                    emeralds += 20
                elif comandexpi == "/em add 50":
                    emeralds += 50
                elif comandexpi == "/em add 100":
                    emeralds += 100
                elif comandexpi == "/em add 200":
                    emeralds += 200
                elif comandexpi == "/em add 500":
                    emeralds += 500
                elif comandexpi == "/em add 1000":
                    emeralds += 1000
                elif comandexpi == "/em add 5000":
                    emeralds += 5000
                elif comandexpi == "/em dell 5":
                    emeralds -= 5
                elif comandexpi == "/em dell 7":
                    emeralds -= 7
                elif comandexpi == "/em dell 10":
                    emeralds -= 10
                elif comandexpi == "/em dell 20":
                    emeralds -= 20
                elif comandexpi == "/em dell 50":
                    emeralds -= 50
                elif comandexpi == "/em dell 100":
                    emeralds -= 100
                elif comandexpi == "/em dell 200":
                    emeralds -= 200
                elif comandexpi == "/em dell 500":
                    emeralds -= 500
                elif comandexpi == "/em dell 1000":
                    emeralds -= 1000
                elif comandexpi == "/em dell 5000":
                    emeralds -= 5000
                elif comandexpi == "/lbox":
                    LBox += int(input("Введите количество для добавления: "))
                elif comandexpi == "/pbox":
                    PBox += int(input("Введите количество для добавления: "))
                elif comandexpi == "/yp":
                    yrprof += int(input("Введите количество для добавления: "))
                elif comandexpi == "/trof":
                    trophei += int(input("Введите количество для добавления: "))
                elif comandexpi == "/nam":
                    playname = input("Введите новое имя: ")
        elif menu == "профиль":
            print("       Ваш никнейм:", playname)
            print("Ваше количество изумрудов: ❇️", emeralds, "❇️")
            print("   Ваш айди пользователя:", IdifendIp)
            print(" Ваш уровень профиля: 🎓", yrprof, "🎓")
            print("Количество ваших трофеев: 🏆", trophei, "🏆")
        elif menu == "выживание":
            if dorstkvazvaniy == 1:
                print("Простите но тут ещё не дороботанно, но по секрету скажу что там будет настоящая виживалка"
                      " и там даже будет верстак и печ с сундуком и возможно холодильник..."
                      " Всё!")
        elif menu == "играть":
            print("Игра началась!")
            if levlpl > 5:
                levlpl = 1
            print("Уровень:", levlpl)
            if levlpl == 0:
                print("Добропожаловать в обучение!")
                print("Ваша задача уничтожить npc, удачи!")
                print("🟫-это граница карты")
                print("🟩-это блок карты по которому можно перемещаться")
                print("🟥-это вражеская точка спавна")
                print("🟦-это ваша точка спавна")
                codrdinite = 6
                vsnpc = 1
                while mcikl:
                    clear()
                    if vsnpc != 0:
                        print("Ваши координаты:", codrdinite)
                        print("Карта: ")
                        pervkart()
                    if obnpc != 0:
                        print("Координаты npc:", obnpc)
                    pyt = input()
                    if pyt == "ц":
                        pyt = "w"
                    elif pyt == "в":
                        pyt = "d"
                    elif pyt == "ы":
                        pyt = "s"
                    elif pyt == "ф":
                        pyt = "a"
                    prcod = pyt
                    if vsnpc == 0:
                        print("Вы прошли обучение!")
                        print("Ваша награда: 1 легаси ящик")
                        print("              + 2 трофея")
                        trophei += 2
                        yrproff += 0.8
                        LBox += 1
                        mtik1 -= 5
                        mcikl = False
                        obnpc = 8
                        vsnpc = 1
                        if trenerigr == 0:
                            levlpl += 1
                    elif pyt == "w":
                        codrdinite += 1
                        if codrdinite == obnpc:
                            obnpc = 8
                            print("Вы уничтожили npc!")
                            vsnpc -= 1
                        elif codrdinite < 4:
                            codrdinite += 5
                            print("Вы вышли за границу зоны!")
                        elif codrdinite > 15:
                            codrdinite -= 5
                            print("Вы вышли за границу зоны!")
                        elif codrdinite == 9:
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif codrdinite == 14:
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif codrdinite == 5:
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif codrdinite == 10:
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif codrdinite == 7:
                            if prcod == "w":
                                codrdinite -= 1
                                print("Вы вышли за границу зоны!")
                            elif prcod == "s":
                                codrdinite += 1
                                print("Вы вышли за границу зоны!")
                            elif prcod == "d":
                                codrdinite -= 5
                                print("Вы вышли за границу зоны!")
                            elif prcod == "a":
                                codrdinite += 5
                                print("Вы вышли за границу зоны!")
                    elif pyt == "s":
                        codrdinite -= 1
                        if codrdinite == obnpc:
                            obnpc = 0
                            print("Вы уничтожили npc!")
                            vsnpc -= 1
                        elif codrdinite < 4:
                            codrdinite += 5
                            print("Вы вышли за границу зоны!")
                        elif codrdinite > 15:
                            codrdinite -= 5
                            print("Вы вышли за границу зоны!")
                        elif codrdinite == 9:
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif codrdinite == 14:
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif codrdinite == 5:
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif codrdinite == 10:
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif codrdinite == 7:
                            if prcod == "w":
                                codrdinite -= 1
                                print("Вы вышли за границу зоны!")
                            elif prcod == "s":
                                codrdinite += 1
                                print("Вы вышли за границу зоны!")
                            elif prcod == "d":
                                codrdinite -= 5
                                print("Вы вышли за границу зоны!")
                            elif prcod == "a":
                                codrdinite += 5
                                print("Вы вышли за границу зоны!")
                    elif pyt == "d":
                        codrdinite += 5
                        if codrdinite == obnpc:
                            obnpc = 0
                            print("Вы уничтожили npc!")
                            vsnpc -= 1
                        elif codrdinite < 4:
                            codrdinite += 5
                            print("Вы вышли за границу зоны!")
                        elif codrdinite > 15:
                            codrdinite -= 5
                            print("Вы вышли за границу зоны!")
                        elif codrdinite == 9:
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif codrdinite == 14:
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif codrdinite == 5:
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif codrdinite == 10:
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif codrdinite == 7:
                            if prcod == "w":
                                codrdinite -= 1
                                print("Вы вышли за границу зоны!")
                            elif prcod == "s":
                                codrdinite += 1
                                print("Вы вышли за границу зоны!")
                            elif prcod == "d":
                                codrdinite -= 5
                                print("Вы вышли за границу зоны!")
                            elif prcod == "a":
                                codrdinite += 5
                                print("Вы вышли за границу зоны!")
                    elif pyt == "a":
                        codrdinite -= 5
                        if codrdinite == obnpc:
                            obnpc = 0
                            print("Вы уничтожили npc!")
                            vsnpc -= 1
                        elif codrdinite < 4:
                            codrdinite += 5
                            print("Вы вышли за границу зоны!")
                        elif codrdinite > 15:
                            codrdinite -= 5
                            print("Вы вышли за границу зоны!")
                        elif codrdinite == 9:
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif codrdinite == 14:
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif codrdinite == 5:
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif codrdinite == 10:
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif codrdinite == 7:
                            if prcod == "w":
                                codrdinite -= 1
                                print("Вы вышли за границу зоны!")
                            elif prcod == "s":
                                codrdinite += 1
                                print("Вы вышли за границу зоны!")
                            elif prcod == "d":
                                codrdinite -= 5
                                print("Вы вышли за границу зоны!")
                            elif prcod == "a":
                                codrdinite += 5
                                print("Вы вышли за границу зоны!")
            elif levlpl == 1:
                codrdinite = 11
                vsnpc = 3
                syzon = -20
                npcxd = 1
                while mcikl:
                    if nuber == 1:
                        nuber -= 1
                        print("Игра окончена!")
                        if yrprof >= 40:
                            trophei -= 40
                            print("     -40 трофеев")
                        elif yrprof < 40:
                            trophei -= 4
                            print("     -4 трофея")
                        if yrprof == yrprof:
                            pyt = input()
                            lives11 = 8
                            lives12 = 20
                            lives13 = 20
                            npc11 = 18
                            npc12 = 56
                            npc13 = 62
                            if pyt == pyt:
                                mcikl = False
                    lives += 0.6
                    if lives >= pervonahallives:
                        lives = pervonahallives
                    print("Количество ваших сердец:", lives)
                    if vsnpc != 0:
                        print("Карта: ")
                        wonekart()
                        # print("🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫")
                        # print("🟫🟥🟩🟩🟩🟩🟩🟫🟩🟫")
                        # print("🟫🟫🟫🟫🟩🟩🟩🟩🟩🟫")
                        # print("🟫🟩🟩🟩🟫🟥🟩🟩🟩🟫")
                        # print("🟫🟩🟩🟩🟫🟩🟩🟩🟫🟫")
                        # print("🟫🟩🟫🟩🟩🟩🟩🟩🟫🟫")
                        # print("🟫🟩🟫🟩🟩🟩🟩🟩🟩🟫")
                        # print("🟫🟩🟫🟫🟩🟩🟥🟩🟩🟫")
                        # print("🟫🟦🟩🟩🟩🟩🟫🟩🟩🟫")
                        # print("🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫")
                    if codrdinite == npc11:
                        print("Сражение с AD1!")
                        lives -= 17
                        lives11 -= Weapon
                        if lives11 <= 0:
                            print("AD1 повержен!")
                            npc11 = 0
                        elif lives <= 0:
                            print("Вы проиграли!")
                            nuber = 1
                    if codrdinite == npc12:
                        print("Сражение со Структурной(1)!")
                        lives -= 5
                        lives12 -= Weapon
                        if lives12 <= 0:
                            print("Структурная(1) повержена!")
                            npc12 = 0
                        elif lives <= 0:
                            print("Вы проиграли!")
                            nuber = 1
                    if codrdinite == npc13:
                        print("Сражение со Структурной(2)!")
                        lives -= 5
                        lives13 -= Weapon
                        if lives13 <= 0:
                            print("Структурная(2) повержена!")
                            npc13 = 0
                        elif lives <= 0:
                            print("Вы проиграли!")
                            nuber = 1
                    if vsnpc != 0:
                        if npc11 != 0:
                            print("Координаты 1 npc:", npc11)
                        if npc12 != 0:
                            print("Координаты 2 npc:", npc12)
                        if npc13 != 0:
                            print("Координаты 3 npc:", npc13)
                    if vsnpc != 0:
                        print("Ваши координаты:", codrdinite)
                    pyt = input()
                    if pyt == "ц":
                        pyt = "w"
                    elif pyt == "в":
                        pyt = "d"
                    elif pyt == "ы":
                        pyt = "s"
                    elif pyt == "ф":
                        pyt = "a"
                    prcod = pyt
                    if vsnpc == 0:
                        print("Вы прошли этот уровень!")
                        print("Ваша награда: 1 простой ящик")
                        print("              + 6 трофеев")
                        yrproff += 0.4
                        trophei += 6
                        yrprod += 1
                        PBox += 1
                        mtik1 -= 5
                        mcikl = False
                    elif codrdinite <= 10:
                        if prcod == "w":
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "s":
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "d":
                            codrdinite -= 5
                            print("Вы вышли за границу зоны!")
                        elif prcod == "a":
                            codrdinite += 5
                            print("Вы вышли за границу зоны!")
                    elif codrdinite >= 89:
                        if prcod == "w":
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "s":
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "d":
                            codrdinite -= 5
                            print("Вы вышли за границу зоны!")
                        elif prcod == "a":
                            codrdinite += 5
                            print("Вы вышли за границу зоны!")
                    elif codrdinite == 79:
                        if prcod == "w":
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "s":
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "d":
                            codrdinite -= 5
                            print("Вы вышли за границу зоны!")
                        elif prcod == "a":
                            codrdinite += 5
                            print("Вы вышли за границу зоны!")
                    elif codrdinite == 69:
                        if prcod == "w":
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "s":
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "d":
                            codrdinite -= 5
                            print("Вы вышли за границу зоны!")
                        elif prcod == "a":
                            codrdinite += 5
                            print("Вы вышли за границу зоны!")
                    elif codrdinite == 59:
                        if prcod == "w":
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "s":
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "d":
                            codrdinite -= 5
                            print("Вы вышли за границу зоны!")
                        elif prcod == "a":
                            codrdinite += 5
                            print("Вы вышли за границу зоны!")
                    elif codrdinite == 49:
                        if prcod == "w":
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "s":
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "d":
                            codrdinite -= 5
                            print("Вы вышли за границу зоны!")
                        elif prcod == "a":
                            codrdinite += 5
                            print("Вы вышли за границу зоны!")
                    elif codrdinite == 39:
                        if prcod == "w":
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "s":
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "d":
                            codrdinite -= 5
                            print("Вы вышли за границу зоны!")
                        elif prcod == "a":
                            codrdinite += 5
                            print("Вы вышли за границу зоны!")
                    elif codrdinite == 29:
                        if prcod == "w":
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "s":
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "d":
                            codrdinite -= 5
                            print("Вы вышли за границу зоны!")
                        elif prcod == "a":
                            codrdinite += 5
                            print("Вы вышли за границу зоны!")
                    elif codrdinite == 19:
                        if prcod == "w":
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "s":
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "d":
                            codrdinite -= 5
                            print("Вы вышли за границу зоны!")
                        elif prcod == "a":
                            codrdinite += 5
                            print("Вы вышли за границу зоны!")
                    elif codrdinite == 20:
                        if prcod == "w":
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "s":
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "d":
                            codrdinite -= 5
                            print("Вы вышли за границу зоны!")
                        elif prcod == "a":
                            codrdinite += 5
                            print("Вы вышли за границу зоны!")
                    elif codrdinite == 30:
                        if prcod == "w":
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "s":
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "d":
                            codrdinite -= 5
                            print("Вы вышли за границу зоны!")
                        elif prcod == "a":
                            codrdinite += 5
                            print("Вы вышли за границу зоны!")
                    elif codrdinite == 40:
                        if prcod == "w":
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "s":
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "d":
                            codrdinite -= 5
                            print("Вы вышли за границу зоны!")
                        elif prcod == "a":
                            codrdinite += 5
                            print("Вы вышли за границу зоны!")
                    elif codrdinite == 50:
                        if prcod == "w":
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "s":
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "d":
                            codrdinite -= 5
                            print("Вы вышли за границу зоны!")
                        elif prcod == "a":
                            codrdinite += 5
                            print("Вы вышли за границу зоны!")
                    elif codrdinite == 60:
                        if prcod == "w":
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "s":
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "d":
                            codrdinite -= 5
                            print("Вы вышли за границу зоны!")
                        elif prcod == "a":
                            codrdinite += 5
                            print("Вы вышли за границу зоны!")
                    elif codrdinite == 70:
                        if prcod == "w":
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "s":
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "d":
                            codrdinite -= 5
                            print("Вы вышли за границу зоны!")
                        elif prcod == "a":
                            codrdinite += 5
                            print("Вы вышли за границу зоны!")
                    elif codrdinite == 80:
                        if prcod == "w":
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "s":
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "d":
                            codrdinite -= 5
                            print("Вы вышли за границу зоны!")
                        elif prcod == "a":
                            codrdinite += 5
                            print("Вы вышли за границу зоны!")
                    elif codrdinite == 84:
                        if prcod == "w":
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "s":
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "d":
                            codrdinite -= 5
                            print("Вы вышли за границу зоны!")
                        elif prcod == "a":
                            codrdinite += 5
                            print("Вы вышли за границу зоны!")
                    elif codrdinite == 85:
                        if prcod == "w":
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "s":
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "d":
                            codrdinite -= 5
                            print("Вы вышли за границу зоны!")
                        elif prcod == "a":
                            codrdinite += 5
                            print("Вы вышли за границу зоны!")
                    elif codrdinite == 61:
                        if prcod == "w":
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "s":
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "d":
                            codrdinite -= 5
                            print("Вы вышли за границу зоны!")
                        elif prcod == "a":
                            codrdinite += 5
                            print("Вы вышли за границу зоны!")
                    elif codrdinite == 78:
                        if prcod == "w":
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "s":
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "d":
                            codrdinite -= 5
                            print("Вы вышли за границу зоны!")
                        elif prcod == "a":
                            codrdinite += 5
                            print("Вы вышли за границу зоны!")
                    elif codrdinite == 45:
                        if prcod == "w":
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "s":
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "d":
                            codrdinite -= 5
                            print("Вы вышли за границу зоны!")
                        elif prcod == "a":
                            codrdinite += 5
                            print("Вы вышли за границу зоны!")
                    elif codrdinite == 46:
                        if prcod == "w":
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "s":
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "d":
                            codrdinite -= 5
                            print("Вы вышли за границу зоны!")
                        elif prcod == "a":
                            codrdinite += 5
                            print("Вы вышли за границу зоны!")
                    elif codrdinite == 32:
                        if prcod == "w":
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "s":
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "d":
                            codrdinite -= 5
                            print("Вы вышли за границу зоны!")
                        elif prcod == "a":
                            codrdinite += 5
                            print("Вы вышли за границу зоны!")
                    elif codrdinite == 37:
                        if prcod == "w":
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "s":
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "d":
                            codrdinite -= 5
                            print("Вы вышли за границу зоны!")
                        elif prcod == "a":
                            codrdinite += 5
                            print("Вы вышли за границу зоны!")
                    elif codrdinite == 22:
                        if prcod == "w":
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "s":
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "d":
                            codrdinite -= 5
                            print("Вы вышли за границу зоны!")
                        elif prcod == "a":
                            codrdinite += 5
                            print("Вы вышли за границу зоны!")
                    elif codrdinite == 23:
                        if prcod == "w":
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "s":
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "d":
                            codrdinite -= 5
                            print("Вы вышли за границу зоны!")
                        elif prcod == "a":
                            codrdinite += 5
                            print("Вы вышли за границу зоны!")
                    elif codrdinite == 24:
                        if prcod == "w":
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "s":
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "d":
                            codrdinite -= 5
                            print("Вы вышли за границу зоны!")
                        elif prcod == "a":
                            codrdinite += 5
                            print("Вы вышли за границу зоны!")
                    elif codrdinite == 27:
                        if prcod == "w":
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "s":
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "d":
                            codrdinite -= 5
                            print("Вы вышли за границу зоны!")
                        elif prcod == "a":
                            codrdinite += 5
                            print("Вы вышли за границу зоны!")
                    elif codrdinite == 17:
                        if prcod == "w":
                            codrdinite -= 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "s":
                            codrdinite += 1
                            print("Вы вышли за границу зоны!")
                        elif prcod == "d":
                            codrdinite -= 5
                            print("Вы вышли за границу зоны!")
                        elif prcod == "a":
                            codrdinite += 5
                            print("Вы вышли за границу зоны!")
                    elif pyt == "w":
                        codrdinite += 1
                    elif pyt == "s":
                        codrdinite -= 1
                    elif pyt == "d":
                        codrdinite += 10
                    elif pyt == "a":
                        codrdinite -= 10
                    # print("🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫")
                    # print("🟫🟥🟩🟩🟩🟩🟩🟫🟩🟫")
                    # print("🟫🟫🟫🟫🟩🟩🟩🟩🟩🟫")
                    # print("🟫🟩🟩🟩🟫🟥🟩🟩🟩🟫")
                    # print("🟫🟩🟩🟩🟫🟩🟩🟩🟫🟫")
                    # print("🟫🟩🟫🟩🟩🟩🟩🟩🟫🟫")
                    # print("🟫🟩🟫🟩🟩🟩🟩🟩🟩🟫")
                    # print("🟫🟩🟫🟫🟩🟩🟥🟩🟩🟫")
                    # print("🟫🟦🟩🟩🟩🟩🟫🟩🟩🟫")
                    # print("🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫")
                    if npcxd == 9:
                        if npc11 != 0:
                            npc11 = 28
                        if npc12 != 0:
                            npc12 = 55
                        if npc13 != 0:
                            npc13 = 52
                        if npcxd == npcxd:
                            npcxd = 0
                    if npcxd == 8:
                        if npc11 != 0:
                            npc11 = 38
                        if npc12 != 0:
                            npc12 = 54
                        if npc13 != 0:
                            npc13 = 42
                        if npcxd == npcxd:
                            npcxd += 1
                    if npcxd == 7:
                        if npc11 != 0:
                            npc11 = 48
                        if npc12 != 0:
                            npc12 = 44
                        if npc13 != 0:
                            npc13 = 52
                        if npcxd == npcxd:
                            npcxd += 1
                    if npcxd == 6:
                        if npc11 != 0:
                            npc11 = 58
                        if npc12 != 0:
                            npc12 = 43
                        if npc13 != 0:
                            npc13 = 53
                        if npcxd == npcxd:
                            npcxd += 1
                    if npcxd == 5:
                        if npc11 != 0:
                            npc11 = 57
                        if npc12 != 0:
                            npc12 = 53
                        if npc13 != 0:
                            npc13 = 54
                        if npcxd == npcxd:
                            npcxd += 1
                    if npcxd == 4:
                        if npc11 != 0:
                            npc11 = 58
                        if npc12 != 0:
                            npc12 = 43
                        if npc13 != 0:
                            npc13 = 53
                        if npcxd == npcxd:
                            npcxd += 1
                    if npcxd == 3:
                        if npc11 != 0:
                            npc11 = 48
                        if npc12 != 0:
                            npc12 = 44
                        if npc13 != 0:
                            npc13 = 52
                        if npcxd == npcxd:
                            npcxd += 1
                    if npcxd == 2:
                        if npc11 != 0:
                            npc11 = 38
                        if npc12 != 0:
                            npc12 = 54
                        if npc13 != 0:
                            npc13 = 42
                        if npcxd == npcxd:
                            npcxd += 1
                    if npcxd == 1:
                        if npc11 != 0:
                            npc11 = 28
                        if npc12 != 0:
                            npc12 = 55
                        if npc13 != 0:
                            npc13 = 52
                        if npcxd == npcxd:
                            npcxd += 1
                    if npcxd == 0:
                        npcxd += 1
