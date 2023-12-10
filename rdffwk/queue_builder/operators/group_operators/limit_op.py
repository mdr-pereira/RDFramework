from rdffwk.queue_builder.operators import Operator

class LimitOperator(Operator):
    def __init__(self, limit: int) -> None:
        super().__init__("LIMIT")
        self.limit = limit
        
    def __repr__(self) -> str:
        return str(self.limit)
    
    def add_to_model(self, model):
        return model.set_limit(self.__repr__())