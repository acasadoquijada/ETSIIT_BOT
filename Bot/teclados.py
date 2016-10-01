from telebot import types

####################################
# Definimos los distintos teclados #
####################################

# Teclado para elegir el menu
teclado_menu = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True,selective=True)
teclado_menu.add('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sábado')

# Teclado para elegir el horario
teclado_horario = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True,selective=True)
teclado_horario.add('Informática', 'Telecomunicaciones', 'Informática + matemáticas')

# Teclado para elegir los examenes
teclado_examenes = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True,selective=True)
teclado_examenes.add('Informática', 'Telecomunicaciones', 'Informática + matemáticas')

# Ocultamos el teclado
hideBoard = types.ReplyKeyboardHide()
