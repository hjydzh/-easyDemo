#coding:utf-8
from Node import Node

#二叉树插入，删除，查询
class Tree:

    def __init__(self):

        self.root = None

    def insert(self,key):
        self.root = self.__insert_node(self.root,key)

    def find(self, key):
        return self.__find(self.root, key)

    def find_max(self):
        return self.__find_max(self.root)

    def delete(self, key):
        self.root = self.__delete_node(self.root,key)

    def __insert_node(self, node, key):
        if node is None:
            return Node(key,None,None)

        if key<=node.key:
            node.left_child =  self.__insert_node(node.left_child, key)
        else:
            node.right_child =  self.__insert_node(node.right_child, key)
        return node

    def __find_max(self, node):
        return node.right_child is None and node or self.__find_max(node.right_child)


    def __find(self, node, key):
        if node is None:
            return None
        if node.key == key:
            return node
        return node.key > key and self.__find(node.left_child, key) or node.key < key and self.__find(node.right_child,key)


    def __delete_node(self, node, key):
        if node is None:
            return
        if node.key < key:
            node.right_child = self.__delete_node(node.right_child, key)
            return node
        elif node.key > key:
            node.left_child = self.__delete_node(node.left_child, key)
            return node
        if node.left_child is None and node.right_child is None:
            return None
        elif node.left_child is None:
            return node.right_child
        elif node.right_child is None:
            return node.left_child
        else:
            max_node = self.__find_max(node)
            max_node.left_child = node.left_child
            max_node.right_child = node.right_child
            return max_node


if __name__ == '__main__':
    tree = Tree()
    tree.insert(7)
    tree.insert(3)
    tree.insert(12)
    tree.insert(9)
    tree.insert(21)
    node = tree.find(7)
    tree.delete(21)
    tree.delete(12)
    print tree.find_max().key