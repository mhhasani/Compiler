from telegram import (Update,
                      ParseMode,
                      InlineKeyboardMarkup,
                      InlineKeyboardButton)
from telegram.ext import (Updater,
                          CommandHandler,
                          MessageHandler,
                          Filters,
                          CallbackQueryHandler,
                          ConversationHandler,)
from main import DFA

def start(update: Update, context):
    update.message.bot.send_message(chat_id=update.message.chat_id, text="please send your dfa in the following format:\nstates\ninitial\naccepting\nalphabet\ntransitions\n\nfor example:\nq0 q1 q2 q3\nq0\nq3\n0 1\nq0:0>q0\nq0:1>q1\nq1:0>q2\nq1:1>q0\nq2:0>q3\nq2:1>q1\nq3:0>q2\nq3:1>q0")

def new_dfa(update: Update, context):
    dfa_data = update.message.text.split("\n")
    states = dfa_data[0].split()
    initial = dfa_data[1]
    accepting = dfa_data[2].split()
    alphabet = dfa_data[3].split()
    transitions = {}
    for transition in dfa_data[4:]:
        state, symbol, next_state = transition.split(":")[0], transition.split(":")[1].split(">")[0], transition.split(":")[1].split(">")[1]
        transitions[(state, symbol)] = next_state
    dfa = DFA(alphabet, states, transitions, initial, accepting)
    # send dfa graph
    photo = open(dfa.generate_dfa_graph(), 'rb')
    update.message.reply_photo(photo)
    # send dfa python code
    update.message.reply_text(dfa.generate_dfa_code())
    # send dfa cpp code
    update.message.reply_text(dfa.generate_dfa_code_cpp())
    
def main():
    print("bot started")
    updater = Updater("6167343455:AAFUNe4or98G1x3adbTG5v_uU7MbqsYjHl8")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text, new_dfa))

    updater.start_polling()
    updater.idle()
    print("bot stopped")

main()





