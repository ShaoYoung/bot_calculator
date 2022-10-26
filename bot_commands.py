from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime

def calc(a, operation, b):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b
    else:
        return None

filename = 'db.log'
def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open(filename, 'a', encoding="utf-8") as file:
        file.write(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}, {update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    out_text = f'/help - помощь\n/rat - арифметика рациональных чисел\n/comp - арифметика комплексных чисел' \
               f'\nЧисла и операции вводить через пробелы\nНапример: /rat 5.6 + 3.3\n' \
               f'или /comp 3 + 0j + 7 - 1j'
    await update.message.reply_text(out_text)


async def rat_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    if msg.find(',') != -1:
        msg = msg.replace(',', '.')
    if msg.find(' ') != -1:
        msg = msg.split(' ')
        if len(msg) == 4:
            a = float(msg[1])
            operation = msg[2]
            b = float(msg[3])
            # eval слишком опасен для работы с внешними текстовыми переменными
            # result = eval(f'{a}{operation}{b}')
            result = calc(a, operation, b)
            out_text = f'{a} {operation} {b} = {round(result, 2)}'
        else:
            out_text = 'Не корректный ввод!'
    else:
        out_text = 'Не корректный ввод!'
    await update.message.reply_text(out_text)


async def comp_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    if msg.find(' ') != -1:
        msg = msg.split(' ')
        if len(msg) == 8:
            a = complex(f'{msg[1]}{msg[2]}{msg[3]}')
            operation = msg[4]
            b = complex(f'{msg[5]}{msg[6]}{msg[7]}')
            # eval слишком опасен для работы с внешними текстовыми переменными
            # result = eval(f'{a}{operation}{b}')
            result = calc(a, operation, b)
            out_text = f'{a} {operation} {b} = {result}'
        else:
            out_text = 'Не корректный ввод!'
    else:
        out_text = 'Не корректный ввод!'
    await update.message.reply_text(out_text)
