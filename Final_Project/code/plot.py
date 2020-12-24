import matplotlib.pyplot as plt

#star2 ls2 seed 1-10 opt 4542

#x1 = 1.13 5133
x1 = [125.19, 201.12, 116.54, 236.46, 255.75, 178.85, 148.25, 325.6, 272.78, 236.77] #miss 6
#x2 = 1.14 5178
x2 = [45.73, 69.80, 67.38, 236.46, 178.85, 131.52, 219.67, 59.5, 56.05, 236.77]
#x3 = 1.15 5223
x3 = [26.77, 69.80, 67.38, 62.44, 131.37, 131.52, 219.67, 56.50, 137.52, 236.77]
#x4 = 1.16 5268
x4 = [26.77, 69.80, 67.38, 62.44, 236.77, 131.52, 131.37, 59.05, 56.50, 129.20]
y = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

x1 = sorted(x1)
x2 = sorted(x2)
x3 = sorted(x3)
x4 = sorted(x4)

plt.plot(x1, y, 'b', label='q*=13%')
plt.plot(x2, y, 'r', label='q*=14%')
plt.plot(x3, y, 'g', label='q*=15%')
plt.plot(x4, y, 'y', label='q*=16%')
plt.xlabel('run-time(sec)')
plt.ylabel('P(solve)')
plt.title('star2.graph LS2 QRTD')
plt.legend(bbox_to_anchor=(0.95, 0.95), loc='upper left', borderaxespad=0.5)
plt.show()

#power ls2 seed 1-10 opt 2203

#w1 = 1.03 2269
w1 = [61.25, 39.39, 49.91, 154.26, 275.16, 297.40, 156.22, 68.08, 121.30, 80.96]
#w2 = 1.04 2291
w2 = [22.84, 17.34, 15.44, 36.08, 22.91, 21.38, 23.98, 32.49, 35.11, 27.12]
#w3 = 1.05 2313
w3 = [16.59, 11.79, 10.43, 20.13, 15.95, 12.73, 14.85, 26.76, 10.84, 10.93] 
#w4 = 1.06 2335
w4 = [15.04, 7.30, 7.64, 12.63, 11.71, 10.71, 10.43, 11.45, 10.09, 6.56]
y = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

w1 = sorted(w1)
w2 = sorted(w2)
w3 = sorted(w3)
w4 = sorted(w4)

plt.plot(w1, y, 'b', label='q*=3%')
plt.plot(w2, y, 'r', label='q*=4%')
plt.plot(w3, y, 'g', label='q*=5%')
plt.plot(w4, y, 'y', label='q*=6%')
plt.xlabel('run-time(sec)')
plt.ylabel('P(solve)')
plt.title('power.graph LS2 QRTD')
plt.legend(bbox_to_anchor=(0.95, 0.95), loc='upper left', borderaxespad=0.5)
plt.show()


# star2 4542
# 1.13 5133

#t1 t=60
t1 = [5170, 5312, 5155, 5164, 5155, 5173, 6212, 5196, 5170, 5162]
#t2 t=120
t2 = [5059, 5252, 5100, 5107, 5126, 6091, 5098, 5106, 5105, 5087]
#t3 t=180
t3 = [5095, 5252, 5115, 5107, 5126, 5098, 6045, 5196, 5105, 5087]
#t4 t = 240
t4 = [5037, 5100, 5312, 5061, 5069, 5038, 5062, 5043, 5087, 4993]
y = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

t1 = sorted(t1)
t2 = sorted(t2)
t3 = sorted(t3)
t4 = sorted(t4)

plt.plot([(x-4542)/4542 for x in t1], y, 'b', label='t=60s')
plt.plot([(x-4542)/4542 for x in t2], y, 'r', label='t=120s')
plt.plot([(x-4542)/4542 for x in t3], y, 'g', label='t=180s')
plt.plot([(x-4542)/4542 for x in t4], y, 'y', label='t=240s')
plt.xlabel('relative solution quality [%]')
plt.ylabel('P(solve)')
plt.title('star2.graph LS2 SQD')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.show()

# star2 4542
# 1.13 5133

#s1 s=10
s1 = [2350, 2321, 2322, 2365, 2340, 2339, 2342, 2337, 2340, 2320]
#t2 s=20
s2 = [2304, 2290, 2297, 2330, 2301, 2309, 2301, 2303, 2316, 2399]
#t3 s=30
s3 = [2287, 2285, 2280, 2298, 2279, 2286, 2290, 2294, 2299, 2287]
#t4 s=40
s4 = [2284, 2268, 2280, 2285, 2275, 2286, 2284, 2287, 2283, 2282]
y = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

s1 = sorted(s1)
s2 = sorted(s2)
s3 = sorted(s3)
s4 = sorted(s4)

plt.plot([(x-2203)/2203 for x in s1], y, 'b', label='t=10s')
plt.plot([(x-2203)/2203 for x in s2], y, 'r', label='t=20s')
plt.plot([(x-2203)/2203 for x in s3], y, 'g', label='t=30s')
plt.plot([(x-2203)/2203 for x in s4], y, 'y', label='t=40s')
plt.xlabel('relative solution quality [%]')
plt.ylabel('P(solve)')
plt.title('power.graph LS2 SQD')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.show()

#ls1 star2 QRTD
x1 = [183.17,204.48,230.31,252.99,299.33,319.46,324.57,335.12,400.33,616.41]
x2 = [157.33,177.24,179.42,205.08,216.08,247.61,272.82,274.00,332.27,525.74]
x3 = [132.28,146.58,153.59,179.22,198.06,200.59,216.08,223.45,246.78,479.64]
x4 = [84.80,105.05,116.12,127.92,150.55,174.64,181.93,200.59,216.08,220.81]
y = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

plt.plot(x1, y, 'b', label='q*=9%')
plt.plot(x2, y, 'r', label='q*=10%')
plt.plot(x3, y, 'g', label='q*=11%')
plt.plot(x4, y, 'y', label='q*=12%')
plt.xlabel('run-time (sec)')
plt.ylabel('P(solve)')
plt.title('star2.graph LS1 QRTD')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)


#ls1 star2 SQD
x1 = sorted([5252,5155,5107,5069,5111,6136,5196,5105,5162,5170])
x2 = sorted([5082,5100,5061,4945,4972,6045,5017,4953,5010,5095])
x3 = sorted([5042,4964,4946,4875,4898,4993,5017,4895,4881,4965])
x4 = sorted([5042,4890,4885,4835,4878,4924,4970,4854,4868,4880])
y = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

plt.plot([(x-4542)/4542 for x in x1], y, 'b', label='t=100s')
plt.plot([(x-4542)/4542 for x in x2], y, 'r', label='t=200s')
plt.plot([(x-4542)/4542 for x in x3], y, 'g', label='t=300s')
plt.plot([(x-4542)/4542 for x in x4], y, 'y', label='t=400s')
plt.xlabel('relative solution quality (%)')
plt.ylabel('P(solve)')
plt.title('star2.graph LS1 SQD')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

#ls1 power QRTD
x1 = [24.75, 32.02, 32.54, 45.92, 50.37, 53.42, 140.28, 168.29, 185.93, 413.04]
x2 = [24.75, 32.02, 32.54, 34.35, 40.5, 50.37, 62.27, 68.32, 74.68, 185.93]
x3 = [15.97, 17.23, 21.77, 23.77, 28.73, 30.46, 30.8, 31.1, 38.74, 41.23]
x4 = [15.43, 17.23, 18.54, 21.27, 23.77, 26.17, 29.15, 30.8, 31.1, 35.36]
y = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

plt.plot(x1, y, 'b', label='q*=3%')
plt.plot(x2, y, 'r', label='q*=3.1%')
plt.plot(x3, y, 'g', label='q*=3.5%')
plt.plot(x4, y, 'y', label='q*=3.6%')
plt.xlabel('run-time (sec)')
plt.ylabel('P(solve)')
plt.legend(bbox_to_anchor=(1.1, 1), loc='upper left', borderaxespad=0.)
plt.title('power.graph LS1 QRTD')

#ls1 power SQ
x1 = sorted([153,194,175,195,197,175,190,193,216,176])
x2 = sorted([125,165,140,139,142,141,157,138,180,152])
x3 = sorted([102,124,111,88,98,107,109,101,130,103])
x4 = sorted([69,68,68,68,76,74,79,74,68,68])
y = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

plt.plot([(2200+x-2203)/2203 for x in x1], y, 'b', label='t=2s')
plt.plot([(2200+x-2203)/2203 for x in x2], y, 'r', label='t=5s')
plt.plot([(2200+x-2203)/2203 for x in x3], y, 'g', label='t=10s')
plt.plot([(2200+x-2203)/2203 for x in x4], y, 'y', label='t=50s')
plt.xlabel('relative solution quality (%)')
plt.ylabel('P(solve)')
plt.legend(bbox_to_anchor=(1.1, 1), loc='upper left', borderaxespad=0.)
plt.title('power.graph LS1 SQD')
