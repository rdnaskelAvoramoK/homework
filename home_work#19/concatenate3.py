import sys

from pygments import highlight
from pygments.lexers import guess_lexer
from pygments.formatters import TerminalTrueColorFormatter

for filename in sys.argv:
    file_handler = open(filename,'r')
    code = file_handler.read()
    try:
        lexer = guess_lexer(code)
    except TypeError:
        lexer = TextLexer()
    print(highlight(code, lexer, TerminalTrueColorFormatter()))
    file_handler.close()