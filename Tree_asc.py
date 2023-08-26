class tree:
  def __init__(self,Data):
    self.right = None
    self.left = None
    self.node = Data
  def show(self):
    if self.left:
      self.left.show()
    print(self.node)
    if self.right:
      self.right.show()
  def insert(self,new_data):
    if new_data>self.node:
      if self.left is None:
        self.left=tree(new_data)
      else:
        self.left.insert(new_data)
    elif new_data<self.node:
      if self.right is None:
        self.right = tree(new_data)
      else:
        self.right.insert(new_data)

lan = tree(55)
lan.insert(25)
lan.insert(60)
lan.insert(75)
lan.insert(79)
lan.insert(-20)
lan.insert(66)
lan.insert(0)
lan.insert(-50)
lan.insert(300)
lan.insert(240)
lan.insert(-2.454)
lan.insert(5)

lan.show()
