from antlr4 import *
from gen.JavaLexer import JavaLexer as JavaLexer
from gen.JavaParser import JavaParser as JavaParser
from gen.JavaParserVisitor import JavaParserVisitor as JavaParserVisitor
from gen.JavaParserListener import JavaParserListener as JavaParserListener


class ExceptionAdderVisitor(JavaParserVisitor):
    def __init__(self, tokens):
        super().__init__()
        self.tokens = tokens


    def visitStatement(self, ctx:JavaParser.StatementContext):        
        if ctx.TRY() is not None:
            catch_clauses = ctx.catchClause()
            # check if there is catch (Exception e) clause
            if catch_clauses is not None:
                if catch_clauses[-1].catchType().getText() != 'Exception':
                    # add catch (Exception e) clause as text
                    self.tokens.insert(catch_clauses[-1].stop.tokenIndex + 1, " catch (Exception e) {")
                    # add System.out.println("Exception message: " + e.getMessage());
                    self.tokens.insert(catch_clauses[-1].stop.tokenIndex + 2, "System.out.println(\"Exception message: \" + e.getMessage());")
                    # add }
                    self.tokens.insert(catch_clauses[-1].stop.tokenIndex + 3, "}")
        return super().visitStatement(ctx)
        
    
            
def main():
    input_stream = FileStream('input.java')
    lexer = JavaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JavaParser(stream)
    tree = parser.compilationUnit()
    visitor = ExceptionAdderVisitor(parser._input.tokens)
    visitor.visit(tree)
    with open('output.java', 'w') as f:
        for i in range(len(visitor.tokens)):
            # if not <EOF>
            if type(visitor.tokens[i]) is not str:
                if visitor.tokens[i].type != -1:
                    f.write(visitor.tokens[i].text)
            else:
                f.write(visitor.tokens[i])
        
    
if __name__ == '__main__':
    main()
        