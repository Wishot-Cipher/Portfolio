from flask import Flask, render_template, request
from flask_mail import Message, Mail
import os

app = Flask(__name__)


@app.route('/home')
@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        subject = request.form.get('subject')
        email = request.form.get('email')
        message = request.form.get('message')
        msg = Message(f'New Message from {email}', sender=f'{email}',
                      recipients=['wishotstudio@gmail.com'])
        msg.body = f"""
     Name :  {name}

    Email :  {email}

    Subject :  {subject}

    Message :  {message}

               """
        mail.send(msg)
    return render_template('index.html')


@app.route('/inner page')
def inner_page():
    return render_template('inner-page.html')


@app.route('/api details')
def api_details():
    return render_template("portfolio's details/api's-details[1].html")


@app.route('/apps details')
def blog_app_details():
    return render_template("portfolio's details/portfolio-details.html")


@app.route('/netflix clone')
def netflix_clone():
    return render_template("portfolio's details/Netflix-clone.html")


@app.route('/yoste clone')
def yoste_clone():
    return render_template("portfolio's details/Yoste-clone.html")


@app.route('/others')
def studio():
    return render_template("portfolio's details/portfolio-details copy.html")


@app.route('/calculator')
def calculator():
    return render_template("portfolio's details/calculator.html")


@app.route('/todo list')
def todo_list():
    return render_template("portfolio's details/Todo-list.html")

@app.route('/expense tracker')
def expense():
    return render_template("portfolio's details/expense-Tracker.html")


app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = os.environ.get('MAIL_USERNAME')
app.config["MAIL_PASSWORD"] = os.environ.get('MAIL_PASSWORD')
app.config["MAIL_ASCII_ATTACHMENTS"] = False

mail = Mail(app)

if __name__ == '__main__':
    app.run(debug=True, port=8500)
