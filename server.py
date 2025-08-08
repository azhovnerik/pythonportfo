# from urllib import request
import csv

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/<username>/<int:post_id>')
def hello_world(username, post_id):
    return render_template('index.html', name=username, post_id=post_id)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', 'a') as f:
      email = data.get('email')
      subject = data.get('subject')
      message = data.get('message')
      file = f.write(f'{email},{subject},{message}\n')

def write_to_csv(data):
    with open('database.csv', 'a', newline='') as db2:
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')
        csv_writer = csv.writer(db2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=('GET', 'POST'))
def submit_form():
    # return render_template('login.html')
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect("thankyou.html")
    else:
        return "something went wrong"
