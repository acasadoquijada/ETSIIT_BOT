import re
import requests
from bs4 import BeautifulSoup
from lxml import html
import telebot 
from bot import bot
from teclados import * 


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
    
#Función auxiliar usado por menu_dia
def aux_menu_dia(m):
    
    try:
        
        dias = { 'Lunes': 0, 'Martes': 1, 'Miercoles': 2,'Jueves': 3,'Viernes': 4,'Sabado': 5}
        
        dia_seleccionado = str(m.text)
        
        info_dias = obtener_menu()
        
        if(len(info_dias)==0):
            bot.reply_to(m,'Hay un error en la web de comedores, intentelo mas tarde',reply_markup=hideBoard)

        else:
        
            mensaje = "¡Hola!\n\nAquí tienes el menú del " + dia_seleccionado.lower() + ", ¡Buen provecho! \n\n"
            
            aux = BeautifulSoup(info_dias[dias[dia_seleccionado]],"lxml")
    
    
            mensaje += obtener_menu_dia(aux)
                    
            mensaje += "Precio por menú: 3,5€"
    
            bot.reply_to(m, mensaje, reply_markup=hideBoard) 
                
    except Exception as e:
        bot.reply_to(m,'Se ha producido un error, intentelo mas tarde')
        #exception_log(e,m)