from flask import Flask, render_template, request
from mashup import create_mashup
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)

SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
APP_PASSWORD = os.environ.get("APP_PASSWORD")

if not SENDER_EMAIL or not APP_PASSWORD:
    raise ValueError("Email credentials not configured in Railway variables.")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            singer = request.form['singer']
            num_videos = int(request.form['num_videos'])
            duration = int(request.form['duration'])
            email = request.form['email']

            zip_file = create_mashup(
                singer,
                num_videos,
                duration,
                singer.replace(" ", "_")
            )

            msg = EmailMessage()
            msg['Subject'] = f'{singer} Mashup'
            msg['From'] = SENDER_EMAIL
            msg['To'] = email
            msg.set_content("Your mashup is attached.")

            with open(zip_file, 'rb') as f:
                msg.add_attachment(
                    f.read(),
                    maintype='application',
                    subtype='zip',
                    filename=os.path.basename(zip_file)
                )

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(SENDER_EMAIL, APP_PASSWORD)
                smtp.send_message(msg)

            # Clean up after sending
            if os.path.exists(zip_file):
                os.remove(zip_file)

            return "Mashup created and emailed successfully!"

        except Exception as e:
            import traceback
            traceback.print_exc()
            return f"Error: {str(e)}"

    return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
