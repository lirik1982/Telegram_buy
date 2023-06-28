from aiogram.types import Message, ShippingOption, ShippingQuery, LabeledPrice, PreCheckoutQuery
from aiogram.types.message import ContentType

from messages import MESSAGES
from config import PAYMENTS_TOKEN, item_url
from main import dp, bot

PRICES = [
    LabeledPrice(label='Gun', amount=10000),
    LabeledPrice(label='Подарочная упаковка', amount=10000)
]


SUPERSSPEED_SHIPPING_OPTION = ShippingOption(
    id = 'superspeed',
    title='супербыстрая'
).add(LabeledPrice('Лично в руки', 10000))

POST_SHIPPNG_OPTION = ShippingOption(
    id = 'post',
    title='Почта России'
)


POST_SHIPPNG_OPTION.add(LabeledPrice('Картонная коробка', 10000))
POST_SHIPPNG_OPTION.add(LabeledPrice('Срочное отправление', 10000))

PICKUP_SHIPPING_OPTION = ShippingOption(
    id = 'pickup',
    title='Самовывоз'
)

PICKUP_SHIPPING_OPTION.add(LabeledPrice('Самовывоз в Мурманске', 10000))

@dp.message_handler(commands=['start'])
async def start_smd(message: Message):
    await message.answer(MESSAGES['start'])

@dp.message_handler(commands=['help'])
async def help_smd(message: Message):
    await message.answer(MESSAGES['help'])

@dp.message_handler(commands=['terms'])
async def terms_smd(message: Message):
    await message.answer(MESSAGES['terms'])

@dp.message_handler(commands=['buy'])
async def buy_process(message: Message):
    await bot.send_invoice(message.chat.id,
                           title=MESSAGES['item_title'],
                           description=MESSAGES['item_description'],
                           provider_token=PAYMENTS_TOKEN,
                           currency='rub',
                           photo_url=item_url,
                           photo_width=512,
                           photo_height=512,
                           photo_size=512,
                           need_email=True,
                           need_phone_number=True,
                           is_flexible=True,
                           prices=PRICES,
                           start_parameter='example',
                           payload='some_invoice')
    
@dp.shipping_query_handler(lambda q: True)
async def shipping_process(shipping_query: ShippingQuery):
    if shipping_query.shipping_address.country_code == 'UK':
        return await bot.answer_shipping_query(
            shipping_query.id,
            ok=False,
            error_message=MESSAGES['UK_error']
        )

    shipping_options = [SUPERSSPEED_SHIPPING_OPTION]

    if shipping_query.shipping_address.country_code == 'RU':
        shipping_options.append(POST_SHIPPNG_OPTION)
        if shipping_query.shipping_address.city == 'Санкт-Петербург':
            shipping_options.append(PICKUP_SHIPPING_OPTION)

    await bot.answer_shipping_query(
        shipping_query.id,
        ok=True,
        shipping_options=shipping_options
    )

@dp.pre_checkout_query_handler(lambda q: True)
async def checkoyt_process(pre_checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: Message):
    await bot.send_message(
        message.chat.id,
        MESSAGES['successful_payment'].format(total_amount=message.successful_payment.total_amount,
                                              currency=message.successful_payment.currency)
    )
