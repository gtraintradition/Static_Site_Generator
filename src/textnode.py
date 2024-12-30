from generator_enums import TextType



class TextNode():

    def __init__(self, text, text_type, url=None):
        self.text = text

        # if a value of TextType is passed, converts it to TextType
        if isinstance(text_type, str):
            for type in TextType:
                if type.value == text_type.lower():
                    self.text_type = type
        else:
            self.text_type = text_type

        if self.text_type not in TextType:
            raise Exception(f"text_type: \"{text_type.lower()}\" not recognized")
        

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
        #final[1] = f"{self.text_type.value}"        # might need adjustment if children classes are created
        return f"{self.__class__.__name__}({", ".join(final)})"
    

