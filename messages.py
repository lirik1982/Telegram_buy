help_message = '''
Отправьте команду /buy, чтобы перейти к покупке.
Узнать условия можно по команде /terms
'''
start_message = 'Привет! Это тест платежей в Telegram!\n' + help_message

pre_buy_demo_alert = '''\
Счет для оплаты:
'''

terms = '''\
Условия!
'''

item_title = 'Аналоговый телефон'
item_description = '''\
Поможет выжить после апокалипсиса!
'''

UK_error = '''\
В данную страну доставка невозможна!
'''

successful_payment = '''
Платеж на сумму '{total_amount} {currency}' прошел успешно! '''

MESSAGES = {
    'start': start_message,
    'help': help_message,
    'pre_buy_demo_aler': pre_buy_demo_alert,
    'terms': terms,
    'item_title': item_title,
    'item_description': item_description,
    'AU_error': UK_error,
    'successful_payment': successful_payment,
}