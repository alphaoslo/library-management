from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

DB_NAME = "books.db"

def get_db():
    return sqlite3.connect(DB_NAME)

# Create table if not exists
with get_db() as conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS books (
            book_id TEXT,
            book_name TEXT,
            author TEXT,
            department TEXT
        )
    """)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insert', methods=['POST'])
def insert():
    book_id = request.form['book_id']
    book_name = request.form['book_name']
    author = request.form['author']
    department = request.form['department']

    with get_db() as conn:
        conn.execute(
            "INSERT INTO books VALUES (?, ?, ?, ?)",
            (book_id, book_name, author, department)
        )

    return "Book inserted successfully!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
