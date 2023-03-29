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
import os

TOKEN = "6167343455:AAFUNe4or98G1x3adbTG5v_uU7MbqsYjHl8"
WEBHOOK_URL = f"https://dfa2code.pythonanywhere.com/{TOKEN}"
# get a free port from the environment variable PORT
PORT = int(os.environ.get('PORT', '8000'))

class UserDFA:
    def __init__(self, alphabet, states, start_state, accepting_states, transitions):
        self.alphabet = alphabet
        self.states = states
        self.start_state = start_state
        self.accepting_states = accepting_states
        self.transitions = transitions

    def run(self, input_string):
        current_state = self.start_state
        for symbol in input_string:
            current_state = self.transitions.get((current_state, symbol))
            if current_state is None:
                return False
        return current_state in self.accepting_states
    
users_dfa = {}
    
def start(update: Update, context):
    update.message.reply_text("please send your dfa in the following format:\nstates\ninitial\naccepting\nalphabet\ntransitions\n\nfor example:\nq0 q1 q2 q3\nq0\nq3\n0 1\nq0:0>q0\nq0:1>q1\nq1:0>q2\nq1:1>q0\nq2:0>q3\nq2:1>q1\nq3:0>q2\nq3:1>q0")

def new_dfa(update: Update, context):
    try:
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
        python_code_file = open("dfa.py", "rb")
        update.message.reply_document(python_code_file)
        # send dfa cpp code
        cpp_code_file = open("dfa.cpp", "rb")
        update.message.reply_document(cpp_code_file)
        # add dfa to user dfa list
        users_dfa[update.message.from_user.id] = UserDFA(alphabet, states, initial, accepting, transitions)

    except:
        update.message.reply_text("wrong format!\nplease send your dfa in the following format:\nstates\ninitial\naccepting\nalphabet\ntransitions\n\nfor example:\nq0 q1 q2 q3\nq0\nq3\n0 1\nq0:0>q0\nq0:1>q1\nq1:0>q2\nq1:1>q0\nq2:0>q3\nq2:1>q1\nq3:0>q2\nq3:1>q0")
    
    
def get_test_input(update: Update, context):
    update.message.reply_text("please send your input:")
    return 1    
    
def test_acceptance(update: Update, context):
    input_string = update.message.text
    user_dfa = users_dfa.get(update.message.from_user.id)
    if user_dfa is None:
        update.message.reply_text("please send your dfa first")
    else:
        if user_dfa.run(input_string):
            update.message.reply_text("accepted")
        else:
            update.message.reply_text("rejected")
        
    return ConversationHandler.END
        

def main():
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(ConversationHandler(
        entry_points=[CommandHandler('test', get_test_input)],
        states={
            1: [MessageHandler(Filters.text, test_acceptance)]
        },
        fallbacks=[]
    ))
    dispatcher.add_handler(MessageHandler(Filters.text, new_dfa))

    # Set the webhook for the bot
    updater.start_webhook(url_path=TOKEN, webhook_url=WEBHOOK_URL, port=PORT)
    updater.bot.set_webhook(WEBHOOK_URL)
    updater.idle()
    
if __name__ == "__main__":
    main()




