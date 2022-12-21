class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    queue = [root]
    string = ""
    while queue:
        curr = queue.pop(0)
        if curr is not None:
            queue.append(curr.left)
            queue.append(curr.right)
            string += curr.val + " "
        else:
            string += "None "
    return string[:-1] # chop off last space lol
        

def deserialize(s):
    
    if s == "":
        return

    str_list_nodes = s.split()
    node_objects = []

    for x in str_list_nodes:
        node_objects.append(Node(x))
        
    for i in range(len(node_objects)):
        if node_objects[i].val != "None":
            node_objects[i].left = node_objects[2*i+1]
            node_objects[i].right = node_objects[2*i+2]
    

    return node_objects[0]


node = Node('root', Node('left', Node('left.left')), Node('right'))

print(deserialize("root left right left.left None None None None None").left.left.val)
assert deserialize(serialize(node)).left.left.val == 'left.left'