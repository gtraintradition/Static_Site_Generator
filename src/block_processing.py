import re

from generator_enums import BlockTypes




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
        
        if block_type.name == "ORDERED_LIST" and re.match("1. ", block[0:3]):
            lines = block.split("\n")
            for i in range(1, len(lines)):
                if lines[i][0:3] != f"{i + 1}. ":
                    return BlockTypes.PARAGRAPH
            return block_type
        
        if block_type.name == "UNORDERED_LIST" and re.match(block_type.value, block[0:2]):
            lines = block.split("\n")
            for line in lines:
                if not re.match(block_type.value, line[0:2]):
                    return BlockTypes.PARAGRAPH
            return block_type
        
        if block_type.name == "QUOTE" and re.match(block_type.value, block[0]):
            lines = block.split("\n")
            for line in lines:
                if not re.match(block_type.value, line[0]):
                    return BlockTypes.PARAGRAPH
            return block_type

    return BlockTypes.PARAGRAPH






