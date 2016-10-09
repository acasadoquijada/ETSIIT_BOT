from bot import bot
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
                
            if("menu" in m.text.lower() and m.text[0] != "/"):
                mensaje = open('../informacion/ayuda_pasiva_menu.txt', 'r').read()
                bot.reply_to(m,mensaje)
        
    except Exception as e:
        exception_log(e,m)