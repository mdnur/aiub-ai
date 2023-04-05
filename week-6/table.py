# storing the information in a dictionary
table = {('A', 'clean'): 'move right',
         ('A', 'dirty'): 'suck',
         ('B', 'clean'): 'move left',
         ('B', 'dirty'): 'suck'}
percepts = []

# agent function


def table_driven_agent(percept):
    percepts.append(percept)
    action = lookup(percepts, table)

    return action

# function to look-up into the table


def lookup(percepts, table):
    recent_percept = percepts[-1]

    for key, val in table.items():
        if key == recent_percept:
            return val

    return None


# testing the implemented agent
while True:
    print("Which location? [Enter 'A' or 'B']")     # 'A' or 'B'
    loc = input()

    print("Is dirty? [Enter 'dirty' or 'clean']")   # 'dirty' or 'clean'
    dust = input()

    current_percept = (loc, dust)
    selected_action = table_driven_agent(current_percept)

    if selected_action != None:
        msg = "The selected action for the current state is '%s'." % selected_action
        print(msg)
    else:
        print("Action not found for the current perception.")

    print("\nWant to check action again? [Enter 'N' for No.]")

    isExit = input()
    if isExit == 'N':
        break
