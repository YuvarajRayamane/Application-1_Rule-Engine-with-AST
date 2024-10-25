class Node:
    def __init__(self, type, value=None, left=None, right=None):
        self.type = type  # operator or operand
        self.value = value  # AND/OR for operator, condition for operand
        self.left = left
        self.right = right

    def to_dict(self):
        return {
            "type": self.type,
            "value": self.value,
            "left": self.left.to_dict() if self.left else None,
            "right": self.right.to_dict() if self.right else None
        }

    @staticmethod
    def from_dict(data):
        if not data:
            return None
        left = Node.from_dict(data.get('left'))
        right = Node.from_dict(data.get('right'))
        return Node(type=data['type'], value=data['value'], left=left, right=right)
