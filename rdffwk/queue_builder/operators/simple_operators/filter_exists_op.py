
from rdffwk.queue_builder.operators.operator import Operator


class FilterExistsOperator(Operator):
    def __init__(self, condition, negation=False):
        super().__init__("filter")
        self.condition = condition
        self.negation = negation
    
    def __repr__(self, model=None) -> str:
        text = "NOT " if self.negation else ""
        text += "EXISTS "
        
        if model and self.condition.__class__ != str:
            text += self.condition.to_model(model.depth + 1).__repr__()
        else:
            text += self.condition.__repr__()
            
        return text
    
    def add_to_model(self, model):
        model.add_filter(self.__repr__())