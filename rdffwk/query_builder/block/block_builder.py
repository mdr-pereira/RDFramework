from rdffwk.query_builder.abstracts import AbstractBuilder

class BlockBuilder(AbstractBuilder):
    
    def __init__(self, model):
        super().__init__(model)
        
    def build(self) -> str:    
        block = self._inner_block_builder()
    
        if block.count("\n") <= 4:
            block = block.replace("\n", "")
        
        return block