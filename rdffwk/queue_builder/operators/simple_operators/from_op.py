from rdffwk.queue_builder.operators.operator import Operator


class FromOperator(Operator):
    def __init__(self, uri) -> None:
        self.uri = uri
    
    def add_to_model(self, model):
        model.set_from(f"<{self.uri}>")