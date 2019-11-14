from linked_queue import LinkedQueue

class TreeWithoutParent:
    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right
 
    def __str__(self):
        return str(self._element)

def PreOrderTraversal(tree):
    if tree == None: 
        return
    print(tree._element, end = " ")
    PreOrderTraversal(tree._left)
    PreOrderTraversal(tree._right)


    
def PostOrderTraversal(tree):
    if tree == None: 
        return
    PostOrderTraversal(tree._left)
    PostOrderTraversal(tree._right)
    print(tree._element, end = " ")

    
def InOrderTraversal(tree):
    if tree == None: 
        return
    InOrderTraversal(tree._left)
    print(tree._element, end = " ")
    InOrderTraversal(tree._right)

def levelOrderTraversal(tree):
    if tree == None: 
        return
    queue = LinkedQueue()
    queue.enqueue(tree)
    while not queue.is_empty():
        next_node = queue.dequeue()
        print(next_node._element, end = " ")
        if next_node._left:
            queue.enqueue(next_node._left)
        if next_node._right:
            queue.enqueue(next_node._right)


### Uncomment the following code if you want to print the tree.
### We assume that you had variables:  _left, _right, _element in the TreeWithoutParent Class.

def pretty_print(A):
    levels = 3      # Need a function to calculate levels. Use 3 for now.
    print_internal([A], 1, levels)

def print_internal(this_level_nodes, current_level, max_level):
    if (len(this_level_nodes) == 0 or all_elements_are_None(this_level_nodes)):
        return  # Base case of recursion: out of nodes, or only None left

    floor = max_level - current_level;
    endgeLines = 2 ** max(floor - 1, 0);
    firstSpaces = 2 ** floor - 1;
    betweenSpaces = 2 ** (floor + 1) - 1;
    print_spaces(firstSpaces)
    next_level_nodes = []
    for node in this_level_nodes:
        if (node is not None):
            print(node._element, end = "")
            next_level_nodes.append(node._left)
            next_level_nodes.append(node._right)
        else:
            next_level_nodes.append(None)
            next_level_nodes.append(None)
            print_spaces(1)

        print_spaces(betweenSpaces)
    print()
    for i in range(1, endgeLines + 1):
        for j in range(0, len(this_level_nodes)):
            print_spaces(firstSpaces - i)
            if (this_level_nodes[j] == None):
                    print_spaces(endgeLines + endgeLines + i + 1);
                    continue
            if (this_level_nodes[j]._left != None):
                    print("/", end = "")
            else:
                    print_spaces(1)
            print_spaces(i + i - 1)
            if (this_level_nodes[j]._right != None):
                    print("\\", end = "")
            else:
                    print_spaces(1)
            print_spaces(endgeLines + endgeLines - i)
        print()

    print_internal(next_level_nodes, current_level + 1, max_level)

def all_elements_are_None(list_of_nodes):
    for each in list_of_nodes:
        if each is not None:
            return False
    return True

def print_spaces(number):
    for i in range(number):
        print(" ", end = "")


print("\nUsing Tree Data Structure Without a parent")

##Create a expression tree for this expression:  3*2 + 5-2"

tree = TreeWithoutParent("+")
tree._left = TreeWithoutParent("*")
tree._right = TreeWithoutParent("-")
tree._left._left = TreeWithoutParent("3")
tree._left._right = TreeWithoutParent("2")
tree._right._left = TreeWithoutParent("5")
tree._right._right = TreeWithoutParent("2")



pretty_print(tree) #Call pretty_print to print the tree

print("\nPreOrder:")
PreOrderTraversal(tree)       # should print: + * 3 2 - 5 2  
print("\nPostOrder:")
PostOrderTraversal(tree)    # should print: 3 2 * 5 2 - + 
print("\nInOrder:")
InOrderTraversal(tree)        # should print: 3 * 2 + 5 - 2
print("\nLevelOrder:")
levelOrderTraversal(tree)        # should print: 3 * 2 + 5 - 2  