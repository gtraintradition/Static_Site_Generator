from enum import Enum

class Bender(Enum):
    AIR_BENDER = "air"
    WATER_BENDER = "water"
    EARTH_BENDER = "earth"
    FIRE_BENDER = "fire"

class TextNode():

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type      # linked to bender enum
        self.url = url

    def __eq__(self):
        if self.text == self.text_type == self.url:
            return True
        
    def __repr__(self):
        # returns a string representation of the object
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    