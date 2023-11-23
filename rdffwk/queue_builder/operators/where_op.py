from rdffwk.queue_builder.operators.operator import Operator


class WhereOperator(Operator):
    
    def __init__(self, arg1, arg2, arg3):
        super().__init__("id")
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
    
    def __repr__(self):
        return f"{{{self.arg1} {self.arg2} {self.arg3}}}"