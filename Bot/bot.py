import telebot
import sys
import time
import os.path

sys.path.append('../informacion/')
from conf import token

bot = telebot.TeleBot(token)

tiempo_arranque = int(time.time())

#Limpiar archivo de log
if os.path.isfile("../informacion/registro.txt"):
    open('../informacion/registro.txt', 'w').close()
