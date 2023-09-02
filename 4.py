class Entry:
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value
    
    def __str__(self):
        return f"{self.name}\t\t{self.type}\t{self.value}\t{hex(id(self))}"

def parse_to_entry(data):
    d = data.split("=")
    left = d[0].strip()
    right = d[1].strip()
    e = left.split(" ")
    return Entry(e[1], e[0], right)

def parse_entries(data):
    return list(map(lambda x: parse_to_entry(x.strip()), data.split(",")))

symbol_table = []

input = "int a = 2, float b = 3.5"

symbol_table.extend(parse_entries(input))

print(f"Variable Name\tType\tValue\tAddress");
print("\n".join(map(lambda x: f"{x}",symbol_table)))
    