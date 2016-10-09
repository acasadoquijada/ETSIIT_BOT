# Bot realizado por Alejandro Casado Quijada

import telebot
from telebot import types
from bs4 import BeautifulSoup
from lxml import html
import requests
import re
import os.path,sys #cookielib, os.path, time,
import urllib.request, urllib.parse, urllib.error
#from menu import *
from teclados import *
from funciones_auxiliares import *
from ayuda_pasiva import *
from registros import *
from bot import bot
from pycomedoresugr import *




############
# Listener #
############

def listener(messages):
    for m in messages:
        log(m)

bot.set_update_listener(listener)

#######################################
# Comandos a los que reacciona el bot #
#######################################

# Función start
@bot.message_handler(commands=['start'])
def start(m):

    #log(m)

    cid = m.chat.id

    try:
        mensaje = open('../informacion/start.txt', 'r').read()
        bot.send_message(cid,mensaje)

    except Exception as e:
        exception_log(e,m)
        bot.reply_to(m,'Se ha producido un error, intentelo mas tarde')

# Muestra la ayuda
@bot.message_handler(commands=['ayuda'])
def ayuda(m):

    #log(m)

    cid = m.chat.id

    try:
        mensaje = open('../informacion/ayuda.txt', 'r').read()
        bot.send_message(cid,mensaje)

    except Exception as e:
        exception_log(e,m)
        bot.reply_to(m,'Se ha producido un error, intentelo mas tarde')

# Función encargada de dar el horario
@bot.message_handler(commands=['horario'])
def horario(m):

    try:
        #log(m)
        cid = m.chat.id
        texto = "Elige el grado"
        msg = bot.send_message(cid,texto, reply_markup=teclado_horario)
        bot.register_next_step_handler(msg, aux_horario)

    except Exception as e:
        bot.reply_to(m,'Se ha producido un error, intentelo mas tarde')
        exception_log(e,m)


# Función encargada de dar el calendario de examenes
@bot.message_handler(commands=['examenes'])
def examenes(m):

    try:
        #log(m)
        cid = m.chat.id

        texto = "Elige el grado"
        msg = bot.send_message(cid,texto, reply_markup=teclado_examenes)
        bot.register_next_step_handler(msg,aux_examenes)

    except Exception as e:
        bot.reply_to(m,'Se ha producido un error, intentelo mas tarde')
        exception_log(e,m)


# Información de contacto de la escuela
@bot.message_handler(commands=['contacto'])
def contacto(m):

    #log(m)

    cid = m.chat.id

    mensaje = "Información de contacto de la escuela:\n\n" \
    "Teléfono: +34 958242802\n" \
    "Fax: +34 958242801\n" \

    bot.send_message(cid,mensaje)

# Envia localizacion
@bot.message_handler(commands=['localizacion'])
def obtener_localizacion(m):

    try:
        #log(m)

        cid = m.chat.id

        bot.send_location(cid,37.196689,-3.624534)
    except Exception as e:
        bot.reply_to(m,'Se ha producido un error, intentelo mas tarde')
        exception_log(e,m)


# Envia web
@bot.message_handler(commands=['web'])
def obtener_web(m):

    try:
        #log(m)

        cid = m.chat.id
        mensaje = 'Aquí tienes la web de la ETSIIT: '

        bot.send_message(cid,mensaje + 'http://etsiit.ugr.es/')

    except Exception as e:
        bot.reply_to(m,'Se ha producido un error, intentelo mas tarde')
        exception_log(e,m)


#Obtiene y envia menú
@bot.message_handler(commands=['menu_semana'])
def obtener_menu_semana(m):

    try:

        #log(m)

        cid = m.chat.id

        menu = get_menu_semana()

        menu = "\n\n".join(menu)

        bot.send_message(cid, menu)

    except Exception as e:
        bot.reply_to(m,'Se ha producido un error, intentelo mas tarde')
        exception_log(e,m)


#Obtiene y envia menú del dia seleccionado
@bot.message_handler(commands=['menu_dia'])
def obtener_menu_dia(m):
    try:

        #log(m)

        cid = m.chat.id

        texto = "Selecciona dia para saber el menú"

        msg = bot.send_message(cid,texto, reply_markup=teclado_menu)

        bot.register_next_step_handler(msg, aux_menu_dia)

    except Exception as e:
        bot.reply_to(m,'Se ha producido un error, intentelo mas tarde')
        exception_log(e,m)


#Obtiene y envia menú del dia de hoy
@bot.message_handler(commands=['menu_hoy'])
def obtener_menu_hoy(m):
    try:

        #log(m)

        cid = m.chat.id

        menu = menu_dia()
        menu = " ".join(menu)

        #Si el dia es domingo devuelve ""
        if menu != "":
            bot.send_message(m.chat.id,menu, reply_markup=hideBoard)
        else:
            bot.send_message(m.chat.id,"Los domingos no está abierto el comedor", reply_markup=hideBoard)

    except Exception as e:
        bot.reply_to(m,'Se ha producido un error, intentelo mas tarde')
        exception_log(e,m)

# Envia calendario academico
@bot.message_handler(commands=['calendario'])
def obtener_calendario(m):

    try:
        #log(m)

        mandar_calendario(m)

    except Exception as e:
        bot.reply_to(m,'Se ha producido un error, intentelo mas tarde')
        exception_log(e,m)


def main_loop():
    #Comprueba si es un mensaje antiguo para no ejecutarlo
    bot.skip_pending = True
    bot.polling(True)
    while 1:
        time.sleep(3)


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print('\nExiting by user request.\n', file=sys.stderr)
        sys.exit(0)
