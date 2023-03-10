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
        # create last dfa python code of user
        with open(f"{update.message.from_user.id}.py", "w") as f:
            f.write(dfa.generate_dfa_code())
    except:
        update.message.reply_text("wrong format!\nplease send your dfa in the following format:\nstates\ninitial\naccepting\nalphabet\ntransitions\n\nfor example:\nq0 q1 q2 q3\nq0\nq3\n0 1\nq0:0>q0\nq0:1>q1\nq1:0>q2\nq1:1>q0\nq2:0>q3\nq2:1>q1\nq3:0>q2\nq3:1>q0")
    
    
def test_acceptance(update: Update, context):
    user_last_dfa_file = f"{update.message.from_user.id}.py"
    # check if user has last dfa
    if os.path.exists(user_last_dfa_file):
        # import user last dfa
        import_code = f"from {user_last_dfa_file} import DFA as UserDFA"
        # execute import code
        exec(import_code)
        # create user dfa object
        user_dfa = UserDFA()
        # check if user input is accepted by dfa
        if user_dfa.run(update.message.text):
            update.message.reply_text("accepted")
        else:
            update.message.reply_text("rejected")
    else:
        update.message.reply_text("please send your dfa first")
        
        
def main():
    updater = Updater("6167343455:AAFUNe4or98G1x3adbTG5v_uU7MbqsYjHl8")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text, new_dfa))

    updater.start_polling()
    updater.idle()

main()





