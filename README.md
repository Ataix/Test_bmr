
# Test exercise
### Python 3.11, Django 4.2, DRF

### Разработано в соответствии с заданием:
#### API для интернет-магазина с базовым функционалом управления товарами, заказами и пользователями

1. Аутентификация и регистрация пользователей. JWT
2. Создание, чтение, обновление и удаление (CRUD) товаров
3. Просмотр списка товаров с возможностью фильтрации по различным параметрам: название, категория, цена
4. Добавление товаров в корзину пользователем. (Create, List)
5. Тесты по apps. Запуск стандартный python3 manage.py test
6. Развернуть приложение и базу данных в Docker-контейнерах с использованием docker-compose

### Допольнительные бонусы:
1. Документация Swagger.
2. Модель отзывов к товарам - Review
3. Админ панель django

#### Список эндпонтов доступен по ссылке localhost/api/schema/swagger-ui/

* Перед запуском необходимо заполнить .env (для локального запуска) .env.dev (docker запуск). Шаблоны .env-example и .env.dev-example
* В .env и .env.dev есть возможность выбора бд. Локально по умолчания - sqlite. Через докер - postgres

### Запуск:
    1.  docker-compose build
    2.  docker-compose up
