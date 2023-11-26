from rdffwk.queue_builder.operators.operator import Operator

class FilterOperator(Operator):
    
    
    def __init__(self, condition):
        super().__init__("filter")
        self.condition = condition
    
    def __repr__(self):
        return f"{self.condition}"
    