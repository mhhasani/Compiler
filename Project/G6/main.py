from antlr4 import *
from XMLLexer import XMLLexer
from XMLParser import XMLParser
from XMLParserVisitor import XMLParserVisitor as XMLVisitor


class FindPhotoImage(XMLVisitor):
    def __init__(self):
        self.result = None

    def visitElement(self, ctx: XMLParser.ElementContext):
        if ctx.Name().getText() == 'PhotoImage':
            self.result = ctx.content().STRING()

    def enterElement(self, ctx: XMLParser.ElementContext):
        # print(ctx.children[1].getText())
        if (ctx.children[1].getText() == "image"):
            self.image.append(ctx.children[1].getText())

def find_photoimage(tree):
    visitor = FindPhotoImage()
    visitor.visit(tree)
    return visitor.result


# Load the XML file
with open('data.xml', 'r') as f:
    input_stream = InputStream(f.read())

# Create a lexer and parser
lexer = XMLLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = XMLParser(token_stream)

# Parse the XML file
tree = parser.document()

# Find the PhotoImage tag
photoimage_node = find_photoimage(tree)

# Print the text content of the PhotoImage tag
if photoimage_node is not None:
    print(photoimage_node.STRING().getText())
else:
    print('PhotoImage tag not found')
