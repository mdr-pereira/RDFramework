class AbstractBuilder(object):
    """Abstract class for the building of SPARQL queries.
    It creates a string representation of the SPARQL query or block.

    This class is not meant to be used directly, but to be inherited by the other builders. All methods here
    included are shared between the other builders.
    """
    def __init__(self, model):
        self.model = model
        self.OFF = " "*(model.depth+2)
        self.OFF_WOP = " " * model.depth

    def build(self):
        raise NotImplementedError("Abstract method")
    
    def triples(self) -> str:
        """Builds the triples of the query.

        :returns: A string representation of all triples, in their call order.
        :rtype: str
        """
        triples = ""
        for triple in self.model.triples:
            triples += f"{self.OFF}{triple}.\n"
        return triples
    
    def filters(self):
        """Builds the FILTER clauses of the query.

        :returns: A string representation of all filters, in their call order.
        :rtype: str
        """
        filters = ""
        for _filter in self.model.filters:
            filters += f"{self.OFF}FILTER ( {_filter} )\n"
        return filters
    
    def bind(self) -> str:
        """Builds the non-inline BIND clauses of the query.

        :returns: A string representation of all bindings.
        :rtype: str
        """
        binds = ""
        for bind in self.model.bindings:
            binds += f"{self.OFF}BIND ( {bind} )\n"
        return binds
    
    def services(self) -> str:
        """Builds the calls to external services of the query. Ie SERVICE clauses.

        :returns: A string representation of queries to all services.
        :rtype: str
        """
        services = ""
        for service in self.model.services:
            services += f"{self.OFF}SERVICE {service}\n"
        return services
    
    def values(self) -> str:
        """Builds the VALUES clauses of the query.

        :returns: A string representation of all values.
        :rtype: str
        """
        values = ""
        for value in self.model.values:
            values += f"{self.OFF}VALUES {value}\n"
        return values
    
    def sub_queries(self) -> str:
        """Builds the sub-queries of the query.

        :returns: A string representation of all sub-queries.
        :rtype: str
        """
        sub_queries = ""
        for query in self.model.subQueries:
            sub_queries += f"{self.OFF}{{\n"
            sub_queries += query.to_sparql()
            sub_queries += f"{self.OFF}}}\n"
        return sub_queries
    
    def _inner_block_builder(self) -> str:
        """Builds the inner block of the query. This is, the block that is inside the WHERE clause.

        :returns: A string representation of the inner block.
        :rtype: str
        """
        where_str = "{\n"
        where_str += self.triples()
        where_str += self.filters()
        where_str += self.sub_queries()
        where_str += self.values()
        where_str += self.bind()
        where_str += self.services()
        where_str += f"{self.OFF_WOP}}}\n"
        return where_str
    
    