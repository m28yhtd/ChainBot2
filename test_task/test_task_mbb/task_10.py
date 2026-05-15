initial_prompt = """place the purple block in bowl of the matching color, and Stack the blocks from the bottom up in the order: blue block, red block, brown block."""

initial_state = """
The red block is placed on top of the brown block.
The brown block is placed on top of the table.
The blue block is placed on top of the table.
The purple block is placed on top of the blue block.
The blue bowl is placed on top of the table.
The red bowl is placed on top of the table.
The blue bowl is placed on top of the table.
The purple bowl is placed on top of the table.
The brown bowl is placed on top of the table.
The red bowl is empty on top.
The blue bowl is empty on top.
The blue bowl is empty on top.
The purple bowl is empty on top.
The brown bowl is not empty on top.
The red block is empty on top.
The blue block is not empty on top.
The purple block is empty on top.
The brown block is not empty on top."""

found_objects = """objects = ['red block', 'blue block', 'purple block', 'brown block', 'red bowl', 'blue bowl', 'purple bowl', 'brown bowl']"""