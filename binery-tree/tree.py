
#Criando Avore Binaria
class Node:
    def __init__(self, data, esq, dir):
        self.data = data
        self.esq = esq
        self.dir = dir

class BinaryTree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None
    
    #Inserindo valores
    def insert(self, value):
        parent = None
        x = self.root
        while(x):
            parent = x
            if value < x.data: 
                x = x.left
            else:
                x = x.right
        if parent is None: #condição p/esquerda
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        #condição p/direita
        else:
            parent.right = Node(value)            
    # Percurso em In-Ordem
    def inOrder(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            print(end='') 
            self.inOrder(node.left)
        print(node, end='')
        if node.right:
            self.inOrder(node.right)
            print(end='')
    
    # Percurso em Pos-Ordem
    def posOrder(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder(node.left)
        if node.right:
            self.postorder(node.right)
        print(node)
    
    # Percurso em Pre-Ordem
     def preOrder(self, node=None):
         if Node = None:
              print(node.item,end=" ")
              self.preOrder(node.esq)
              self.preOrder(node.dir)

#Altura da Avore
    def height(self, node=None):
        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        if hright > hleft:
            return hright + 1
        return hleft + 1

#Buscando valores "ABB"
    def _search(self, value, node):
        if node is None: 
            return node
        if node.data == value: #procurando
            return BinaryTree(node) 
        if value < node.data:
            while node.data = value: # enquanto nao encontrou
               if value < node.data:
                    node = node.esq # ir para esquerda
               else:
                    node = node.dir # ir para direita
               if node == None:
                    return None # encontrou a folha então sai!
         return node

    def min(self, node):
        if node == None:
            node = self.root
        while node.left:
            node = node.left
        return node.data

    def max(self, node):
        if node == None:
            node = self.root
        while node.right:
            node = node.right
        return node.data

        print(" Exibindo em ordem: ",end="")
          self.inOrder(self.root)
          print("\n Exibindo em pos-ordem: ",end="")
          self.posOrder(self.root)
          print("\n Exibindo em pre-ordem: ",end="")
          self.preOrder(self.root)
          print("\n Altura da arvore: %d" %(self.height(self.root)))
          