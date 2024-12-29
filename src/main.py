from textnode import *
from htmlnode import *







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

    dummy = TextNode("dummy text", "italic", "https://url.org")


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


    print(dummyHTML2.props_to_html())
    print("-----")
    print(parent_node2)
    print("-----")
    
    print(parent_node3.to_html())
    print("-----")
    print(parent_node2.to_html())
    print()


    """
    print(dummyLeafNode1)
    print(dummyLeafNode2)
    print("-----")
    print(dummyLeafNode1.to_html())
    print()
    print(dummyLeafNode2.to_html())
    print()
    print(dummyLeafNode3.to_html())
    print()
    print(dummyLeafNode3)
    print()
    """





if __name__ == "__main__":
    main()