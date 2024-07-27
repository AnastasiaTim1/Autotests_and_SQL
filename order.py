# Анастасия Тимощук, 19-я когорта — Финальный проект. Инженер по тестированию плюс

import data
import sender_stand_request

def track_order():
    return str(sender_stand_request.post_new_order(data.order_body))

def positive(track):
   order_response = sender_stand_request.get_order_tract(track)
   assert order_response.status_code == 200

def test_kod_response():
     positive(track_order())