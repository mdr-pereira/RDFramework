from rdffwk.queue_builder.operators import Operator

class ValuesOperator(Operator):
    def __init__(self, var, values):
        self.var = var
        self.values = values
    
    def __repr__(self) -> str:
        return f"{self.var} ({', '.join([str(v) for v in self.values])})"
    
    def add_to_model(self, model):
        model.add_values(self.__repr__())