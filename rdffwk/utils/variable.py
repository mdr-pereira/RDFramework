class Variable():
    
    def __init__(self, name: str, f_op: bool = False) -> None:
        self.name = f"?{name}" if not f_op else name
        
    def __repr__(self) -> str:
        return self.name
    
    
    #Logical operators
    
    def __eq__(self, __value: object):
        return Variable(f"{self.name} = {__value}", True)
    
    def __ne__(self, __value: object):
        return Variable(f"{self.name} != {__value}", True)
    
    def __lt__(self, __value: object):
        return Variable(f"{self.name} < {__value}", True)
    
    def __le__(self, __value: object):
        return Variable(f"{self.name} <= {__value}", True)
    
    def __gt__(self, __value: object):
        return Variable(f"{self.name} > {__value}", True)
    
    def __ge__(self, __value: object):
        return Variable(f"{self.name} >= {__value}", True)
    
    def __and__(self, __value: object):
        return Variable(f"({self.name}) && ({__value})", True)
    
    def __or__(self, __value: object):
        return Variable(f"({self.name}) || ({__value})", True)
    
    #Arithmetic operators
    
    def __add__(self, __value: object):
        return Variable(f"{self.name} + {__value}", True)
    
    def __sub__(self, __value: object):
        return Variable(f"{self.name} - {__value}", True)
    
    def __mul__(self, __value: object):
        return Variable(f"{self.name} * {__value}", True)
    
    def __truediv__(self, __value: object):
        return Variable(f"{self.name} / {__value}", True)
    
    
    