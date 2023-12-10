from rdffwk.queue_builder.operators.operator import Operator

class HavingOperator(Operator):
    def __init__(self, condition) -> None:
        self.condition = condition

    def __repr__(self) -> str:
        return self.condition

    def add_to_model(self, model):
        return model.add_having(self.condition)