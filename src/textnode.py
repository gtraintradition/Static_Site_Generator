from enum import Enum



class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TagType(Enum):
    TEXT = {"tag": None, "props": None}
    BOLD = {"tag": "b", "props": None}
    ITALIC = {"tag": "i", "props": None}
    CODE = {"tag": "code", "props": None}
    LINK = {"tag": "a", "props": ["href",]}
    IMAGE = {"tag": "img", "props": ["src","alt",]}


class TextNode():

    def __init__(self, text, text_type, url=None):
        self.text = text

        if text_type not in TextType:
            raise Exception(f"text_type: \"{text_type}\" not recognized")
        
        # if a value of TextType is passed, converts it to TextType
        if isinstance(text_type, str):
            for type in TextType:
                if type.value == text_type:
                    self.text_type = type

        else:
            self.text_type = text_type

        self.url = url


    def __eq__(text_node_1, text_node_2):
        # returns True if all TextNode attibutes match its counterpart
        match (text_node_1.text, text_node_1.text_type, text_node_1.url):
            case (text_node_2.text, text_node_2.text_type, text_node_2.url):
                return True

        return False


    def __repr__(self):
        # returns a string with class name and variables
        final = list(map(str, vars(self).values()))
        final[1] = f"{self.text_type.value}"        # might need adjustment if children classes are created
        return f"{self.__class__.__name__}({", ".join(final)})"
    

