from antlr4 import *
from gen.Java9Lexer import Java9Lexer as JavaLexer
from gen.Java9Parser import Java9Parser as JavaParser
from gen.Java9ParserListener import Java9ParserListener as JavaParserListener


class MethodListener(JavaParserListener):
    def __init__(self):
        self.access_levels = {
            'public': [],
            'private': [],
            'protected': [],
        }

    def enterMethodDeclaration(self, ctx: JavaParser.MethodDeclarationContext):
        modifiers = ctx.methodModifier()
        for modifier in modifiers:
            if modifier.PUBLIC():
                self.access_levels['public'].append(ctx.methodHeader().methodDeclarator().getText())
            elif modifier.PRIVATE():
                self.access_levels['private'].append(ctx.methodHeader().methodDeclarator().getText())
            elif modifier.PROTECTED():
                self.access_levels['protected'].append(ctx.methodHeader().methodDeclarator().getText())



def parse_java_file(filename):
    with open(filename, "r") as file:
        input_stream = InputStream(file.read())
        lexer = JavaLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = JavaParser(stream)
        tree = parser.compilationUnit()
        printer = MethodListener()
        walker = ParseTreeWalker()
        walker.walk(printer, tree)
        return printer.access_levels

if __name__ == '__main__':
    filename = 'input.java'
    access_levels = parse_java_file(filename)
    print(access_levels)
