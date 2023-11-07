# graphdb-simplified

## Abstract

    Due to the rising usage of graph-based databases, there is a rising clash of individuals with little informatics backgrounds with the complex and rich syntaxes and semantics of these databases.

    Our goal is thus to create a simplified graphical interface which would allow the building of queries through drag-and-drop of visual components.

    As we see it at this moment, the project would be composed of 3-4 components:
        - Neo4J graph feature extractor.
        - Graphical Interface.
        - Graphical to Cypher Interpreter.
        - Connection to Neo4J drivers.

    So, the workflow of our application would allow for a user to input a database, where its features (incl. Node Types, Relationships, Properties, etc...) would be extracted and fed into the graphical interface. By moving visual blocks around, forcing relationships and properties, the user would build a visual representation of a query, which would then be possible to translate into a Cypher textual query.
    If development time allows it, this could later be paired with the Neo4J drivers to form a fully-enclosed application for query building and matching.