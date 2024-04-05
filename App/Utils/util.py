from email.utils import formatdate
import re, string, random, datetime
from datetime import date, datetime, timedelta

class Util:

    def calculate_age(self, born):
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def check_email(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.search(regex, email)):
            return True
        else:
            return False

    def passwordGenerator(self, size=8, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
        return ''.join(random.choice(chars) for _ in range(size))

    def validateDateTime(self, data, typeVal, dateformat=None):
        formatDate = "%Y-%m-%d"
        formatTime = "%H:%M:%S"
        formatDateTime = "%Y-%m-%d %H:%M:%S"
        res = False
 
        if typeVal == 'datetime':
            
            if not dateformat == None:
                formatDateTime = dateformat

            try:
                res = bool(datetime.strptime(data, formatDateTime))
            except ValueError:
                res = False
        
        elif typeVal == 'date':
            
            if not dateformat == None:
                formatDate = dateformat

            try:
                res = bool(datetime.strptime(data, formatDate))
            except ValueError:
                res = False

        elif typeVal == 'time':
            
            if not dateformat == None:
                formatTime = dateformat

            try:
                res = bool(datetime.strptime(data, formatTime))
            except ValueError:
                res = False

        return res