from functools import reduce

def split_productions(multiproduction):
    splitted = multiproduction.split("->");
    left = splitted[0].strip()
    right = splitted[1]

    return list(map(lambda a : f"{left} -> {a.strip()}", right.split("|")));

def get_productions(grammar):
    productions = []
    for prod in grammar.split("\n"):
        if "|"  in prod:
            productions.extend(split_productions(prod))
        else:
            productions.append(prod)

    return productions


def extract_start_symbol(grammar):
    first_production = grammar.split("\n")[0]
    return first_production.split("->")[0].strip()

def extract_non_terminals(right_side):
    return filter(lambda x: x.islower(),[*right_side])

def find_terminals_and_non_terminals(productions):
    lefts = list(map(lambda x: x.split("->")[0].strip(), productions))
    rights = list(map(lambda x: x.split("->")[1].strip(), productions))

    non_terminals = list(set(lefts))
    terminals = list(set(reduce(lambda a,b : [*a, *b], map(extract_non_terminals, rights))))

    return non_terminals, terminals


grammar = "S-> Sab | ab | a | b";

start_symbol = extract_start_symbol(grammar)
productions = get_productions(grammar)
non_terminals, terminals = find_terminals_and_non_terminals(productions)

print("Set of non-terminals", non_terminals)
print("Set of terminals", terminals)
print("Set of productions", productions)
print("Starting symbol", start_symbol)