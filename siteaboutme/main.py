from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route("/")
def index():
    conn = psycopg2.connect(
        dbname=os.environ['DATABASE_NAME'],
        user=os.environ['DATABASE_USERNAME'],
        password=os.environ['DATABASE_PASSWORD'],
        host=os.environ['DATABASE_HOST']
    )

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM table1 LIMIT 10')
    records = cursor.fetchall()

    cursor.close()
    conn.close()

    return '<h1>Hello from my First site with Docker</h1>' + f'{"<p>".join(map(str, records))}'
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4000)
