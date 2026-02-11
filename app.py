from flask import Flask, render_template, request, send_file
from mashup import create_mashup
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)

SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
APP_PASSWORD = os.environ.get("APP_PASSWORD")

if not SENDER_EMAIL or not APP_PASSWORD:
    raise ValueError("Email environment variables not set properly.")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        singer = request.form['singer']
        num_videos = int(request.form['num_videos'])
        duration = int(request.form['duration'])
        email = request.form['email']

        try:
            zip_file = create_mashup(singer, num_videos, duration, singer.replace(" ", "_"))

            # Send email
            msg = EmailMessage()
            msg['Subject'] = 'Your Mashup File'
            msg['From'] = SENDER_EMAIL
            msg['To'] = email
            msg.set_content('Your mashup is attached.')

            with open(zip_file, 'rb') as f:
                file_data = f.read()
                msg.add_attachment(file_data, maintype='application', subtype='zip', filename=zip_file)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(SENDER_EMAIL, APP_PASSWORD)
                smtp.send_message(msg)

            return "Mashup created and sent successfully!"

        except Exception as e:
            return f"Error: {str(e)}"

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
