from bot import *
import os.path
from teclados import *
import urllib.request, urllib.parse, urllib.error

#Links horarios
from links import *

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
            url = link_horario_gii

        elif grado == 'Telecomunicaciones':
            url = link_horario_gitt

        elif grado == 'Informática + matemáticas':
            url = link_horario_gim


        #Enviar el archivo
        bot.send_message(m.chat.id,url,reply_markup=hideBoard)

    except Exception as e:
        bot.reply_to(m,'Se ha producido un error, intentelo mas tarde')
        #exception_log(e,m)

# Comprobamos si existe el horario y se actua en consecuencia
def mandar_examenes(grado,m):

    path = '../archivos/'
    nombre_fichero = ''

    try:

        if grado == 'Informática':
            nombre_fichero = 'calendarioexamenes1617gii.pdf'
            url = link_horario_gii

        elif grado == 'Telecomunicaciones':
            nombre_fichero = 'calendarioexamenes1617gitt.pdf'
            url = link_horario_gitt

        elif grado == 'Informática + matemáticas':
            nombre_fichero = 'calendarioexamenes1617gim.pdf'
            url = link_horario_gim


        #Enviar el archivo
        bot.send_message(m.chat.id,url, reply_markup=hideBoard)


    except Exception as e:
        bot.reply_to(m,'Se ha producido un error, intentelo mas tarde')
        #exception_log(e,m)

# Función auxiliar usada por el comando "horario"
def aux_horario(m):

    grado = str(m.text)
    mandar_horario(grado,m)

# Función auxiliar usada por el comando "examenes"
def aux_examenes(m):

    grado = str(m.text)
    mandar_examenes(grado,m)

# Comprueba el tiempo del mensaje y el de arranque del bot, para evitar
# enviar mensajes que el bot recibio estando apagado
def check_time(m):
    if tiempo_arranque > m.date:
        return False
    else:
        return True
