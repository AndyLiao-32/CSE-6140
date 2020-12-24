import time
import networkx as nx
import os

def maxDeg(graph):
	lst = graph.degree(graph.nodes())
	n = ()
	maxDeg = 0
	for i, j in lst:
		if j > maxDeg:
			maxDeg = j
			n = (i, j)
	return n

def output_file(file_name, T, number_VC, VC, trace):
	os.chdir('../')
	outputPath = './output'
	file_name = file_name.split('/')[-1].split('.')[0]
	saveAs = os.path.join(outputPath, file_name + "_" + "BnB" + "_" + str(T) + ".sol")
	file_1 = open(saveAs, "w+")
	file_1.write(str(number_VC) + "\n")
	file_1.write(str(VC) + "\n")
	file_1.close()

	saveAs = os.path.join(outputPath, file_name + "_" + "BnB" + "_" + str(T) + ".trace")
	file_2 = open(saveAs, "w+")
	
	for i in trace:
		file_2.write(str(i[0]) + ", " + str(i[1]) + "\n")
	
	file_2.close()

def vcsz(vc):
	sz = 0
	for element in vc:
		sz += element[1]
	return sz


def lb(g):
	_lb = g.number_of_edges() / maxDeg(g)[1]
	if _lb > int(_lb):
		return int(_lb) + 1
	else:
		return int(_lb)



# read graph
def bnb(inst, cutoff, seed):
	graph = nx.Graph()
	adj_list = []
	v = 0
	e = 0
	with open(inst, 'r') as readGraph:
		i = 0
		for line in readGraph.readlines():
			if i == 0:
				tmp = line.split()
				v, e = int(tmp[0]), int(tmp[1])
				i += 1
			
			else:
				adj_list.append(str(i) + ' ' + line)
				i += 1

	graph = nx.parse_adjlist(adj_list, nodetype=int)


	graphDup = graph.copy()
	vDup = maxDeg(graphDup)
	f = []
	f.append((vDup[0], 0, (-1, -1)))
	f.append((vDup[0], 1, (-1, -1)))

	
	best = []
	current = []
	sol = []
	ub = graph.number_of_nodes()

	s = time.time()
	end = s
	t = end - s

	while f != [] and t < cutoff:
		(vx, state, parent) = f.pop()
		bt = False
		if state == 0:
			for i in list(graphDup.neighbors(vx)):
				current.append((i, 1))
				graphDup.remove_node(i)
		elif state == 1:
			graphDup.remove_node(vx)
		else:
			pass
		
		current.append((vx, state))
		currentSz = vcsz(current)
		
		if graphDup.number_of_edges() == 0:
			if currentSz < ub:
				best = current.copy()
				
				ub = currentSz
				sol.append([time.time() - s, currentSz])
			bt = True
		else:
			currlb= currentSz + lb(graphDup)
			if currlb < ub:
				vy = maxDeg(graphDup)
				f.append((vy[0], 0, (vx, state)))
				f.append((vy[0], 1, (vx, state)))
			else:
				bt = True
		
		if bt:
			if f:
				#nnp = f[-1][2]
				if f[-1][2] in current:
					i = current.index(f[-1][2]) + 1
					while i < len(current):
						currN, currState = current.pop()
						graphDup.add_node(currN)
						
						currvcn = list(map(lambda t: t[0], current))
						for n in graph.neighbors(currN):
							if n in graphDup.nodes() and n not in currvcn:
								graphDup.add_edge(n, currN)
				elif f[-1][2] == (-1, -1):
					current.clear()
					graphDup = graph.copy()
		
		end = time.time()
		t = end - s

		
	for v in best:
		if v[1] == 0:
			best.remove(v)
		
	vc = []
	for v, d in best:
		vc.append(v)
		
	output_file(inst, cutoff, len(vc), vc, sol)





