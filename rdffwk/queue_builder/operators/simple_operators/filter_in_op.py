from rdffwk.queue_builder.operators import Operator

class FilterInOperator(Operator):
    def __init__(self, var, values, negation=False):
        super().__init__("filter")
        self.var = var
        self.values = values
        self.negation = negation
    
    def __repr__(self) -> str:
        text = self.var + " NOT " if self.negation else " "
        text += "IN ("
        
        if self.values.__class__ == tuple or self.values.__class__ == list:
            self.values = ", ".join([f"\"{v}\"" for v in self.values])
            
        text += f"{self.values})"
        return text
    
    def add_to_model(self, model):
        model.add_filter(self.__repr__())