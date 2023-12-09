
class QueryBuilder():

    def __init__(self, model) -> None:
        self.model = model
        self.off = " "*(model.depth+1)
        self.off_wop = " "*(model.depth)
   
    def build(self) -> str:
        query = ""
        
        query += "" if self.model.depth != 0 else self.prefixes()
        
        query += self.select()
        
        query += self.triples()
        
        query += self.filter()
        
        query += self.sub_queries()
        
        query += self.values()
        
        query += self.bind()
        
        query += self.services()
        
        query += f"{self.off_wop}}}\n"
        
        query += self.group_by()
        
        query += self.order_by()
        
        query += self.having()
        
        query += self.limit()
        
        query += self.offset()
        
        return query
    
    def prefixes(self) -> str:
        prefixes = ""
        for prefix, uri in self.model.prefixes.items():
            prefixes += f"PREFIX {prefix}: <{uri}>\n"
        return prefixes
    
    
    def select(self) -> str:
        variables = self.model.variables
        var_str = "SELECT "
        
        if(variables.__class__ != tuple):
            var_str += f"{variables}"
        else:    
            for var in variables:
                var_str += f"{var} "
                    
        return var_str + "\n"
    
    
    def triples(self) -> str:
        where_str = f"{self.off_wop}WHERE {{\n"
        
        for i in range(len(self.model.triples)):
            where_str += self.off + f"{self.model.triples[i]}.\n"
            
        return where_str
    
    
    def filter(self) -> str:
        if(self.model.filters == []): return ""
        filter_str = ""

        for i in range(len(self.model.filters)):
            filter_str += f"{self.off}FILTER ({self.model.filters[i]}).\n"

        return filter_str
    
    def bind(self) -> str:
        bind_str = ""

        for bind in self.model.bindings:
            bind_str += self.off + f"BIND ({bind}).\n"

        return bind_str
    
    def services(self) -> str:
        service_str = ""
        
        for service in self.model.services:
            service_str += self.off + f"SERVICE {service}.\n"
            
        return service_str
    
    def values(self) -> str:
        values_str = ""
        
        for values in self.model.values:
            values_str += self.off + f"VALUES {values}.\n"
            
        return values_str
    
    def group_by(self) -> str:
        if(self.model.grouping == None): return ""
    
        return f"{self.off_wop}GROUP BY {self.model.grouping}\n"
    
    def order_by(self) -> str:
        if(self.model.ordering == None): return ""
        
        return f"{self.off_wop}ORDER BY {self.model.ordering}\n"
    
    def having(self) -> str:
        if(self.model.having == []): return ""
        
        if(self.model.grouping == None):
            raise SystemExit("HAVING clause without GROUP BY clause")
        
        having_str = f"{self.off_wop}HAVING ("
        
        for i in range(len(self.model.having)):
            if(i != 0): having_str += " && "
            having_str += f"{self.model.having[i]}"
            
        having_str += ").\n"
        return having_str
    
    def limit(self) -> str:
        if(self.model.limit == None): return ""
        
        return f"{self.off_wop}LIMIT {self.model.limit}\n"
    
    def offset(self) -> str:
        if(self.model.offset == None): return ""
        
        return f"{self.off_wop}OFFSET {self.model.offset}\n"
                
    def sub_queries(self) -> str:
        sub_queries = ""
        
        for query in self.model.subQueries:
            sub_queries += f"{self.off}{{\n"
            sub_queries += query.to_sparql()
            sub_queries += f"{self.off}}}\n"
            
        return sub_queries