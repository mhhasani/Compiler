from antlr4 import *
from XMLLexer import XMLLexer
from XMLParser import XMLParser

# Load the XML file
with open('data.xml', 'r') as f:
    input_stream = InputStream(f.read())

# Create a lexer and parser
lexer = XMLLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = XMLParser(token_stream)

# Parse the XML file
tree = parser.document()
