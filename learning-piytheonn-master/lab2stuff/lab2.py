# Fall 2012 6.034 Lab 2: Search
#
# Your answers for the true and false questions will be in the following form.  
# Your answers will look like one of the two below:
#ANSWER1 = True
#ANSWER1 = False

# 1: True or false - Hill Climbing search is guaranteed to find a solution
#    if there is a solution
ANSWER1 = False

# 2: True or false - Best-first search will give an optimal search result
#    (shortest path length).
#    (If you don't know what we mean by best-first search, refer to
#     http://courses.csail.mit.edu/6.034f/ai3/ch4.pdf (page 13 of the pdf).)
ANSWER2 = False

# 3: True or false - Best-first search and hill climbing make use of
#    heuristic values of nodes.
ANSWER3 = True

# 4: True or false - A* uses an extended-nodes set.
ANSWER4 = None

# 5: True or false - Breadth first search is guaranteed to return a path
#    with the shortest number of nodes.
ANSWER5 = None

# 6: True or false - The regular branch and bound uses heuristic values
#    to speed up the search for an optimal path.
ANSWER6 = None

# Import the Graph data structure from 'search.py'
# Refer to search.py for documentation
from search import Graph

## Optional Warm-up: BFS and DFS
# If you implement these, the offline tester will test them.
# If you don't, it won't.
# The online tester will not test them.
def bfs(graph, start, goal):
    stack=[]
    iiii=0
    if goal==start:
        return start

    ##print(graph.get_connected_nodes(start))
    for u in graph.get_connected_nodes(start):
        stack.append(graph.get_edge(start, u))
        ##print("46")
        ##print(stack)

    howbig=len(stack)
    for i in range(0,howbig):
        #print("51")
        ##print(stack)
        topstack=stack.pop(0)
        ##print("topstack",topstack)
        if topstack.node1 == start:
            endofnode = topstack.node2
        else:
            endofnode = topstack.node1
        if endofnode == goal:
            ##print(topstack)
            result = [start]
            if topstack.node1 not in result:
                result.append(topstack.node1)
            if topstack.node2 not in result:
                result.append(topstack.node2)
            return result


        for u in graph.get_connected_nodes(endofnode):
            if u != start:

                dummytopstack=(topstack,(graph.get_edge(endofnode, u)))
                stack.append(dummytopstack)

    ##print("stack 69",stack)
    while stack:
        ##print (stack)
        next=[]

        topstack=stack.pop(0)



        lastedge=topstack[len(topstack)-1]
        nexttolastedge=topstack[len(topstack)-2]
        if lastedge.node1==nexttolastedge.node1:
            common=lastedge.node1
            endofnode=lastedge.node2
        elif lastedge.node1==nexttolastedge.node2:
            common = lastedge.node1
            endofnode = lastedge.node2
        elif lastedge.node2==nexttolastedge.node1:
            common = lastedge.node2
            endofnode = lastedge.node1
        else:##not needed as we know if node1 doesnt match node 2 must.
            common = lastedge.node2
            endofnode = lastedge.node1
        if endofnode==goal:
            result = [start]
            dummy = list(topstack)
            for x in range(0, len(dummy)):
                if dummy[x].node1 not in result:
                    result.append(dummy[x].node1)
                if dummy[x].node2 not in result:
                    result.append(dummy[x].node2)
            ##result.append(goal)
            return result
        if common == goal:
            result=[]
            dummy=list(topstack)
            result.append(start)
            for x in range(0,len(dummy)):
                if dummy[x].node1 not in result:
                    result.append(dummy[x].node1)
                if dummy[x].node2 not in result:
                    result.append(dummy[x].node2)
            return result



        for u in graph.get_connected_nodes(endofnode):
            dummyvar=list(topstack)
            randomstuff=1
            for qq in range(0,len(dummyvar)):
                ##print("node1",dummyvar[qq].node1)
                ##print("node2",dummyvar[qq].node2)
                ##print("u",u)
                if u == dummyvar[qq].node1:
                    randomstuff=0
                    ##print("node1 fail")
                elif u == dummyvar[qq].node2:
                    randomstuff=0
                    ##print("node2 fail")
                else:
                    bird=1
            dummytopstack=list(topstack)
            ##print("topstack",topstack)
            dummytopstack.append(graph.get_edge(endofnode,u))
            if randomstuff ==1:
                stack.append(dummytopstack)

    return("error")


NEWGRAPH1 = Graph(edgesdict=[
        { 'NAME': 'e1',  'LENGTH':  6, 'NODE1': 'S', 'NODE2': 'A' },
        { 'NAME': 'e2',  'LENGTH':  4, 'NODE1': 'A', 'NODE2': 'B' },
        { 'NAME': 'e3',  'LENGTH':  7, 'NODE1': 'B', 'NODE2': 'F' },
        { 'NAME': 'e4',  'LENGTH':  6, 'NODE1': 'C', 'NODE2': 'D' },
        { 'NAME': 'e5',  'LENGTH':  3, 'NODE1': 'C', 'NODE2': 'A' },
        { 'NAME': 'e6',  'LENGTH':  7, 'NODE1': 'E', 'NODE2': 'D' },
        { 'NAME': 'e7',  'LENGTH':  6, 'NODE1': 'D', 'NODE2': 'H' },
        { 'NAME': 'e8',  'LENGTH':  2, 'NODE1': 'S', 'NODE2': 'C' },
        { 'NAME': 'e9',  'LENGTH':  2, 'NODE1': 'B', 'NODE2': 'D' },
        { 'NAME': 'e10', 'LENGTH': 25, 'NODE1': 'E', 'NODE2': 'G' },
        { 'NAME': 'e11', 'LENGTH':  5, 'NODE1': 'E', 'NODE2': 'C' } ])



print(bfs(NEWGRAPH1,'S','H'))




## Once you have completed the breadth-first search,
## this part should be very simple to complete.
def dfs(graph, start, goal):
    raise NotImplementedError


## Now we're going to add some heuristics into the search.
## Remember that hill-climbing is a modified version of depth-first search.
## Search direction should be towards lower heuristic values to the goal.
def hill_climbing(graph, start, goal):
    raise NotImplementedError

## Now we're going to implement beam search, a variation on BFS
## that caps the amount of memory used to store paths.  Remember,
## we maintain only k candidate paths of length n in our agenda at any time.
## The k top candidates are to be determined using the
## graph get_heuristic function, with lower values being better values.
def beam_search(graph, start, goal, beam_width):
    raise NotImplementedError

## Now we're going to try optimal search.  The previous searches haven't
## used edge distances in the calculation.

## This function takes in a graph and a list of node names, and returns
## the sum of edge lengths along the path -- the total distance in the path.
def path_length(graph, node_names):
    raise NotImplementedError


def branch_and_bound(graph, start, goal):
    raise NotImplementedError

def a_star(graph, start, goal):
    raise NotImplementedError


## It's useful to determine if a graph has a consistent and admissible
## heuristic.  You've seen graphs with heuristics that are
## admissible, but not consistent.  Have you seen any graphs that are
## consistent, but not admissible?

def is_admissible(graph, goal):
    raise NotImplementedError

def is_consistent(graph, goal):
    raise NotImplementedError

HOW_MANY_HOURS_THIS_PSET_TOOK = ''
WHAT_I_FOUND_INTERESTING = ''
WHAT_I_FOUND_BORING = ''