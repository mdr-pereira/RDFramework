from rdffwk.queue_builder.operators import Operator

class BindOperator(Operator): 
    def __init__(self, arg, as_var):
        super().__init__("bind")
        self.arg = arg
        self.as_var = as_var
    
    def __repr__(self):
        return f"({self.arg}) AS {self.as_var}"
    
    def add_to_model(self, model):
        model.add_bind(self.__repr__())