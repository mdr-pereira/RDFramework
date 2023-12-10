from rdffwk.query_builder.block.block import Block
from rdffwk.query_builder.query.query_star import QueryStar
from rdffwk.queue_builder.operators.star_operators import WhereStarOperator

class BlockStar(Block):
    def __init__(self, knowledge_base) -> None:
        super().__init__(knowledge_base)
        
    def query(self, *variables):
        return QueryStar(self.knowledge_base, variables)
    
    def block(self):
        return BlockStar(self.knowledge_base)
    
    def where(self, *args):
        if(len(args) > 4 or len(args) < 1):
            raise SystemExit("Invalid number of arguments for where clause")

        self.queue.add(WhereStarOperator(*args))
        return self