'''
CSE 6140 2020 Fall group project
Shen-Yi Cheng
Chin Wang
Ting Liao
'''

import argparse
from Approx import Approx
from BnB import bnb
from LS1 import ls1_main
from LS2 import ls2




# parse
parser = argparse.ArgumentParser()
parser.description = "Minumun vertex cover problem with 4 different algorithms."
parser.add_argument("-inst", help="Please enterfile path" , default='../DATA/dummy1.graph')
parser.add_argument("-alg", help="Please enter algorithms name <BnB, Approx, LS1, LS2>", default='BnB', choices=["BnB", "Approx", "LS1", "LS2"])
parser.add_argument("-time", help="Please enter computing cutoff time", type=int, default=600)
parser.add_argument("-seed", help="Please enter random seed number for local search", type=int, default=10)
args = parser.parse_args()

if __name__ == '__main__':
	if args.alg == "Approx":
		run = Approx(args.inst, args.time)
		run.main()
	elif args.alg == "BnB":
		bnb(args.inst, args.time, args.seed)
	elif args.alg == "LS1":
		ls1_main(args.inst, args.time, args.seed)
	elif args.alg == "LS2":
		ls2(args.inst, args.time, args.seed)

	

