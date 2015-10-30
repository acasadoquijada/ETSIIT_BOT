import time
import pytest
import os

import telebot
from telebot import types
from telebot import util

should_skip = 'TOKEN' and 'CHAT_ID' not in os.environ

class TestTeleBot():

    def test_message_listener(self):
        msg_list = []
        for x in range(100):
            msg_list.append(self.create_text_message('Message ' + str(x)))
            
            
    def test_localizacion(self):
      
        tb = telebot.TeleBot(TOKEN)
        lat = 26.3875591
        lon = -161.2901042
        ret_msg = tb.send_location(CHAT_ID, lat, lon)
        assert int(ret_msg.location.longitude) == int(lon)
        assert int(ret_msg.location.latitude) == int(lat)