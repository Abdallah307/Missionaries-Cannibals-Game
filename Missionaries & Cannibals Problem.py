import time
state = [3, 3, 0, 0, 0]

state = {
    "m1": 3,
    "c1": 3,
    "m2": 0,
    "c2": 0,
    "bs": 0
}

while True:
    if state['m1'] == 0 and state['c1'] == 0 and state['m2'] == 3 and state['c2'] == 3:
        print("Congrats you Won The Game!!")
        break
    if state['bs'] == 0:
        if state['m1'] > 0 and (state['m1'] - 1 >= state['c1'] or state['m1']-1 == 0) and state['m2'] + 1 >= state['c2']:
            state['m1'] -= 1
            state['m2'] += 1
        elif state['m1'] >= 2 and (state['m1'] - 2 >= state['c1'] or state['m1'] - 2 == 0) and state['m2'] + 2 >= state['c2']:
            state['m1'] -= 2
            state['m2'] += 2
        elif state['c1'] > 0 and (state['c2'] + 1 <= state['m2'] or state['m2'] == 0):
            state['c1'] -= 1
            state['c2'] += 1
        elif state['c1'] >= 2 and (state['c2'] + 2 <= state['m2'] or state['m2'] == 0):
            state['c1'] -= 2
            state['c2'] += 2
        elif state['m1'] >= 1 and state['c1'] >= 1 and state['c2'] == state['m2']:
            state['c1'] -= 1
            state['c2'] += 1
            state['m1'] -= 1
            state['m2'] += 1 

                       
    elif state['bs'] == 1:
        if state['m2'] > 0 and (state['m2'] - 1 >= state['c2'] or state['m2']-1 == 0) and state['m1'] + 1 >= state['c1']:
            state['m2'] -= 1
            state['m1'] += 1
        elif state['m2'] >= 2 and (state['m2'] - 2 >= state['c2'] or state['m2'] - 2 == 0) and state['m1'] + 2 >= state['c1']:
            state['m2'] -= 2
            state['m1'] += 2
        elif state['c2'] > 0 and (state['c1'] + 1 <= state['m1'] or state['m1'] == 0):
            state['c2'] -= 1
            state['c1'] += 1
        elif state['c2'] >= 2 and (state['c1'] + 2 <= state['m1'] or state['m1'] == 0):
            state['c2'] -= 2
            state['c1'] += 2
        elif state['m2'] >= 1 and state['c2'] >= 1 and state['c1'] == state['m1']:
            state['c2'] -= 1
            state['c1'] += 1
            state['m2'] -= 1
            state['m1'] += 1

            

    print(f"Current State now : {state}")
    time.sleep(1)