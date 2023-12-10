from rdffwk.queue_builder.operators.operator import Operator

class UnionOperator(Operator):
    def __init__(self, block1, block2):
        super().__init__("UNION")
        self.block1 = block1
        self.block2 = block2

    def __repr__(self, model=None) -> str:
        text = ""
        
        if model and self.block1.__class__ != str:
            text += self.block1.to_model(model.depth + 1).__repr__()
        else:
            text += self.block1.__repr__()
        
        text += " UNION "
        
        if model and self.block2.__class__ != str:
            text += self.block2.to_model(model.depth + 1).__repr__()
        else:
            text += self.block2.__repr__()
            
        return text
    
    def add_to_model(self, model):
        return model.add_triple(self.__repr__(model))
