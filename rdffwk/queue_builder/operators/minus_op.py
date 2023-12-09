from rdffwk.queue_builder.operators.operator import Operator

class MinusOperator(Operator):
    def __init__(self, block):
        self.block = block
        
    def __repr__(self, model=None) -> str:
        text = "MINUS "
        
        if model and self.block.__class__ != str:
            text += self.block.to_model(model.depth + 1).__repr__()
        else:
            text += self.block.__repr__()
            
        return text
    
    def add_to_model(self, model):
        model.add_triple(self.__repr__(model))