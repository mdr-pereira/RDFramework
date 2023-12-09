# graphdb-simplified

## Abstract


## TODO

### Improve features
- [x] The way that WHERE is processed to allow for the joined queries
- [x] The way that we create groupings
- [ ] Change how the where clause is stored to a map of maps, thus allowing us to optimize the query ad-hoc. (Explained below)
- [ ] The way that strings are processed so we don't have to put double quotation marks


### Add new features
- [x] VALUES 
- [ ] Bnodes

### Explanation

By changing the where clause from a list to a map of maps, it allows us to dynamically compress the queries to use the common prefix rules (, and ;) instead of relying on the
user to give us these himself.