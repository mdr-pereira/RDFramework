from rdffwk.query_builder.abc_builder import AbstractBuilder

class BlockBuilder(AbstractBuilder):
    
    def __init__(self, model):
        super().__init__(model)
        
    def build(self) -> str:
        block = f"{{\n"
        
        block += self.triples()
        
        block += self.sub_queries()
        
        block += self.filters()
        
        block += self.bind()
        
        block += self.services()
        
        block += f"{self.OFF_WOP}}}"
        
        if block.count("\n") <= 3:
            block = block.replace("\n", "")
        
        return block
    
    