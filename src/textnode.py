from enum import Enum

class TextType(Enum):
    BOLD_TYPE   = "bold"
    ITALIC_TYPE = "italic"
    CODE_TYPE   = "code"
    LINK_TYPE   = "link"
    IMAGE_TYPE  = "image"

    #bold   = "**Bold text**"
    #italic = "_Italic text_"
    #code   = "`Code text`"
    #link   = "[anchor text](url)"
    #image  = "![alt text](url)"

class TextNode():
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url
 
    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False
 
    def __repr__(self):
        # TODO: string representation TextNode(TEXT, TEXT_TYPE, URL)
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
