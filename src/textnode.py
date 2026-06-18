from enum import Enum

class TextType(Enum):
    BOLD   = "bold"
    ITALIC = "italic"
    CODE   = "code"
    LINK   = "link"
    IMAGE  = "image"

    #bold   = "**Bold text**"
    #italic = "_Italic text_"
    #code   = "`Code text`"
    #link   = "[anchor text](url)"
    #image  = "![alt text](url)"

class TextNode():
    def __init__(self, text: str, text_type: TextType, url: str | None = None) -> None:
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url
 
    def __eq__(self, other: "TextNode") -> bool:
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False
 
    def __repr__(self) -> str:
        # TODO: string representation TextNode(TEXT, TEXT_TYPE, URL)
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
