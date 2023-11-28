def NOT(expr) -> str :
    return f"NOT {expr}"

def EXISTS(expr) -> str :
    return f"EXISTS {{{expr}}}"

def ASC(expr) -> str :
    return f"ASC({expr})"

def DESC(expr) -> str :
    return f"DESC({expr})"