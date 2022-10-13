import random
last_was = ''
battery = ['N','P','N','P','N','P']
obscured_battery = ['-','-','-','-','-','-']
num_peeks = 2
peek_list = []

def spin():
    global battery 
    global last_was

    last_was = 'SPIN'
    battery_set = True
    for i in range(0,len(battery)-1):
        if battery[i] == battery[i+1]:
            continue
        else:
            battery_set = False
            break

    if(not battery_set):
        offset = -1 * random.randint(1,len(battery))
        battery = battery[offset:] + battery[:offset]
    else:
        return(battery_set)

def peek(pattern):
    global obscured_battery
    global num_peeks
    global last_was 
    global peek_list 

    pattern_peeks = 0
    peek_list = []
    for i in range(0,len(pattern)):
        if pattern[i] == '?':
            pattern_peeks += 1
            peek_list.append(i)

    if last_was == 'SPIN' and pattern_peeks == num_peeks:
        last_was = 'PEEK'
        peeked_battery = obscured_battery
        for i in peek_list:
            peeked_battery[i] = battery[i]

        return peeked_battery

def change(pattern):
    global battery
    global last_was
    global peek_list

    if last_was == 'PEEK':
        for i in peek_list:
            battery[i] = pattern[i]


p_counter = 0
n_counter = 0
counter = 0
while(True):
    counter += 1
    if(spin()):
        break
    peeked_pattern = peek(['?','-','?','-','-','-'])

    if peeked_pattern[0] == 'P':
        p_counter += 1
        if p_counter <= n_counter:
            p_counter -= 1
            n_counter += 1
            peeked_pattern[0] = 'N'
    else:
        n_counter += 1
        if p_counter >= n_counter:
            n_counter -= 1
            p_counter += 1
            peeked_pattern[0] = 'P'
    
    if peeked_pattern[2] == 'P':
        p_counter += 1
        if p_counter <= n_counter:
            p_counter -= 1
            n_counter += 1
            peeked_pattern[2] = 'N'
    else:
        n_counter += 1
        if p_counter >= n_counter:
            n_counter -= 1
            p_counter += 1
            peeked_pattern[2] = 'P'
        
    change(peeked_pattern)

print(counter)