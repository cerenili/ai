from simpleai.search.local import  hill_climbing,hill_climbing_random_restarts
import numpy as np
from simpleai.search.viewers import BaseViewer
from simpleai.search import SearchProblem
from simpleai.search.viewers import BaseViewer


count = 15
capacity = 50
items_w = [24, 10, 10, 7, 2, 8, 6, 5, 9, 12, 20, 18, 13, 5, 4]
items_val = [50, 10, 25, 30, 20, 25, 40, 15, 12, 22, 35, 45, 55, 100, 60]

def totValue(state):
    total_value = 0
    for i in range(count):
        if state[i] != 0:
            total_value += items_val[i]
    return total_value 

def totWeigth(state):
    total_Weigth = 0
    for i in range(count):
        if state[i] != 0:
            total_Weigth += items_w[i]
    return total_Weigth

def checkCap(state):
    return capacity < totWeigth(state)

class knapsackProblem(SearchProblem):
    def actions(self,state):
        actions = []
        for i in range(count): 
            temp = state.copy()
            if temp[i] == 1:
                temp[i] = 0
            else:
                temp[i] = 1
            if not checkCap(temp):  
                actions.append(i)
        return actions
    def result(self, state, action):
        temp = state.copy()
        if temp[action] == 1:
            temp[action] = 0
        else:
            temp[action] = 1
        if not checkCap(temp):  
            return temp
        return state
        
    def generate_random_state(self):
        random = np.random.randint(2, size=count).tolist()
        while checkCap(random):
            random = np.random.randint(2, size=count).tolist()    
        return random  

    def value(self, state):
        return totValue(state)



my_viewer = BaseViewer()


problem = knapsackProblem(np.random.randint(2, size=count).tolist())
results = hill_climbing(problem, 100, viewer=my_viewer)
results = hill_climbing_random_restarts(problem, 5,100, viewer=my_viewer)


print(my_viewer.stats)
print("Results")
print(results.state)
print("val")
print(totValue(results.state))
print("weigth")
print(totWeigth(results.state))
