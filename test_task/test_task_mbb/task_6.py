initial_prompt = """Stack the blocks from the bottom up in the order: yellow block, blue block, brown block at any location, and place the other blocks into the bowls matching their colors."""

initial_state = """
The blue block is placed on top of the brown block.
The red block is placed on top of the table.
The brown block is placed on top of the table.
The yellow block is placed on top of the table.
The purple block is placed on top of the yellow block.
The blue bowl is placed on top of the table.
The red bowl is placed on top of the table.
The yellow bowl is placed on top of the table.
The purple bowl is placed on top of the table.
The brown bowl is placed on top of the table.
The red bowl is empty on top.
The blue bowl is empty on top.
The yellow bowl is empty on top.
The purple bowl is empty on top.
The brown bowl is empty on top.
The red block is empty on top.
The yellow block is not empty on top.
The purple block is empty on top.
The blue block is empty on top.
The brown block is not empty on top."""

found_objects = """objects = ['blue block', 'red block', 'yellow block', 'purple block',
'brown block', 'blue bowl', 'red bowl', 'yellow bowl', 'purple bowl', 'brown bowl']"""