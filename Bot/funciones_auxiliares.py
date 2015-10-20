from bot import bot
import os.path
from teclados import *
import urllib.request, urllib.parse, urllib.error

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
        
            urllib.request.urlretrieve(url, path + nombre_fichero)
    
            enviar_archivo(m,path + nombre_fichero)
            
    except Exception as e:
        bot.reply_to(m,'Se ha producido un error, intentelo mas tarde')
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