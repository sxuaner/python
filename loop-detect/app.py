#!/Users/xuansong/.bin/py38

# How to get user input?
import sys
from tkinter.tix import Tree;

for i in sys.argv:
    print(i);

class TreeNode:
    def __init__(self, leId, parents):
        self.leId=leId
        self.parents=parents
    
    # By default this method return False unless a loop is found
    # single_parent_link is the list that stores all the le ids from the root to a leaf
    def detect_loop(self, known_nodes, single_parent_link):
        print(single_parent_link)
        print("current node's le-id", self.leId)
        if(self.parents is not None):
            # This stack is used to store multiple parents of a node if it has them.
            parent_stack = []
            # Loop though the parent array and add them to the parent_stack
            for i in self.parents:
                parent_stack.append(i)

            # while parent_stack is not empty
            while parent_stack:            
                current_parent_leId = parent_stack.pop()
                # if this current node's parents have never been found in the link.
                if current_parent_leId not in single_parent_link:
                    single_parent_link.append(current_parent_leId)
                    # Retrieve the node with le id
                    # Error check here
                    current_parent_node = known_nodes[current_parent_leId]
                    # print this id 
                    print("detecting %s", current_parent_leId)
                    current_parent_node.detect_loop(
                        known_nodes, single_parent_link)
                    print()
                else:
                    raise Exception(
                        "This node's parent is in the link, raising an exception")
        else: 
            print("This node's parent is None")

            # parent_stack.pop gets the last parent id. Retrive this node from the dict
          
        

    
# Test data
parent_node_00424 = ["09628", "00342", "02685", "12918"]
node_00424 = TreeNode("00424", parent_node_00424)
node_09628 = TreeNode("09628", None)
node_00342 = TreeNode("00342", None)
node_02685 = TreeNode("02685", None)

parent_node_02848 = ["00543", "00424"]
node_02848 = TreeNode("02848", parent_node_02848)
node_00543 = TreeNode("00543", None)

parent_node_00425 = ["00424", "02848"]
node_00425 = TreeNode("00425", parent_node_00425)

parent_node_12918 = ["02848", "02350"]
node_12918 = TreeNode("12918", parent_node_12918)
node_02350 = TreeNode("02350", None)

# known_nodes is mock for data source)
known_nodes = {node_00425.leId: node_00425,
               node_00424.leId: node_00424,
               node_02848.leId: node_02848,
               node_12918.leId: node_12918,
               node_09628.leId: node_09628,
               node_00342.leId: node_00342,
               node_02685.leId: node_02685,
               node_00543.leId: node_00543,
               node_02350.leId: node_02350
               }
# End of test data

# test case:
# With detect_loop(), I should know whether there is a loop among the parents
node = node_00425
# this stack is used to trace a single link.
single_parent_link = []
single_parent_link.append(node.leId)

try:
    node.detect_loop(known_nodes, single_parent_link)
except Exception:
    print("An exception occurred")
