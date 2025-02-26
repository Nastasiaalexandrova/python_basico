import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

logger = logging.getLogger(__name__)

# Email configuration
EMAIL_SENDER = "salon.romashka@example.com"
EMAIL_PASSWORD = "your_email_password"  # You should use environment variables for this in production
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587

def send_email(recipient, name, service, sub_option, additional_option, date_str, time_str):
    """
    Send booking confirmation email
    
    Args:
        recipient (str): Customer email
        name (str): Customer name
        service (str): Selected service
        sub_option (str): Service sub-option
        additional_option (str): Additional service option
        date_str (str): Date in 'YYYY-MM-DD' format
        time_str (str): Time slot
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Format date for display
        formatted_date = datetime.strptime(date_str, '%Y-%m-%d').strftime('%d.%m.%Y')
        
        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = recipient
        msg['Subject'] = "Салон красоты Ромашка - Подтверждение записи"
        
        body = f"""
        Уважаемый(ая) {name},
        
        Благодарим вас за запись в салон красоты Ромашка!
        
        Детали вашей записи:
        Услуга: {service}
        Опция: {sub_option}
        Дополнительно: {additional_option}
        Дата: {formatted_date}
        Время: {time_str}
        
        Мы будем ждать вас!
        
        С уважением,
        Салон красоты Ромашка
        Тел: +7 (123) 456-78-90
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_SENDER, recipient, text)
        server.quit()
        
        logger.info(f"Confirmation email sent to {recipient}")
        return True
    except Exception as e:
        logger.error(f"Error sending email: {e}", exc_info=True)
        return False

def send_cancellation_email(recipient, name, service, date_str, time_str):
    """
    Send booking cancellation email
    
    Args:
        recipient (str): Customer email
        name (str): Customer name
        service (str): Service that was booked
        date_str (str): Date in 'YYYY-MM-DD' format
        time_str (str): Time slot
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Format date for display
        formatted_date = datetime.strptime(date_str, '%Y-%m-%d').strftime('%d.%m.%Y')
        
        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = recipient
        msg['Subject'] = "Салон красоты Ромашка - Отмена записи"
        
        body = f"""
        Уважаемый(ая) {name},
        
        Ваша запись в салон красоты Ромашка была отменена:
        
        Услуга: {service}
        Дата: {formatted_date}
        Время: {time_str}
        
        Если вы не запрашивали отмену, пожалуйста, свяжитесь с нами.
        
        С уважением,
        Салон красоты Ромашка
        Тел: +7 (123) 456-78-90
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_SENDER, recipient, text)
        server.quit()
        
        logger.info(f"Cancellation email sent to {recipient}")
        return True
    except Exception as e:
        logger.error(f"Error sending cancellation email: {e}", exc_info=True)
        return False

def send_reminder_email(recipient, name, service, sub_option, additional_option, date_str, time_str):
    """
    Send appointment reminder email (can be scheduled to run 24h before appointment)
    
    Args:
        recipient (str): Customer email
        name (str): Customer name
        service (str): Selected service
        sub_option (str): Service sub-option
        additional_option (str): Additional service option
        date_str (str): Date in 'YYYY-MM-DD' format
        time_str (str): Time slot
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Format date for display
        formatted_date = datetime.strptime(date_str, '%Y-%m-%d').strftime('%d.%m.%Y')
        
        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = recipient
        msg['Subject'] = "Салон красоты Ромашка - Напоминание о записи"
        
        body = f"""
        Уважаемый(ая) {name},
        
        Напоминаем о вашей записи в салон красоты Ромашка:
        
        Услуга: {service}
        Опция: {sub_option}
        Дополнительно: {additional_option}
        Дата: {formatted_date}
        Время: {time_str}
        
        Мы будем ждать вас!
        
        С уважением,
        Салон красоты Ромашка
        Тел: +7 (123) 456-78-90
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_SENDER, recipient, text)
        server.quit()
        
        logger.info(f"Reminder email sent to {recipient}")
        return True
    except Exception as e:
        logger.error(f"Error sending reminder email: {e}", exc_info=True)
        return False