from rdffwk.queue_builder.operators import Operator


class OrderByOperator(Operator):
    def __init__(self, *variables):
        super().__init__("ORDER BY")
        self.variables = variables
    
    def __repr__(self, model=None) -> str:
        return " ".join([str(var) for var in self.variables])
        
    def add_to_model(self, model):
        model.set_order_by(self.__repr__(model))