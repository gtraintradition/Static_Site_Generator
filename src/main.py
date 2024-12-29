from textnode import *
from htmlnode import *

from textnode_to_htmlnode import *





def main():

    d1 = {
    "href": "https://www.google.com", 
    "target": "_blank",
    }
    d2 = {
    "href": "https://www.duckduckgo.com", 
    "target": "_green_____",
    }
    lc1 = ["children1", "children2", "children3"]

    parent_node1 = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    dummy = TextNode("alt text", "image", "https://url.org")
    dummy2 = TextNode("dummy text", "bold", "https://url.org")
    dummy3 = TextNode("anchor text", "link", "https://url.org")


    dummyHTML1 = HTMLNode("tag name 1", 
                         "html tag value",
                         lc1,
                         d1)
    
    dummyHTML2 = HTMLNode("tag name 1", 
                         "html tag value",
                         lc1,
                         )

    dummyLeafNode1 = LeafNode("p", "This is a paragraph of text.")
    dummyLeafNode2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    dummyLeafNode3 = LeafNode("a", "Click me!", d1)

    parent_node2 = ParentNode(
    "io",
    [
        dummyLeafNode1,
        parent_node1,
        dummyLeafNode3,
        LeafNode("gg", "non text"),
    ],
    d2
    )

    parent_node3 = ParentNode("nc",[],)

    #######


    print("-----")
    converted1 = text_node_to_html_node(dummy)
    print("-----")
    

    print("-----")
    converted2 = text_node_to_html_node(dummy2)
    print("-----")
    print("-----")
    converted3 = text_node_to_html_node(dummy3)
    print("-----")
    
    print("------ converted")
    print(converted1)
    print("------ converted")
    print(converted2)
    print("------ converted")
    print(converted3)


if __name__ == "__main__":
    main()