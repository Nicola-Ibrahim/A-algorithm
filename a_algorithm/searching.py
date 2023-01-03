
from copy import deepcopy
import numpy as np
import time
 
def best_solution(state):
    best_solution = np.array([], int).reshape(-1, 9)
    count = len(state) - 1
    while count != -1:
        best_solution = np.insert(best_solution, 0, state[count]['start'], 0)
        count = (state[count]['parent'])
    return best_solution.reshape(-1, 3, 3)
 
        
# checks for the uniqueness of the iteration(it).
def all(arr):
    set=[]
    for it in set:
        for arr in it:
            return 1
        else:
            return 0
 
 
# number of misplaced tiles 
def misplaced_tiles(start,target):
    mscost = np.sum(start != target) - 1
    return mscost if mscost > 0 else 0
 
 
def coordinates(start):
    pos = np.array(range(9))
    for p, q in enumerate(start):
        pos[q] = p
    return pos
 
 
# start of 8 start evaluvation, using Misplaced tiles heuristics
def eval_misplaced(start, target):
    steps = np.array([('up', [0, 1, 2], -3),('down', [6, 7, 8],  3),('left', [0, 3, 6], -1),('right', [2, 5, 8],  1)],
                dtype =  [('move',  str, 1),('position', list),('head', int)])
 
    dtstate = [('start',  list),('parent', int),('gn',  int),('hn',  int)]
 
    costg = coordinates(target)
    # initializing the parent, gn and hn, where hn is misplaced_tiles  function call  
    parent = -1
    gn = 0
    hn = misplaced_tiles(coordinates(start), costg)
    state = np.array([(start, parent, gn, hn)], dtstate)
 
   #priority queues with position as keys and fn as value.
    dtpriority = [('position', int),('fn', int)]
 
    priority = np.array([(0, hn)], dtpriority)
     
    while 1:
        priority = np.sort(priority, kind='mergesort', order=['fn', 'position'])      
        position, fn = priority[0]       
        # sort priority queue using merge sort,the first element is picked for exploring.                                          
        priority = np.delete(priority, 0, 0)                         
        start, parent, gn, hn = state[position]
        start = np.array(start)
          
        blank = int(np.where(start == 0)[0])   
       
        gn = gn + 1                            
        c = 1
        start_time = time.time()
        for s in steps:
            c = c + 1
            if blank not in s['position']:
                openstates = deepcopy(start)         
                openstates[blank], openstates[blank + s['head']] = openstates[blank + s['head']], openstates[blank]
                
                if ~(np.all(list(state['start']) == openstates, 1)).any():          
                    end_time = time.time()
                    if (( end_time - start_time ) > 2):
                        print(" The 8 start is unsolvable \n")
                        break
                     
                    hn = misplaced_tiles(coordinates(openstates), costg) 
                    # generate and add new state in the list                    
                    q = np.array([(openstates, position, gn, hn)], dtstate)         
                    state = np.append(state, q, 0)
                    # f(n) is the sum of cost to reach node
                    fn = gn + hn                                        
                     
                    q = np.array([(len(state) - 1, fn)], dtpriority)
                    priority = np.append(priority, q, 0)
                     
                    if np.array_equal(openstates, target):                      
                        print(' The 8 start is solvable \n')
                        return state, len(priority)
                         
    return state, len(priority)
 
 
def a_start(start, target):
    state, visited = eval_misplaced(start, target) 
    best_path = best_solution(state)
    return best_path
