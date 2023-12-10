from rdffwk.queue_builder.operators import Operator


class GroupByOperator(Operator):
    def __init__(self, *args) -> None:
        super().__init__("GROUP BY")
        self.variables = args
        
    def __repr__(self) -> str:
        return " ".join([str(var) for var in self.variables])
    
    def add_to_model(self, model):
        return model.set_grouping(self.__repr__())