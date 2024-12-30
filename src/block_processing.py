import re

from generator_enums import BlockTypes



def markdown_to_blocks(markdown):
    # Accepts a markdown string, returns a list of block strings
    
    if type(markdown) != str:
        raise ValueError("Only a string is accepted")
    
    block_list = list(filter(lambda split: split != "", markdown.split("\n\n")))
    
    if len(block_list) == 1:
        return [block_list[0].strip()]
    
    stripped_block_list = list(map(lambda block: block.strip(), block_list))

    return stripped_block_list


def block_to_block_type(block):
    # Takes a single block of markdown text as input and returns a string representing the type of block it is

    if type(block) != str:
        raise ValueError("Only a string is accepted, it should represent a block of markdown")

    if block == "":
        return BlockTypes.PARAGRAPH

    for block_type in BlockTypes:
        # line below is safety just in case "BlockTypes.PARAGRAPH" is moved to the 1st index of "BlockTypes"
        if block_type.name == "PARAGRAPH":
            continue
        if block_type.name == "CODE" and re.match(block_type.value, block[-3:]) and re.match(block_type.value, block[0:4]):
            return block_type
        if block_type.name == "HEADING" and re.match(block_type.value, block[0:7]):
            return block_type
        if block_type.name == "ORDERED_LIST" and re.match(block_type.value, block[0:2]):
            return block_type
        if re.match(block_type.value, block[0]):
            return block_type

    return BlockTypes.PARAGRAPH






