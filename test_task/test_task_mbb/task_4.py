initial_prompt = "Find the matching color block for each bowl and place it inside."

initial_state = """
The blue block is placed on top of the table.
The red block is placed on top of the table.
The yellow block is placed on top of the table.
The purple block is placed on top of the yellow block.
The blue bowl is placed on top of the table.
The red bowl is placed on top of the table.
The yellow bowl is placed on top of the table.
The purple bowl is placed on top of the table.
The red bowl is empty on top.
The blue bowl is empty on top.
The yellow bowl is empty on top.
The purple bowl is empty on top.
The blue block is empty on top.
The yellow block is not empty on top.
The purple block is empty on top.
The red block is empty on top."""

found_objects = """objects = ['blue block', 'red block', 'yellow block', 'purple block', 'blue bowl', 'red bowl', 'yellow bowl', 'purple bowl']"""