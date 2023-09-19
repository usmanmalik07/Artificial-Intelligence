
class node:     
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
        initialState='A'     
        goalState='D'      
        graph= {'A': node('A',None,['B','C','E'],None),                 
                'B': node('B', None, ['A', 'D', 'E'], None),                 
                'C': node('C', None, ['A', 'F', 'G'], None),                 
                'D': node('D', None, ['B','E'], None),                 
                'E': node('E', None, ['A', 'B', 'D'], None),                 
                'F': node('F', None, ['C'], None),                 
                'G': node('G', None, ['C'], None)}      
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