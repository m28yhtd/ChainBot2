REPLANNING_PROMPT2 = """
The plan generation prompt you must follow by default is: {plan_prompt}

In the current environment, the objects are: {found_objects}

and the domain rule is : {domain_rules}

and the prompt that collects such examples: {example}

The initial state of the environment in which the actions will be performed is as follows: {initial_state}

The task to be performed is as follows: {instruction}

The previous execution plan produced accordingly is as follows: {prev_plan}

Here is the current state where execution stopped midway while following the above plan: {current_state}

At this point, generate a new plan by excluding from the original execution plan any steps that are already considered accomplished in the current state toward achieving the task.
When creating the new plan, any remaining steps that were not deleted must not be further modified from the original execution plan.

The newly generated plan, when verified against the plan generation prompt and the domain rules, must be able to satisfy the task upon execution.

[output example]
plan = "
    <plan>
        <sequence>
            <apack>
                <precondition>The red block is empty on top.</precondition>
                <precondition>The bottom side is empty on top.</precondition>
                <action>robot.pick_and_place("red block", "bottom side")</action>
                <postcondition>The red block is placed on top of the bottom side.</postcondition>
                <postcondition>The bottom side is not empty on top.</postcondition>
            </apack>
            <apack>
                <precondition>The yellow block is empty on top.</precondition>
                <precondition>The red block is empty on top.</precondition>
                <action>robot.pick_and_place("yellow block", "red block")</action>
                <postcondition>The yellow block is placed on top of the red block.</postcondition>
                <postcondition>The red block is not empty on top.</postcondition>
            </apack>
            <apack>
                <precondition>The brown block is empty on top.</precondition>
                <precondition>The yellow block is empty on top.</precondition>
                <action>robot.pick_and_place("brown block", "yellow block")</action>
                <postcondition>The brown block is placed on top of the yellow block.</postcondition>
                <postcondition>The yellow block is not empty on top.</postcondition>
            </apack>
            <apack>
                <precondition>The purple block is empty on top.</precondition>
                <precondition>The brown block is empty on top.</precondition>
                <action>robot.pick_and_place("purple block", "brown block")</action>
                <postcondition>The purple block is placed on top of the brown block.</postcondition>
                <postcondition>The brown block is not empty on top.</postcondition>
            </apack>
            <apack>
                <precondition>The blue block is empty on top.</precondition>
                <precondition>The purple block is empty on top.</precondition>
                <action>robot.pick_and_place("blue block", "purple block")</action>
                <postcondition>The blue block is placed on top of the purple block.</postcondition>
                <postcondition>The purple block is not empty on top.</postcondition>
            </apack>
        </sequence>
    </plan>
    "

current state = "
    the blue block is placed on top of the table.
    the blue block is not empty on top.
    the red block is placed on top of the table.
    the red block is not empty on top.
    the yellow block is placed on top of the red block.
    the yellow block is not empty on top.
    the purple block is placed on top of the blue block.
    the purple block is empty on top.
    the brown block is placed on top of the yellow block.
    the brown block is empty on top.
    the blue bowl is placed on top of the table.
    the blue bowl is empty on top.
    the red bowl is placed on top of the table.
    the red bowl is empty on top.
    the yellow bowl is placed on top of the table.
    the yellow bowl is empty on top.
    the purple bowl is placed on top of the table.
    the purple bowl is empty on top.
    the brown bowl is placed on top of the table.
    the brown bowl is empty on top.
    "

output (newly generated plan) = "
    <plan>
        <sequence>
            <apack>
                <precondition>The purple block is empty on top.</precondition>
                <precondition>The brown block is empty on top.</precondition>
                <action>robot.pick_and_place("purple block", "brown block")</action>
                <postcondition>The purple block is placed on top of the brown block.</postcondition>
                <postcondition>The brown block is not empty on top.</postcondition>
            </apack>
            <apack>
                <precondition>The blue block is empty on top.</precondition>
                <precondition>The purple block is empty on top.</precondition>
                <action>robot.pick_and_place("blue block", "purple block")</action>
                <postcondition>The blue block is placed on top of the purple block.</postcondition>
                <postcondition>The purple block is not empty on top.</postcondition>
            </apack>
        </sequence>
    </plan>
    "


Please respond like examples. Do NOT use markdown or code blocks (e.g. no ```python).
Just return the response like examples.
"""
