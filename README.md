# ETSIIT BOT
Bot de telegram en python3 sobre la ETSIIT de la universidad de Granada

La idea de este bot es proporcionar información sobre la escuela de manera simple y sencilla.

Nombre del bot: @ETSIITBOT

Por motivos de privacidad de los usuarios el bot no puede ser incluido en grupos.

##Funcionalidades

ETSIITBOT ahora es un poquito mas inteligente, al detectar que buscas el horario, menu o examenes
te responderá indicando como obtener lo que buscas

![Captura1](http://i1045.photobucket.com/albums/b460/Alejandro_Casado/ETSIITBOT/pasiva_zpsu03alnpi.png)

La interacción con ETSIITBOT se realiza de una manera natural.

![Captura2](http://i1045.photobucket.com/albums/b460/Alejandro_Casado/ETSIITBOT/horario1_zpsxbtn0gva.png)

Tras seleccionar el grado del que queramos el horario ETSIITBOT nos lo enviará

![Captura3](http://i1045.photobucket.com/albums/b460/Alejandro_Casado/ETSIITBOT/horario2_zpsmpepeu9a.png)

Esta interacción esta disponible para elegir el horario, los examenes y el menú de un dia concreto

Antes el bot respondia a los mensajes recibidos cuando estaba apagado, lo que podía ser molesto, ahora solo
responde a aquellos mensajes que reciba cuando este operativo.

##Comandos

* **/horario** - Ofrece los diferentes horarios a traves de un teclado
* **/examenes** - Proporciona los examenes del curso 2015/2016 para todos los grados.
* **/localizacion** - Localización de la escuela en google maps.
* **/contacto** - Información de contacto de la escuela.
* **/web** - Web de la escuela
* **/menu_semana** - Menú de la semada de los comedores de la ugr
* **/menu_dia** - Menú del día seleccionado
* **/ayuda** - Información detallada sobre las funciones.

##Estructura

ETSIITBOT cuenta con los siguientes módulos:

* **ayuda_pasiva.py** - Se encarga de la gestión de la ayuda pasiva
* **bot.py** - Crea el bot
* **etsiit_bot** - "Cuerpo" del bot, donde se definen los comandos a los que reacciona
* **funciones_auxiliares.py** - Una serie de funciones auxiliares usadas por el bot
* **menu.py** - Gestiona la obtención del menú de comedores
* **registros.py** - Funciones relacionadas con el registro de actividad y excepciones
* **teclados.py** - Creación de teclados

##Ficheros

Los ficheros usados tienen la siguiente estructura:

    |-- Bot
    |   |-- ayuda_pasiva.py
    |   |-- bot.py
    |   |-- etsiit_bot.py
    |   |-- funciones_auxiliares.py
    |   |-- menu.py
    |   |-- registros.py
    |   |-- teclados.py      
    |-- Horarios
    |   |-- horarios_gii.pdf
    |   |-- horarios_gim.pdf
    |   |-- horarios_git.pdf
    |-- examenes
    |   |-- examenes.pdf
    |   |-- examenes_gii.pdf
    |   |-- examenes_gitt.pdf
    |-- informacion
        |-- ayuda.txt
        |-- ayuda_pasiva_examenes.txt
        |-- ayuda_pasiva_horario.txt
        |-- ayuda_pasiva_menu.txt
        |-- comandos.txt
        |-- conf.py
        |-- registro.txt
        |-- start.txt
        
Algunos de los ficheros, como los examenes, horarios y registros no han sido subidos al repositorio por temas de limpieza y privacidad

Para crear el arbol de directorios he usado [mddir](https://www.npmjs.com/package/mddir)

**IMPORTANTE** Es necesario crear un archivo conf.py en la carpeta Bot con un string llamado token que corresponde al token necesario para acceder a la API de Telegram.

##Autores
![Alejandro Casado Quijada](https://github.com/acasadoquijada)
![Diego Granados](https://github.com/diegogran94)
acasadoquijada@gmail.com

[Licencia](https://github.com/acasadoquijada/ETSIIT_BOT/blob/master/LICENSE)
