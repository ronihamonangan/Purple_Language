from sly import Parser

import purple_lexer

# Membuat class Basic Parser untuk memperluas Lexer, dengan mengalirkan Token
#dari BasicLexer ke Token Variabel

class BasicParser(Parser):

    # Token diteruskan dari lexer ke parser
    tokens = BasicLexer.tokens

    precedence = (
        ('left', '+', '-'),
        ('left', '*', '/'),
        ('right', 'UMINUS')
    )

    def __init__(self):
        self.env = { }
    
    @_(' ')
    def statement(self, p):
        pass