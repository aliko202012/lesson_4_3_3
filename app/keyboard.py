from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton


start_button = [
    [KeyboardButton(text='Направления'),
    KeyboardButton(text='Geeks')]
]


start_keyboard = ReplyKeyboardMarkup(keyboard=start_button, resize_keyboard=True)

direction_inline = [
   [InlineKeyboardButton(text='Backend',callback_data='back'),
    InlineKeyboardButton(text='Frontend',callback_data='front'),
    InlineKeyboardButton(text='UX-UI',callback_data='uxui'),
    InlineKeyboardButton(text='Android',callback_data='android')]
]


direction_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=direction_inline,resize_keyboard=True)
keyboargeeks = [
    [InlineKeyboardButton(text='Geeks',url='https://geeks.kg/'),
     InlineKeyboardButton(text='Geeks pro',url='https://geeks.kg/geeks-pro'),
     InlineKeyboardButton(text='Geeks studio',url='https://geekstudio.kg/')]
]
keyboard_geeks_markup = InlineKeyboardMarkup(inline_keyboard=keyboargeeks,resize_keyboard=True)

backen = [
    [InlineKeyboardButton(text='Aiogram',callback_data='aiogram'),
     InlineKeyboardButton(text='Python',callback_data='python'),
     InlineKeyboardButton(text='django',callback_data='dj')]
]
backen_keyboard = InlineKeyboardMarkup(inline_keyboard=backen,size_keyboard=True)


fronte = [
    [InlineKeyboardButton(text='HTML',callback_data='html'),
     InlineKeyboardButton(text='SCC',callback_data='scc'),
     InlineKeyboardButton(text='JS',callback_data='js')]
]
fronte_keyboard = InlineKeyboardMarkup(inline_keyboard=fronte,resize_keyboard=True)
dizain = [
    [InlineKeyboardButton(text='Figma',callback_data='figma')]
]
dizain_keyboard = InlineKeyboardMarkup(inline_keyboard=dizain,resize_keyboard=True)
androi = [
    [InlineKeyboardButton(text='Android studio',callback_data='ands')]
]
andrioid_keyboard = InlineKeyboardMarkup(inline_keyboard=androi, resize_keyboard=True)