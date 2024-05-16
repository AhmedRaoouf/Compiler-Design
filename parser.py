import re

class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children is not None else []

class Parser:
    def __init__(self, code):
        self.code = code
        self.variables = {}
        self.parse_tree = Node("Program")

    def parse(self):
        for line in self.code.split('\n'):
            if not line.strip():
                continue  
            match_declaration = re.match(r'^\s*(int|float|char|bool)\s+([a-zA-Z_]\w*)\s*(?:=\s*(.*?))?;', line)
            if match_declaration:
                var_type, var_name, var_value = match_declaration.groups()
                if var_name not in self.variables:
                    self.variables[var_name] = {'type': var_type, 'value': var_value}
                    declaration_node = Node("Declaration", [Node(var_type), Node(var_name), Node(var_value), Node(";")])
                    self.parse_tree.children.append(declaration_node)
            else:
                match_assignment = re.match(r'^\s*([a-zA-Z_]\w*)\s*=\s*(.*?);', line)
                if match_assignment:
                    var_name, expression = match_assignment.groups()
                    if var_name in self.variables:
                        try:
                            value = eval(expression, {}, self.variables)
                            self.variables[var_name]['value'] = value
                            assignment_node = Node("Assignment", [Node(var_name), Node(value), Node(";")])
                            self.parse_tree.children.append(assignment_node)
                        except:
                            pass

    def display_parse_tree(self, node=None, depth=0):
        if node is None:
            node = self.parse_tree
        print("  " * depth + str(node.value))
        for child in node.children:
            self.display_parse_tree(child, depth + 1)

code = open('code.txt','r').read()
parser = Parser(code)
parser.parse()
parser.display_parse_tree()
