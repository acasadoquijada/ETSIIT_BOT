import telebot 
from telebot import types 
import time 
import urllib2, cookielib, os.path

TOKEN = <Mi_token>


bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.

def listener(messages): 
    for m in messages: 
        cid = m.chat.id 
        print "[" + str(cid) + "]: " + m.text 

bot.set_update_listener(listener) 

bot.polling(none_stop=True) 
# Comprobamos si existe el fichero y se actua en consecuencia
def comprobar_fichero(grado,id_chat):
    
    nombre_fichero = 'horarios_gi'
    descriptor = 'horariosgi'
    
    if grado == 'informatica':
        descriptor += 'i1516/!'
        nombre_fichero += 'i.pdf'
        
    elif grado == 'teleco':
        descriptor += 'tt1516/!'
        nombre_fichero += 't.pdf'
    
    elif grado == 'matematicas':
       descriptor +=  'm1516/!'
       nombre_fichero += 'm.pdf'
    
    if os.path.isfile(nombre_fichero):
        bot.send_document(id_chat, open( nombre_fichero, 'rb'))
    
    else:
        url = 'http://etsiit.ugr.es/pages/calendario_academico/horarios1516/' + descriptor

        bot.send_message(id_chat,url)
        cj = cookielib.CookieJar()
        
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        
        request = urllib2.Request(url)
        
        f = opener.open(request)
        data = f.read()
        f.close()
        opener.close()
        
        FILE = open(nombre_fichero, "wb+")
        FILE.write(data)
        FILE.close()
        
        bot.send_document(id_chat, open( nombre_fichero, 'rb'))


        
def obtener_horario(grado,id_chat):
    if grado == 'informatica':
        comprobar_fichero('informatica',id_chat)
        
    elif grado == 'teleco':
        comprobar_fichero('teleco',id_chat)
        
    elif grado == 'matematicas':
        comprobar_fichero('matematicas',id_chat)
        
#Horario grado ingenieria informatica
    
@bot.message_handler(commands=['horario_gii'])
def obtener_horario_gii(m):
    obtener_horario('informatica',m.chat.id)


#Horario grado ingenieria telecomunicaciones

@bot.message_handler(commands=['horario_git'])
def obtener_horario_git(m):
    obtener_horario('teleco',m.chat.id)
        
#Horario grado ingenieria inf+mates

@bot.message_handler(commands=['horario_gim'])
def obtener_horario_gim(m):
    obtener_horario('matematicas',m.chat.id)
    
while True: 
    time.sleep(300)