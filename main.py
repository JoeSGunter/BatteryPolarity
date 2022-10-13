import BatteryStore

store = BatteryStore.BatteryStore(6)

print("--Initial Batteries--")
store.print()

print("--Operations--")

initial_peek = store.initial_peek
p_counter = 0
n_counter = 0
counter = 0
while(True):
    counter += 1
    if(store.spin()):
        break
    peeked_pattern = store.peek(initial_peek)

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
        
    store.change(peeked_pattern)

print("\n--Battery Store after Operations--")
store.print()