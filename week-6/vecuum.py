
def reflex_vacuum_agent(loc,dust):
    if status =='dirty':
        action = 'suck'
    elif status =='A':
        action = 'move right'
    elif status =='B':
        action = 'move left'
    return action;
location = input("Enter the location")




while True:
    print("which location? [Enter 'A' or 'B']")
    
    loc = input()
    
    print("is dirty [ Enter 'dirty' or 'clear']")
    dust = input()
    
    selected_action = reflex_vacuum_agent(loc,dust)
    
    if selected_action != NOne:
        msg ="The selected action for the current state is '%s'."




