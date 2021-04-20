from sly import Parser

import purple_lexer

# Membuat class Basic Parser untuk memperluas Lexer, dengan mengalirkan Token
#dari BasicLexer ke Token Variabel

class BasicParser(Parser):

    # Token diteruskan dari lexer ke parser
    tokens = purple_lexer.BasicLexer.tokens

    precedence = (
        ('left', '+', '-'),
        ('left', '*', '/'),
        ('right', 'UMINUS')
    )

    def __init__(self):
        self.env = { }
    
    @_('')
    def statement(self, p):
        pass

    @_('FOR var_assign TO expr THEN statement')
    def statement(self,p):
        return ('for_loop', ('for_loop_setup', p.var_assign, p.expr), p.statement)
    
    @_('IF condition THEN statement ELSE statement')
    def statement(self,p):
        return('if_stmt', p.condition,('branch', p.statement0, p.statement1))

    @_('expr EQEQ expr')
    def condition(self, p):
        return ('condition_eqeq', p.expr0, p.expr1)
    
    @_('var_assign')
    def statement(self, p):
        return p.var_assign
