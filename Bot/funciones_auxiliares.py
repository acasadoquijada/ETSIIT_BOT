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
        path = '../docs/'

        if grado == 'Informática':
            nombre_fichero = 'horariosgii1617definitivos.pdf'
            url = link_horario_gii

        elif grado == 'Telecomunicaciones':
            nombre_fichero = 'horariosgitt1617definitivos.pdf'
            url = link_horario_gitt

        elif grado == 'Informática + matemáticas':
            nombre_fichero = 'horariosgim1617definitivos.pdf'
            url = link_horario_gim


        #Si el pdf no esta descargado
        if not os.path.isfile(path + nombre_fichero):
            #Lo descargamos
            urllib.request.urlretrieve(url, path + nombre_fichero)

        #Enviar el archivo
        enviar_archivo(m,path + nombre_fichero)

    except Exception as e:
        bot.reply_to(m,'Se ha producido un error, intentelo mas tarde')
        print(str(e))
        #exception_log(e,m)

# Comprobamos si existe el horario y se actua en consecuencia
def mandar_examenes(grado,m):

    try:
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
