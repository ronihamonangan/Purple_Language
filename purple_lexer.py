# Hal pertama yang dilakukan yaitu mengkonversi karakter menjadi token, hal ini disebut leksikal. Dipermudah dengan menggunakan SLY(Sly Lex Yacc)

from sly import Lexer

# Membangun class Lexer dari SLY, dan membuat kompiler yang membuat operasi aritmatika sederhana.

class BasicLexer(Lexer):
    tokens = {NAME, NUMBER, STRING, FOR, IF, THEN, TO, ELSE, EQEQ}
    literals = {'+', '-', '*', '/', '=', ',', ';', '(', ')'}
    ignore = '\t'

# Menentukan token sebagai ekspresi reguler dan menyimpannya sebagai string

    FOR = r'FR'
    IF = r'FI'
    THEN = r'THN'
    TO = r'OT'
    ELSE = r'ELS'
    EQEQ = r'=='

    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?"'

    # Number Token
    @_(r'\d+')
    def NUMBER(self,t):
        # mengkonversi kedalam bentuk integer
        t.value = int(t.value)
        return t

    # Comment Token
    @_(r'//.*')
    def COMMENT(self, t):
        pass
    
    # New Line Token
    @_(r'\n+')
    def newline(self, t):
        self.lineno = t.value.count('\n')