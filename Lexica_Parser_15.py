#Fungsi Parser
def parser(sentence):
 print('''\n
|====================================|
|============== Parser ==============|
|====================================|\n''')
 import re
 tokens = re.split(r'\s+', sentence.lower())
 tokens.append('EOS')
 non_terminals = ['statement', 'action', 'var', 'value', 'cond', 'operator', 'int']
 terminals = ['while', 'true', ':', 'if', 'break', '=', 'a', 'int(input())', '==', '>=', '<=', '<', '>', '1', '2', '3']

 parse_table = {}

 #Parse Table statement
 parse_table[('statement', 'while')] = ['while', 'true', ':', 'action', 'if', 'cond', ':', 'break']
 parse_table[('statement', ' true')] = ['error']
 parse_table[('statement', ':')] = ['error']
 parse_table[('statement', 'if')] = ['error']
 parse_table[('statement', 'break')] = ['error']
 parse_table[('statement', '=')] = ['error']
 parse_table[('statement', 'a')] = ['error']
 parse_table[('statement', 'int(input())')] = ['error']
 parse_table[('statement', '==')] = ['error']
 parse_table[('statement', '>=')] = ['error']
 parse_table[('statement', '<=')] = ['error']
 parse_table[('statement', '>')] = ['error']
 parse_table[('statement', '<')] = ['error']
 parse_table[('statement', '1')] = ['error']
 parse_table[('statement', '2')] = ['error']
 parse_table[('statement', '3')] = ['error']
 parse_table[('statement', 'EOS')] = ['error']

 #Parse Table action
 parse_table[('action', 'while')] = ['error']
 parse_table[('action', ' true')] = ['error']
 parse_table[('action', ':')] = ['error']
 parse_table[('action', 'if')] = ['error']
 parse_table[('action', 'break')] = ['error']
 parse_table[('action', '=')] = ['error']
 parse_table[('action', 'a')] = ['var', '=', 'value']
 parse_table[('action', 'int(input())')] = ['error']
 parse_table[('action', '==')] = ['error']
 parse_table[('action', '>=')] = ['error']
 parse_table[('action', '<=')] = ['error']
 parse_table[('action', '>')] = ['error']
 parse_table[('action', '<')] = ['error']
 parse_table[('action', '1')] = ['error']
 parse_table[('action', '2')] = ['error']
 parse_table[('action', '3')] = ['error']
 parse_table[('action', 'EOS')] = ['error']

 #Parse Table var
 parse_table[('var', 'while')] = ['error']
 parse_table[('var', ' true')] = ['error']
 parse_table[('var', ':')] = ['error']
 parse_table[('var', 'if')] = ['error']
 parse_table[('var', 'break')] = ['error']
 parse_table[('var', '=')] = ['error']
 parse_table[('var', 'a')] = ['a']
 parse_table[('var', 'int(input())')] = ['int(input())']
 parse_table[('var', '==')] = ['error']
 parse_table[('var', '>=')] = ['error']
 parse_table[('var', '<=')] = ['error']
 parse_table[('var', '>')] = ['error']
 parse_table[('var', '<')] = ['error']
 parse_table[('var', '1')] = ['error']
 parse_table[('var', '2')] = ['error']
 parse_table[('var', '3')] = ['error']
 parse_table[('var', 'EOS')] = ['error']

 #Parse Table value
 parse_table[('value', 'while')] = ['error']
 parse_table[('value', ' true')] = ['error']
 parse_table[('value', ':')] = ['error']
 parse_table[('value', 'if')] = ['error']
 parse_table[('value', 'break')] = ['error']
 parse_table[('value', '=')] = ['error']
 parse_table[('value', 'a')] = ['error']
 parse_table[('value', 'int(input())')] = ['int(input())']
 parse_table[('value', '==')] = ['error']
 parse_table[('value', '>=')] = ['error']
 parse_table[('value', '<=')] = ['error']
 parse_table[('value', '>')] = ['error']
 parse_table[('value', '<')] = ['error']
 parse_table[('value', '1')] = ['error']
 parse_table[('value', '2')] = ['error']
 parse_table[('value', '3')] = ['error']
 parse_table[('value', 'EOS')] = ['error']

 #Parse Table cond
 parse_table[('cond', 'while')] = ['error']
 parse_table[('cond', ' true')] = ['error']
 parse_table[('cond', ':')] = ['error']
 parse_table[('cond', 'if')] = ['error']
 parse_table[('cond', 'break')] = ['error']
 parse_table[('cond', '=')] = ['error']
 parse_table[('cond', 'a')] = ['var', 'operator', 'int']
 parse_table[('cond', 'int(input())')] = ['error']
 parse_table[('cond', '==')] = ['error']
 parse_table[('cond', '>=')] = ['error']
 parse_table[('cond', '<=')] = ['error']
 parse_table[('cond', '>')] = ['error']
 parse_table[('cond', '<')] = ['error']
 parse_table[('cond', '1')] = ['error']
 parse_table[('cond', '2')] = ['error']
 parse_table[('cond', '3')] = ['error']
 parse_table[('cond', 'EOS')] = ['error']

 #Parse Table operator
 parse_table[('operator', 'while')] = ['error']
 parse_table[('operator', ' true')] = ['error']
 parse_table[('operator', ':')] = ['error']
 parse_table[('operator', 'if')] = ['error']
 parse_table[('operator', 'break')] = ['error']
 parse_table[('operator', '=')] = ['error']
 parse_table[('operator', 'a')] = ['error']
 parse_table[('operator', 'int(input())')] = ['error']
 parse_table[('operator', '==')] = ['==']
 parse_table[('operator', '>=')] = ['>=']
 parse_table[('operator', '<=')] = ['<=']
 parse_table[('operator', '>')] = ['>']
 parse_table[('operator', '<')] = ['<']
 parse_table[('operator', '1')] = ['error']
 parse_table[('operator', '2')] = ['error']
 parse_table[('operator', '3')] = ['error']
 parse_table[('operator', 'EOS')] = ['error']

 #Parse Table int
 parse_table[('int', 'while')] = ['error']
 parse_table[('int', ' true')] = ['error']
 parse_table[('int', ':')] = ['error']
 parse_table[('int', 'if')] = ['error']
 parse_table[('int', 'break')] = ['error']
 parse_table[('int', '=')] = ['error']
 parse_table[('int', 'a')] = ['error']
 parse_table[('int', 'int(input())')] = ['error']
 parse_table[('int', '==')] = ['error']
 parse_table[('int', '>=')] = ['error']
 parse_table[('int', '<=')] = ['error']
 parse_table[('int', '>')] = ['error']
 parse_table[('int', '<')] = ['error']
 parse_table[('int', '1')] = ['1']
 parse_table[('int', '2')] = ['2']
 parse_table[('int', '3')] = ['3']
 parse_table[('int', 'EOS')] = ['error']

 stack = []
 stack.append('#')
 stack.append('statement')

 index_token = 0
 symbol = tokens[index_token]

 #Parser
 while(len(stack) > 0):
  top = stack[ len(stack) - 1 ]
  print('TOP : ', top)
  print('SYMBOL : ', symbol)
  if top in terminals:
   print('TOP ADALAH SYMBOL TERMINAL')
   if top == symbol:
    stack.pop()
    index_token = index_token + 1
    symbol = tokens[index_token]
    if symbol == "EOS":
     stack.pop()
     print('ISI STACK : ', stack)
   else:
    print('ERROR')
    break;
  elif top in non_terminals:
   print('TOP ADALAH SYMBOL NON-TERMINAL')
   if parse_table[(top, symbol)][0] != 'error':
    stack.pop()
    symbol_to_be_pushed = parse_table[(top, symbol)]
    for i in range(len(symbol_to_be_pushed)-1, -1, -1):
     stack.append(symbol_to_be_pushed[i])
   else:
    print('ERROR')
    break;
  else:
   print('ERROR')
   break;
  print('ISI STACK : ', stack)
  print()
 print()

 #Conclusion || Hasil Akhir dari Proses Parser
 print('''\n
|------------------------------------|''')
 if symbol == 'EOS' and len(stack) == 0:
  print('Inputan String :\n', sentence, '"', '\nDiterima, Sesuai Grammar')
 else:
  print('ERROR, Inputan String:\n', sentence, ', \nTidak Diterima, Tidak Sesuai Grammar')
 print('''|------------------------------------|''')
 return parser

#Lexical Analyzer

class Token:
    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value

class Lexer:
    def __init__(self, sentence):
        self.sentence = sentence
        self.position = 0

    def get_next_token(self):
        while self.position < len(self.sentence):
            current_char = self.sentence[self.position]

            if current_char == 'a':
                self.position += 1
                return Token('VAR', current_char)

            if current_char == '1':
                self.position += 1
                return Token('NUMBER', current_char)

            if current_char == '2':
                self.position += 1
                return Token('NUMBER', current_char)

            if current_char == '3':
                self.position += 1
                return Token('NUMBER', current_char)

            if current_char == '(':
                self.position += 1
                return Token('LPAREN', '(')

            if current_char == ')':
                self.position += 1
                return Token('RPAREN', ')')

            if current_char == 'i':
                self.position += 1
                current_char = self.sentence[self.position]
                if current_char == 'f':
                    self.position += 1
                    return Token('KEYWORD', 'if')
                elif current_char == 'n':
                    self.position += 1
                    current_char = self.sentence[self.position]
                    if current_char == 't':
                        self.position += 1
                        return Token('KEYWORD', 'int')
                    elif current_char == 'p':
                        self.position += 1
                        current_char = self.sentence[self.position]
                        if current_char == 'u':
                            self.position += 1
                            current_char = self.sentence[self.position]
                            if current_char == 't':
                                self.position += 1
                                return Token('KEYWORD', 'input')

            if current_char == 'w':
                self.position += 1
                current_char = self.sentence[self.position]
                if current_char == 'h':
                    self.position += 1
                    current_char = self.sentence[self.position]
                    if current_char == 'i':
                        self.position += 1
                        current_char = self.sentence[self.position]
                        if current_char == 'l':
                            self.position += 1
                            current_char = self.sentence[self.position]
                            if current_char == 'e':
                                self.position += 1
                                return Token('KEYWORD', 'while')

            if current_char == 'T':
                self.position += 1
                current_char = self.sentence[self.position]
                if current_char == 'r':
                    self.position += 1
                    current_char = self.sentence[self.position]
                    if current_char == 'u':
                        self.position += 1
                        current_char = self.sentence[self.position]
                        if current_char == 'e':
                            self.position += 1
                            return Token('KEYWORD', 'True')

            if current_char == 'b':
                self.position += 1
                current_char = self.sentence[self.position]
                if current_char == 'r':
                    self.position += 1
                    current_char = self.sentence[self.position]
                    if current_char == 'e':
                        self.position += 1
                        current_char = self.sentence[self.position]
                        if current_char == 'a':
                            self.position += 1
                            current_char = self.sentence[self.position]
                            if current_char == 'k':
                                self.position += 1
                                return Token('KEYWORD', 'break')

            if current_char == ':':
                self.position += 1
                return Token('COLON', ':')

            if current_char == '=':
                self.position += 1
                current_char = self.sentence[self.position]
                if current_char == '=':
                    self.position += 1
                    return Token('OPERATOR', '==')
                else:
                    return Token('ASSIGN', '=')

            if current_char == '>':
                self.position += 1
                current_char = self.sentence[self.position]
                if current_char == '=':
                    self.position += 1
                    return Token('OPERATOR', current_char + '=')
                else:
                    return Token('OPERATOR', current_char)

            if current_char == '<':
                self.position += 1
                current_char = self.sentence[self.position]
                if current_char == '=':
                    self.position += 1
                    return Token('OPERATOR', current_char + '=')
                else:
                    return Token('OPERATOR', current_char)

            if current_char == '\n':
                self.position += 1
                return Token('NEWLINE', '\n')

            if current_char == '\t':
                self.position += 1
                return Token('INDENT', '\t')

            if current_char.isspace():
                self.position += 1
                continue

            print("Invalid character:", current_char)
            print("Karena invalid, maka tidak bisa dilanjutkan ke proses parser")
            break

        return Token('EOF', None)
def LexernParser(sentence):
  print('''\n
|====================================|
|========= Lexical Analyzer =========|
|====================================|\n\n''')
  lexer = Lexer(sentence)
  i = 0
  while True:
      token = lexer.get_next_token()
      i+=1
      if token.type == 'EOF':
          break
      print(f"Token: {token.type}\tValue: {token.value}")
  if i >= 21:
    parser(sentence)
  return 0

#Main Program
print("|============= TERMINAL =============|\n")
'''file = open("file.txt", "r")
sentence = file.read()
file.close()'''
sentence = '''while True :
    a = int(input())
    if a 1 == :
        break'''
print(sentence)
input_string = sentence.lower()+'#'
LexernParser(sentence)
