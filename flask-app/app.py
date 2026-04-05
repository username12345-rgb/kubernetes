from flask import Flask
import mysql.connector
import os
import time

app = Flask(__name__)

@app.route('/')
def db_check():
    time.sleep(1)

    db_connection = mysql.connector.connect(
        host = os.getenv('DB_HOST', 'localhost'),
        user = os.getenv('DB_USER', 'root'),
        password = os.getenv('DB_PASSWORD', 'root'),
        database = os.getenv('DB_NAME', 'test1')
    )
    if not db_connection:
        return "Не удалось подключиться к базе данных", 500
    
    db_cursor = db_connection.cursor()
    
    #создание таблицы
    db_cursor.execute("CREATE TABLE IF NOT EXISTS logs (id INT AUTO_INCREMENT PRIMARY KEY, message VARCHAR(255), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
    
    #запись новых данных
    msg = "новое сообщение, время: "
    db_cursor.execute("INSERT INTO logs (message) VALUES (%s)", (msg,))
    db_connection.commit()
    
    #чтение данных
    db_cursor.execute("SELECT message, created_at FROM logs ORDER BY id DESC")
    rows = db_cursor.fetchall()
    db_cursor.close()
    db_connection.close()
    
    response_html = "<h1>Подключено к базе данных (обновить страницу для проверки базу данных)</h1><ul>"
    for row in rows:
        response_html += f"<li>{row[0]} {row[1]}</li>"
    response_html += "</ul>"
    
    return response_html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
