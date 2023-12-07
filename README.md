# Product-markup-backend

Сервис для полуавтоматической разметки товаров

## сведения о команде

- [Константин Назаров](https://github.com/K1N88)
- [Дмитрий Луконин](https://github.com/LukoninDmitryPy)

## ссылка на Swagger

[http://81.31.246.17/docs](http://81.31.246.17/docs)

## инструкция по сборке и запуску

- Клонируем репозиторий
```
git@github.com:K1N88/product-markup-backend.git
```
- создаем переменные окружения по примеру env_example
- скачиваем образы с Docker Hub
```
sudo docker pull k1n8/prosept_app:latest
sudo docker pull hackaton1pros/prosept:latest
```
- переходим в папку infra/
```
cd infra/
```
- собираем и запускам контейнеры
```
sudo docker-compose up -d --build
```
- открываем главную страницу [http://81.31.246.17/](http://81.31.246.17/)

## стэк технологий

Python==3.10
Fastpi==0.78.0
SQLAlchemy==1.4.36
Alembic==1.7.7
Fastapi-users==10.0.6
Alembic==1.7.7
Pydantic==1.10.12
Gunicorn==21.2.0
Nginx
Sentry
