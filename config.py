import os

# --- for email notification(s)
os.environ['SMTP_SERVER_ADDRESS'] = 'enter server address'
SMTP_SERVER_ADDRESS = os.environ.get('SMTP_SERVER_ADDRESS')
os.environ['TEST_SENDER_EMAIL'] = 'enter sender email'
TEST_SENDER_EMAIL = os.environ.get('TEST_SENDER_EMAIL')
os.environ['TEST_SENDER_EMAIL_PASSWORD'] = 'enter sender password'
TEST_SENDER_EMAIL_PASSWORD = os.environ.get('TEST_SENDER_EMAIL_PASSWORD')
os.environ['TEST_RECEIVER_EMAIL'] = 'enter receiver email'
TEST_RECEIVER_EMAIL = os.environ.get('TEST_RECEIVER_EMAIL')
