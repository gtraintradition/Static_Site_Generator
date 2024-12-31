import re

from htmlnode import LeafNode
from textnode import TextNode

from generator_enums import TextType, DelimiterType, TagType, BlockTypes




def text_node_to_html_node(text_node):

    def process_list_to_dict(props_list):
        if len(props_list) > 1:
            return {props_list[0]: ""} | process_list_to_dict(props_list[1:])
        return {props_list[0]: ""}

    if not isinstance(text_node, TextNode):
        raise ValueError("Argument passed is not a TextNode")
    
    if text_node.text_type not in TextType:
        raise Exception(f"text_type: \"{text_node.text_type}\" not recognized")
    
    for tag in TagType:
        if text_node.text_type.name == tag.name:
            leaf_tag = tag.value['tag']
            props = tag.value['props']

    if props == None:
        new_LeafNode = LeafNode(leaf_tag, text_node.text, props)
        return new_LeafNode

    if props != None and props != []:
        leaf_props = process_list_to_dict(props)
        for prop in leaf_props.keys():
            match prop:
                case "href":
                    leaf_props["href"] = text_node.url
                case "src":
                    leaf_props["src"] = text_node.url
                case "alt":
                    leaf_props["alt"] = text_node.text
        
        leaf_text = text_node.text
        if text_node.text_type == TextType.IMAGE:
            leaf_text = ""
        new_LeafNode = LeafNode(leaf_tag, leaf_text, leaf_props)
        return new_LeafNode
    

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # old_nodes is a list of TextNodes, 
    # delimiter, text_type are strings (?)


    def process_node(node, delimiter, text_type):
    # node is a TextNode object, of TextType.TEXT only

        if type(node) != TextNode:
            raise Exception(f"Can only process TextNode objects, not \n{node}\n of type \n{type(node)}\n")

        if node.text_type not in TextType or delimiter not in node.text:
            return [node]
        
        #need to get rid of this
        if delimiter == "*" and "**" in node.text:
            return [node]

        if delimiter == "*":
            delimiter = r"\*(.*?)\*"

        if delimiter == "**":
            delimiter = r"\*\*(.*?)\*\*"

        if delimiter == r"\*(.*?)\*" or delimiter == r"\*\*(.*?)\*\*":
            splitted_node = re.split(delimiter, node.text)
        else:    
            splitted_node = node.text.split(delimiter)

        if len(splitted_node) <= 1:
            return [node]

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


    if type(old_nodes) != list:
        raise Exception("\"old_nodes\" (arg 1) needs to be a list of TextNodes.")
    if old_nodes == []:
        raise Exception("\"old_nodes\" (arg 1) can't be empty.")
    if delimiter not in DelimiterType:
        raise ValueError(f"Delimiter \"{delimiter}\" not recognized, only the following delimiters are accepted: \"**\", \"*\", \"`\".")

    splitted_nodes = map(lambda node: (process_node(node, delimiter, text_type)) , old_nodes)


    final = []
    for node in splitted_nodes:
        final.extend(node)

    return final


def split_nodes_delimiter2(old_nodes, delimiter, text_type):
    # old_nodes is a list of TextNodes, 
    # delimiter, text_type are strings (?)


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


    if type(old_nodes) != list:
        raise Exception("\"old_nodes\" (arg 1) needs to be a list of TextNodes.")
    if old_nodes == []:
        raise Exception("\"old_nodes\" (arg 1) can't be empty.")
    if delimiter not in DelimiterType:
        raise ValueError(f"Delimiter \"{delimiter}\" not recognized, only the following delimiters are accepted: \"**\", \"*\", \"`\".")

    splitted_nodes = map(lambda node: (process_node(node, delimiter, text_type)) , old_nodes)

    final = []
    for node in splitted_nodes:
        final.extend(node)

    return final






def split_nodes_image(old_nodes):
    # takes a list of TextType.TEXT, returns a list of TextType.TEXT and TextType.IMAGE if there are any


    def process_node_image(node):
    # node is a TextNode object, of TextType.TEXT only

        if type(node) != TextNode:
            raise Exception(f"Can only process TextNode objects, make sure all the objects in the list you passed are TextNodes")

        if node.text_type != TextType.TEXT:
            return [node]
        

        delimiter = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
        splitted_node = re.split(delimiter, node.text)

        if len(splitted_node) <= 1:
            return [node]

        result = []
        for i in range(0, len(splitted_node), 3):
            if splitted_node[i] != "":
                result.append(TextNode(splitted_node[i], TextType.TEXT))
            if i != (len(splitted_node) - 1):
                result.append(TextNode(splitted_node[i + 1], TextType.IMAGE, splitted_node[i + 2]))

        return result
    

    if type(old_nodes) != list:
        raise Exception("\"old_nodes\" (arg 1) needs to be a list of TextNodes.")
    if old_nodes == []:
        raise Exception("\"old_nodes\" (arg 1) can't be empty.")

    splitted_nodes = map(lambda node: (process_node_image(node)) , old_nodes)

    final = []
    for node in splitted_nodes:
        final.extend(node)

    return final


def split_nodes_link(old_nodes):
    # takes a list of TextType.TEXT, returns a list of TextType.TEXT and TextType.LINK if there are any


    def process_node_image(node):
    # node is a TextNode object, of TextType.TEXT only

        if type(node) != TextNode:
            raise Exception(f"Can only process TextNode objects, make sure all the objects in the list you passed are TextNodes")

        if node.text_type != TextType.TEXT:
            return [node]
        

        delimiter = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
        splitted_node = re.split(delimiter, node.text)

        if len(splitted_node) <= 1:
            return [node]

        result = []
        for i in range(0, len(splitted_node), 3):
            if splitted_node[i] != "":
                result.append(TextNode(splitted_node[i], TextType.TEXT))
            if i != (len(splitted_node) - 1):
                result.append(TextNode(splitted_node[i + 1], TextType.LINK, splitted_node[i + 2]))

        return result
    

    if type(old_nodes) != list:
        raise Exception("\"old_nodes\" (arg 1) needs to be a list of TextNodes.")
    if old_nodes == []:
        raise Exception("\"old_nodes\" (arg 1) can't be empty.")

    splitted_nodes = map(lambda node: (process_node_image(node)) , old_nodes)

    final = []
    for node in splitted_nodes:
        final.extend(node)

    return final


def split_nodes_heading(old_nodes):
    # takes a list of TextType.TEXT, returns a list of TextType.TEXT and TextType.LINK if there are any


    def process_node_heading(node):
    # node is a TextNode object, of TextType.TEXT only

        if type(node) != TextNode:
            raise Exception(f"Can only process TextNode objects, make sure all the objects in the list you passed are TextNodes")

        if node.text_type != TextType.TEXT:
            return [node]
        
        result = []
        match = re.match(BlockTypes.HEADING.value, node.text[0:8])

        if match != None:
            for a_type in TextType:
                if a_type.value[-1] == str(len(match[0]) - 1):
                    node_type = a_type
            result.append(TextNode(node.text[len(match[0]):], node_type))       
            return result
        else:
            return [node]
    

    if type(old_nodes) != list:
        raise Exception("\"old_nodes\" (arg 1) needs to be a list of TextNodes.")
    if old_nodes == []:
        raise Exception("\"old_nodes\" (arg 1) can't be empty.")

    splitted_nodes = map(lambda node: (process_node_heading(node)) , old_nodes)

    final = []
    for node in splitted_nodes:
        final.extend(node)

    return final


def split_nodes_quote(old_nodes):
    # takes a list of TextType.TEXT, returns a list of TextType.TEXT and TextType.LINK if there are any


    def process_node_quote(node):
    # node is a TextNode object, of TextType.TEXT only

        if type(node) != TextNode:
            raise Exception(f"Can only process TextNode objects, make sure all the objects in the list you passed are TextNodes")

        if node.text_type != TextType.TEXT:
            return [node]
        
        result = []
        new_lines = []
        lines = node.text.split("\n")
        for line in lines:
            if not re.match(BlockTypes.QUOTE.value, line[0]):
                return [node]
            new_lines.append(line[1:])
        cleaned_text = "\n".join(new_lines)
        result.append(TextNode(cleaned_text, TextType.QUOTE))       

        return result

    if type(old_nodes) != list:
        raise Exception("\"old_nodes\" (arg 1) needs to be a list of TextNodes.")
    if old_nodes == []:
        raise Exception("\"old_nodes\" (arg 1) can't be empty.")

    splitted_nodes = map(lambda node: (process_node_quote(node)) , old_nodes)

    final = []
    for node in splitted_nodes:
        final.extend(node)

    return final


def split_nodes_unordered_list(old_nodes):
    # takes a list of TextType.TEXT, returns a list of TextType.TEXT and TextType.LINK if there are any


    def process_node_unordered_list(node):
    # node is a TextNode object, of TextType.TEXT only

        if type(node) != TextNode:
            raise Exception(f"Can only process TextNode objects, make sure all the objects in the list you passed are TextNodes")

        if node.text_type != TextType.TEXT:
            return [node]
        
        result = []
        new_lines = []
        lines = node.text.split("\n")
        for line in lines:
            if not re.match(BlockTypes.UNORDERED_LIST.value, line[0:3]):
                return [node]
            new_lines.append("<li>" + line[2:] + "</li>")
        cleaned_text = "\n".join(new_lines)
        result.append(TextNode(cleaned_text, TextType.UNORDERED_LIST))       

        return result
    

    if type(old_nodes) != list:
        raise Exception("\"old_nodes\" (arg 1) needs to be a list of TextNodes.")
    if old_nodes == []:
        raise Exception("\"old_nodes\" (arg 1) can't be empty.")

    splitted_nodes = map(lambda node: (process_node_unordered_list(node)) , old_nodes)

    final = []
    for node in splitted_nodes:
        final.extend(node)

    return final


#todo
def split_nodes_ordered_list(old_nodes):
    # takes a list of TextType.TEXT, returns a list of TextType.TEXT and TextType.LINK if there are any


    def process_node_ordered_list(node):
    # node is a TextNode object, of TextType.TEXT only

        if type(node) != TextNode:
            raise Exception(f"Can only process TextNode objects, make sure all the objects in the list you passed are TextNodes")

        if node.text_type != TextType.TEXT:
            return [node]
        
        result = []
        new_lines = []
        lines = node.text.split("\n")
        for i in range(len(lines)):
            if not re.match(BlockTypes.ORDERED_LIST.value, lines[i][0:4]) or int(lines[i][0]) -1 != i:
                return [node]
            new_lines.append("<li>" + lines[i][3:] + "</li>")
        cleaned_text = "\n".join(new_lines)
        result.append(TextNode(cleaned_text, TextType.ORDERED_LIST))       

        return result
    

    if type(old_nodes) != list:
        raise Exception("\"old_nodes\" (arg 1) needs to be a list of TextNodes.")
    if old_nodes == []:
        raise Exception("\"old_nodes\" (arg 1) can't be empty.")

    splitted_nodes = map(lambda node: (process_node_ordered_list(node)) , old_nodes)

    final = []
    for node in splitted_nodes:
        final.extend(node)

    return final
