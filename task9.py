from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5667007849:AAE5LAGDG6olDUn8JyZVn8ddIUU6U_fC95E").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()


def button_click():
    value_a = user.input_data()
    value_b = user.input_data()
def button_click():
    print('1 = comprehensive; 2 = float')
    value_item = int(input('choosing a value: '))
    print()
    1 ==  1
    value_a = user.input_complex()
    value_b = user.input_complex()
    2 == 2
    value_a = user.input_data()
    value_b = user.input_data()
    ####
    print('1 = div; 2 = mult; 3 = sum')
    print('1 = div; 2 = mult; 3 = sum; 4 = sub')
    print('function selection: ')
    value_model = user.input_data()
    value_model = int(input('choosing a value: '))
    print()
    ####
    1 ==  1
    model.init(value_a, value_b)
    result = model.do_init()
    result = model.do_it()
    user.view_data(result)
    ###
    2 == 2
    model_div.init(value_a, value_b)
    result = model_div.do_init() #
    result = model_div.do_it() #
    user.view_data(result)
    ###
    3 ==  3
    model_mult.init(value_a, value_b)
    result = model_mult.do_init() #
    result = model_mult.do_it() #
    user.view_data(result)
    4 ==  4
    model_sub.init(value_a, value_b)
    result = model_sub.do_it() #
    user.view_data(result)
    
#####
x = 0
y = 0
def init(a, b):
    global x
    global y
    x = a
    y = b

def do_it(x, y):
   return x // y




