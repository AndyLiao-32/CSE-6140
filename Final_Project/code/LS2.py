import time
import networkx as nx
import numpy as np
import random
import os



def mvcHills(graph, cutoff, randomSeed):
	global start_time, bestLS
	vc, t = adjacent(graph)
	vcCopy = vc
	start_time = time.time()
	graphCopy = graph.copy()

	preSort = []
	for i in range(0, len(vcCopy)):
		tmp = graphCopy.degree(vcCopy[i])
		preSort.append(tmp)
		
	postSort = []
	postSort.append(preSort)
	postSort.append(vcCopy)
	sorted(postSort, key=lambda x:x[0])
	sortVC = []
	for i in range(len(postSort)):
		sortVC.append(postSort[i][1])
	random.seed(randomSeed)


	currentBest = []
	trace = []
	nodeList = list(graphCopy.nodes())
	random.shuffle(nodeList)
	bestLS = vc
	for i in range(0, len(vc)):
		intervalVC = sortVC[i:len(vc)]
		for j in range(0, len(intervalVC)):
			v = intervalVC[j]
			nodeList = list(graphCopy.nodes())
			if not nodeList:
				bestLS = currentBest
				trace.append([len(bestLS), time.time() - start_time])
				break

			if v not in nodeList:
				v = nodeList[0]

			for k in range(i, len(nodeList)):
				if graphCopy.degree(nodeList[k + 1]) > graphCopy.degree(nodeList[k]):
					v1 = nodeList[k + 1]
					break
				elif k == 0:
					v1 = v
					break
				elif graphCopy.degree(nodeList[k - 1]) > graphCopy.degree(nodeList[k]):
					v1 = nodeList[k - 1]
					break
				elif graphCopy.degree(nodeList[k]) == graphCopy.degree(nodeList[k + 1]) and k == len(nodeList) - 1:
					v1 = nodeList[k]
					break
				else:
					v1 = nodeList[k]
			currentBest.append(v1)

			time_stop = time.time() - start_time
			if time_stop > cutoff:
				trace.append([len(bestLS), time.time() - start_time])
				break
			if j == len(intervalVC) - 1:
				if not graphCopy.nodes():
					bestLS = currentBest
					trace.append([len(bestLS), time.time() - start_time])

			if not graphCopy.nodes():
				bestLS = currentBest
				trace.append([len(bestLS), time.time() - start_time])
				break
	return bestLS, trace

def ls2(inst, cutoff, seed):
	v = 0
	e = 0
	unweighted = 0
	header = []
	adj_list = []
	graph = nx.Graph()

	read = open(inst, 'r')
	for line in read:
		line = line.strip().split()
		tmp = [int(x) for x in line]
		adj_list.append(tmp)
	read.close()
	for i in range(len(adj_list) - 1):
		if i == 0:
			header = adj_list[i]
		else:
			n = len(adj_list[i])
			for j in range(1, n):
				graph.add_edge(adj_list[i][0], adj_list[i][j])
	randomSeed = seed
	start = time.time()
	cover, trace = mvcHills(graph, cutoff, randomSeed)
	total_time = time.time() - start_time
	#print("runtime: {}, number of vertices: {}".format(total_time, len(cover)))
	#print(cover)
	cover.sort()
	output_file(inst, cutoff, len(cover), cover, total_time, seed)

def output_file(file_name, T, number_VC, VC, trace, seed):
	os.chdir('../')
	outputPath = './output'
	file_name = file_name.split('/')[-1].split('.')[0]
	saveAs = os.path.join(outputPath, file_name + "_" + "LS2" + "_" + str(T) + "_" + str(seed) + ".sol")
	file_1 = open(saveAs, "w+")
	file_1.write(str(number_VC) + "\n")
	file_1.write(str(VC) + "\n")
	file_1.close()

	saveAs = os.path.join(outputPath, file_name + "_" + "LS2" + "_" + str(T) + "_" + str(seed) + ".trace")
	file_2 = open(saveAs, "w+")

	#for i in trace:
	file_2.write(str(trace) + ", " + str(number_VC) + "\n")
	
	file_2.close()

def adjacent(graph):
	global start_time
	start_time = time.time()
	total_vertices = len(graph.nodes())
	vertex_cover = []
	edge = []
	for u, v in graph.edges():
		if u in vertex_cover or v in vertex_cover:
			continue
		else:
			vertex_cover.append(u)
			vertex_cover.append(v)
			edge.append([len(vertex_cover), time.time() - start_time])
	return vertex_cover, edge
