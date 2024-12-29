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


class DelimiterType(Enum):
    BOLD = "**"
    ITALIC = "*"
    CODE = "`"