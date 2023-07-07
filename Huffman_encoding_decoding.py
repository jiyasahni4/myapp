import streamlit as st
import random
from streamlit import session_state
from graphviz import Digraph
import time

# Define the Node class
class Node:
    def _init_(self, symbol, prob):
        self.symbol = symbol
        self.prob = prob
        self.left = None
        self.right = None

# Define the function to generate a random Huffman tree
def generate_random_huffman_tree():
    # Generate random symbols and probabilities
    symbols = ['A', 'B', 'C', 'D', 'E']
    probs = [random.random() for _ in symbols]
    
    # Create nodes for each symbol-probability pair
    nodes = [Node(symbol, prob) for symbol, prob in zip(symbols, probs)]
    
    # Build the Huffman tree
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.prob)
        left = nodes.pop(0)
        right = nodes.pop(0)
        parent = Node(None, left.prob + right.prob)
        parent.left = left
        parent.right = right
        nodes.append(parent)
    
    return nodes[0]

# Define the function to create the Huffman tree visualization
def create_huffman_tree_visualization(node):
    dot = Digraph()
    
    def create_graph(node, parent=None):
        nonlocal dot
        if node.left:
            dot.node(str(node.left), label=f"{node.left.symbol}\n{node.left.prob}", style='filled', fillcolor='#00CCFF')
            if parent:
                dot.edge(str(parent), str(node.left), label='0', color='#FF0000')
            create_graph(node.left, node.left)
    
        if node.right:
            dot.node(str(node.right), label=f"{node.right.symbol}\n{node.right.prob}", style='filled', fillcolor='#00CCFF')
            if parent:
                dot.edge(str(parent), str(node.right), label='1', color='#00FF00')
            create_graph(node.right, node.right)
    
    create_graph(node)
    
    # Set graph attributes
    dot.graph_attr.update(bgcolor='None', size='10,10')
    dot.node_attr.update(shape='circle', style='filled', color='white')
    dot.edge_attr.update(color='white', fontcolor='white')
    
    return dot

# Streamlit app
def main():
    st.title("Huffman Tree Animation")
    
    if 'huffman_tree' not in session_state:
        # Generate a random Huffman tree
        session_state.huffman_tree = generate_random_huffman_tree()
        session_state.animation_step = 0
    
    # Create the Huffman tree visualization
    dot = create_huffman_tree_visualization(session_state.huffman_tree)
    
    # Perform animation step
    if session_state.animation_step < 3:
        # Increment the animation step
        session_state.animation_step += 1
        
        # Create an empty placeholder for the visualization
        placeholder = st.empty()
        
        # Update the placeholder with the current animation step
        dot_copy = dot.copy()
        placeholder.image(dot_copy.render(format='png'), use_column_width=True)
        
        # Wait for a brief moment before proceeding to the next animation step
        time.sleep(1)
    
    # Display the final Huffman tree visualization
    st.image(dot.render(format='png'), use_column_width=True)


if __name__ == '__main__':
    main()
