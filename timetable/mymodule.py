def num_to_day(param):
    if param == 0:
        return 'Суббота'
    if param == 1:
        return 'Воскресенье'
    if param == 2:
        return 'Понедельник'
    if param == 3:
        return 'Вторник'
    if param == 4:
        return 'Среда'
    if param == 5:
        return 'Четверг'
    if param == 6:
        return 'Пятница'



def code_of_month(month):
    if month == '01' or month == '10':
        return 1
    if month == '02' or month == '03' or month == '11':
        return 4
    if month == '04' or month == '07':
        return 0
    if month == '05':
        return 2
    if month == '06':
        return 5
    if month == '08':
        return 3
    if month == '09' or month == '12':
        return 6

def code_of_year(year):
    return (6 + int(year[2:]) + int(year[2:])//4) % 7

def code_of_day(code_of_year, code_of_month, day):
    return (code_of_year + code_of_month + day) % 7


def parse(date):
    c_o_y = code_of_year(date[:4])
    c_o_m = code_of_month(date[5:7])
    c_o_d = int(date[8:])
    return num_to_day(code_of_day(c_o_y, c_o_m, c_o_d))
