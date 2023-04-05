# storing the information in a dictionary
table = {('A', 'clean', 'B', 'clean'): 'No Operation',
          ('A', 'clean', 'B', 'dirty'): 'Move Right',
          ('A', 'dirty', 'B', 'clean'): 'Suck',
          ('A', 'dirty', 'B', 'dirty'): 'suck',
          ('B', 'clean', 'A', 'clean'): 'No Operation',
          ('B', 'clean', 'A', 'dirty'): 'Move Left',
          ('B', 'dirty', 'A', 'clean'): 'suck',
          ('B', 'dirty', 'A', 'dirty'): 'suck'}
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
    print("Which location is 1? [Enter 'A' or 'B']")     # 'A' or 'B'
    loc1 = input()

    print("Enter status! [Enter 'dirty' or 'clean']")   # 'dirty' or 'clean'
    stat1 = input()

    print("Which location is 2? [Enter 'A' or 'B']")     # 'A' or 'B'
    loc2 = input()

    print("Enter status! [Enter 'dirty' or 'clean']")   # 'dirty' or 'clean'
    stat2 = input()

    current_percept = (loc1, stat1, loc2, stat2)
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
