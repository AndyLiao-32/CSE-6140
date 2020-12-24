import time
import sys
import networkx as nx
from random import choice
import os

class Approx:
	def __init__(self, inst, cutoff):
		self.inst = inst
		self.cutoff = cutoff

	def read_file(self, file):
		graph_list = []
		with open(file, 'r') as graph:
			i = 0
			for line in graph.readlines():
				if i > 0:
					graph_list.append(str(i) + ' ' + line)
				i += 1
		Adjlist = nx.parse_adjlist(graph_list, nodetype=int)
		return Adjlist

	def node_max_degree(self, degrees):
		[node, degree] = max(degrees, key=lambda x:x[1])
		possible_best_node = [V for V in degrees  if V[1] == degree]
		[node1, degree1] = choice(possible_best_node)
		return node1

	# def approximate(self, Graph, Time):
	#     start = time.time()
	#     t = 0
	#     times = []
	#     number_VC = float('inf')
	#     while t < Time:
	#         degree_list = nx.degree(Graph)
	#         top = self.node_max_degree(degree_list)
	#         vertex_cover = []
	#         while degree_list[top] > 0:
	#             vertex_cover.append(top)
	#             node_list = []
	#             for node in nx.neighbors(Graph, top):
	#                 node_list.append(node)
		
	#             for node1 in node_list:
	#                 Graph.remove_edge(node1, top)
	#             Graph.remove_node(top)
	#             top = self.node_max_degree(nx.degree(Graph))
	#         t = time.time() - start
	#         if len(vertex_cover) < number_VC:
	#             times.append([t, len(vertex_cover)])
	#             best_VC = vertex_cover
	#             number_VC = len(vertex_cover)
			
	#     return best_VC, times

	def approximate(self, Graph):
		degree_list = nx.degree(Graph)
		top = self.node_max_degree(degree_list)
		vertex_cover = []
		while degree_list[top] > 0:
			vertex_cover.append(top)
			node_list = []
			for node in nx.neighbors(Graph, top):
				node_list.append(node)
		
			for node1 in node_list:
				Graph.remove_edge(node1, top)
			Graph.remove_node(top)
			top = self.node_max_degree(nx.degree(Graph))
		return vertex_cover

	def iterate(self, graph, T):
		t = 0
		number_VC = float('inf')
		trace = []
		start = time.time()
		while t < T:
			Graph_Read = self.read_file(graph)
			VC = self.approximate(Graph_Read)
			t = time.time() - start
			if len(VC) < number_VC:
				trace.append([t, len(VC)])
				number_VC = len(VC)
			t = time.time() - start
		VC.sort()
		return VC, trace, number_VC
	
	def output_file(self, file_name, T, number_VC, VC, trace):
		os.chdir('../')
		outputPath = './output'
		file_name = file_name.split('/')[-1]
		saveAs = os.path.join(outputPath, file_name + "_" + "Approx" + "_" + str(T) + ".sol")
		file_1 = open(saveAs, "w+")
		file_1.write(str(number_VC) + "\n")
		file_1.write(str(VC) + "\n")
		file_1.close()

		saveAs = os.path.join(outputPath, file_name + "_" + "Approx" + "_" + str(T) + ".trace")
		file_2 = open(saveAs, "w+")

		for i in trace:
			file_2.write(str(i[0]) + ", " + str(i[1]) + "\n")
	
		file_2.close()
	
	def main(self):

		#graph = sys.argv[1]
		#T = int(sys.argv[2])
		graph = self.inst
		T = int(self.cutoff)

		file_name = graph[:-6]

		VC, trace, number_VC = self.iterate(graph, T)

		self.output_file(file_name, T, number_VC, VC, trace)

#if __name__ == '__main__':
#	runexp = project()
#	runexp.main()
	