import telebot 
from telebot import types 
import time 
import urllib2, cookielib, os.path


TOKEN = '130984576:AAGwSFR-CQcl0S0Bnc7oAyfGoD9Ko92Klhg'

bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.

def listener(messages): 
    for m in messages: 
        cid = m.chat.id 
        print "[" + str(cid) + "]: " + m.text 

bot.set_update_listener(listener) 

bot.polling(none_stop=True) 

#Horario grado ingenieria informatica

@bot.message_handler(commands=['horario_gii'])
def obtener_horario_gii(m):
    cid = m.chat.id 
    
    if os.path.isfile('horario_gii.pdf'):
        bot.send_document(cid, open( 'horario_gii.pdf', 'rb'))

    else:
        url = 'http://etsiit.ugr.es/pages/calendario_academico/horarios1516/horariosgii1516/!'
        
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        request = urllib2.Request(url)
        
        f = opener.open(request)
        data = f.read()
        f.close()
        opener.close()
        
        FILE = open('horario_gii.pdf', "wb+")
        FILE.write(data)
        FILE.close()
         
        bot.send_document(cid, open( 'horario_gii.pdf', 'rb'))
    #Horario grado ingenieria informatica


@bot.message_handler(commands=['horario_git'])
def obtener_horario_git(m):
    cid = m.chat.id 
    
    if os.path.isfile('horario_git.pdf'):
        bot.send_document(cid, open( 'horario_git.pdf', 'rb'))

    else:
        url = 'http://etsiit.ugr.es/pages/calendario_academico/horarios1516/horariosgitt1516/!'
        
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        request = urllib2.Request(url)
        
        f = opener.open(request)
        data = f.read()
        f.close()
        opener.close()
        
        FILE = open('horario_git.pdf', "wb+")
        FILE.write(data)
        FILE.close()
         
        bot.send_document(cid, open( 'horario_git.pdf', 'rb'))
        
        
@bot.message_handler(commands=['horario_gim'])
def obtener_horario_gim(m):
    cid = m.chat.id 
    
    if os.path.isfile('horario_gim.pdf'):
        bot.send_document(cid, open( 'horario_gim.pdf', 'rb'))

    else:
        url = 'http://etsiit.ugr.es/pages/calendario_academico/horarios1516/horariosgim1516/!'
        
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        request = urllib2.Request(url)
        
        f = opener.open(request)
        data = f.read()
        f.close()
        opener.close()
        
        FILE = open('horario_gim.pdf', "wb+")
        FILE.write(data)
        FILE.close()
         
        bot.send_document(cid, open( 'horario_gim.pdf', 'rb'))
while True: 
    time.sleep(0)