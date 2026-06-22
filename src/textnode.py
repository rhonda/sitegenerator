from enum import Enum
from htmlnode import LeafNode


class TextType(Enum):
    TEXT   = "text"
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
        # string representation TextNode(TEXT, TEXT_TYPE, URL)
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"



def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text, None)

        case TextType.BOLD:
            return LeafNode("b", text_node.text, None)

        case TextType.ITALIC:
            return LeafNode("i", text_node.text, None)

        case TextType.CODE:
            return LeafNode("code", text_node.text, None)

        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})

        case TextType.IMAGE:
            return LeafNode("img", None, {"src": text_node.url})

        case _:
            raise ValueError("Unkown textnode type")
