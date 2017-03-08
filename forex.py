from forex_python.converter import CurrencyRates
from email.mime.text import MIMEText
import smtplib

c = CurrencyRates()
GBP = c.get_rate('GBP', 'EUR')

print GBP
