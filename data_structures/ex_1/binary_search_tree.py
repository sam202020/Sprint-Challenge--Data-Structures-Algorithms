class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    current = self
    cb(current)
    traversed = []
    traversed.append(current)
    while current.left:
      print(current.value)
      current = current.left
      current.depth_first_for_each(cb)
    for index, i in reversed(list(enumerate(traversed))):
      if i.right:
        current = i.right
        current.depth_first_for_each(cb)

    # def main_traverse(current, main_traversed, cb):
    #   if not main_traversed:
    #     return
    #   if not current.left:
    #     for index, i in reversed(list(enumerate(main_traversed))):

    #   if not s
      # root = self
      # def traverse_left(root, cb):
      #   traversed = []
      #   current = root
      #   while root.left != None:
      #     cb(current)
      #     traversed.append(current)
      #     current = current.left
      #   return traversed
      # if root.left:
      #   main_traversed = traverse_left(root, cb)
      # for i in reversed(main_traversed):
      #   if main_traversed[i].right:
      #     current = main_traversed[i].right
      #     cb(current)
      #     main_traversed.pop(current)
      #   else:
      #     main_traversed.pop(current)
      # def recurse_left(root, cb):
      #   if not root.left:
      #     return root
      #   cb(root.value)
      #   main_traversed.append(root)
      #   root = root.left
      #   recurse_left(root, cb)
      # root = recurse_left(root, cb)
      # for index, i in reversed(list(enumerate(main_traversed))):
      #   if i.right:
      #     root = i.right
      #     main_traversed.pop(index)
      #     recurse_left(root, cb)
    
  def breadth_first_for_each(self, cb):
    pass

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value

bst = BinarySearchTree(5)
bst.insert(2)
bst.insert(3)
bst.insert(7)
bst.insert(9)
print(bst.value)
max_val = bst.get_max
print(max_val)
# arr = []
# cb = lambda x: arr.append(x)
# bst.depth_first_for_each(cb)