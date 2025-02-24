import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

# Email Configuration
SMTP_SERVER = "smtp.gmail.com"  # Change based on your email provider
SMTP_PORT = 587
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_password"
RECEIVER_EMAIL = "receiver_email@example.com"

def get_daily_report():
    """Generate or fetch the daily report."""
    today = datetime.date.today().strftime("%Y-%m-%d")
    report_content = f"Daily Report for {today}\n\n- Task 1: Completed\n- Task 2: Pending\n- Task 3: In Progress"
    return report_content

def send_email(report):
    """Send the email with the daily report."""
    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = "Daily Report"
        
        msg.attach(MIMEText(report, 'plain'))
        
        context = ssl.create_default_context()
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls(context=context)
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    daily_report = get_daily_report()
    send_email(daily_report)
