# storing the information in a dictionary
# table = {
#     (('A', 'clean'), ('B', 'clean')): 'No operation',
#     (('A', 'clean'), ('B', 'Dirty')): 'move right',
#     (('A', 'Dirty'), ('B', 'clean')): 'Suck',
#     (('A', 'Dirty'), ('B', 'Dirty')): 'Suck',
#     (('B', 'clean'), ('A', 'clean')): 'No operation',
#     (('B', 'clean'), ('A', 'Dirty')): 'move left',
#     (('B', 'Dirty'), ('A', 'clean')): 'Suck',
#     (('B', 'Dirty'), ('A', 'Dirty')): 'Suck'
# }

table = {
    ('A', 'clean', 'B', 'clean'): 'No operation',
    ('A', 'clean', 'B', 'Dirty'): 'move right',
    ('A', 'Dirty', 'B', 'clean'): 'Suck',
    ('A', 'Dirty', 'B', 'Dirty'): 'Suck',
    ('B', 'clean', 'A', 'clean'): 'No operation',
    ('B', 'clean', 'A', 'Dirty'): 'move left',
    ('B', 'Dirty', 'A', 'clean'): 'Suck',
    ('B', 'Dirty', 'A', 'Dirty'): 'Suck'
}
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
    print("Which location 1? [Enter 'A' or 'B']")     # 'A' or 'B'
    loc1 = input()
    # 'dirty' or 'clean'
    print("Is dirty for location 1? [Enter 'dirty' or 'clean']")
    dust1 = input()

    print("Which location 2? [Enter 'A' or 'B']")     # 'A' or 'B'
    loc2 = input()

    # 'dirty' or 'clean'
    print("Is dirty for location 2? [Enter 'dirty' or 'clean']")
    dust2 = input()

    # current_percept = (loc1, dust1,loc2,dust2)
    current_percept = (loc1, dust1, loc2, dust2)
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
