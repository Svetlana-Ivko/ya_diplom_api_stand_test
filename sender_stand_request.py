# Импортируем модуль configuration, он содержит актуальный URL и путь для создания заказа
import configuration

# Импортируем модуль requests, который предназначен для отправки HTTP-запросов
import requests

# Импортируем данные для запросов из модуля data, в котором определены заголовки и тело запроса
import data

# Объявляем функцию для создания нового заказа
def post_new_order():
    order_body = data.order_body.copy()
    # POST-запрос для создания заказа
    response = requests.post(url=configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
        json=order_body,
        headers=data.header_order)
    return response.json()["track"]
# Объявляем функцию для получения заказа по трекеру
def get_order_by_track(track):
    # GET-запрос для получения заказа по трекеру
    response = requests.get(url=configuration.URL_SERVICE + configuration.GET_ORDERS_PATH,
                           params={"t": track})
    return response
