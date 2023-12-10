
class AbstractBuilder(object):
    def __init__(self, model):
        self.model = model
        self.OFF = " "*(model.depth+1)
        self.OFF_WOP = " "*(model.depth)

    def build(self):
        raise NotImplementedError("Abstract method")
    
    def triples(self) -> str:
        triples = ""
        for triple in self.model.triples:
            triples += f"{self.OFF}{triple}.\n"
        return triples
    
    def filters(self):
        filters = ""
        for filter in self.model.filters:
            filters += f"{self.OFF}FILTER({filter})\n"
        return filters
    
    def bind(self) -> str:
        binds = ""
        for bind in self.model.bindings:
            binds += f"{self.OFF}BIND({bind})\n"
        return binds
    
    def services(self) -> str:
        services = ""
        for service in self.model.services:
            services += f"{self.OFF}SERVICE {service}\n"
        return services
    
    def values(self) -> str:
        values = ""
        for value in self.model.values:
            values += f"{self.OFF}VALUES {value}\n"
        return values
    
    def sub_queries(self) -> str:
        sub_queries = ""
        for query in self.model.subQueries:
            sub_queries += f"{self.OFF}{{\n"
            sub_queries += query.to_sparql()
            sub_queries += f"{self.OFF}}}\n"
        return sub_queries
    
    