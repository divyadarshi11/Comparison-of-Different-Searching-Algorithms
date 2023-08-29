#Divya Darshi
#1002090905

# import the tkinter module and alias it as "tk"
import tkinter as tk

# import the time module
import time

#LINEAR SEARCH

# define the function linear_search which takes an array and a value to search for
def linear_search(arr, x):
    
    # start the timer for performance measurement
    start_time = time.perf_counter()
    
    # iterate through the array
    for i in range(len(arr)):
        # check if the current element equals the search value
        if arr[i] == x:
            # end the timer for performance measurement
            end_time = time.perf_counter()
            # return the index of the found value and the time it took to find it
            return i, end_time - start_time
    
    # if the value is not found, end the timer for performance measurement
    end_time = time.perf_counter()
    # return -1 to indicate the value was not found and the time it took to search the array
    return -1, end_time - start_time

#BINARY SEARCH

def binary_search(arr, x):
    # Import the time module and start the timer
    start_time = time.perf_counter()
    # Initialize left and right pointers to the start and end of the array
    left = 0
    right = len(arr) - 1
    
    # Perform the binary search
    while left <= right:
        # Calculate the middle index of the current subarray
        mid = (left + right) // 2
        # If the middle element is the target element, stop and return the index and the time taken
        if arr[mid] == x:
            # Stop the timer and return the index and the time taken
            end_time = time.perf_counter()
            return mid, end_time - start_time
        # If the middle element is less than the target element, move the left pointer to mid+1
        elif arr[mid] < x:
            left = mid + 1
        # If the middle element is greater than the target element, move the right pointer to mid-1
        else:
            right = mid - 1
    
    # If the target element is not found, stop the timer and return -1 and the time taken
    end_time = time.perf_counter()
    return -1, end_time - start_time

#BST 

# Define a Node class that will be used to create nodes of the binary search tree
class Node:
    def __init__(self, data):
        # Initialize the left and right child nodes to None
        self.left = None
        self.right = None
        # Set the value of the node to the data passed as an argument
        self.data = data

# Define a Binary Search Tree (BST) class
class BST:
    def __init__(self):
        # Initialize an empty tree with a None root node
        self.root = None

    # Define an insert method to add a new node to the tree
    def insert(self, data):
        # If the tree is empty, set the new node as the root node
        if self.root is None:
            self.root = Node(data)
        else:
            # If the tree is not empty, call a recursive helper function to insert the node
            self._insert(data, self.root)

    # Define a recursive helper function to insert a node into the tree
    def _insert(self, data, node):
        # If the data to be inserted is less than the value of the current node, go left
        if data < node.data:
            # If the left child of the current node is None, add the new node here
            if node.left is None:
                node.left = Node(data)
            # If the left child is not None, call this method recursively on the left child
            else:
                self._insert(data, node.left)
        # If the data to be inserted is greater than the value of the current node, go right
        elif data > node.data:
            # If the right child of the current node is None, add the new node here
            if node.right is None:
                node.right = Node(data)
            # If the right child is not None, call this method recursively on the right child
            else:
                self._insert(data, node.right)

    # Define a search method to search for a node with a given value in the tree
    def search(self, data):
        # Call a recursive helper function to search for the node
        return self._search(data, self.root)

    # Define a recursive helper function to search for a node with a given value in the tree
    def _search(self, data, node):
        # If the node is None, return False
        if node is None:
            return False
        # If the value of the node matches the search value, return True
        elif data == node.data:
            return True
        # If the search value is less than the value of the node, search the left subtree
        elif data < node.data:
            return self._search(data, node.left)
        # If the search value is greater than the value of the node, search the right subtree
        else:
            return self._search(data, node.right)

# Define a function that creates a BST and searches for a given value in an array of integers
def bst_search(arr, x):
    # Record the start time of the search
    start_time = time.perf_counter()
    # Create a new BST
    bst = BST()
    # Insert each value in the array into the BST
    for i in arr:
        bst.insert(i)
    # Search for the given value in the BST
    result = bst.search(x)
    # Record the end time of the search and return the result and the time taken
    end_time = time.perf_counter()
    return result, end_time - start_time

#RED-BLACK TREE SEARCH

class NodeRB:
    def __init__(self, key, value, color):
        # Initialize a new instance of the NodeRB class with the given key, value, and color.
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.color = color

class Color:
    RED = "RED"
    BLACK = "BLACK"

class RedBlackTree:
    def __init__(self):
        # Initialize a new instance of the RedBlackTree class with an empty root node.
        self.root = None

    def insert(self, key, value=None):
        # Insert a new node with the given key and value into the tree.
        self.root = self._insert(self.root, key, value)
        self.root.color = Color.BLACK

    def _insert(self, nodeRB, key, value):
        # Insert a new node with the given key and value into the subtree rooted at nodeRB.
        if nodeRB is None:
            return NodeRB(key, value, Color.RED)

        if key < nodeRB.key:
            nodeRB.left = self._insert(nodeRB.left, key, value)
        elif key > nodeRB.key:
            nodeRB.right = self._insert(nodeRB.right, key, value)
        else:
            nodeRB.value = value if value is not None else nodeRB.value
        
        # Perform a color flip if both children of the current node are red.
        if self._is_red(nodeRB.left) and self._is_red(nodeRB.right):
            self._flip_colors(nodeRB)

        return nodeRB

    def rb_search(self, key):
        # Search for a node with the given key in the tree and return its value, or False if it is not found.
        nodeRB = self.root
        while nodeRB is not None:
            if key < nodeRB.key:
                nodeRB = nodeRB.left
            elif key > nodeRB.key:
                nodeRB = nodeRB.right
            else:
                return nodeRB.value
        return False

    def _rotate_left(self, nodeRB):
        # Rotate the subtree rooted at nodeRB to the left.
        x = nodeRB.right
        nodeRB.right = x.left
        x.left = nodeRB
        x.color = nodeRB.color
        nodeRB.color = Color.RED
        return x

    def _rotate_right(self, nodeRB):
        # Rotate the subtree rooted at nodeRB to the right.
        x = nodeRB.left
        nodeRB.left = x.right
        x.right = nodeRB
        x.color = nodeRB.color
        nodeRB.color = Color.RED
        return x

    def _flip_colors(self, nodeRB):
        # Flip the colors of nodeRB and its children.
        nodeRB.color = Color.RED
        nodeRB.left.color = Color.BLACK
        nodeRB.right.color = Color.BLACK

    def _is_red(self, nodeRB):
        # Return True if the color of nodeRB is red, False otherwise.
        if nodeRB is None:
            return False
        return nodeRB.color == Color.RED

def RBTree_search(arr, x):
    # Perform a Red-Black Tree search on the given array using the given key x and measure the time it takes to complete.
    start_time = time.perf_counter()
    rb_tree = RedBlackTree()
    for i in arr:
       rb_tree.insert(i)
    result = rb_tree.rb_search(x)
    end_time = time.perf_counter()
    return result, end_time - start_time


def search():
    # Get the input values from the user
    arr = list(map(int, arr_entry.get().split()))
    x = int(x_entry.get())

    # Call the selected search function
    if search_var.get() == 0:
        result, time_taken = linear_search(arr, x)
        if result == -1:
           result_label.config(text="Linear Search : Element not found", font=("Arial 10 bold"))
        else:
           result_label.config(text=f"Linear Search : Element found at index {result}", font=("Arial 10 bold"))
    elif search_var.get() == 1:
        result, time_taken = binary_search(sorted(arr), x)
        if result == -1:
           result_label.config(text="Binary Search : Element not found", font=("Arial 10 bold"))
        else:
           result_label.config(text=f"Binary Search : Element found at index {result}, Sorted array: {sorted(arr)}", font=("Arial 10 bold"))
    elif search_var.get() == 2:
        result, time_taken = bst_search(arr, x)
        if result == False:
           result_label.config(text="BST Search : Element not found", font=("Arial 10 bold"))
        else:
           result_label.config(text=f"BST Search : Element found", font=("Arial 10 bold"))
    else:
        result, time_taken = RBTree_search(arr, x)
        if result == None:
           result_label.config(text="RBTree Search : Element found", font=("Arial 10 bold"))
        else:
           result_label.config(text=f"RBTree Search : Element not found", font=("Arial 10 bold"))
     
    runtime_label.config(text=f"Time Taken: {time_taken*1000:.6f} ms", font=("Arial 10 bold"))
    
    #length of the array label
    length_label.config(text=f"Array Size: {len(arr)}", font=("Arial 8 bold"))
    
# Create the main window
root = tk.Tk()
root.title("Search Algorithms")
# Set the size of the window
root.geometry("600x500")


# Create the search input widgets
arr_label = tk.Label(root, text="Enter the Elements:", font=("Arial 10 bold"))
arr_label.pack()
arr_entry = tk.Entry(root, width=50)
arr_entry.pack()

length_label = tk.Label(root, text="", font=("Arial 8 bold"))
length_label.pack()

x_label = tk.Label(root, text="Search Element:", font=("Arial 10 bold"))
x_label.pack()
x_entry = tk.Entry(root, width=50)
x_entry.pack()

Algo_label = tk.Label(root, text="Select search Algorithm:", font=("Arial 10 bold"))
Algo_label.pack()

# Create the search algorithm selection widget
search_var = tk.IntVar()
linear_rb = tk.Radiobutton(root, text="Linear Search", variable=search_var, value=0)
linear_rb.pack()
binary_rb = tk.Radiobutton(root, text="Binary Search", variable=search_var, value=1)
binary_rb.pack()
BST_rb = tk.Radiobutton(root, text="Binary Search Tree", variable=search_var, value=2)
BST_rb.pack()
RedBlackTree_rb = tk.Radiobutton(root, text="RedBlackTree Search", variable=search_var, value=3)
RedBlackTree_rb.pack()

# Create the search button and result label
search_button = tk.Button(root, text="Search", command=search, width=10, height=1)
search_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()
runtime_label = tk.Label(root, text="")
runtime_label.pack()

# Start the main event loop
root.mainloop()