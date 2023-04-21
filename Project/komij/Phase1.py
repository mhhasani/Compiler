from antlr4 import *
from gen.XMLLexer import XMLLexer
from gen.XMLParser import XMLParser
from gen.XMLParserListener import XMLParserListener


class XMLParserListener(ParseTreeListener):
    def __init__(self):
        self.comboBox = []

    def enterElement(self, ctx:XMLParser.ElementContext):
        #print(ctx.children[1].getText())
        if(ctx.children[1].getText() == "combobox"):
            self.comboBox.append(ctx.children[1].getText())


def find_combobox(file_path):
    stream = FileStream(file_path)
    lexer = XMLLexer(stream)
    token_stream = CommonTokenStream(lexer)
    parser = XMLParser(token_stream)
    parse_tree = parser.document()
    myClass = XMLParserListener()
    walker = ParseTreeWalker()
    walker.walk(myClass, parse_tree)
    return myClass.comboBox


if __name__ == '__main__':
    address = "compilerProject.xml"
    answer = find_combobox(address)
    print(answer)