import datetime

def dateformat(value, format="%d-%b-%Y"):
    if isinstance(value, datetime.date):
        return value.strftime(format)
    return value

filters = {}
filters['dateformat'] = dateformat
