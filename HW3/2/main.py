import sys
import os
# Add the path to the generated parser to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from antlr4 import *
from gen.Java9Lexer import Java9Lexer as JavaLexer
from gen.Java9Parser import Java9Parser as JavaParser
from gen.Java9ParserListener import Java9ParserListener as JavaParserListener

# To check and improve the efficiency of the codes, it is necessary to
# obtain the time complexity of the execution of the functions. Using
# Python language and Antler tool, write a program that displays the
# maximum number of nested loops (while, for) in this program by
# the address of a Java program for each of the functions in this program.

class LoopListener(JavaParserListener):
    def __init__(self):
        self.max = 0
        self.count = 0

    def enterWhileStatement(self, ctx):
        self.count += 1
        if self.count > self.max:
            self.max = self.count

    def exitWhileStatement(self, ctx):
        self.count -= 1

    def enterForStatement(self, ctx):
        self.count += 1
        if self.count > self.max:
            self.max = self.count

    def exitForStatement(self, ctx):
        self.count -= 1


def parse_java_file(filename):
    with open(filename, "r") as file:
        input_stream = InputStream(file.read())
        lexer = JavaLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = JavaParser(stream)
        tree = parser.compilationUnit()
        printer = LoopListener()
        walker = ParseTreeWalker()
        walker.walk(printer, tree)
        return printer.max

if __name__ == '__main__':
    filename = 'input.java'
    access_levels = parse_java_file(filename)
    print(access_levels)


