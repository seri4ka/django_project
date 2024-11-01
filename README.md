# Strategies Marketplace

Этот проект представляет собой маркетплейс для продажи и покупки алгоритмических торговых стратегий. Он реализован на Django и предназначен для создания платформы, где продавцы могут предлагать свои стратегии, а покупатели — приобретать их.

## Функционал
- Каталог стратегий с подробной информацией о каждой стратегии
- Административная панель для управления стратегиями
- Возможность добавления новых стратегий через интерфейс администрирования

## Установка и запуск проекта

### Требования
- Python 3.8+
- Django 4.x
- Виртуальное окружение (рекомендуется)
- Pillow для обработки изображений

### Установка

1. Клонируйте репозиторий:
   ```bash
   git clone <URL_твоего_репозитория>
   cd strategies_market
   ```

2. Создайте виртуальное окружение:
  ```bash
  python -m venv venv
  ```

3. Активируйте виртуальное окружение:
   - На Windows: `venv\Scripts\activate`
   - На macOS/Linux: `source venv/bin/activate`

4. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

5. Создайте миграции и настройте базу данных:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

6. Создайте суперпользователя для доступа к админке:
  ```bash
  python manage.py createsuperuser
  ```

7. Запустите сервер разработки:
  ```bash
  python manage.py runserver
  ```

8. Перейдите в браузере по адресу ```http://127.0.0.1:8000/``` и убедитесь, что проект работает.

## Структура проекта

- `marketplace/` — настройки Django проекта
- `strategies/` — приложение для управления стратегиями
- `venv/` — виртуальное окружение (не включено в репозиторий)

## Будущие доработки
- Реализовать страницу деталей для каждой стратегии
- Добавить фильтрацию и поиск по стратегиям
- Интеграция корзины и оплаты

## Лицензия
Этот проект находится под лицензией MIT. Подробности см. в файле LICENSE.