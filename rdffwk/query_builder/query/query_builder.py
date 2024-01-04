from rdffwk.query_builder.abstracts import AbstractBuilder


class QueryBuilder(AbstractBuilder):
    """Query builder class
    This class is responsible for building a query string from a QueryModel object.

    It currently makes some assumptions about the SPARQL language ordering of clauses, but may be changed to allow
    for some more flexibility in the future.
    This has to be decided whether we should allow for more flexibility at the cost of requiring more work and domain-
    specific knowledge from the user, or if we should keep it simple and make some assumptions about the language.
    """

    def __init__(self, model) -> None:
        super().__init__(model)

    def build(self) -> str:
        """Builds the query string from the QueryModel object.

        :returns: The query string.
        """
        query = "" if self.model.depth > 0 else self.prefixes()

        query += self.select()

        query += self.from_uri()

        query += self.where()

        query += self.group_by()

        query += self.order_by()

        query += self.having()

        query += self.limit()

        query += self.offset()

        return query

    def prefixes(self) -> str:
        """Builds the prefixes string from the QueryModel object.

        :returns: The prefixes string.
        """
        prefixes = ""
        for prefix, uri in self.model.prefixes.items():
            prefixes += f"PREFIX {prefix}: <{uri}>\n"
        return prefixes

    def select(self) -> str:
        """Builds the SELECT clause string from the QueryModel object.

        :returns: The SELECT clause string.
        """
        var_str = f"{self.OFF_WOP}SELECT "
        for var in self.model.variables:
            var_str += f"{var} "
        var_str += "\n"
        return var_str

    def from_uri(self) -> str:
        """Builds the FROM clause string from the QueryModel object.

        :returns: The FROM clause string.
        """
        return self._solve_if_exists(self.model.from_uri, "FROM")

    def where(self) -> str:
        """Builds the WHERE clause string from the QueryModel object.

        :returns: The WHERE clause string.
        """
        block = f"{self.OFF_WOP}WHERE {self._inner_block_builder()}"

        if block.count("\n") <= 3:
            block = block.replace("\n", "")

        return block

    def group_by(self) -> str:
        """Builds the GROUP BY clause string from the QueryModel object.

        :returns: The GROUP BY clause string.
        """
        return self._solve_if_exists(self.model.grouping, "GROUP BY")

    def order_by(self) -> str:
        """Builds the ORDER BY clause string from the QueryModel object.

        :returns: The ORDER BY clause string.
        """
        return self._solve_if_exists(self.model.ordering, "ORDER BY")

    def limit(self) -> str:
        """Builds the LIMIT clause string from the QueryModel object.

        :returns: The LIMIT clause string.
        """
        return self._solve_if_exists(self.model.limit, "LIMIT")

    def offset(self) -> str:
        """Builds the OFFSET clause string from the QueryModel object.

        :returns: The OFFSET clause string.
        """
        return self._solve_if_exists(self.model.offset, "OFFSET")

    def having(self) -> str:
        """Builds the HAVING clause string from the QueryModel object.

        If the HAVING clause is used, the GROUP BY clause must also be used.

        :returns: The HAVING clause string.
        """
        if not self.model.having:
            return ""

        if self.model.grouping is None:
            raise SystemExit("HAVING clause without GROUP BY clause")

        having_str = f"{self.OFF_WOP}HAVING ("

        for i in range(len(self.model.having)):
            if i != 0:
                having_str += " && "

            having_str += f"{self.model.having[i]}"

        having_str += ").\n"
        return having_str

    def _solve_if_exists(self, var, prefix) -> str:
        """Solves a clause if it exists.
        This method is purely for code reuse, and should not be used outside of this class.

        :param var: The variable to check.
        :param prefix: The operator to use as prefix, e.g. FROM, GROUP BY, etc.
        :returns: The clause string if the variable exists, otherwise an empty string.
        """
        if var is None:
            return ""

        return f"{self.OFF_WOP}{prefix} {var}\n"
