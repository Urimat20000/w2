from bts import Tree
from red_black_tree import RedBlackTree
from hash_table import HashTable
from collections import defaultdict

import time
import matplotlib.pyplot as plt
import sys
import random as rs

marr = []
for i in range(8):
    f = open('readydata8' + str(i + 1) + '.txt', "r", encoding="utf-8")
    arr = []
    for j in f.readlines():
        tikit = j.split()
        if(len(tikit) == 6 and tikit[4].isnumeric()):
            arr.append(j.split())
    marr.append(arr)
    f.close()

class ticket:
    def __init__(self, owner_name:list, cabin_number:int, cabin_type:int, dest_point:str):
        self.owner_name = owner_name
        self.cabin_number = cabin_number
        self.cabin_type = cabin_type
        self.dest_point = dest_point


    def __gt__(self, other): # >
        if self.cabin_number > other.cabin_number:            
            return True
        else:
            return False
        
    def __ge__(self, other): # >=
        if self.cabin_number >= other.cabin_number:
            return True
        else:
            return False

    def __lt__(self, other): # <
        if self.cabin_number < other.cabin_number:
            return True
        else:
            return False

    def __le__(self, other): # <=
        if self.cabin_number <= other.cabin_number:
            return True
        else:
            return False

ticketmarr = []
for j in range(len(marr)):
    ticketarr = []
    for i in range(len(marr[j])):
        ticketarr.append(ticket(marr[j][i][:3], int(marr[j][i][3]), int(marr[j][i][4]), marr[j][i][5]))
    ticketmarr.append(ticketarr)

tm = []
tmtmp = []

for i in range(8):
    bts = Tree()
    bts.creation(ticketmarr[i])
    
    start = time.time()
    for j in range(1000):
        key = ticketmarr[i][rs.randrange(0, len(ticketmarr[i]))].owner_name
        bts.find(key)
    tmtmp.append((time.time() - start) / 1000)
    
tm.append(tmtmp)
tmtmp = []

for i in range(8):
    reddead = RedBlackTree()
    reddead.build_from_list(ticketmarr[i])
    
    start = time.time()
    for j in range(1000):
        key = ticketmarr[i][rs.randrange(0, len(ticketmarr[i]))].owner_name
        reddead.find_element(reddead.root, key)
    tmtmp.append((time.time() - start) / 1000)
    
tm.append(tmtmp)
tmtmp = []

for i in range(8):
    table = HashTable(ticketmarr[i])
    
    start = time.time()
    for j in range(1000):
        key = ticketmarr[i][rs.randrange(0, len(ticketmarr[i]))].owner_name
        table.get(f"{key[0]} {key[1]} {key[2]}")
    tmtmp.append((time.time() - start) / 1000)
    
tm.append(tmtmp)
tmtmp = []

for i in range(8):
    md = defaultdict(list)
    for ticket in ticketmarr[i]:
        temp = f"{ticket.owner_name[0]} {ticket.owner_name[1]} {ticket.owner_name[2]}"
        md[temp].append(ticket)
        
    start = time.time()
    for j in range(1000):
        key = ticketmarr[i][rs.randrange(0, len(ticketmarr[i]))].owner_name
        key1 = f"{key[0]} {key[1]} {key[2]}"
        md[key1]
    tmtmp.append((time.time() - start) / 1000)
    
tm.append(tmtmp)
tmtmp = []

print(tm[0])
print(tm[1])
print(tm[2])
print(tm[3])

plt.plot([12500, 25000, 37500, 50000, 62500, 75000, 87500, 100000], tm[0], [12500, 25000, 37500, 50000, 62500, 75000, 87500, 100000], tm[1], [12500, 25000, 37500, 50000, 62500, 75000, 87500, 100000], tm[2], [12500, 25000, 37500, 50000, 62500, 75000, 87500, 100000], tm[3])
plt.legend(["Binary Search Tree", "Red Black Tree", "Hash table", "Multimap"])
plt.show()
