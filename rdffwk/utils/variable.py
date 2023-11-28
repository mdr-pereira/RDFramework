
class Variable():
    
    def __init__(self, name: str) -> None:
        self.name = f"?{name}"
        self.post_operators = None
        
    def __repr__(self) -> str:
        return self.name
    
    def __eq__(self, __value: object) -> str:
        return f"{self.name} = {__value}"
    
    def __ne__(self, __value: object) -> str:
        return f"{self.name} != {__value}"
    
    def __lt__(self, __value: object) -> str:
        return f"{self.name} < {__value}"
    
    def __gt__(self, __value: object) -> str:
        return f"{self.name} > {__value}"
    
    def __le__(self, __value: object) -> str:
        return f"{self.name} <= {__value}"
    
    def __ge__(self, __value: object) -> str:
        return f"{self.name} >= {__value}"
    
    def __add__(self, __value: object) -> str:
        return f"{self.name} + {__value}"
    
    def __sub__(self, __value: object) -> str:
        return f"{self.name} - {__value}"
    
    def __mul__(self, __value: object) -> str:
        return f"{self.name} * {__value}"
    
    def __truediv__(self, __value: object) -> str:
        return f"{self.name} / {__value}"
    
    def __mod__(self, __value: object) -> str:
        return f"{self.name} % {__value}"
    
    
    
    