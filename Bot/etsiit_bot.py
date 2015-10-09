# --* coding: utf-8 -*-

import telebot 
from telebot import types 
from lxml import html
from bs4 import BeautifulSoup

import string
import requests
import re
import urllib2, cookielib, os.path, time, sys
import chardet

sys.path.append('../informacion/')
from conf import token


reload(sys) 
sys.setdefaultencoding("utf-8")

# Creamos el objeto bot que representa a ETSIITBOT
bot = telebot.TeleBot(token)

# Para que el bot siga ejecutandose aunque presente errores
bot.polling(none_stop=True) 


####################################
# Definimos los distintos teclados #
####################################

# Teclado para elegir el menu
teclado_menu = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True,selective=True)
teclado_menu.add('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado')

# Teclado para elegir el horario
teclado_horario = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True,selective=True)
teclado_horario.add('Informática', 'Telecomunicaciones', 'Informática + matemáticas')

# Teclado para elegir los examenes
teclado_examenes = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True,selective=True)
teclado_examenes.add('Informática', 'Telecomunicaciones', 'Todos')

# Ocultamos el teclado
hideBoard = types.ReplyKeyboardHide()

########################
# Funciones auxiliares #
########################

# Función encarga de enviar el archivo al chat del mensaje
def enviar_archivo(m,archivo):
    
    fo = open(archivo, 'rb')
    
    bot.send_chat_action(m.chat.id,'upload_document')

    bot.send_document(m.chat.id, fo,reply_markup=hideBoard)

    fo.close()
    
# Limpiamos la fecha 
def limpiar_fecha(aux):
    
    fecha_limpia = ""
    
    fecha_limpia = re.sub('<div class="numero">', '',aux)
    
    fecha_limpia = re.sub('</div>', '',fecha_limpia)
    
    fecha_limpia = re.sub('\s+',' ',fecha_limpia)
    
    return fecha_limpia
    
# Limpiamos plato   
def limpiar_plato(aux):
    
    plato_limpio = ""
    plato_limpio = re.sub('<br/>', ' ',aux)
    plato_limpio = re.sub('\s+',' ',plato_limpio)
    
    return plato_limpio
    
    

# Devuelve la informacion sobre el menú en una lista
def obtener_menu():
    
    r  = requests.get("http://comedoresugr.tcomunica.org/")
    
    data = r.text
    
    soup = BeautifulSoup(data,"lxml")
    
    result = soup.find_all('div', id='plato')
    
    menu_semana = []
    
    for x in result:
        menu_semana.append(str(x))

    return menu_semana

# Devuelve el menu de un dia concreto
def obtener_menu_dia(dia):
    
    mensaje = ""
    
    #Obtenemos la fecha
    fecha = dia.find('div', id='fechaplato')     # TODA LA INFORMACION SOBRE EL DIA DEL PLATO
    
    fecha = ''.join(map(str, fecha.contents))
    
    fecha = limpiar_fecha(fecha)
    
    mensaje += fecha + "\n\n"
    

    #Obtenemos el primer plato
    plato1 = dia.find('div', id='plato1')
    
    plato1 = ''.join(map(str, plato1.contents))

    plato1 = limpiar_plato(plato1)
    
    mensaje += plato1 + "\n"

    #Obtenemos el segundo plato
    plato2 = dia.find('div', id='plato2')
    
    plato2 = ''.join(map(str, plato2.contents))

    plato2 = limpiar_plato(plato2)
    
    mensaje += plato2 + "\n"


    #Obtenemos el tercer plato
    plato3 = dia.find('div', id='plato3')
    
    plato3 = ''.join(map(str, plato3.contents))

    plato3 = limpiar_plato(plato3)
    
    mensaje += plato3 + "\n\n"    

    return mensaje

# Comprobamos si existe el horario y se actua en consecuencia
def mandar_horario(grado,m):
    
    try:
        log(m)
        path = '../Horarios/'
        nombre_fichero = 'horarios_gi'
        descriptor = 'horariosgi'
        
        if grado == 'Informática':
            descriptor += 'i1516/!'
            nombre_fichero += 'i.pdf'       
            
        elif grado == 'Telecomunicaciones':
            descriptor += 'tt1516/!'
            nombre_fichero += 't.pdf'
        
        elif grado == 'Informática + matemáticas':
           descriptor +=  'm1516/!'
           nombre_fichero += 'm.pdf'

        
        if os.path.isfile(path + nombre_fichero):
    
            enviar_archivo(m,path + nombre_fichero)
            
        
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

            enviar_archivo(m,path + nombre_fichero)
            
    except Exception as e:
        bot.reply_to(m,'Se ha producido un error, intentelo mas tarde')
        #exception_log(e,m)


# Comprobamos si existe el horario y se actua en consecuencia
def mandar_examenes(grado,m):
    
    try:
        log(m)
        path = '../examenes/'
        nombre_fichero = ''

        
        if grado == 'Informática':
            nombre_fichero += 'examenes_gii.pdf'

        elif grado == 'Telecomunicaciones':
            nombre_fichero += 'examenes_gitt.pdf'
            
        elif grado == 'Todos':
            nombre_fichero += 'examenes.pdf'


        if os.path.isfile(path + nombre_fichero):

            enviar_archivo(m,path+nombre_fichero)

        else:
            bot.reply_to(m,'Se ha producido un error, intentelo mas tarde')

            
    except Exception as e:
        bot.reply_to(m,'Se ha producido un error, intentelo mas tarde')
        exception_log(e,m)
        
# Comprobamos si existe los examenes y se actua en consecuencia
def obtener_examenes(m):
    
    log(m)
    try:
        if os.path.isfile('../examenes/examenes.pdf'):

            enviar_archivo(m,'../examenes/examenes.pdf')

        else:
            url = 'http://etsiit.ugr.es/pages/calendario_academico/calendarioexamenes1516/!'
            cj = cookielib.CookieJar()
        
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
            
            request = urllib2.Request(url)
            
            f = opener.open(request)
            data = f.read()
            f.close()
            opener.close()
            
            FILE = open('../examenes/examenes.pdf', "wb+")
            FILE.write(data)
            FILE.close()
            
            enviar_archivo(m,'../examenes/examenes.pdf')
            
    except Exception as e:
        bot.reply_to(m,'Se ha producido un error, intentelo mas tarde')
        exception_log(e,m)        
        
#Función auxiliar usado por menu_dia
def aux_menu_dia(m):
    
    try:
        
        dias = { 'Lunes': 0, 'Martes': 1, 'Miercoles': 2,'Jueves': 3,'Viernes': 4,'Sabado': 5}
        
        dia_seleccionado = str(m.text)
        
        info_dias = obtener_menu()
        
        if(len(info_dias)==0):
            bot.reply_to(m,'Hay un error en la web de comedores, intentelo mas tarde')

        else:
        
            mensaje = "¡Hola!\n\nAquí tienes el menú del " + dia_seleccionado.lower() + ", ¡Buen provecho! \n\n"
            
            aux = BeautifulSoup(info_dias[dias[dia_seleccionado]],"lxml")
    
    
            mensaje += obtener_menu_dia(aux)
                    
            mensaje += "Precio por menú: 3,5€"
    
            bot.reply_to(m, mensaje, reply_markup=hideBoard) 
                
    except Exception as e:
        bot.reply_to(m,'Se ha producido un error, intentelo mas tarde')
        exception_log(e,m)

        
        
# Función auxiliar usada por el comando "horario"
def aux_horario(m):
    
    grado = str(m.text)
    mandar_horario(grado,m)
        
# Función auxiliar usada por el comando "examenes"
def aux_examenes(m):
    
    grado = str(m.text)
    mandar_examenes(grado,m)
    
############
# Listener #
############

def listener(messages):
    for m in messages: 
        ayuda_pasiva(m)
        
bot.set_update_listener(listener) 


#####################
# Registros del bot #
#####################

# Registro de actividad
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
 
# Registro de excepciones
def exception_log(e,m):
    hour = time.strftime("%H:%M:%S")
    date = time.strftime("%d/%m/%y")
        
    complete_date = 'Times exception: '  + str(date) + ' ' + str(hour) + '\n'
    
    cause = 'Cause of the exception: ' + str(m.text) + '\n'
    
    exception = 'Exception: ' + str(e)
    
    information = complete_date + cause + exception
    
    
    aux = open( '../informacion/exception.txt', 'a') 
    aux.write( str(information) + "\n\n")
    aux.close()   

########################
# Ayuda pasiva del bot #
########################

#Ayuda pasiva para obtener el horario y/o examenes
def ayuda_pasiva(m):
    
    try:
        
        if hasattr(m, 'text'):
            mensaje = ""
                
            #m.text[0] != "/" evita que la ayuda pasiva se active al user /horario_gii
            if "horario" in m.text.lower() and m.text[0] != "/":
                mensaje = open('../informacion/ayuda_pasiva_horario.txt', 'r').read()
                bot.reply_to(m,mensaje)
            
            if ("examenes" in m.text.lower() or "exámenes" in m.text.lower()) and m.text[0] != "/" :
                mensaje = open('../informacion/ayuda_pasiva_examenes.txt', 'r').read()
                bot.reply_to(m,mensaje)
        
    except Exception as e:
        exception_log(e,m)
        
        
#######################################
# Comandos a los que reacciona el bot #
#######################################

# Función start
@bot.message_handler(commands=['start'])
def start(m):
    
    log(m)
    
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
    
    log(m)
    
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
        log(m)
        cid = m.chat.id
        texto = "Elige el grado"
        msg = bot.send_message(cid,texto, reply_markup=teclado_horario)
        bot.register_next_step_handler(msg, aux_horario)
        
    except Exception as e:
        bot.reply_to(m,'Se ha producido un error, intentelo mas tarde')
        exception_log(e,m)
        
        
# Función encargada de dar el horario
@bot.message_handler(commands=['examenes'])
def examenes(m):
    
    try:
        log(m)
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
    
    log(m)
    
    cid = m.chat.id

    mensaje = "Información de contacto de la escuela:\n\n" \
    "Teléfono: +34 958242802\n" \
    "Fax: +34 958242801\n" \

    bot.send_message(cid,mensaje)    
    
# Envia localizacion
@bot.message_handler(commands=['localizacion'])
def obtener_localizacion(m):

    try:
        log(m)

        cid = m.chat.id
        
        bot.send_location(cid,37.196689,-3.624534)
    except Exception as e:
        bot.reply_to(m,'Se ha producido un error, intentelo mas tarde')
        exception_log(e,m)
        
        
# Envia web
@bot.message_handler(commands=['web'])
def obtener_web(m):

    try:
        log(m)

        cid = m.chat.id
        mensaje = 'Aquí tienes la web de la ETSIIT: '
        
        bot.send_message(cid,mensaje + 'http://etsiit.ugr.es/')

    except Exception as e:
        bot.reply_to(m,'Se ha producido un error, intentelo mas tarde')
        exception_log(e,m)
        
        
#Obtiene y envia menú
@bot.message_handler(commands=['menu_semana'])
def menu_semana(m):

    try:
        
        log(m)

        cid = m.chat.id
        
        info_dias = obtener_menu()
        
        #Con esto comprobamos que hemos extraido informacion de la web de comedores
        if(len(info_dias) == 0):
            bot.reply_to(m,'Hay un error en la web de comedores, intentelo mas tarde')
            
        else:
            mensaje = "¡Hola!\n\nAquí tienes el menú de la semana, ¡Buen provecho! \n\n"
            
            for dia in info_dias:  
                
                aux = BeautifulSoup(dia,"lxml") #Sacamos la información de un dia concreto
                
                mensaje += obtener_menu_dia(aux) #Sacamos el menu de la informacion de dicho dia
        
            mensaje += "Precio por menú: 3,5€"
            bot.send_message(cid,mensaje)
    
    except Exception as e:
        bot.reply_to(m,'Se ha producido un error, intentelo mas tarde')
        exception_log(e,m)


#Obtiene y envia menú del dia seleccionado
@bot.message_handler(commands=['menu_dia'])
def menu_dia(m):
    
    
    try:
        
        log(m)
        
        cid = m.chat.id
        
        texto = "Selecciona dia para saber el menú"
        
        msg = bot.send_message(cid,texto, reply_markup=teclado_menu)
        
        bot.register_next_step_handler(msg, aux_menu_dia)
        
    except Exception as e:
        bot.reply_to(m,'Se ha producido un error, intentelo mas tarde')
        exception_log(e,m)
        
# Evita sobrecarga de la cpu    
while True: 
    time.sleep(300)