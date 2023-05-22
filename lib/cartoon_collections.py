def roll_call_dwarves(names):
    for i in range(len(names)):
        print(f'{i + 1}. {names[i]}')

def summon_captain_planet(calls):
    new_calls = [call.capitalize() + "!" for call in calls]
    return new_calls

def long_planeteer_calls(calls):
    for call in calls: 
        if len(call) > 4:
            return True
    return False

def find_the_cheese(strs):
    for str in strs: 
        if str in ['cheddar', 'gouda', 'camembert']:
            return str 
    return None
