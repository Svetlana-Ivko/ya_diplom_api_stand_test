# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API
import sender_stand_request

# Импортируем модуль data, содержащий данные для HTTP-запросов
import data

# Функция для позитивной проверки GET-запроса по трек-номеру
def positive_assert_get_order_by_track():
    # Создаем заказ
    track = sender_stand_request.post_new_order()
    # Проверяем, что заказ создан и у него есть трек-номер
    assert track is not None, "Трек-номер заказа равен None (null)"
    # Выполняем запрос на получение заказа по трек-номеру
    order_response = sender_stand_request.get_order_by_track(track)
    # Проверяем, что код ответа равен 200
    assert order_response.status_code == 200, f"Ожидался код 200, получен {order_response.status_code}"
    # Парсим в JSON
    response_data = order_response.json()
    # Проверяем, что значение ключа трекера заказа в JSON-ответе соответствует поисковому
    assert response_data["order"]["track"] == track, \
        f"Трек в ответе ({response_data['order']['track']}) не совпадает с ожидаемым ({track})"
# Тест 1. Успешное получение заказа по его трекеру
def test_get_order_by_track_success_response():
    positive_assert_get_order_by_track()
