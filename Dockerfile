# Базовый образ для Python
FROM python:3.11.9

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл с зависимостями
COPY ./requirements.txt ./

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем остальные файлы проекта
COPY . .

EXPOSE 5000

# Указываем команду для запуска приложения
CMD ["python3", "app.py"]