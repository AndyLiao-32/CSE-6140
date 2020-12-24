#!/usr/bin/python
# CSE6140 HW2
# This is an example of how your experiments should look like.
# Feel free to use and modify the code below, or write your own experimental code, as long as it produces the desired output.
# To execute the code: py -3 runexperiment.py xxx.gr xxx.extra xxx.out.txt
import time
import sys

class RunExperiments:
    # set the initial empty set, source, for storing the node as the key and its root as the value
    source = {}

    # implementing the unionfind function
    def find(self, node):
        # check whether the node exists or not
        if node not in self.source:
            self.source[node] = node        
        else:
            # if the node is not the root, then call the function again to find the root
            if self.source[node] != node:
                self.source[node] = self.find(self.source[node])
            else:
                return self.source[node]

        return self.source[node]

    def union(self, node1, node2):
        self.source[node1] = self.source[node2]

    def parse_edges(self, filename):
        # count = 0
        # Write this function to parse edges from graph file to create your graph object
        with open(filename) as file:
            index = 0
            data_list = []
            for row in file:
                # print(row)
                if index == 0:
                    index += 1
                    continue
                else:
                    item = row.split()
                    # count += int(item[2])
                    # print(item)
                    # use int() to ensure that every item has been transformed to be integer
                    data_list.append((int(item[0]),int(item[1]),int(item[2])))
        # sort the data by its weight
        data_list.sort(key=lambda data: data[2])

        # check the total of the weight
        # print(count)

        # return the data_list, will assigned to G, our graph
        return data_list

    # using Kruskal's Algorithm
    def computeMST(self, G):
        # To renew the item in the source dict
        self.source = {}
        # initial cost of the MST
        cost = 0
        # Write this function to compute total weight of MST
        for i in G:
            root1 = self.find(i[0])
            root2 = self.find(i[1])

            if root1 != root2:
                cost += i[2]

                # implement the union function if two nodes have different root
                self.union(root1, root2)

        return cost

    def recomputeMST(self, u, v, weight, G):
        # Write this function to recompute total weight of MST with the newly added edge
        G.append((u, v, weight))
        G.sort(key=lambda data: data[2])
        
        return self.computeMST(G)

    def main(self):

        num_args = len(sys.argv)

        if num_args < 4:
            print("error: not enough input arguments")
            exit(1)

        graph_file = sys.argv[1]
        change_file = sys.argv[2]
        output_file = sys.argv[3]

        # Construct graph
        G1 = self.parse_edges(graph_file)

        start_MST = time.time()  # time in seconds
        # call MST function to return total weight of MST
        MSTweight = self.computeMST(G1)
        total_time = (time.time() - start_MST) * \
            1000  # to convert to milliseconds

        # Write initial MST weight and time to file
        output = open(output_file, 'w')
        output.write(str(MSTweight) + " " + str(total_time) + "\n")

        # Construct graph
        G2 = self.parse_edges(change_file)

        for i in G2:
            u, v, weight = i[0], i[1], i[2]

            # call recomputeMST function
            start_recompute = time.time()
            new_weight = self.recomputeMST(u, v, weight, G1)
            # to convert to milliseconds
            total_recompute = (time.time() - start_recompute) * 1000
            # write new weight and time to output file
            output.write(str(new_weight) + " " + str(total_recompute) + "\n")


if __name__ == '__main__':
    # run the experiments
    runexp = RunExperiments()
    runexp.main()
