from datetime import datetime as dt 

class Expenditure(list):
    def __init__(self, currency='rur'):
        super().__init__()
        self.time_line = []
        self.currency = currency

    def __iadd__(self, value):
        self.time_line.append(dt.now())
        self.append(value)
        return self
    

class Wallet(dict):
    def __init__(self):
        super(Wallet, self).__init__()
    
    def make_expenditure(self, name):
        self[name] = Expenditure()
    
    def __repr__(self) -> str:
        str_res = ''
        for name in self:
            str_res += f'{name} = {sum(self[name])}, '
        return str_res[:-2]
        
if __name__ == '__main__':
    A = Wallet()
    print(A)
    A.make_expenditure('q')
    A.make_expenditure('w')

    A['q'] += 1
    print(A)
    A['q'] += 1
    A['w'] += 13
    print(A)
    print(A['q'].time_line)
    print(A['w'].time_line)

