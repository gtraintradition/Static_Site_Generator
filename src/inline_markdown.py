from text_enums import TextType, DelimiterType

from textnode import TextNode




def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # old_nodes is a list of TextNodes, 
    # delimiter, text_type are strings (?)

    if type(old_nodes) != list:
        raise Exception("\"old_nodes\" (arg 1) needs to be a list of TextNodes.")
    if old_nodes == []:
        raise Exception("\"old_nodes\" (arg 1) can't be empty.")
    if delimiter not in DelimiterType:
        raise ValueError("\"Delimiter\" not recognized, only the following delimiters are accepted: \"**\", \"*\", \"`\".")

    splitted_nodes = map(lambda node: (process_node(node, delimiter, text_type)) , old_nodes)

    final = []
    for node in splitted_nodes:
        final.extend(node)

    return final


def process_node(node, delimiter, text_type):
    # node is a TextNode object, of TextType.TEXT only

    if type(node) != TextNode:
        raise Exception(f"Can only process TextNode objects")

    if node.text_type not in TextType or delimiter not in node.text:
        return [node]
    
    if delimiter == "*" and "**" in node.text:
        return [node]

    splitted_node = node.text.split(delimiter)

    if len(splitted_node) <= 1:
        return splitted_node

    # after thinking about it, it could be a choice of the user to use an odd number of delimiters
    # to check if the number of delimiters present in the node is even (we must have an odd number of splits),
    # if not it means there is too much or not enough delimiters. The markdown is invalid
    if len(splitted_node) % 2 == 0:
        raise Exception(f"Number of delimiters must be an even number/section must be closed for the markdown to be valid.")

    result = []
    for i in range(len(splitted_node)):
        if splitted_node[i] == "":
            continue
        if i % 2 == 0:
            result.append(TextNode(splitted_node[i], TextType.TEXT))
        else:
            result.append(TextNode(splitted_node[i], text_type))

    return result

