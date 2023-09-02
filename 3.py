import functools

def split_productions(multiproduction):
    splitted = multiproduction.split("->");
    left = splitted[0].strip()
    right = splitted[1]

    return list(map(lambda a : f"{left} -> {a.strip()}", right.split("|")));

def filter_non_recursive_productions(productions):
    def is_non_recursive(p):
        splitted = p.split("->");
        left = splitted[0].strip()
        right = splitted[1].strip()
        return right[0] != left

    non_recursive = []
    recursive = []

    for prod in productions:
        if is_non_recursive(prod):
            non_recursive.append(prod)
        else:
            recursive.append(prod)

    return non_recursive, recursive

def get_alternative_non_terminal(non_terminal):
    return f"{non_terminal}'"

def get_non_terminal(production):
    return production.split('->')[0].strip()

def right_recursion_to_non_recursive(productions, alt_non_terminal):
    return list(map(lambda x: f"{x}{alt_non_terminal}", productions))

def right_recursion_to_recursive(productions, alt_non_terminal):
    def change(prod):
        x = prod.split('->')
        left = x[0].strip()
        right = x[1].strip()
        right = f"{right.lstrip(left)}{alt_non_terminal}"
        left = alt_non_terminal
        return f"{left} -> {right}"
    
    return list(map(change, productions))

def remove_left_recursion(productions):
    non_terminal = get_non_terminal(productions)
    alt_non_terminal = get_alternative_non_terminal(non_terminal);
    singular_productions = split_productions(productions)
    non_recursive, recursive = filter_non_recursive_productions(singular_productions);
    non_recursive = right_recursion_to_non_recursive(non_recursive, alt_non_terminal)
    recursive = right_recursion_to_recursive(recursive, alt_non_terminal);
    return [*non_recursive, *recursive, f"{alt_non_terminal} -> epsilon"]

productions = [
    "S-> Sab | ab | a | b",
    "A -> A0 | A1 | 0"
]

for prod in productions:
    res = remove_left_recursion(prod);
    print("\n".join(res));
    print()