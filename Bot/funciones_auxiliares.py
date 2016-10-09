from bot import *
import os.path
from teclados import *
import urllib.request, urllib.parse, urllib.error
from pycomedoresugr import *

#Lee el fichero donde se almacenan los links y se cargan en un diccionario
with open('../informacion/links.json', encoding='utf-8') as data_file:
    links = json.loads(data_file.read())

########################
# Funciones auxiliares #
########################

# Función encarga de enviar el archivo al chat del mensaje
def enviar_archivo(m,archivo):

    fo = open(archivo, 'rb')

    bot.send_chat_action(m.chat.id,'upload_document')

    bot.send_document(m.chat.id, fo,reply_markup=hideBoard)

    fo.close()


# Comprobamos si existe el horario y se actua en consecuencia
def mandar_horario(grado,m):

    try:

        url = ''

        if grado == 'Informática':
            url = links["link_horario_gii"]

        elif grado == 'Telecomunicaciones':
            url = links["link_horario_gitt"]

        elif grado == 'Informática + matemáticas':
            url = links["link_horario_gim"]


        #Enviar el archivo
        bot.send_message(m.chat.id,url,reply_markup=hideBoard)

    except Exception as e:
        bot.reply_to(m,'Se ha producido un error, intentelo mas tarde')
        #exception_log(e,m)

# Comprobamos si existe el horario y se actua en consecuencia
def mandar_examenes(grado,m):

    try:

        if grado == 'Informática':
            url = links["link_examenes_gii"]

        elif grado == 'Telecomunicaciones':
            url = links["link_examenes_gitt"]

        elif grado == 'Informática + matemáticas':
            url = links["link_examenes_gim"]

        #Enviar el archivo
        bot.send_message(m.chat.id,url, reply_markup=hideBoard)


    except Exception as e:
        bot.reply_to(m,'Se ha producido un error, intentelo mas tarde')
        #exception_log(e,m)

def mandar_calendario(m):

    cid = m.chat.id

    url = links["link_calendario"]

    bot.send_message(cid,url)

# Función auxiliar usada por el comando "horario"
def aux_horario(m):

    grado = str(m.text)
    mandar_horario(grado,m)

# Función auxiliar usada por el comando "examenes"
def aux_examenes(m):

    grado = str(m.text)
    mandar_examenes(grado,m)
 
#Función auxiliar para devolver el menú de comedores del dia 
def aux_menu_dia(m):

    dia = str(m.text)
    menu = menu_dia(dia)
    menu = " ".join(menu)
    bot.send_message(m.chat.id,menu, reply_markup=hideBoard)


   
# Comprueba el tiempo del mensaje y el de arranque del bot, para evitar
# enviar mensajes que el bot recibio estando apagado
def check_time(m):
    if tiempo_arranque > m.date:
        return False
    else:
        return True
