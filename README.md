# Django REST Framework Marketplace с авторизацией Simple JWT

## Описание

Это приложение на Django REST Framework включает систему авторизации с использованием Simple JWT и функционал маркетплейса для управления товарами. Пользователи могут регистрироваться, входить в систему, а также добавлять, редактировать и удалять товары.

## Установка

### Предварительные требования

- Python 3.6 или выше
- Django 3.0 или выше
- Django REST Framework
- Simple JWT

### Шаги установки

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/twe1n/marketplace.git
   cd marketplace
   ```

2. **Создайте виртуальное окружение:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # На Windows используйте: venv\Scripts\activate
   ```

3. **Установите зависимости:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Настройте базу данных:**

   В файле `settings.py` настройте параметры подключения к вашей базе данных.

5. **Создайте и примените миграции:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Создайте суперпользователя:**

   ```bash
   python manage.py createsuperuser
   ```

7. **Запустите сервер:**

   ```bash
   python manage.py runserver
   ```

## Использование

### Авторизация

- Для получения токена доступа выполните POST-запрос на `/api/token/` с параметрами `username` и `password`.

   ```bash
   curl -X POST http://localhost:8000/api/token/ -d "username=your_username&password=your_password"
   ```

- Чтобы получить обновленный токен, выполните POST-запрос на `/api/token/refresh/` с параметром `refresh`.

### API Маркетплейса

#### Получить список товаров

```http
GET /api/products/
```

#### Добавить товар

```http
POST /api/products/
```
**Запрос:**
```json
{
    "name": "Product Name",
    "description": "Product Description",
    "price": "100",
    "author": "user_id"
}
```

#### Обновить товар

```http
PUT /api/products/{id}/
```

**Запрос:**
```json
{
    "name": "Updated Product Name",
    "description": "Updated Description",
    "price": 150.0
}
```

#### Удалить товар

```http
DELETE /api/products/{id}/
```

## Структура проекта

```
project/
├── project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── ...
├── marketplace/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
├── authorization/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
└── manage.py
requirements.txt
```
