class Input_stream:
    def __init__(self, input):
        self.stream = list(input)  #char array
    def putback(self, char):
        self.stream.insert(0, char)
    def is_int(self, char):
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        if char in numbers:
            return True
        return False
    def get(self, int=False):
        if int:
            result = ""
            for i in self.stream:
                if self.is_int(i):
                    result += i
                else:
                    self.stream = self.stream[len(result):]
                    return int(result)
            self.stream = []
            return int(result)
        return self.stream.pop(0)


class Token:
    def __init__(self, kind, value=None):
        self.kind = kind; # char
        self.value = value # int for numbers, none for operators
    

class Token_stream:
    def __init__(self):
        self.buffer = None
        self.empty = True;

    def get(self, cin):
        if not self.empty:
            return self.buffer
        


def main():
    while True:
        cin = Input_stream(input("> "))
        print(cin.get(int=True))
        print(cin.stream)

main()

