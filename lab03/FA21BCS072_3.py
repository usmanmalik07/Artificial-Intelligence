
class Node:     
        #state=state  
    def __init__(self,state,parent,actions,totalCost):          
        self.state=state          
        self.parent=parent          
        self.action=actions          
        self.totalCost=totalCost  
def actionSequence(graph,initialState,goalState):    
        solution=[goalState]     
        currentParent=graph[goalState].parent     
        while currentParent!=None:         
            solution.append(currentParent)         
            currentParent=graph[currentParent].parent     
        solution.reverse()     
        return solution   
def BFS():     
        initialState=1     
        goalState=25      
        graph = {1: Node(1, None, [2], None),
                2: Node(2, None, [1, 3], None),
                3: Node(3, None, [2, 4], None),
                4: Node(4, None, [3, 5, 26], None),
                5: Node(5, None, [4, 6], None),
                6: Node(6, None, [5, 7, 9], None),
                7: Node(7, None, [6, 8], None),
                8: Node(8, None, [7, 9, 10], None),
                9: Node(9, None, [6, 8], None),
                10: Node(10, None, [8, 11], None),
                11: Node(11, None, [10, 12, 13], None),
                12: Node(12, None, [11], None),
                13: Node(13, None, [11, 14], None),
                14: Node(14, None, [13, 15], None),
                15: Node(15, None, [14, 16, 17], None),
                16: Node(16, None, [15], None),
                17: Node(17, None, [15, 18], None),
                18: Node(18, None, [17, 19], None),
                19: Node(19, None, [18, 20], None),
                20: Node(20, None, [19, 21], None),
                21: Node(21, None, [20, 22], None),
                22: Node(22, None, [21, 23], None),
                23: Node(23, None, [22, 24], None),
                24: Node(24, None, [23, 25], None),
                25: Node(25, None, [24, 26], None),
                26: Node(26, None, [4, 25], None)
            }      
        frontier=[initialState]     
        explored=[]     
        while len (frontier)!=0:         
            currentNode=frontier.pop(0)         
            explored.append(currentNode)         
            for child in graph[currentNode].action:             
                if child not in frontier and child not in explored: 
                    graph[child].parent=currentNode                 
                    if graph[child].state==goalState:                     
                        return actionSequence(graph,initialState,goalState)                 
                    frontier.append(child) 
solution=BFS() 
print(solution)