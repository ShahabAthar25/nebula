from Lexer.Lexer import Lexer
from Parser.Parser import Parser
from Interpreter.Interpreter import Interpreter

def shell():
    while True:
        try:
            text = input(">>> ")

            lexer = Lexer(text)
            tokens, error = lexer.make_tokens()

            if error: print(error.asString()); continue

            parser = Parser(tokens)
            ast = parser.parse()
            if ast.error: print(ast.error.asString()); continue

            print(ast.value)

            # interpreter = Interpreter()
            # result = interpreter.visit(ast.value)

            # if result.error: print(result.error.asString()); continue
            # else: print(result.value)
        except KeyboardInterrupt:
            print("\nIgnoring. (If you want to quit use ctrl + d)")
        except EOFError:
            print("\nExiting...")
            exit()