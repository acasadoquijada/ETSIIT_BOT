import time

#####################
# Registros del bot #
#####################

# Registro de actividad
def log(m):
    if m.content_type == 'text':
        if (m.chat.type == 'group' and m.text.startswith("/")) or m.chat.type == 'private':            
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
