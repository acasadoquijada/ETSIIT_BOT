import telebot 
import sys
import time

sys.path.append('../informacion/')
from conf import token

bot = telebot.TeleBot(token)

tiempo_arranque = int(time.time())
