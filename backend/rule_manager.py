import ast
from models import Node

class RuleManager:
    def create_rule(self, rule_string):
        """Parse the rule string and return its AST representation."""
        try:
            root = self._parse_rule_string(rule_string)
            return root.to_dict()  # Converting AST to a storable dictionary
        except Exception as e:
            raise Exception(f"Error parsing rule: {str(e)}")

    def _parse_rule_string(self, rule_string):
        """Manually parse the rule string into a custom AST."""
        # Using Python's ast module to safely parse the string into an abstract syntax tree.
        tree = ast.parse(rule_string, mode='eval')
        return self._build_ast(tree.body)

    def _build_ast(self, node):
        """Recursively build a custom AST using Node objects."""
        if isinstance(node, ast.BoolOp):  # AND/OR operations
            op = 'AND' if isinstance(node.op, ast.And) else 'OR'
            return Node(type='operator', value=op, left=self._build_ast(node.values[0]), right=self._build_ast(node.values[1]))
        elif isinstance(node, ast.Compare):  # Comparison operations
            left = node.left.id if isinstance(node.left, ast.Name) else None
            op = node.ops[0].__class__.__name__
            right = node.comparators[0].n if isinstance(node.comparators[0], ast.Constant) else node.comparators[0].s
            return Node(type='operand', value=f"{left} {op} {right}")
        else:
            raise Exception("Unsupported operation in rule")

    def evaluate_rule(self, rule_ast, data):
        """Evaluate the rule AST against the provided data."""
        return self._evaluate_node(Node.from_dict(rule_ast), data)

    def _evaluate_node(self, node, data):
        if node.type == 'operator':
            left_result = self._evaluate_node(node.left, data)
            right_result = self._evaluate_node(node.right, data)
            return (left_result and right_result) if node.value == 'AND' else (left_result or right_result)
        elif node.type == 'operand':
            # Split operand to get field, operator, and value
            field, op, value = node.value.split()
            field_value = data.get(field)
            if op == 'Gt':  # Greater than
                return field_value > int(value)
            elif op == 'Lt':  # Less than
                return field_value < int(value)
            elif op == 'Eq':  # Equal to
                return field_value == value
            else:
                return False
        return False
