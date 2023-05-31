from antlr4 import *
from XMLLexer import XMLLexer
from XMLParser import XMLParser

# Create an input stream from the data.xml file
input_stream = InputStream(open('data.xml').read())

# Create a lexer and parser
lexer = XMLLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = XMLParser(token_stream)

# Parse the XML code and get the root of the parse tree
tree = parser.document()
parse_tree = tree.children[0]

# Print the parse tree
print(parse_tree.toStringTree(recog=parser))

# Import the necessary classes from the Python AST module
from ast import Module, Name, Load, Str, Attribute, Num, BoolOp, And, Or, List, Tuple

# Convert the parse tree to an AST
def to_ast(parse_tree):
    print(parse_tree.getText())
    if parse_tree.getText() == 'document':
        return Module(body=[to_ast(child) for child in parse_tree.children])
    elif parse_tree.getText() == 'element':
        return to_ast(parse_tree.children[0])
    elif parse_tree.getText() == 'content':
        return to_ast(parse_tree.children[0])
    elif parse_tree.getText() == 'STRING':
        return Str(s=parse_tree.getText()[1:-1])
    elif parse_tree.getText() == 'Name':
        return Name(id=parse_tree.getText(), ctx=Load())
    elif parse_tree.getText() == 'attribute':
        return Attribute(value=to_ast(parse_tree.children[0]), attr=to_ast(parse_tree.children[1]), ctx=Load())
    elif parse_tree.getText() == 'chardata':
        return Str(s=parse_tree.getText())
    elif parse_tree.getText() == 'NUMBER':
        return Num(n=int(parse_tree.getText()))
    elif parse_tree.getText() == 'BOOL':
        return BoolOp(op=Or() if parse_tree.getText() == 'true' else And(), values=[to_ast(parse_tree.children[0]), to_ast(parse_tree.children[1])])
    elif parse_tree.getText() == 'list':
        return List(elts=[to_ast(child) for child in parse_tree.children])
    elif parse_tree.getText() == 'tuple':
        return Tuple(elts=[to_ast(child) for child in parse_tree.children])
    else:
        raise Exception('Unknown parse tree node type: ' + parse_tree.getText())

# Print the AST
print(to_ast(parse_tree))
