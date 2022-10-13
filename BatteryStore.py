import random


class BatteryStore:

  def __init__(self, num):
    self.batteries = [random.choice(['N', 'P']) for i in range(num)]
    self.obscured_batteries = ['-' for i in range(num)]
    self.initial_peek = ['?','-','?','-','-','-']
    self.last_was = ''
    self.peek_list = []
    self.num_peeks = 2

  def print(self):

  	print("\n***************************")
  	print(f"Batteries:          {self.batteries}")
  	print(f"Obscured Batteries: {self.obscured_batteries}")
  	print(f"Initial Peek:       {self.initial_peek}")
  	print(f"last_was:           {self.last_was}")
  	print(f"Peek List:          {self.peek_list}")
  	print("***************************\n")

  def spin(self):
    battery = self.batteries

    self.last_was = 'SPIN'
    battery_set = True
    for i in range(0,len(battery)-1):
        if battery[i] == battery[i+1]:
            continue
        else:
            battery_set = False
            break

    if(not battery_set):
        offset = -1 * random.randint(1,len(self.batteries))
        self.batteries = self.batteries[offset:] + self.batteries[:offset]
    else:
        return(battery_set)

  def peek(self, pattern):

    pattern_peeks = 0
    self.peek_list = []
    for i in range(0,len(pattern)):
        if pattern[i] == '?':
            pattern_peeks += 1
            self.peek_list.append(i)

    if self.last_was == 'SPIN' and pattern_peeks == self.num_peeks:
        self.last_was = 'PEEK'
        peeked_battery = self.obscured_batteries
        for i in self.peek_list:
            peeked_battery[i] = self.batteries[i]

        return peeked_battery
    
    elif self.last_was != 'SPIN':
        raise Exception("Peek can only be called immediately following Spin")
    else:
        raise Exception("Number of peeks ({}) is greater than allowed peeks ({})".format(len(self.peek_list),self.num_peeks))

  def change(self, pattern):

    for i in range(0,len(pattern)):
        if pattern[i] != '-' and self.initial_peek[i] == '-':
            raise Exception("Cannot change orientation of batteries which were not peeked")
    if self.last_was == 'PEEK':
        for i in self.peek_list:
            self.batteries[i] = pattern[i]
    else:
        raise Exception("Change can only be called immediately following Peek")

