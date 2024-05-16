from  lexer import *
from unorder_symbol_table import *
from order_symbol_table import *
from parser import *



code = open('code.txt', 'r').read()
lexer = Lexer(code)
tokens = lexer.tokens

parser = Parser(code)
parser.parse()
parser.display_parse_tree()

unorder_symbol_table = UnOrderSymbolTable()
unorder_symbol_table.parse_code(code)
unorder_symbol_table.display_table()

