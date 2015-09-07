import telebot 
from telebot import types 
import urllib2, cookielib, os.path, time, sys

sys.path.append('../informacion/')
from conf import token


bot = telebot.TeleBot(token) # Creamos el objeto de nuestro bot.

def listener(messages): 
    for m in messages: 
        cid = m.chat.id 
        print "[" + str(cid) + "]: " + m.text 

bot.set_update_listener(listener) 

#Registro de actividad
def log(m):
    user_id = m.from_user.id
    name = m.from_user.first_name
    last_name = m.from_user.last_name
    username = m.from_user.username
    hour = time.strftime("%H:%M:%S")
    date = time.strftime("%d/%m/%y")
    information = "["+ str(date) + ' ' + str(hour) + ' ' +str(name)  + ' ' +  str(last_name) + ' ' + str(user_id) + ' @' + str(username) + "]: " + m.text 
    
    aux = open( '../informacion/registro.txt', 'a') 
    aux.write( str(information) + "\n")
    aux.close()
        
bot.polling(none_stop=True) 
# Comprobamos si existe el horario y se actua en consecuencia
def mandar_horario(grado,m):
    
    try:
        log(m)
        path = '../Horarios/'
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
        
        if os.path.isfile(path + nombre_fichero):
            bot.send_document(m.chat.id, open( path + nombre_fichero, 'rb'))
        
        else:
            url = 'http://etsiit.ugr.es/pages/calendario_academico/horarios1516/' + descriptor
            cj = cookielib.CookieJar()
            
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
            
            request = urllib2.Request(url)
            
            f = opener.open(request)
            data = f.read()
            f.close()
            opener.close()
            
            FILE = open(path + nombre_fichero, "wb+")
            FILE.write(data)
            FILE.close()
            
            bot.send_document(m.chat.id, open( path + nombre_fichero, 'rb'))
            
    except Exception as e:
        bot.reply_to(m,'Se ha producido un error, intentelo mas tarde')


#Horario grado ingenieria informatica
    
@bot.message_handler(commands=['horario_gii'])
def obtener_horario_gii(m):
    mandar_horario('informatica',m)


#Horario grado ingenieria telecomunicaciones

@bot.message_handler(commands=['horario_git'])
def obtener_horario_git(m):
    mandar_horario('teleco',m)
        
#Horario grado ingenieria inf+mates

@bot.message_handler(commands=['horario_gim'])
def obtener_horario_gim(m):
    mandar_horario('matematicas',m)

while True: 
    time.sleep(300)