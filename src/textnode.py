from enum import Enum


class Bender(Enum):
    AIR_BENDER = "air"
    WATER_BENDER = "water"
    EARTH_BENDER = "earth"
    FIRE_BENDER = "fire"


class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode():

    def __init__(self, text, text_type, url=None):
        self.text = text
        if text_type in TextType:
            self.text_type = text_type
        else:
            raise Exception(f"text_type: \"{text_type}\" not recognized")
        self.url = url

    def __eq__(text_node_1, text_node_2):
        # returns True if all TextNode attibutes match its counterpart
        match (text_node_1.text, text_node_1.text_type, text_node_1.url):
            case (text_node_2.text, text_node_2.text_type, text_node_2.url):
                return True

        return False
        
    def __repr__(self):
        # returns a string representation of the object
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    