from rdffwk.queue_builder.operators import Operator


class GraphOperator(Operator):
    def __init__(self, graph, group):
        super().__init__("graph")
        self.graph = graph
        self.group = group

    def __repr__(self, model=None) -> str:
        text = f"GRAPH {self.graph} "

        if model and self.group.__class__ != str:
            text += self.group.to_model(model.depth + 1).__repr__()
        else:
            text += self.group.__repr__()

        return text

    def add_to_model(self, model):
        return model.add_triple(self.__repr__(model))
