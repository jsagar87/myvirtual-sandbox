from flask import Flask
import pymysql as mysql

app = Flask(__name__)


@app.route("/")
def main():
    connection = mysql.connect(host='127.0.0.1',
                               user='root',
                               password='root',
                               database='db',
                               port=6603,
                               charset='utf8mb4',
                               cursorclass=mysql.cursors.DictCursor
                               )

    with connection:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
            cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
            cursor.execute(sql, ('webmaster@python.org',))
            result = cursor.fetchone()
            print(result)
