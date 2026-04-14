from datetime import datetime

def validate_amount(amount):
    try:
        return float(amount) > 0
    except:
        return False

def validate_date(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except:
        return False
