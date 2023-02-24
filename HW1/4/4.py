FILE = "index.html"
# FILE = "index2.html"

with open(FILE, "r") as f:
    text = f.read().replace("\n", "").split("\"")
    temp_text = []
    for i in range(len(text)):
        if i == 0:
            temp_text += text[i].split()
        elif text[i-1][-1] == "=":
            temp_text += [text[i]]
        else:
            temp_text += text[i].split() 
    text = temp_text
    temp_text = []
    for i in range(len(text)):
        temp_text += text[i].split('<')
    text = temp_text
    temp_text = []
    for i in range(len(text)):
        temp_text += text[i].split('>')
    text = temp_text
        
        
    for i in range(len(text)):
        if text[i] == "":
            continue
        is_attribiute = text[i-1][-1] == "=" if i != 0 and text[i-1] else False
        close_tag = text[i].split('/')
        if is_attribiute:
            ATTRIBUTE = text[i-1][:-1]
            VALUE = '"' + text[i] + '"'
            print(f'ATTRIBUTE: {ATTRIBUTE} VALUE: {VALUE}')
        elif len(close_tag) == 2:
            CLOSING_TAG = close_tag[1]
            print(f'CLOSING_TAG: {CLOSING_TAG}')
        elif text[i][-1] != "=":
            OPENING_TAG = text[i]
            print(f'OPENING_TAG: {OPENING_TAG}')