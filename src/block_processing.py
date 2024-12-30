from text_enums import TextType



def markdown_to_blocks(markdown):
    # accepts a markdown string, returns a list of block strings
    
    if type(markdown) != str:
        raise ValueError("Only a string is accepted")
    
    block_list = list(filter(lambda split: split != "", markdown.split("\n\n")))
    
    if len(block_list) == 1:
        return [block_list[0].strip()]
    
    stripped_block_list = list(map(lambda block: block.strip(), block_list))

    return stripped_block_list