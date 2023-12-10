# RDFramework

This project was done under the Data Modelling course of the Winter Semester 2023/24, and is based on the project developed by @qcri (https://github.com/qcri/RDFframes).

An access framework within Python which allows users to construct and run Turtle-SPARQL and Turtle-Star-SPARQL using familiar python-like API calls.

## Abstract


## TODO

### Issues/Errors
- [x] Block currently does not accept subqueries, and will break if we try to apply it.

### Improve features
- [x] The way that WHERE is processed to allow for the joined queries
- [x] The way that we create groupings
- [ ] Change how the where clause is stored to a map of maps, thus allowing us to optimize the query ad-hoc. (Explained below)
- [x] The way that strings are processed so we don't have to put double quotation marks. (Added a new auxiliary operator that just wraps arguments in quotation marks)


### Add new features
- [x] VALUES 
- [ ] Bnodes

### Explanation

By changing the where clause from a list to a map of maps, it allows us to dynamically compress the queries to use the common prefix rules (, and ;) instead of relying on the
user to give us these himself.
