import time
import pytest
import os

import telebot
from telebot import types
from telebot import util

should_skip = 'TOKEN' and 'CHAT_ID' not in os.environ

class TestTeleBot():

    def test_localizacion(self):
      
        tb = telebot.TeleBot(TOKEN)
        lat = 37.196689
        lon = -3.624534
        ret_msg = tb.send_location(CHAT_ID, lat, lon)
        assert int(ret_msg.location.longitude) == int(lon)
        assert int(ret_msg.location.latitude) == int(lat)
        print("Test localizacion pasado con exito")