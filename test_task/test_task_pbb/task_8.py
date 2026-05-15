# 16
initial_prompt = "Place the blue and purple blocks in a bowl that matches their colors. Place the red and brown blocks in empty bowls that do not match their colors. Put the yellow block in the bottom right corner."

initial_state = """
The blue block is empty on top.
The blue block is placed on top of the table.
The red block is empty on top.
The red block is placed on top of the table.
The yellow block is empty on top.
The yellow block is placed on top of the table.
The purple block is empty on top.
The purple block is placed on top of the table.
The brown block is empty on top.
The brown block is placed on top of the table.
The blue bowl is empty on top.
The blue bowl is placed on top of the table.
The red bowl is empty on top.
The red bowl is placed on top of the table.
The yellow bowl is empty on top.
The yellow bowl is placed on top of the table.
The purple bowl is empty on top.
The purple bowl is placed on top of the table.
"""

found_objects = """
objects = [
"blue block", 
"red block", 
"yellow block",
"purple block",
"brown block",
"blue bowl", 
"red bowl", 
"yellow bowl",
"purple bowl"
]
"""