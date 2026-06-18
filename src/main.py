#!/usr/bin/python3

print("hello world")

import textnode

def main():
    print(textnode.TextNode("This is some anchor text", textnode.TextType('link'), "https://www.boot.dev"))


main()
