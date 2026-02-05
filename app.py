from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

FILE_NAME = "books.xlsx"

if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Book ID", "Book Name", "Author", "Department"])
    df.to_excel(FILE_NAME, index=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insert', methods=['POST'])
def insert():
    book_id = request.form['book_id']
    book_name = request.form['book_name']
    author = request.form['author']
    department = request.form['department']

    df = pd.read_excel(FILE_NAME)
    df.loc[len(df)] = [book_id, book_name, author, department]
    df.to_excel(FILE_NAME, index=False)

    return "Book inserted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
