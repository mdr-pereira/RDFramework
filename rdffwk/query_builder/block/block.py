from rdffwk.query_builder.abc_query_block import Abstract
from rdffwk.query_builder.query.query import Query

class Block(Abstract):
    def __init__(self, knowledge_base) -> None:
        super().__init__(knowledge_base)
    
    def query(self, *variables):
        self.queue.add(Query(self.knowledge_base, *variables))
        return self
    
    def to_model(self, depth=0):
        return self.queue.to_block_model(depth)
    
    