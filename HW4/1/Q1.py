from antlr4 import *
from gen.JavaLexer import JavaLexer
from gen.JavaParser import JavaParser
from gen.JavaParserVisitor import JavaParserVisitor


class MyClassVisitor(JavaParserVisitor):
    def __init__(self):
        self.private_fields = []

    def visitClassBodyDeclaration(self, ctx: JavaParser.ClassBodyDeclarationContext):
        modifiers = ctx.modifier()
        is_private = False
        is_final = False

        for modifier in modifiers:
            modifier_text = modifier.classOrInterfaceModifier().getText()

            # Check if the modifier is private
            if modifier_text == "private":
                is_private = True

            # Check if the modifier is final
            if modifier_text == "final":
                is_final = True

        field_declaration = ctx.memberDeclaration().fieldDeclaration()
        field_type = field_declaration.typeType().getText()
        field_name = field_declaration.variableDeclarators().getText()

        if is_private:
            self.private_fields.append((field_type, field_name, is_final))

    def generate_getter_setter(self, field_type, field_name, is_final):
        getter_name = "get" + field_name.capitalize()
        getter_method = f"    public {field_type} {getter_name}() {{\n        return {field_name};\n    }}"

        if not is_final:
            setter_name = "set" + field_name.capitalize()
            setter_method = f"    public void {setter_name}({field_type} value) {{\n        {field_name} = value;\n    }}"

            return f"{setter_method}\n{getter_method}"
        else:
            return getter_method


def adding_get_set(input_file):
    # Read input file
    with open(input_file, 'r') as file:
        java_code = file.read()

    # Lexing and parsing
    lexer = JavaLexer(InputStream(java_code))
    stream = CommonTokenStream(lexer)
    parser = JavaParser(stream)
    tree = parser.compilationUnit()

    # Visit the parsed tree
    visitor = MyClassVisitor()
    visitor.visit(tree)

    # Generate output
    output = ""
    for field_type, field_name, is_final in visitor.private_fields:
        output += f"    private {field_type} {field_name};\n"
        methods = visitor.generate_getter_setter(field_type, field_name, is_final)
        output += f"{methods}\n"

    # Create the output class
    if output:
        output = f"public class Sample {{\n{output}\n}}"

    # Write the output to a file
    with open('output.java', 'w') as file:
        file.write(output)


if __name__ == '__main__':
    input_file = 'input.java'
    adding_get_set(input_file)
