from rdffwk.query_builder.abstracts import AbstractInterface
from rdffwk.query_builder.query.query import Query
from rdffwk.queue_builder.queue import QueueOperator

class Block(AbstractInterface):
    def __init__(self, knowledge_base) -> None:
        super().__init__(knowledge_base)
    
    def query(self, *variables):
        if len(variables) == 1 and variables[0].__class__ == Query:
            self.queue.add(QueueOperator("query", variables[0], False))
        else:
            self.queue.add(QueueOperator("query", Query(self.knowledge_base, *variables), True))
        return self
    
    def to_model(self, depth=0):
        return self.queue.to_block_model(depth)
    
    