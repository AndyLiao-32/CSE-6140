import networkx as nx
import sys,os,getopt
import time
import itertools
from operator import itemgetter
import scipy.optimize as opt
import random
import argparse
from math import floor

def read_graph(filename):
    # The adjacency list stores the adjacent nodes for each node
    adj_list = []

    # The header stores the first line of the input graph, 
    #   mentioning the size and the weight of the graph
    header = []

    with open(filename, 'r') as file:
        line_index = 0

        for line in file.readlines():
            items = line.strip().split()

            if line_index == 0:
                header.append([int(items[0]), int(items[1]), int(items[2])])
                line_index += 1

            else:
                item_list = []

                for item in items:
                    item_list.append(int(item))

                adj_list.append(item_list)

    # Create the graph G and add edges from the adjacency list to G
    G = nx.Graph()

    # For each node in the adjacency list, add the connected edges (u,v) to each node
    for i in range(len(adj_list)):
        # Our node starts from 1 instead of 0
        u = i + 1

        # add the edge by the adjacency list
        for j in range(len(adj_list[i])):
            v = adj_list[i][j]
            G.add_edge(u, v)

    return G, header

def ls1(G, cutoff, rand_seed):
    random.seed(rand_seed)

    start_time = time.time()
    curr_time = 0
    curr_MVC = []
    best_MVC = []
    trace = []
    iteration = 0

    # initialize the two array filling with all nodes
    for node in G.nodes():
        curr_MVC.append(node)
        best_MVC.append(node)

    # set the cutoff
    while curr_time < cutoff:
        if iteration != 0:
            p = random.randint(1, 4)

            # the probably which allows random steps decrease due to the time
            if curr_time < cutoff/2:
                if (p == 2) or (p == 3):
                    discard_node = []
                    for node in G.nodes():
                        if node not in curr_MVC:
                            discard_node.append(node)
                        
                    # randomize the reassign length
                    reassign_length = int(floor(len(discard_node)/4 + 1))

                    # randomly choose the discard node and reassign into curr_MVC set
                    for i in range(reassign_length):
                        reassign_node = random.choice(discard_node)

                        if reassign_node not in curr_MVC:
                            curr_MVC.append(reassign_node)
            else:
                if p == 2:
                    discard_node = []
                    for node in G.nodes():
                        if node not in curr_MVC:
                            discard_node.append(node)
                        
                    # randomize the reassign length
                    reassign_length = int(floor(len(discard_node)/4 + 1))

                    # randomly choose the discard node and reassign into curr_MVC set
                    for i in range(reassign_length):
                        reassign_node = random.choice(discard_node)

                        if reassign_node not in curr_MVC:
                            curr_MVC.append(reassign_node)

        edge_list = G.edges()
        # print(edge_list)
        edges = []

        for edge in edge_list:
            edges.append(edge)

        random.shuffle(edges)

        # compute and update the MVC
        for edge in edges:
            if (edge[0] in curr_MVC) and (edge[1] in curr_MVC):
                if G.degree(edge[0]) > G.degree(edge[1]):
                    if set(G.neighbors(edge[1])).issubset(set(curr_MVC)):
                        curr_MVC.remove(edge[1])

                else:
                    if set(G.neighbors(edge[0])).issubset(set(curr_MVC)):
                        curr_MVC.remove(edge[0])

        # upddate the best_MVC when we find a smaller number of vertices
        if len(curr_MVC) < len(best_MVC):
            best_MVC = []
            for node in curr_MVC:
                best_MVC.append(node)

            # record the trace
            trace.append([len(curr_MVC), time.time() - start_time])

        # update the time
        curr_time = time.time() - start_time

        iteration += 1

    return best_MVC, trace

# def main(inputFile, algo, cutoff=600, rand_seed=None):
def ls1_main(inst, cutoff, rand_seed):
    # inputFile = sys.argv[1]
    algo = "LS1"
    # cutoff = 600
    # rand_seed = 10
    inputFile = inst


    # get the file direction
    os.chdir('../')
    direction = os.getcwd()
    direction = direction + '/output'
    inputFilename = os.path.basename(inputFile)
    
    
    # Read in the input file
    G, header = read_graph(inputFile)
    
    # Store the start time
    start_time = time.time()

    if algo == "LS1": #edge by edge

        # Run the algorithm
        MVC, trace = ls1(G, cutoff, rand_seed)

        # calculate the total time
        total_time = time.time() - start_time
        # check timing and vertices, reference from stackoverflow
        #print ("runtime: {}, number of vertices: {}".format(total_time, len(MVC))) 
        # sort the MVC
        MVC.sort()
        
        # Name the solution file
        inputFilename = inputFilename.split('.')[0]
        sol_file = inputFilename +'_'+algo+'_'+str(cutoff)+'_'
        sol_file += str(rand_seed)+'.sol'

        # Name the solution trace file
        trace_file = inputFilename +'_'+algo+'_'+str(cutoff)+'_'
        trace_file += str(rand_seed)+'.trace'

    # write output files, add in comma, reference from geeksforgeeks
    MVC_list = ','.join(map(str, MVC))

    # solution file
    sol_output = open(direction + os.path.sep + sol_file, 'w')
    sol_output.write(str(len(MVC))+'\n'+ MVC_list)
    sol_output.close()

    # trace file
    trace_output = open(direction + os.path.sep + trace_file, 'w')
    for sol in trace:
        sol.reverse()
        sol_list = ','.join(map(str,sol))
        trace_output.write(sol_list+'\n')
    trace_output.close()

# parser = argparse.ArgumentParser(description='Run a Local Search Algorithm for Min Vertex Cover Problem')
# parser.add_argument("-inst", help='Which file to run', default='./DATA/dummy1.graph') 
# parser.add_argument("-alg", help='Choose which method to run (BnB, Approx, LS1, LS2)', default="LS1", choices=["BnB", "Approx", "LS1", "LS2"])
# parser.add_argument("-time", help='When to stop the run in seconds', type=int, default=600)
# parser.add_argument("-seed", help='Random Seed for Local Search', type=int, default=32)
# args = parser.parse_args()

# if __name__ == '__main__':
#     # inputFile = args.inst
#     # algo = args.alg
#     # cutoff = args.time
#     # rand_seed = args.seed
#     main()
