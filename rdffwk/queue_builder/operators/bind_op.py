from rdffwk.queue_builder.operators.operator import Operator


class BindOperator(Operator): 
    def __init__(self, arg1, as_var):
        super().__init__("bind")
        self.arg1 = arg1
        self.as_var = as_var
    
    def __repr__(self):
        return f"{self.arg1} AS {self.as_var}"
    
    def add_to_model(self, model):
        model.add_bind(self.__repr__())