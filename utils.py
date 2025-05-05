import os
import random
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_verification_code(email, verification_code):
    """
    Send a verification code to the provided email using Timeweb Cloud SMTP server.
    
    Args:
        email (str): The email address to send the verification code to
        verification_code (str): The verification code to send
        
    Returns:
        tuple: (success, message) where success is a boolean and message is a descriptive string
    """
    # SMTP server configurations
    smtp_server = 'smtp.timeweb.ru'
    smtp_port = 465
    smtp_username = 'info@help-droplucky.ru'
    smtp_password = 'v6wtoznle4'
    
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = email
    msg['Subject'] = 'Ваш код подтверждения'
    
    # Email body
    body = f"""
    <html>
    <body>
        <h2>Код подтверждения</h2>
        <p>Ваш код подтверждения: <strong>{verification_code}</strong></p>
        <p>Этот код истечет через 10 минут.</p>
        <p>Если вы не запрашивали этот код, пожалуйста, проигнорируйте это письмо.</p>
    </body>
    </html>
    """
    msg.attach(MIMEText(body, 'html'))
    
    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP_SSL(smtp_server, smtp_port, timeout=10) as smtp:
            smtp.login(smtp_username, smtp_password)
            smtp.send_message(msg)
        return True, 'Код подтверждения успешно отправлен'
    except smtplib.SMTPAuthenticationError:
        logging.error("SMTP Authentication Error: Invalid username or password")
        return False, 'Ошибка аутентификации на SMTP сервере'
    except smtplib.SMTPException as e:
        logging.error(f"SMTP Error: {str(e)}")
        return False, f'Ошибка SMTP: {str(e)}'
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return False, f'Непредвиденная ошибка: {str(e)}'
