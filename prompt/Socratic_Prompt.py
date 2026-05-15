DOMAIN_PROMPT1 = """
We will be working on a task where a robotic arm moves objects in an environment.
Your role is the task planner that should generate a sequence of robotic manipluation actions to achieve the user instruction from the given initial state.
The robot is assumed to be able to do only the pick_and_place action, which picks up a block and then places it on another block, a bowl, or one of the on-table locations.

Valid pick_targets: blocks  
Valid place_targets: blocks, bowls, and on-table locations in the environment  
Valid on-table locations:  
          top left corner, top side, top right corner,  
          left side, right side, bottom left corner, bottom side, bottom right corner

A plan must be expressed in the following XML format:
<plan>
    <sequence>
        <apack>
            <precondition>...</precondition>
            <precondition>...</precondition>
            <action>robot.pick_and_place("pick_target", "place_target")</action>
            <postcondition>...</postcondition>
            <postcondition>...</postcondition>
        </apack>
        <apack>
            <precondition>...</precondition>
            <precondition>...</precondition>
            <action>robot.pick_and_place("pick_target", "place_target")</action>
            <postcondition>...</postcondition>
            <postcondition>...</postcondition>
        </apack>
        ...
    </sequence>
</plan>

Explanations of the plan XML format:
 - Each <apack> block in the plan consists of two <precondition> elements, one <action> elements, two <postcondition> elements.
 - One <precondition> element should include the condition that the block to be picked up (pick_target) must be empty on top.  
          For example, "The red block is empty on top."
 - The other <precondition> element should include the condition that the target location to be placed on the picking block (pick_target) must be empty on top.  For example, "The yellow bowl is empty on top."
 - The <action> element should contain a pick_and_place action like `robot.pick_and_place("pick_target", "place_target")`,
     which picks one of pick_targets and then places on one of place_targets.
 - One <postcondition> elements should include the condition that the pick_target is placed on the top of the place_target.  
          For example, "The red block is placed on top of the yellow bowl."
 - The other <postcondition> elements should include the condition that the place_target is no longer empty on top.  
          For example, "The yellow bowl is not empty on top."

- Do not use symbols such as arrows (→) or shorthand notations. All relationships must be described in complete natural language sentences.

- Ensure that the final stack follows the target instruction precisely, and that all blocks are used according to domain rules.

Now plan the current task.
In the current environment, the objects are:
{found_objects}
User instruction:
{instruction}

Don't add any explanation—just output the converted plan.
Please respond like the examples. Do NOT use markdown or code blocks (e.g. no ```python).
Just return the response like examples.
"""

DOMAIN_PROMPT2 = """
We will be working on a task where a robotic arm moves objects in an environment.
Your role is the task planner that should generate a sequence of robotic manipluation actions to achieve the user instruction from the given initial state.
The robot is assumed to be able to do only the pick_and_place action, which picks up a block and then places it on another block, a bowl, or one of the on-table locations.

Valid pick_targets: blocks  
Valid place_targets: blocks, bowls, and on-table locations in the environment  
Valid on-table locations:  
          top left corner, top side, top right corner,  
          left side, right side, bottom left corner, bottom side, bottom right corner

A plan must be expressed in the following XML format:
<plan>
    <sequence>
        <apack>
            <precondition>...</precondition>
            <precondition>...</precondition>
            <action>robot.pick_and_place("pick_target", "place_target")</action>
            <postcondition>...</postcondition>
            <postcondition>...</postcondition>
        </apack>
        <apack>
            <precondition>...</precondition>
            <precondition>...</precondition>
            <action>robot.pick_and_place("pick_target", "place_target")</action>
            <postcondition>...</postcondition>
            <postcondition>...</postcondition>
        </apack>
        ...
    </sequence>
</plan>

Explanations of the plan XML format:
 - Each <apack> block in the plan consists of two <precondition> elements, one <action> elements, two <postcondition> elements.
 - One <precondition> element should include the condition that the block to be picked up (pick_target) must be empty on top.  
          For example, "The red block is empty on top."
 - The other <precondition> element should include the condition that the target location to be placed on the picking block (pick_target) must be empty on top.  For example, "The yellow bowl is empty on top."
 - The <action> element should contain a pick_and_place action like `robot.pick_and_place("pick_target", "place_target")`,
     which picks one of pick_targets and then places on one of place_targets.
 - One <postcondition> elements should include the condition that the pick_target is placed on the top of the place_target.  
          For example, "The red block is placed on top of the yellow bowl."
 - The other <postcondition> elements should include the condition that the place_target is no longer empty on top.  
          For example, "The yellow bowl is not empty on top."

- Do not use symbols such as arrows (→) or shorthand notations. All relationships must be described in complete natural language sentences.

- Ensure that the final stack follows the target instruction precisely, and that all blocks are used according to domain rules.

Now plan the current task.
In the current environment, the objects are:
{found_objects}
The initial state:
{initial_state}
User instruction:
{instruction}

Don't add any explanation—just output the converted plan.
Please respond like the examples. Do NOT use markdown or code blocks (e.g. no ```python).
Just return the response like examples.
"""

DOMAIN_PROMPT3 = """
We will be working on a task where a robotic arm moves objects in an environment.
Your role is the task planner that should generate a sequence of robotic manipluation actions to achieve the user instruction from the given initial state.
The robot is assumed to be able to do only the pick_and_place action, which picks up a block and then places it on another block, a bowl, or one of the on-table locations.

Valid pick_targets: blocks  
Valid place_targets: blocks, bowls, and on-table locations in the environment  
Valid on-table locations:  
          top left corner, top side, top right corner,  
          left side, right side, bottom left corner, bottom side, bottom right corner

A plan must be expressed in the following XML format:
<plan>
    <sequence>
        <apack>
            <precondition>...</precondition>
            <precondition>...</precondition>
            <action>robot.pick_and_place("pick_target", "place_target")</action>
            <postcondition>...</postcondition>
            <postcondition>...</postcondition>
        </apack>
        <apack>
            <precondition>...</precondition>
            <precondition>...</precondition>
            <action>robot.pick_and_place("pick_target", "place_target")</action>
            <postcondition>...</postcondition>
            <postcondition>...</postcondition>
        </apack>
        ...
    </sequence>
</plan>

Explanations of the plan XML format:
 - Each <apack> block in the plan consists of two <precondition> elements, one <action> elements, two <postcondition> elements.
 - One <precondition> element should include the condition that the block to be picked up (pick_target) must be empty on top.  
          For example, "The red block is empty on top."
 - The other <precondition> element should include the condition that the target location to be placed on the picking block (pick_target) must be empty on top.  For example, "The yellow bowl is empty on top."
 - The <action> element should contain a pick_and_place action like `robot.pick_and_place("pick_target", "place_target")`,
     which picks one of pick_targets and then places on one of place_targets.
 - One <postcondition> elements should include the condition that the pick_target is placed on the top of the place_target.  
          For example, "The red block is placed on top of the yellow bowl."
 - The other <postcondition> elements should include the condition that the place_target is no longer empty on top.  
          For example, "The yellow bowl is not empty on top."

- Do not use symbols such as arrows (→) or shorthand notations. All relationships must be described in complete natural language sentences.

- Ensure that the final stack follows the target instruction precisely, and that all blocks are used according to domain rules.

The following information is provided to support your planning task:
    - Example plan: {example}

Now plan the current task.
In the current environment, the objects are:
{found_objects}
The initial state:
{initial_state}
User instruction:
{instruction}

Don't add any explanation—just output the converted plan.
Please respond like the examples. Do NOT use markdown or code blocks (e.g. no ```python).
Just return the response like examples.
"""

DOMAIN_PROMPT4 = """
We will be working on a task where a robotic arm moves objects in an environment.
Your role is the task planner that should generate a sequence of robotic manipluation actions to achieve the user instruction from the given initial state.
The robot is assumed to be able to do only the pick_and_place action, which picks up a block and then places it on another block, a bowl, or one of the on-table locations.

Valid pick_targets: blocks  
Valid place_targets: blocks, bowls, and on-table locations in the environment  
Valid on-table locations:  
          top left corner, top side, top right corner,  
          left side, right side, bottom left corner, bottom side, bottom right corner

A plan must be expressed in the following XML format:
<plan>
    <sequence>
        <apack>
            <precondition>...</precondition>
            <precondition>...</precondition>
            <action>robot.pick_and_place("pick_target", "place_target")</action>
            <postcondition>...</postcondition>
            <postcondition>...</postcondition>
        </apack>
        <apack>
            <precondition>...</precondition>
            <precondition>...</precondition>
            <action>robot.pick_and_place("pick_target", "place_target")</action>
            <postcondition>...</postcondition>
            <postcondition>...</postcondition>
        </apack>
        ...
    </sequence>
</plan>

Explanations of the plan XML format:
 - Each <apack> block in the plan consists of two <precondition> elements, one <action> elements, two <postcondition> elements.
 - One <precondition> element should include the condition that the block to be picked up (pick_target) must be empty on top.  
          For example, "The red block is empty on top."
 - The other <precondition> element should include the condition that the target location to be placed on the picking block (pick_target) must be empty on top.  For example, "The yellow bowl is empty on top."
 - The <action> element should contain a pick_and_place action like `robot.pick_and_place("pick_target", "place_target")`,
     which picks one of pick_targets and then places on one of place_targets.
 - One <postcondition> elements should include the condition that the pick_target is placed on the top of the place_target.  
          For example, "The red block is placed on top of the yellow bowl."
 - The other <postcondition> elements should include the condition that the place_target is no longer empty on top.  
          For example, "The yellow bowl is not empty on top."

- Do not use symbols such as arrows (→) or shorthand notations. All relationships must be described in complete natural language sentences.

- Ensure that the final stack follows the target instruction precisely, and that all blocks are used according to domain rules.

The following information is provided to support your planning task:
    - Domain rules: {domain_rules}

Now plan the current task.
In the current environment, the objects are:
{found_objects}
The initial state:
{initial_state}
User instruction:
{instruction}

Don't add any explanation—just output the converted plan.
Please respond like the examples. Do NOT use markdown or code blocks (e.g. no ```python).
Just return the response like examples.
"""

DOMAIN_PROMPT5 = """
We will be working on a task where a robotic arm moves objects in an environment.
Your role is the task planner that should generate a sequence of robotic manipluation actions to achieve the user instruction from the given initial state.
The robot is assumed to be able to do only the pick_and_place action, which picks up a block and then places it on another block, a bowl, or one of the on-table locations.

Valid pick_targets: blocks  
Valid place_targets: blocks, bowls, and on-table locations in the environment  
Valid on-table locations:  
          top left corner, top side, top right corner,  
          left side, right side, bottom left corner, bottom side, bottom right corner

A plan must be expressed in the following XML format:
<plan>
    <sequence>
        <apack>
            <precondition>...</precondition>
            <precondition>...</precondition>
            <action>robot.pick_and_place("pick_target", "place_target")</action>
            <postcondition>...</postcondition>
            <postcondition>...</postcondition>
        </apack>
        <apack>
            <precondition>...</precondition>
            <precondition>...</precondition>
            <action>robot.pick_and_place("pick_target", "place_target")</action>
            <postcondition>...</postcondition>
            <postcondition>...</postcondition>
        </apack>
        ...
    </sequence>
</plan>

Explanations of the plan XML format:
 - Each <apack> block in the plan consists of two <precondition> elements, one <action> elements, two <postcondition> elements.
 - One <precondition> element should include the condition that the block to be picked up (pick_target) must be empty on top.  
          For example, "The red block is empty on top."
 - The other <precondition> element should include the condition that the target location to be placed on the picking block (pick_target) must be empty on top.  For example, "The yellow bowl is empty on top."
 - The <action> element should contain a pick_and_place action like `robot.pick_and_place("pick_target", "place_target")`,
     which picks one of pick_targets and then places on one of place_targets.
 - One <postcondition> elements should include the condition that the pick_target is placed on the top of the place_target.  
          For example, "The red block is placed on top of the yellow bowl."
 - The other <postcondition> elements should include the condition that the place_target is no longer empty on top.  
          For example, "The yellow bowl is not empty on top."

- Do not use symbols such as arrows (→) or shorthand notations. All relationships must be described in complete natural language sentences.

- Ensure that the final stack follows the target instruction precisely, and that all blocks are used according to domain rules.

The following information is provided to support your planning task:
    - Example plan: {example}
    - Domain rules: {domain_rules}

Now plan the current task.
In the current environment, the objects are:
{found_objects}
The initial state:
{initial_state}
User instruction:
{instruction}

Don't add any explanation—just output the converted plan.
Please respond like the examples. Do NOT use markdown or code blocks (e.g. no ```python).
Just return the response like examples.
"""