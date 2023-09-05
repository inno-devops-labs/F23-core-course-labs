from your_app import app  # Замените 'your_app' на имя вашего приложения
import datetime

def test_index():
    client = app.test_client()

    # Ожидаем HTTP-код 200 (OK) при доступе к корневому URL
    response = client.get('/')
    assert response.status_code == 200

    # Проверяем, что в ответе есть текущее время в Москве
    moscow_time = datetime.datetime.now().strftime("%H:%M:%S")
    assert moscow_time.encode() in response.data