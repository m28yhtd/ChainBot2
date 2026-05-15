Domain_3_example = """
objects = ["blue block", "red block", "yellow block", "blue bowl", "red bowl", "yellow bowl"]
initial_state = '
The blue block is placed on top of the red block.
The red block is placed on top of the yellow block.
The yellow block is placed on top of the table.
The blue bowl is placed on top of the table.
The red bowl is placed on top of the table.
The yellow bowl is placed on top of the table.
The blue block is empty on top.
The red block is not empty on top.
The yellow block is not empty on top.
The red bowl is empty on top.
The blue bowl is empty on top.
The yellow bowl is empty on top.'
# Place all blocks except the red ones on the matching color bowl.
<plan>
    <sequence>
        <apack>
            <precondition>The blue block is empty on top.</precondition>
            <precondition>The blue bowl is empty on top.</precondition>
            <action>robot.pick_and_place("blue block", "blue bowl")</action>
            <postcondition>The blue block is placed on top of the blue bowl.</postcondition>
            <postcondition>The blue bowl is not empty on top.</postcondition>
        </apack>
        <apack>
            <precondition>The red block is empty on top.</precondition>
            <precondition>The bottom side is empty on top.</precondition>
            <action>robot.pick_and_place("red block", "bottom side")</action>
            <postcondition>The red block is placed on top of the bottom side.</postcondition>
            <postcondition>The bottom side is not empty on top.</postcondition>
        </apack>
        <apack>
            <precondition>The yellow block is empty on top.</precondition>
            <precondition>The yellow bowl is empty on top.</precondition>
            <action>robot.pick_and_place("yellow block", "yellow bowl")</action>
            <postcondition>The yellow block is placed on top of the yellow bowl.</postcondition>
            <postcondition>The yellow bowl is not empty on top.</postcondition>
        </apack>
    </sequence>
</plan>
objects = ["blue block", "red block", "yellow block", "purple block", "blue bowl", "red bowl", "yellow bowl"]
initial_state = '
The blue block is placed on top of the table.
The red block is placed on top of the blue block.
The yellow block is placed on top of the purple block.
The purple block is placed on top of the table.
The blue bowl is placed on top of the table.
The red bowl is placed on top of the table.
The yellow bowl is placed on top of the table.
The red bowl is empty on top.
The blue bowl is empty on top.
The yellow bowl is empty on top.
The yellow block is empty on top.
The purple block is not empty on top.
The blue block is not empty on top.
The red block is empty on top.'
# Put the blue block and the purple block into bowls of their matching colors.
<plan>
    <sequence>
        <apack>
            <precondition>The yellow block is empty on top.</precondition>
            <precondition>The bottom side is empty on top.</precondition>
            <action>robot.pick_and_place("yellow block", "bottom side“)</action>
            <postcondition>The yellow block is placed on top of the bottom side.</postcondition>
            <postcondition>The bottom side is not empty on top.</postcondition>
        </apack>
        <apack>
            <precondition>The red block is empty on top.</precondition>
            <precondition>The left side is empty on top.</precondition>
            <action>robot.pick_and_place("red block", "left side“)</action>
            <postcondition>The red block is placed on top of the left side.</postcondition>
            <postcondition>The left side is not empty on top.</postcondition>
        </apack>
        <apack>
            <precondition>The blue block is empty on top.</precondition>
            <precondition>The blue bowlis empty on top.</precondition>
            <action>robot.pick_and_place("blue block", "blue bowl“)</action>
            <postcondition>The blue block is placed on top of the blue bowl.</postcondition>
            <postcondition>The blue bowl is not empty on top.</postcondition>
        </apack>
        <apack>
            <precondition>The purple block is empty on top.</precondition>
            <precondition>The purple bowl is empty on top.</precondition>
            <action>robot.pick_and_place("purple block", "purple bowl")</action>
            <postcondition>The yellow block is placed on top of the purple bowl.</postcondition>
            <postcondition>The purple bowl is not empty on top.</postcondition>
        </apack>
    </sequence>
</plan>
objects = ["blue block", "red block", "yellow block", "purple block", "blue bowl", "red bowl", "yellow bowl"]
initial_state = '
The blue block is placed on top of the red block.
The red block is placed on top of the table.
The yellow block is placed on top of the blue block.
The purple block is placed on top of the yellow block.
The blue bowl is placed on top of the table.
The red bowl is placed on top of the table.
The yellow bowl is placed on top of the table.
The red bowl is empty on top.
The blue bowl is empty on top.
The yellow bowl is empty on top.
The purple block is empty on top.
The blue block is not empty on top.
The red block is not empty on top.
The yellow block is not empty on top.'
# Stack the blocks from the bottom in the order: blue, red, purple, yellow.
<plan>
    <sequence>
        <apack>
            <precondition>The purple block is empty on top.</precondition>
            <precondition>The bottom side is empty on top.</precondition>
            <action>robot.pick_and_place("purple block", "bottom side“)</action>
            <postcondition>The purple block is placed on top of the bottom side.</postcondition>
            <postcondition>The bottom side is not empty on top.</postcondition>
        </apack>
        <apack>
            <precondition>The yellow block is empty on top.</precondition>
            <precondition>The left side is empty on top.</precondition>
            <action>robot.pick_and_place("yellow block", "left side“)</action>
            <postcondition>The yellow block is placed on top of the left side.</postcondition>
            <postcondition>The left side is not empty on top.</postcondition>
        </apack>
        <apack>
            <precondition>The blue block is empty on top.</precondition>
            <precondition>The top left corner is empty on top.</precondition>
            <action>robot.pick_and_place("blue block", "top left corner")</action>
            <postcondition>The blue block is placed on top of the top left corner.</postcondition>
            <postcondition>The top left corner is not empty on top.</postcondition>
        </apack>
        <apack>
            <precondition>The red block is empty on top.</precondition>
            <precondition>The blue block is empty on top.</precondition>
            <action>robot.pick_and_place("red block", "blue block")</action>
            <postcondition>The red block is placed on top of the blue block.</postcondition>
            <postcondition>The blue block is not empty on top.</postcondition>
        </apack>
        <apack>
            <precondition>The purple block is empty on top.</precondition>
            <precondition>The red block is empty on top.</precondition>
            <action>robot.pick_and_place("purple block", "red block")</action>
            <postcondition>The purple block is placed on top of the red block.</postcondition>
            <postcondition>The red block is not empty on top.</postcondition>
        </apack>
        <apack>
            <precondition>The yellow block is empty on top.</precondition>
            <precondition>The purple block is empty on top.</precondition>
            <action>robot.pick_and_place("yellow block", "purple block")</action>
            <postcondition>The yellow block is placed on top of the purple block.</postcondition>
            <postcondition>The purple block is not empty on top.</postcondition>
        </apack>
    </sequence>
</plan>
"""

Domain_3_rules = """
These rules define the valid conditions for generating, verifying, and refining block placement plans. They must be followed to ensure successful execution.

- General Execution Rules
    1. Avoid unnecessary movements and aim for clear and efficient execution.
    2. Any action not aligned with the user's instruction is considered invalid, even if it does not violate physical constraints.
    3. Repeated or redundant actions should be avoided whenever possible.

- Rules for Picking Up Objects
    1. Only one block can be held and moved at a time.
    2. A block can only be picked up if there is no other block on top of it.
    3. If a block to be picked up has another block on top, the top block must first be moved to another space on the table.

- Rules for Placing Objects
    1. A block can only be placed:
       - into a bowl that currently contains no block,
       - or another block that currently contains no block on top of it,
       - or onto a clear space on the table.
       - The spaces on the table are:
         top left corner, top side, top right corner,
         left side, right side,
         bottom left corner, bottom side, bottom right corner.
    2. Each bowl can contain only one block at a time (no multiple occupancy).

- Instruction Compliance Rules
    1. Blocks must be placed according to the user's instruction (e.g., matching color or position).
    2. Such placement rules must be followed consistently throughout the task.
    3. All placements must satisfy the given constraints before being executed.

- Final Configuration Rules
    1. At the end of the task, it is acceptable for some blocks to remain outside the bowls.
    2. The final configuration must not violate any placement constraints given in the instruction.
"""