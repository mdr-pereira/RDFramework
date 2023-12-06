
class BlockBuilder():
    
    def __init__(self, block):
        self.block = block
        self.off = " "*(block.depth+1)
        
    def build(self) -> str:
        block = "{\n"
        
        block += self.triples()
        
        block += self.sub_queries()
        
        block += self.filters()
        
        block += self.bind()
        
        block += self.services()
        
        block += "}"
        
        return block
    
    def triples(self) -> str:
        triples = ""
        for triple in self.block.triples:
            triples += f"{self.off}{triple}.\n"
        return triples
    
    def sub_queries(self) -> str:
        sub_queries = ""
        for query in self.block.subQueries:
            sub_queries += f"{self.off}{{\n"
            sub_queries += query.to_sparql()
            sub_queries += f"{self.off}}}\n"
        return sub_queries
    
    def filters(self) -> str:
        filters = ""
        for filter in self.block.filters:
            filters += f"{self.off}FILTER({filter})\n"
        return filters
    
    def bind(self) -> str:
        binds = ""
        for bind in self.block.bindings:
            binds += f"{self.off}BIND({bind})\n"
        return binds
    
    def services(self) -> str:
        services = ""
        for service in self.block.services:
            services += f"{self.off}SERVICE {service}\n"
        return services
    