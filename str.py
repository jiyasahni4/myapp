import streamlit as st

def huffman_decoding(encoded_text, huffman_tree):
    decoded_text = ""
    current_node = huffman_tree

    for bit in encoded_text:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.value is not None:
            decoded_text += current_node.value
            current_node = huffman_tree

    return decoded_text


def main():
    st.title("Huffman Decoding")

    encoded_text_input = st.text_input("Enter the encoded text:")
    tree_input = st.text_input("Enter the Huffman tree:")
    if st.button("Decode"):
        tree = build_huffman_tree(tree_input)
        decoded_text = huffman_decoding(encoded_text_input, tree)
        st.success(f"Decoded text: {decoded_text}")

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_huffman_tree(level_order):
    if not level_order:
        return None

    nodes = []
    root = TreeNode(level_order[0])
    nodes.append(root)

    i = 1
    while i < len(level_order):
        node = nodes.pop(0)

        # Left child
        if level_order[i] is not None:
            node.left = TreeNode(level_order[i])
            nodes.append(node.left)
        i += 1

        # Right child
        if i < len(level_order) and level_order[i] is not None:
            node.right = TreeNode(level_order[i])
            nodes.append(node.right)
        i += 1

    return root


if __name__ == "__main__":
    main()
