#Created by  Md Jisan.  tg @Jisan7509


import random, re
import asyncio
from telethon import events
from userbot.utils import mellow_cmd
from platform import uname
from userbot import ALIVE_NAME


A = ("⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣠⣤⣶⣶\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢰⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⣀⣾⣿⣿⣿⣿\n"
"⣿⡏⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁⠀⣿\n"
"⣿⣿⣧⡀⠀⠀⠀⠀⠙⠿⠿⠻⠿⠟⠿⠛⠉⠀⠀⠀⠀⠀⣸⣿\n"
"⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿\n"
"⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⡟⠀⠀⢰⣹⡆⠀⠀⠀⠀⠀⠀⣭⣷⠀⠀⠸⣿⣿⣿\n"
"⣿⣿⣿⣿⠃⠀⠀⠈⠉⠀⠀⠀⠤⠄⠀⠀⠉⠁⠀⠀⠀⢿⣿⣿\n"
"⣿⣿⣿⣿⠀⢾⣿⣷⠀⠀⠀⠀⡠⠤⢄⠀⠀⠠⣿⣿⣷⠀⣿⣿\n"
"⣿⣿⣿⣿⡀⠀⠉⠀⠀⠀⠀⠀⢄⠀⢀⠀⠀⠀⠉⠉⠁⠀⣿⣿\n"
"⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿\n"
"⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿\n"
"⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿\n"
"⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿🅼🅰️ 🅺🅸 🅲🅷🆄⢸⣿⣿⣿⣿⣿⣿\n"
"🅿️🅸🅺🅰️ 🅿️🅸🅺🅰️ 🅿️🅸🅺🅰️🅲🅷🆄\n")


B = ("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
"⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⡀⠀⠀⠀⠀⠀⠀\n"
"⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀\n"
"⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⠟⠀⠀⠀⠀⠀⠀\n"
"⠀⠀⠀⠀⠀⠀⠀⠘⠻⣿⣷⣄⠀⠀⠀⠀⠀\n"
"⠀⠀⠀⠀⣴⣶⣿⡆⠀⠀⠉⠉⠀⠈⣶⡆⠀\n"
"⠀⠀⠀⢠⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⢻⣷⠀\n"
"⠀⠀⠀⣼⣿⡿⠟⠀⠀⠀⠀⠀⠀⠀⣸⣿⡄\n"
"⠀⠀⠀⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣷\n"
"⠀⠀⠘⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⢰⣾⣿⠏\n"
"⠀⢠⣧⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠟⠁⠀\n"
"⠀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ Ah\n shit, here we go again.\n")


C = ("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
"⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀\n"
"⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀\n"
"⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀\n"
"⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀\n"
"⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀\n"
"⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦\n"
"⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟\n"
"⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n"
"⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇\n"
"⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇\n"
"⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀\n"
"⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀\n"
"⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀\n"
"⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀\n"
"⠄⠄⠄⠄⠄⠄⣠⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡄⠄⠄⠄\n"
"⠄⠄⣀⣤⣴⣾⣿⣷⣭⣭⣭⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠄⠄\n"
"⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⣿⣧⠄⠄\n"
"⠄⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢻⣿⣿⡄⠄\n"
"⠄⢸⣿⣮⣿⣿⣿⣿⣿⣿⣿⡟⢹⣿⣿⣿⡟⢛⢻⣷⢻⣿⣧⠄\n"
"⠄⠄⣿⡏⣿⡟⡛⢻⣿⣿⣿⣿⠸⣿⣿⣿⣷⣬⣼⣿⢸⣿⣿⠄\n"
"⠄⠄⣿⣧⢿⣧⣥⣾⣿⣿⣿⡟⣴⣝⠿⣿⣿⣿⠿⣫⣾⣿⣿⡆\n"
"⠄⠄⢸⣿⣮⡻⠿⣿⠿⣟⣫⣾⣿⣿⣿⣷⣶⣾⣿⡏⣿⣿⣿⡇\n"
"⠄⠄⢸⣿⣿⣿⡇⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣿⣿⣿⡇\n"
"⠄⠄⢸⣿⣿⣿⡇⠄⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⠄\n"
"⠄⠄⣼⣿⣿⣿⢃⣾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣿⣿⡇⠄\n"
"⠄⠄⠸⣿⣿⢣⢶⣟⣿⣖⣿⣷⣻⣮⡿⣽⣿⣻⣖⣶⣤⣭⡉⠄\n"
"⠄⠄⠄⢹⠣⣛⣣⣭⣁⡛⠻⢽⣿⣿⣿⣿⢻⣿⣿⣿⣽⡧⡄⠄\n"
"⠄⠄⠄⠄⣼⣿⣿⣿⣿⣿⣿⣶⣌⡛⢿⣽⢘⣿⣷⣿⡻⠏⣛⣀\n"
"⠄⠄⠄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠙⡅⣿⠚⣡⣴⣿⣿⡆\n"
"⠄⠄⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠄⣱⣾⣿⣿⣿⣿⣿\n"
"⠄⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿\n"
"⠄⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠣⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠑⣿⣮⣝⣛⠿⠿⣿⣿⣿\n"
"⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⡟\n"
"⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠄⠄⠄⠄⢹⣿⣿⣿⣿⣿⣿⣿⡟\n"
"⣸⣿⣿⣿⣿⣿⣿⣿⣿⠏⠄⠄⠄⠄⠄⠸⣿⣿⣿⣿⡿⢟⣣\n"
"ɮǟȶǟʊ ȶɦǟʀӄɨօ ӄʏǟ ɦǟǟʟ ,ӄɛֆǟ ʟǟɢǟ\n")


D = ("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣧⣤⣤⠀⢠⣤⡄⢸⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⣿   ⠸⠿⠇⢸⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⠿⠷⣤⣀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡏⢀⣤⣤⡀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡇⠘⠿⠿⠃⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡿⠦⠤⠤⠴⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣧⣤⣤⣄⡀   ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣇⣀⣀⣀⡀   ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠟⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣧⣤⣤⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⠉⠉⢉⣉⣉⣉⣉⣉⣉⡉⠉⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⠀⠀⠻⠿⠿⠿⣿⡿⠿⠇⠀⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⠀⠀⣤⣤⣤⣤⣾⡇⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⠀⠀⢉⣩⣭⣭⣭⡄⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⠀⠀⣿⡟⠋⠉⠋⠁⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⠀⠀⣾⣿⣶⣶⣶⡆⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⠀⠀⣶⣶⣶⣶⣶⣶⣶⡆⠀⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⠀⠀⣾⣏⠀⠀⣹⡇⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⠀⠀⠘⠿⠿⠿⠟⠃⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n")


E = ("⠀⠀⠀⠀⢀⣀⣀⣀\n"
"⠀⠀⠀⠰⡿⠿⠛⠛⠻⠿⣷\n"
"⠀⠀⠀⠀⠀⠀⣀⣄⡀⠀⠀⠀⠀⢀⣀⣀⣤⣄⣀⡀\n"
"⠀⠀⠀⠀⠀⢸⣿⣿⣷⠀⠀⠀⠀⠛⠛⣿⣿⣿⡛⠿⠷\n"
"⠀⠀⠀⠀⠀⠘⠿⠿⠋⠀⠀⠀⠀⠀⠀⣿⣿⣿⠇\n"
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁\n"
"⠀\n"
"⠀⠀⠀⠀⣿⣷⣄⠀⢶⣶⣷⣶⣶⣤⣀\n"
"⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠈⠙⠻⠗\n"
"⠀⠀⠀⣰⣿⣿⣿⠀⠀⠀⠀⢀⣀⣠⣤⣴⣶⡄\n"
"⠀⣠⣾⣿⣿⣿⣥⣶⣶⣿⣿⣿⣿⣿⠿⠿⠛⠃\n"
"⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄\n"
"⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁\n"
"⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁\n"
"⠀⠀⠛⢿⣿⣿⣿⣿⣿⣿⡿⠟\n")
    

F = ("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠖⠲⢄\n"
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠞⠁⠀⠀⠀⠀⢱\n"
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠎⠀⠀⠀⠀⠀⠀⠀⣸\n"
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣄⠀⠀⠀⠀⢀⡠⠖⠁\n"
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⠁⠀⠀\n"
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣯⣿⣿⣿⣿⣿⠇⠀⠀⠀\n"
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⣻⣿⣿⣿⣿⣯⠏⠀⠀⠀⠀\n"
"⠀⠀⠀⠀⠀⠀⠀⣠⠾⣽⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀\n"
"⠀⠀⠀ ⠀⠀.⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀\n"
"⠀⠀⠀⠀⣴⣻⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀\n"
"⠀⠀⣠⢾⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
"⠀⣼⣷⣿⣿⣿⣿⣿⣿⣟⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
"⢸⢿⣿⣿⣿⣿⣿⣿⣿⣯⣻⡟⡆⠀⠀⠀⠀⠀⠀⠀⠀\n"
"⠸⣿⣿⣿⣿⣿⣿⣿⣿⣹⣿⡿⡇⠀⠀⠀⠀⠀⠀⠀⠀\n"
"⠀⠹⣟⣿⣿⣿⣿⡿⣷⡿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀\n"
"⠀⠀⠈⠛⠯⣿⡯⠟⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n")
    

G = ("⠄⠄⠄⠄⠄⣀⣀⣤⣶⣿⣿⣶⣶⣶⣤⣄⣠⣴⣶⣿⣶⣦⣄⠄\n"
"⠄⣠⣴⣾⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦\n"
"⢠⠾⣋⣭⣄⡀⠄⠙⠻⣿⣿⡿⠛⠋⠉⠉⠉⠙⠛⠿⣿⣿⣿⣿\n"
"⡎⡟⢻⣿⣷⠄⠄⠄⠄⡼⣡⣾⣿⣿⣦⠄⠄⠄⠄⠄⠈⠛⢿⣿\n"
"⡇⣷⣾⣿⠟⠄⠄⠄⢰⠁⣿⣇⣸⣿⣿⠄⠄⠄⠄⠄⠄⠄⣠⣼\n"
"⣦⣭⣭⣄⣤⣤⣴⣶⣿⣧⡘⠻⠛⠛⠁⠄⠄⠄⠄⣀⣴⣿⣿⣿\n"
"⢉⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿\n"
"⡿⠛⠛⠛⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⡇⠄⠄⢀⣀⣀⠄⠄⠄⠄⠉⠉⠛⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⠈⣆⠄⠄⢿⣿⣿⣷⣶⣶⣤⣤⣀⣀⡀⠄⠄⠉⢻⣿⣿⣿⣿⣿\n"
"⠄⣿⡀⠄⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠄⢠⣿⣿⣿⣿⣿\n"
"⠄⣿⡇⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄⢀⣼⣿⣿⣿⣿⣿\n"
"⠄⣿⡇⠄⠠⣿⣿⣿⣿⣿⣿⣿⡿⠋⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿\n"
"⠄⣿⠁⠄⠐⠛⠛⠛⠉⠉⠉⠉⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⠄⠻⣦⣀⣀⣀⣀⣀⣤⣤⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋\n")
    
    
H = ("⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣵⣿⣿⣿⠿⡟⣛⣧⣿⣯⣿⣝⡻⢿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⠋⠁⣴⣶⣿⣿⣿⣿⣿⣿⣿⣦⣍⢿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⢷⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⢼⣿⣿⣿⣿\n"
"⢹⣿⣿⢻⠎⠔⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣿⣿⣿\n"
"⢸⣿⣿⠇⡶⠄⣿⣿⠿⠟⡛⠛⠻⣿⡿⠿⠿⣿⣗⢣⣿⣿⣿⣿\n"
"⠐⣿⣿⡿⣷⣾⣿⣿⣿⣾⣶⣶⣶⣿⣁⣔⣤⣀⣼⢲⣿⣿⣿⣿\n"
"⠄⣿⣿⣿⣿⣾⣟⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⢟⣾⣿⣿⣿⣿\n"
"⠄⣟⣿⣿⣿⡷⣿⣿⣿⣿⣿⣮⣽⠛⢻⣽⣿⡇⣾⣿⣿⣿⣿⣿\n"
"⠄⢻⣿⣿⣿⡷⠻⢻⡻⣯⣝⢿⣟⣛⣛⣛⠝⢻⣿⣿⣿⣿⣿⣿\n"
"⠄⠸⣿⣿⡟⣹⣦⠄⠋⠻⢿⣶⣶⣶⡾⠃⡂⢾⣿⣿⣿⣿⣿⣿\n"
"⠄⠄⠟⠋⠄⢻⣿⣧⣲⡀⡀⠄⠉⠱⣠⣾⡇⠄⠉⠛⢿⣿⣿⣿\n"
"⠄⠄⠄⠄⠄⠈⣿⣿⣿⣷⣿⣿⢾⣾⣿⣿⣇⠄⠄⠄⠄⠄⠉⠉\n"
"⠄⠄⠄⠄⠄⠄⠸⣿⣿⠟⠃⠄⠄⢈⣻⣿⣿⠄⠄⠄⠄⠄⠄⠄\n"
"⠄⠄⠄⠄⠄⠄⠄⢿⣿⣾⣷⡄⠄⢾⣿⣿⣿⡄⠄⠄⠄⠄⠄⠄\n"
"⠄⠄⠄⠄⠄⠄⠄⠸⣿⣿⣿⠃⠄⠈⢿⣿⣿⠄⠄⠄⠄⠄⠄⠄\n")
  

I = ("⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⡇⠄⣿⣿⣿⡿⠋⣉⣉⣉⡙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⠃⠄⠹⠟⣡⣶⢟⣛⣛⡻⢿⣦⣩⣤⣬⡉⢻⣿⣿⣿⣿\n"
"⣿⣿⣿⠄⢀⢤⣾⣿⣿⣿⡿⠿⠿⠿⢮⡃⣛⡻⢿⠈⣿⣿⣿⣿\n"
"⣿⡟⢡⣴⣯⣿⣿⣿⠤⣤⣭⣶⣶⣶⣮⣔⡈⠛⢓⠦⠈⢻⣿⣿\n"
"⠏⣠⣿⣿⣿⣿⣿⣿⣯⡪⢛⠿⢿⣿⣿⣿⡿⣼⣿⣿⣮⣄⠙⣿\n"
"⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⡭⠴⣶⣶⣽⣽⣛⡿⠿⠿⠇⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣷⣝⣛⢛⢋⣥⣴⣿⣿\n"
"⣿⣿⣿⣿⣿⢿⠱⣿⣛⠾⣭⣛⡿⢿⣿⣿⣿⣿⣿⡀⣿⣿⣿⣿\n"
"⠑⠽⡻⢿⣮⣽⣷⣶⣯⣽⣳⠮⣽⣟⣲⠯⢭⣿⣛⡇⣿⣿⣿⣿\n"
"⠄⠄⠈⠑⠊⠉⠟⣻⠿⣿⣿⣿⣷⣾⣭⣿⠷⠶⠂⣴⣿⣿⣿⣿\n"
"⠄⠄⠄⠄⠄⠄⠄⠁⠙⠒⠙⠯⠍⠙⢉⣡⣶⣿⣿⣿⣿⣿⣿⣿\n"
"⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿\n")
    
    
    
J = ("⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⠉⡉⣉⡛⣛⠿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⡿⠋⠁⠄⠄⠄⠄⠄⢀⣸⣿⣿⡿⠿⡯⢙⠿⣿⣿⣿⣿\n"
"⣿⣿⡿⠄⠄⠄⠄⠄⡀⡀⠄⢀⣀⣉⣉⣉⠁⠐⣶⣶⣿⣿⣿⣿\n"
"⣿⣿⡇⠄⠄⠄⠄⠁⣿⣿⣀⠈⠿⢟⡛⠛⣿⠛⠛⣿⣿⣿⣿⣿\n"
"⣿⣿⡆⠄⠄⠄⠄⠄⠈⠁⠰⣄⣴⡬⢵⣴⣿⣤⣽⣿⣿⣿⣿⣿\n"
"⣿⣿⡇⠄⢀⢄⡀⠄⠄⠄⠄⡉⠻⣿⡿⠁⠘⠛⡿⣿⣿⣿⣿⣿\n"
"⣿⡿⠃⠄⠄⠈⠻⠄⠄⠄⠄⢘⣧⣀⠾⠿⠶⠦⢳⣿⣿⣿⣿⣿\n"
"⣿⣶⣤⡀⢀⡀⠄⠄⠄⠄⠄⠄⠻⢣⣶⡒⠶⢤⢾⣿⣿⣿⣿⣿\n"
"⣿⡿⠋⠄⢘⣿⣦⡀⠄⠄⠄⠄⠄⠉⠛⠻⠻⠺⣼⣿⠟⠛⠿⣿\n"
"⠋⠁⠄⠄⠄⢻⣿⣿⣶⣄⡀⠄⠄⠄⠄⢀⣤⣾⣿⡀⠄⠄⠄⢹\n"
"⠄⠄⠄⠄⠄⠄⢻⣿⣿⣿⣷⡤⠄⠰⡆⠄⠄⠈⠛⢦⣀⡀⡀⠄\n"
"⠄⠄⠄⠄⠄⠄⠈⢿⣿⠟⡋⠄⠄⠄⢣⠄⠄⠄⠄⠄⠈⠹⣿⣀\n"
"⠄⠄⠄⠄⠄⠄⠄⠘⣷⣿⣿⣷⠄⠄⢺⣇⠄⠄⠄⠄⠄⠄⠸⣿\n"
"⠄⠄⠄⠄⠄⠄⠄⠄⠹⣿⣿⡇⠄⠄⠸⣿⡄⠄⠈⠁⠄⠄⠄⣿\n"
"⠄⠄⠄⠄⠄⠄⠄⠄⠄⢻⣿⡇⠄⠄⠄⢹⣧⠄⠄⠄⠄⠄⠄⠘\n")
    
    
    
K = ("⣿⣿⣿⣿⠟⠋⢁⢁⢁⢁⢁⢁⢁⢁⠈⢻⢿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⡀⠭⢿⣿⣿⣿⣿\n"
"⣿⣿⣿⡟⠄⢀⣾⣿⣿⣿⣷⣶⣿⣷⣶⣶⡆⠄⠄⠄⣿⣿⣿⣿\n"
"⣿⣿⣿⡇⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠄⠄⢸⣿⣿⣿⣿\n"
"⣿⣿⣿⣇⣼⣿⣿⠿⠶⠙⣿⡟⠡⣴⣿⣽⣿⣧⠄⢸⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣾⣿⣿⣟⣭⣾⣿⣷⣶⣶⣴⣶⣿⣿⢄⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⡟⣩⣿⣿⣿⡏⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣹⡋⠘⠷⣦⣀⣠⡶⠁⠈⠁⠄⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣍⠃⣴⣶⡔⠒⠄⣠⢀⠄⠄⠄⡨⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣦⡘⠿⣷⣿⠿⠟⠃⠄⠄⣠⡇⠈⠻⣿⣿⣿⣿\n"
"⣿⣿⣿⡿⠟⠋⢁⣷⣠⠄⠄⠄⠄⣀⣠⣾⡟⠄⠄⠄⠄⠉⠙⠻\n"
"⡿⠟⠁⠄⠄⠄⢸⣿⣿⡯⢓⣴⣾⣿⣿⡟⠄⠄⠄⠄⠄⠄⠄⠄\n"
"⠄⠄⠄⠄⠄⠄⣿⡟⣷⠄⠹⣿⣿⣿⡿⠁⠄⠄⠄⠄⠄⠄⠄⠄\n"
"⠄⠄⠄⠄⠄⣸⣿⡷⡇⠄⣴⣾⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄\n"
"⠄⠄⠄⠄⠄⣿⣿⠃⣦⣄⣿⣿⣿⠇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n"
"⠄⠄⠄⠄⢸⣿⠗⢈⡶⣷⣿⣿⡏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n")



L = ("___________ \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　／￣￣＼| \n"
"＜ ´･ 　　 |＼ \n"
"　|　３　 | 丶＼ \n"
"＜ 、･　　|　　＼ \n"
"　＼＿＿／∪ _ ∪) \n"
"　　　　　 Ｕ Ｕ\n")
    
M = ("_/﹋\_\n"
"(҂`_´)\n"
f"<,︻╦╤─ ҉ - - - 🤯\n"
"_/﹋\_\n")

N = ("▄███████▄\n"
"█▄█████▄█\n"
"█▼▼▼▼▼█\n"
"██________█▌\n"
"█▲▲▲▲▲█\n"
"█████████\n"
"_████\n")

O = ("┈┈┏━╮╭━┓┈╭━━━━╮\n"
"┈┈┃┏┗┛┓┃╭┫ⓞⓘⓝⓚ┃\n"
"┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
"┈╭━┻╮╲┗━━━━╮╭╮┈\n"
"┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
"┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
"┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
"┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n")

P = ("░▐█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄\n"
"░███████████████████████ \n"
"░▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓◤ \n"
"░▀░▐▓▓▓▓▓▓▌▀█░░░█▀░\n"
"░░░▓▓▓▓▓▓█▄▄▄▄▄█▀░░\n"
"░░█▓▓▓▓▓▌░░░░░░░░░░\n"
"░▐█▓▓▓▓▓░░░░░░░░░░░\n"
"░▐██████▌░░░░░░░░░░\n")

Q = ("╥━━━━━━━━╭━━╮━━┳\n"
"╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
"╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
"╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
"╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
"╨━━┗┛┗┛━━┗┛┗┛━━┻\n")
R = ("╔┓┏╦━╦┓╔┓╔━━╗\n" 
"║┗┛║┗╣┃║┃║X X║\n"
"║┏┓║┏╣┗╣┗╣╰╯║\n"
"╚┛┗╩━╩━╩━╩━━╝\n")
S = ("▬▬▬.◙.▬▬▬ \n"
"═▂▄▄▓▄▄▂ \n"
"◢◤ █▀▀████▄▄▄▄◢◤ \n"
"█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
"◥█████◤ \n"
"══╩══╩══ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ Hello, My Friend :D \n"
"╬═╬☻/ \n"
"╬═╬/▌ \n"
"╬═╬/ \\n")

T = ("┳┻┳┻╭━━━━╮╱▔▔▔╲\n"
"┻┳┻┳┃╯╯╭━┫▏╰╰╰▕\n"
"┳┻┳┻┃╯╯┃▔╰┓▔▂▔▕╮\n"
"┻┳┻┳╰╮╯┃┈╰┫╰━╯┏╯\n"
"┳┻┳┻┏╯╯┃╭━╯┳━┳╯\n"
"┻┳┻┳╰━┳╯▔╲╱▔╭╮▔╲\n"
"┳┻┳┻┳┻┃┈╲┈╲╱╭╯╮▕\n"
"┻┳┻┳┻┳┃┈▕╲▂╱┈╭╯╱\n"
"┳┻┳┻┳┻┃'''┈┃┈┃┈'''╰╯\n"
"┻┳┻┳┻┏╯▔'''╰┓┣━┳┫\n"
"┳┻┳┻┳╰┳┳┳'''╯┃┈┃┃\n"
"┻┳┻┳┻┳┃┃┃┈'''┃┈┃┃\n"
"┳┻┳┻┳┻┃┃┃'''┊┃┈┃┃\n"
"┻┳┻┳┻┳┃┃┃┈'''┃┈┃┃.\n"
"┳┻┳┻┳┻┣╋┫'''┊┣━╋┫\n"
"┻┳┻┳┻╭╯╰╰-╭╯━╯.''╰╮\n"
"**I Love You 💕** \n")

U = ("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡿⠋⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⠀⣠⣾⣿⡿⠋⠀⠀⠉⠻⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⠃⠀⠀⣀⡀⠀⢹⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡄⠀⠙⠻⠋⠀⠀⣸⣿⣿⠀⠀⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⣰⣿⣿⠟⠀⢠⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡿⠛⠛⠒⠶⠾⢿⣿⣿⣷⣄⣾⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⢰⣿⣿⣷⣶⣦⣼⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡀⠀⠙⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⢿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⠀⠀⠀⠉⠉⠛⠛⠛⠶⢶⣤⣼⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣦⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠁⠀⣾⣿⣷⡄⠀⢼⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⠀⢿⣿⣿⡿⠀⠈⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣇⠀⠀⠉⠋⠁⠀⢠⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠿⢷⣤⣀⣀⣀⣠⣾⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⠀⠀⠈⠉⠉⠛⢻⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣶⣦⣤⣤⣀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠹⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡿⠛⠉⠉⠙⠻⣀⣀⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠁⠀⣀⡀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⢸⣿⡇⠀⣷⡀⠘⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡄⠈⢻⡇⠀⡿⠃⠀⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣷⣄⢸⡇⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⠉⠉⠑⠒⠲⠿⢿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣤⣄⣀⡀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⢺⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⠀⠉⠉⠙⠋⠀⠀⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣤⣤⣀⣀⡀⠀⠀⣰⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣷⠀⢹⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⠉⠉⠀⠀⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣶⣤⣤⣀⣀⣀⣀⣰⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡟⠉⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⢀⣤⡄⠀⡀⠀⢹⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⢸⣿⡇⠀⣿⡄⠈⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡆⠀⢹⡇⠀⠟⠁⢀⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣦⣸⡇⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n")

V = ("⣿⣿⣿⣿⣿⣍⠀⠉⠻⠟⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠓⠀⠀⢒⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿\n"
"⣿⡿⠋⠋⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⢿⣿⣿⡿⣿⣿⡟⠋⠀⢀⣩\n"
"⣿⣿⡄⠀⠀⠀⠀⠀⠁⡀⠀⠀⠀⠀⠈⠉⠛⢷⣭⠉⠁⠀⠀⣿⣿\n"
"⣇⣀. INDIA🇮🇳INDIA🇮🇳⠆⠠..⠘⢷⣿⣿⣛⠐⣶⣿⣿\n"
"⣿⣄⠀⣰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢀⣠⣿⣿⣿⣾⣿⣿⣿\n"
"⣿⣿⣿⣿⠀⠀⠀⠀⡠⠀⠀⠀⠀⠀⢀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠄⠀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⣠⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⠀⠀⠂⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣇⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡆⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"**🇮🇳PROUD TO BE AN INDIAN🇮🇳**\n")



W = ("───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───\n"
"───█▒▒░░░░░░░░░▒▒█───\n"
"────█░░█░░░░░█░░█────\n"
"─▄▄──█░░░▀█▀░░░█──▄▄─\n"
"█░░█─▀▄░░░░░░░▄▀─█░░█\n"
"█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n"
"█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n"
"█░░║║║╠─║─║─║║║║║╠─░░█\n"
"█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n"
"█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

X = ("░░░░▓\n"
"░░░▓▓\n"
"░░█▓▓█\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░░██▓▓██\n"
"░░██▓▓██\n"
"░░██▓▓██\n"
"░░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓███\n"
"░░░░██▓▓████\n"
"░░░░░██▓▓█████\n"
"░░░░░░██▓▓██████\n"
"░░░░░░███▓▓███████\n"
"░░░░░████▓▓████████\n"
"░░░░█████▓▓█████████\n"
"░░░█████░░░█████●███\n"
"░░████░░░░░░░███████\n"
"░░███░░░░░░░░░██████\n"
"░░██░Ab Mar Bsdk░████\n"
"░░░░░░░░░░░░░░░░███\n"
"░░░░░░░░░░░░░░░░░░░\n")


Y = ("────██──────▀▀▀██\n"
"──▄▀█▄▄▄─────▄▀█▄▄▄\n"
"▄▀──█▄▄──────█─█▄▄\n"
"─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n"
"─▀───────▀▀─▀───────▀▀\n🚶🏻‍♂️🚶🏻‍♂️ɮʏɛ ʄʀɨɛռɖֆ..")

Z = ("╭━━━┳╮╱╱╭╮╱╭━━━┳━━━╮\n"
"┃╭━╮┃┃╱╭╯╰╮┃╭━╮┃╭━╮┃\n"
"┃╰━━┫╰━╋╮╭╯┃┃╱┃┃╰━━╮\n"
"╰━━╮┃╭╮┣┫┃╱┃┃╱┃┣━━╮┃\n"
"┃╰━╯┃┃┃┃┃╰╮┃╰━╯┃╰━╯┃\n"
"╰━━━┻╯╰┻┻━╯╰━━━┻━━━╯\n")


AA = ("███████▄▄███████████▄\n"
"▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
"▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
"▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
"▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
"▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
"▓▓▓▓▓▓███░░░░░░░░░░░░█\n"
"██████▀░░█░░░░██████▀\n"
"░░░░░░░░░█░░░░█\n"
"░░░░░░░░░░█░░░█\n"
"░░░░░░░░░░░█░░█\n"
"░░░░░░░░░░░█░░█\n"
"░░░░░░░░░░░░▀▀\n")




@borg.on(mellow_cmd(pattern="flower ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(".........▒▒▒▒▒▒▒▒▒\n      ▒▒▒▒▒▒▒▒▒▒▒▒\n  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n▒▒▒▒▒▒▓▓▓▓▓▒▒▒▒▒▒\n▒▒▒▒▒▓▓▓▓▓▓▓▒▒▒▒▒\n▒▒▒▒▓▓▓▓▓▓▓▓▓▒▒▒▒\n▒▒▒▒▒▓▓▓▓▓▓▓▒▒▒▒▒\n  ▒▒▒▒▒▒▓▓▓▓▓▒▒▒▒▒\n    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n       ▒▒▒▒▒▒▒▒▒▒▒▒▒\n         ▒▒▒▒▒▒▒▒▒▒\n              ▒▒▒▒▒▒\n                     ▓\n     ▓▓▓       ▓\n ▓▓▓▓▓▓  ▓\n▓▓            ▓▓\n ▓                 ▓     ▓▓▓▓▓\n ▓                 ▓     ▓▓▓▓▓\n                     ▓   ▓▓▓▓▓▓\n                     ▓▓           ▓▓\n                     ▓               ▓\n                     ▓\n     ████████████\n         █████████\n            ███████\n             ██████\n.................███..............\n")
        
        
        
@borg.on(mellow_cmd(pattern="vheart ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
       await event.edit("..........###########\n......##############\n....################\n..##################.............########\n...##################.......#############\n....##################.....##############\n.....#################...################\n.......#################################\n.........###############################\n...........#############################\n..............##########################\n................########################\n...................#####################\n.....................##################\n.......................###############\n........................#############\n..........................##########\n...........................########\n............................######\n.............................#####\n..............................###\n...............................#")
   
 
 
@borg.on(mellow_cmd(pattern="luvart ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(" 📺📺📺📺📺📺📺📺📺📺📺📺📺\n 📺📺📺💖💖💖💖💖💖💖📺📺📺\n 📺📺📺📺📺💖💖💖📺📺📺📺📺\n 📺📺📺📺📺💖💖💖📺📺📺📺📺\n 📺📺📺📺📺💖💖💖📺📺📺📺📺\n 📺📺📺📺📺💖💖💖📺📺📺📺📺\n 📺📺📺💖💖💖💖💖💖💖📺📺📺\n 📺📺📺📺📺📺📺📺📺📺📺📺📺\n 💖💖💖💖💖💖💖💖💖💖💖💖💖\n 💖💖📺📺📺💖💖💖📺📺📺💖💖\n 💖📺📺📺📺📺💖📺📺📺📺📺💖\n 💖📺📺📺📺📺📺📺📺📺📺📺💖\n 💖💖📺📺📺📺📺📺📺📺📺💖💖\n 💖💖💖📺📺📺📺📺📺📺💖💖💖\n 💖💖💖💖📺📺📺📺📺💖💖💖💖\n 💖💖💖💖💖📺📺📺💖💖💖💖💖\n 💖💖💖💖💖💖📺💖💖💖💖💖💖\n 💖💖💖💖💖💖💖💖💖💖💖💖💖\n 📺📺📺📺📺📺📺📺📺📺📺📺📺\n 📺📺💖💖📺📺📺📺📺💖💖📺📺\n 📺📺💖💖📺📺📺📺📺💖💖📺📺\n 📺📺💖💖📺📺📺📺📺💖💖📺📺\n 📺📺💖💖📺📺📺📺📺💖💖📺📺\n 📺📺💖💖💖📺📺📺💖💖💖📺📺\n 📺📺💖💖💖💖💖💖💖💖💖📺📺\n 📺📺📺💖💖💖💖💖💖💖📺📺📺\n 📺📺📺📺📺📺📺📺📺📺📺📺📺\n")
 
 

 
@borg.on(mellow_cmd(pattern=r"spika"))
async def kakashi(pikachu):
    await pikachu.edit(A)
    
@borg.on(mellow_cmd(pattern=r"sshit"))
async def kakashi(shit):
    await shit.edit(B)
    
@borg.on(mellow_cmd(pattern=r"sxx"))
async def kakashi(saxy):
    await saxy.edit(C)
    
@borg.on(mellow_cmd(pattern=r"sporn"))
async def kakashi(pornhub):
    await pornhub.edit(D)
    
@borg.on(mellow_cmd(pattern=r"sthink"))
async def kakashi(think):
    await think.edit(E)
    
@borg.on(mellow_cmd(pattern=r"sdick"))
async def kakashi(dick):
    await dick.edit(F)
    
@borg.on(mellow_cmd(pattern=r"sfrog"))
async def kakashi(frog):
    await frog.edit(G)
    
@borg.on(mellow_cmd(pattern=r"sputin"))
async def kakashi(putin):
    await putin.edit(H)
    
@borg.on(mellow_cmd(pattern=r"sdead"))
async def kakashi(dead):
    await dead.edit(I)
    
@borg.on(mellow_cmd(pattern=r"strump"))
async def kakashi(trump):
    await trump.edit(J)
    
@borg.on(mellow_cmd(pattern=r"schina"))
async def kakashi(china):
    await china.edit(K)
    
@borg.on(mellow_cmd(pattern=r"india"))
async def kakashi(india):
    await india.edit(L)
    
@borg.on(mellow_cmd(pattern=r"monster"))
async def bluedevilmonster(monster):
    await monster.edit(N)
    
@borg.on(mellow_cmd(pattern=r"pig"))
async def bluedevilpig(pig):
    await pig.edit(O)
    
@borg.on(mellow_cmd(pattern=r"killer"))
async def bluedevilkiller(killer):
    await killer.edit(M)
    
@borg.on(mellow_cmd(pattern=r"gun"))
async def bluedevilgun(gun):
    await gun.edit(P)
    
@borg.on(mellow_cmd(pattern=r"dog"))
async def bluedevildog(dog):
    await dog.edit(Q)    
    
@borg.on(mellow_cmd(pattern=r"hello"))
async def bluedevilhello(hello):
    await hello.edit(R)
    
@borg.on(mellow_cmd(pattern=r"hmf"))
async def bluedevilhmf(hmf):
    await hmf.edit(S)
    
@borg.on(mellow_cmd(pattern=r"couple"))
async def bluedevilcouple(couple):
    await couple.edit(T)
    
@borg.on(mellow_cmd(pattern=r"sup"))
async def bluedevilsupreme(supreme):
    await supreme.edit(U)
    
@borg.on(mellow_cmd(pattern=r"india"))
async def bluedevilindia(india):
    await india.edit(J)
    
@borg.on(mellow_cmd(pattern=r"wc"))
async def bluedevilwelcome(welcome):
    await welcome.edit(W)
    
@borg.on(mellow_cmd(pattern=r"snk"))
async def bluedevilsnake(snake):
    await snake.edit(X) 
    
@borg.on(mellow_cmd(pattern=r"ded"))
async def bluedevilded(ded):
    await ded.edit(L)
    
@borg.on(mellow_cmd(pattern=r"bye"))
async def bluedevilbye(bye):
    await bye.edit(Y)
    
@borg.on(mellow_cmd(pattern=r"shitos"))
async def bluedevilshitos(shitos):
    await shitos.edit(Z)
    
@borg.on(mellow_cmd(pattern=r"dislike"))
async def bluedevildislike(dislike):
    await dislike.edit(AA)