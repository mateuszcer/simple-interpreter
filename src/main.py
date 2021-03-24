import math

class InputStream:
    def __init__(self, input):
        self.stream = list(input.replace(" ", ""))  #char array

    def putback(self, char):
        self.stream.insert(0, char)

    
    def get(self):
        return self.stream.pop(0)

    def get_float(self):
        result = ""
        for i in self.stream:
            if is_float(i):
                result += i
            else:
                self.stream = self.stream[len(result):]
                return float(result)
        self.stream = []
        return float(result)


number = '8' #represent that token is number
read = ';' #end of expression
equal = '= '
quit = 'q'
class Token:
    def __init__(self, kind, value=None):
        self.kind = kind; # char
        self.value = value # int for numbers, none for operators
    

class TokenStream:
    def __init__(self, cin=None):
        self.buffer = None
        self.empty = True
        self.cin = cin
    def get(self):
        if not self.empty:
            self.empty = True
            return self.buffer
        if not self.cin.stream:
            return None
        char = self.cin.get()
        if is_float(char):
            self.cin.putback(char)
            value = self.cin.get_float()
            tk = Token(number, value)
            return tk
        tk = Token(char)
        return tk

    def putback(self, token):
        self.buffer = token
        self.empty = False
        return
    def clear(self):
        self.buffer = None
        self.empty = True
ts = TokenStream()
def is_float(char):
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
    if char in numbers:
        return True
    return False
def is_operator(char):
    operators = ["+", "-", "*", "/", "(", ")", "!", "q", ";"]
    if char in operators:
        return True
    return False

def expression():
    left = term()
    while True:
        tk = ts.get()
        if not tk:
            return left
        if tk.kind == "+":
            left += term()
        elif tk.kind == "-":
            left -= term()
        else:
            ts.putback(tk)
            return left
def term():
    left = primary()
    while True:
        tk = ts.get()
        if not tk:
            return left
        if tk.kind == "*":
            left *= primary()
        elif tk.kind == "/":
            val = primary()
            if val == 0:
                print("Division by 0")
            else:
                left /= val 
        else:
            ts.putback(tk)
            return left
def primary():
    tk = ts.get()
    if tk.kind == "(":
        val = expression()
        tk = ts.get()
        if tk.kind != ")":
            print("')' expected")
            return
        return val
    elif tk.kind == number:
        val = tk.value
        tk = ts.get()
        if tk and tk.kind == '!':
            val = int(val)
            val = math.factorial(val)
            return val
        ts.putback(tk)    
        return val
    else:
        print("Error Primary Expected")
        return 0;
    
def get_user_input():
        user_input = ""
        correct_input = False
        while not correct_input:
            correct_input = True
            user_input = input("> ")
            for ch in user_input:
                if not is_float(ch) and not is_operator(ch):
                    print("Unexpected token: ", ch)
                    correct_input = False
                    break
            if correct_input:
                return user_input

def calculate():
    while True:
        user_input = get_user_input()
        cin = InputStream(user_input)
        ts.cin = cin
        tk = ts.get()
        if tk and tk.kind == quit: 
            return 0
        ts.putback(tk)
        result = expression()
        tk = ts.get()
        if tk and tk.kind == read:
            print(equal, result)
            ts.clear()
        else:
            print("';' expected")

def main():
    calculate()
    
main()

