import math

from rest_framework.exceptions import APIException

from .models import Table

dict_eq = {
    '>': '__gt',
    '<': '__lt',
    '=': '',
    'in': '__contains',
}

dict_thead = {
    'Название': 'name',
    'Количество': 'amount',
    'Расстояние': 'distance',
}

dict_sort = {
    'asc': '',
    '': '',
    'desc': '-'
}


class HTTP400(APIException):
    status_code = 400


def do_filter(value, thead, eq):
    if len(value) > 19 and thead in ['Количество', 'Расстояние']:
        raise HTTP400(f'{value} слишком большое число')
    keyword = dict_thead[thead] + dict_eq[eq]
    sorting_params_pack = {keyword: value}
    try:
        return Table.objects.filter(**sorting_params_pack)
    except ValueError:
        raise HTTP400(f'{thead} должно быть целым числом')


def do_sort(table, sort_by, sort_type):
    return table.order_by(dict_sort[sort_type] + dict_thead[sort_by])


def get_table_and_amount(data):
    limit = int(data['limit'])
    offset = int(data['offset'])
    value = data['value']
    if value:
        thead = data['thead']
        eq = data['eq']
        table = do_filter(value, thead, eq)
    else:
        table = Table.objects.all()
    sort_type = data['sort_type']
    if sort_type:
        sort_by = data['sort_by']
        table = do_sort(table, sort_by, sort_type)
    amount = math.ceil(len(table) / limit)
    return table[offset * limit:(offset + 1) * limit], amount
