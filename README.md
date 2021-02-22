Проект "Загрузчик изображений" создан с помощью фреймворков Django, Django REST Framework

В проекте реализованы API запросы:
POST запрос для отправки изображений: http://127.0.0.1:8000/api/v1/images/image/create   (ключ: image)
GET запрос для просмотра всех записей: http://127.0.0.1:8000/api/v1/images/all

Ограничения:
Загружаемое изображение должно быть меньше 200кб
Загружать изображения могут только авторизованные пользователи (инструкция ниже)

	Инструкция для загрузки изображений через Postman

Регистрация:
POST запрос http://127.0.0.1:8000/auth/users/   (ключи: username, password, email)

Авторизация:
POST запрос http://127.0.0.1:8000/auth/token/login  (ключи: username, password)

Получение токена:
После успешного прохождения авторизации, мы получим токен такого типа:
{"auth_token":"1617fd13c6fdecbcca8b56dd9c949acecca6aab5"}

Получение доступа к недоступному API запросу:
Вводим в Postman ссылку:  http://127.0.0.1:8000/api/v1/images/image/create
Переходим в Headers, добавляем поле Authorization, в ключ добавляем значение "Token 1617fd13c6fdecbcca8b56dd9c949acecca6aab5" (без кавычек)

Выход из системы (logout):
POST запрос  http://127.0.0.1:8000/auth/token/logout  (ключи в Headers: Authorization, Token 1617fd13c6fdecbcca8b56dd9c949acecca6aab5)
