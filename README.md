
Это приложение демонстрирует работу веб-сервиса на Flask, который подключается к базе данных MySQL. Оба сервиса развернуты в отдельных контейнерах внутри Kubernetes кластера (Minikube).

## Команды консоли

### Управление кластером
`minikube start --driver=docker`

`minikube stop`  
`minikube delete --all --purge`

### Подготовка Docker-окружения
`eval $(minikube docker-env)`  
*(Выполнять в каждом новом окне терминала перед сборкой образов)*

### Сборка образов
`docker build -t flask-app:latest ./flask-app`  
`docker build -t mysql-db:latest ./mysql-db`

### Развертывание в Kubernetes
`kubectl apply -f k8s-config.yaml`

### Откат изменений
`kubectl delete -f k8s-config.yaml --ignore-not-found`

### Проверка состояния
`kubectl get pods`  
`kubectl get services`

### Просмотр логов
`kubectl logs -l app=flask --tail=50 -f`

### Открытие приложения
`minikube service flask-service --url`

### Очистка образов
`docker rmi flask-app:latest mysql-db:latest`

## Быстрый запуск

1. Запустить кластер: `minikube start --driver=docker
2. Подключить Docker к Minikube: `eval $(minikube docker-env)`
3. Собрать образы: `docker build -t flask-app:latest ./flask-app && docker build -t mysql-db:latest ./mysql-db`
4. Развернуть приложение: `kubectl apply -f k8s-config.yaml`
5. Дождаться статуса `Running` у обоих подов: `kubectl get pods -w`
6. Открыть в браузере: `minikube service flask-service --url`

## Структура проекта

* `flask-app/` — Код приложения и Dockerfile для Flask.
* `mysql-db/` — Dockerfile для базы данных MySQL.
* `k8s-config.yaml` — Конфигурация для развертывания в Kubernetes.

## Проверка работы

После запуска открыть URL, полученный через `minikube service flask-service --url`. На странице отобразится сообщение об успешном подключении к базе данных и список записей. При обновлении страницы список будет пополняться новыми записями.
