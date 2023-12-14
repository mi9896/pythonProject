import json

poldeptopF = {}


def load():
    global poldeptopF
    with open("poldeptopF.json", "r", encoding="utf-8") as f:
        poldeptopF = json.load(f)


def save():
    global poldeptopF
    with open("poldeptopF.json", "w", encoding="utf-8") as nocayt:
        json.dump(poldeptopF, nocayt)


load()


em1 = poldeptopF.get("em1", 234098)
em2 = poldeptopF.get("em2", 41950)
em3 = poldeptopF.get("em3", 16998)
yp1 = poldeptopF.get("yp1", 97)
yp2 = poldeptopF.get("yp2", 45)
yp3 = poldeptopF.get("yp3", 35)
tr1 = poldeptopF.get("tr1", 32983)
tr2 = poldeptopF.get("tr2", 9998)
tr3 = poldeptopF.get("tr3", 7899)
vin1 = poldeptopF.get("vin1", "🥇")
vin2 = poldeptopF.get("vin2", "🥈")
vin3 = poldeptopF.get("vin3", "🥉")
mes1 = poldeptopF.get("mes1", "   1-")
mes2 = poldeptopF.get("mes2", "   2-")
mes3 = poldeptopF.get("mes3", "   3-")

MEST1 = poldeptopF.get("MEST1", "mi9896")
MEST2 = poldeptopF.get("MEST2", "Сенсей")
MEST3 = poldeptopF.get("MEST3", "дероево")

MEST1_1 = poldeptopF.get("MEST1_1", "❇️ кол.изумрудов: 234098 ❇️ ID: MM9-F89-6MPL-wMY-7")
MEST2_2 = poldeptopF.get("MEST2_2", "❇️ кол.изумрудов: 41950 ❇️ ID: HM5-L50-3LuD-LJm-2")
MEST3_3 = poldeptopF.get("MEST3_3", "❇️ кол.изумрудов: 16998 ❇️ ID: qH6-E26-9cwY-wct-4")

MESTPY1 = poldeptopF.get("MESTPY1", "mi9896")
MESTPY2 = poldeptopF.get("MESTPY2", "Сенсей")
MESTPY3 = poldeptopF.get("MESTPY3", "дероево")

MESTPY1_1 = poldeptopF.get("MESTPY1_1", "🎓 Уровень профиля: 97 🎓 ID: MM9-F89-6MPL-wMY-7")
MESTPY2_2 = poldeptopF.get("MESTPY2_2", "🎓 Уровень профиля: 45 🎓 ID: HM5-L50-3LuD-LJm-2")
MESTPY3_3 = poldeptopF.get("MESTPY3_3", "🎓 Уровень профиля: 35 🎓 ID: qH6-E26-9cwY-wct-4")

MESTPT1 = poldeptopF.get("MESTPT1", "mi9896")
MESTPT2 = poldeptopF.get("MESTPT2", "Сенсей")
MESTPT3 = poldeptopF.get("MESTPT3", "неомелей")

MESTPT1_1 = poldeptopF.get("MESTPT1_1", "🏆 Количество трофеев: 32983 🏆 ID: MM9-F89-6MPL-wMY-7")
MESTPT2_2 = poldeptopF.get("MESTPT2_2", "🏆 Количество трофеев: 9998 🏆 ID: HM5-L50-3LuD-LJm-2")
MESTPT3_3 = poldeptopF.get("MESTPT3_3", "🏆 Количество трофеев: 7899 🏆 ID: YE3-P35-6utL-woI-3")


renPBox = poldeptopF.get("renPBox", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
renLBox = poldeptopF.get("renLBox", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
codrdinite = poldeptopF.get("codrdinite", 0)
signature = poldeptopF.get("signature", "mi97-98lo-g011-rim6")
persona = poldeptopF.get("persona", 1)
Weapon = poldeptopF.get("Weapon", 5)
lives = poldeptopF.get("lives", 12)
pervonahalWeapon = poldeptopF.get("pervonahalWeapon", 5)
pervonahallives = poldeptopF.get("pervonahallives", 12)


# Игра только на обучении = 1
# Игра только на обучении = 1
trenerigr = poldeptopF.get("trenerigr", 1)
# Игра нетолько на обучении = 0
# Игра нетолько на обучении = 0


yrprod = poldeptopF.get("yrprod", 0)
lives11 = poldeptopF.get("lives11", 8)
lives12 = poldeptopF.get("lives12", 20)
lives13 = poldeptopF.get("lives13", 20)
npc11 = poldeptopF.get("npc11", 18)
npc12 = poldeptopF.get("npc12", 56)
npc13 = poldeptopF.get("npc13", 62)

# НЕ ТРОГАТЬ
# НЕ ТРОГАТЬ
ADMINPRAV = poldeptopF.get("ADMINPRAV", 9896)
# НЕ ТРОГАТЬ
# НЕ ТРОГАТЬ

npcxd = poldeptopF.get("npcxd", 0)
loc1 = poldeptopF.get("loc1", 0)
loc2 = poldeptopF.get("loc2", 0)
loc3 = poldeptopF.get("loc3", 0)
loc4 = poldeptopF.get("loc4", 0)
loc5 = poldeptopF.get("loc5", 0)
loc6 = poldeptopF.get("loc6", 0)
loc7 = poldeptopF.get("loc7", 0)
lispv = poldeptopF.get("lispv", 0)
MAXtrophei = poldeptopF.get("MAXtrophei", 0)
trophei = poldeptopF.get("trophei", 0)
yrproff = poldeptopF.get("yrproff", 0)
yrprof = poldeptopF.get("yrprof", 0)
mtik1 = poldeptopF.get("mtik1", 10)
mtik10 = poldeptopF.get("mtik10", 10)
magz = poldeptopF.get("magz", 0)
emeralds = poldeptopF.get("emeralds", 100)
rrenLBox = poldeptopF.get("rrenLBox", 1)
rrenPBox = poldeptopF.get("rrenPBox", 10)
DostPersone = poldeptopF.get("DostPersone", ["Путник"])
NeDostPersone = poldeptopF.get("NeDostPersone", ["Путник", "AD1", "Структурный", "Структурная", "Механический", "Нулевой", "Тень", "Кубер"])
namnem = poldeptopF.get("namnem", 0)
magpok1 = poldeptopF.get("magpok1", 1)
magpok2 = poldeptopF.get("magpok2", 1)
magpok3 = poldeptopF.get("magpok3", 1)
obnpc = poldeptopF.get("obnpc", 8)
PBox = poldeptopF.get("PBox", 0)
LBox = poldeptopF.get("LBox", 0)
levlpl = poldeptopF.get("levlpl", 0)
prcod = poldeptopF.get("prcod", 0)
nuber = poldeptopF.get("nuber", 0)
omer = poldeptopF.get("omer", 0)
omerdos = poldeptopF.get("omerdos", 0)
dost = poldeptopF.get("dost", [1, 0])
pololv = poldeptopF.get("pololv", 3)
polol = poldeptopF.get("polol", True)
poroli1 = poldeptopF.get("poroli1", "7011")
poroli2 = poldeptopF.get("poroli2", "0017")
poroli3 = poldeptopF.get("poroli3", "5648")
playname = poldeptopF.get("playname", "nyli")
dorstkvazvaniy = poldeptopF.get("dorstkvazvaniy", 0)
prom = poldeptopF.get("prom", "")
menu = poldeptopF.get("menu", "")
comandexpi = poldeptopF.get("comandexpi", "")
sobp = ""


# ограниченое количество символов имени
name_reg = poldeptopF.get("", True)
nam_sim = poldeptopF.get("", 1)
# ограниченое количество символов имени

# фукции:
# мини-плюшка!
kode_mini_plysh = poldeptopF.get("kode_mini_plysh", "")
kode_mini_plysh1 = poldeptopF.get("kode_mini_plysh1", "")
kode_mini_plysh2 = poldeptopF.get("kode_mini_plysh2", "")
kode_mini_plysh3 = poldeptopF.get("kode_mini_plysh3", "")
kode_mini_plysh4 = poldeptopF.get("kode_mini_plysh4", "")
kode_mini_plysh5 = poldeptopF.get("kode_mini_plysh5", "")
kode_mini_plysh6 = poldeptopF.get("kode_mini_plysh6", "")
mipl6 = poldeptopF.get("mipl6", 0)
mipl5 = poldeptopF.get("mipl5", 0)
mipl4 = poldeptopF.get("mipl4", 0)
mipl3 = poldeptopF.get("mipl3", 0)
mipl2 = poldeptopF.get("mipl2", 0)
mipl1 = poldeptopF.get("mipl1", 0)
mipl = poldeptopF.get("mipl", 0)
# мини-плюшка!
# фукции:

# Поддержка карты:
go_player_minimap_ob = poldeptopF.get("go_player_minimap_ob", 0)
go_player_minimap_ob_st6 = poldeptopF.get("go_player_minimap_ob_st6", "")
go_player_minimap_ob_st11 = poldeptopF.get("go_player_minimap_ob_st11", "")
go_player_minimap_ob_st12 = poldeptopF.get("go_player_minimap_ob_st12", "")
go_player_minimap_ob_st13 = poldeptopF.get("go_player_minimap_ob_st13", "")
go_player_minimap_ob_st8 = poldeptopF.get("go_player_minimap_ob_st8", "")
# Поддержка карты:


# while mcikl:
#     print(codrdinite)
#     pyt = input()
#     if pyt == "w":
#         codrdinite += 1
#
#     if pyt == "s":
#         codrdinite -= 1
#
#     if pyt == "d":
#         codrdinite += 10
#
#     if pyt == "a":
#         codrdinite -= 10
free23 = poldeptopF.get("free23", 0)
HALVA_VC = poldeptopF.get("HALVA_VC", 0)
lapota = poldeptopF.get("lapota", 0)
version = poldeptopF.get("version", "1.6.0-A")
# free23
# HALVA_VC
# lapota
