import snap
import matplotlib.pyplot as plt
import numpy as np

###################################
# Question 1

# Load Wikipedia graph data
wiki_graph = snap.LoadEdgeList(snap.PNGraph,'wikipedia_data.txt',0,1)
count_nodes = snap.CntNonZNodes(wiki_graph)
print('Total nodes in the network: ',count_nodes)
self_edges = snap.CntSelfEdges(wiki_graph)
print('Total self nodes in the network: ',self_edges)
directed_edges = snap.CntUniqDirEdges(wiki_graph)
print('Total directed edges in the network: ',directed_edges)
undirected_edges = snap.CntUniqUndirEdges(wiki_graph)
print('Total undirected edges in the network: ',undirected_edges)
reciprocity = snap.CntUniqBiDirEdges(wiki_graph)
print('Bidirectional edges are: ',reciprocity)
print("Number of zero out-degree:", snap.CntOutDegNodes(wiki_graph, 0))
print("Number of zero in-degree:", snap.CntInDegNodes(wiki_graph, 0))

#Nodes with out degree > 10
count = 0
for i in range(11):
    count+= snap.CntOutDegNodes(wiki_graph, i)
out_deg = wiki_graph.GetNodes() - count
print('Out degree greater than 10: ',out_deg)

#Nodes with in degree < 10
count = 0
for i in range(10):
    count+= snap.CntInDegNodes(wiki_graph, i)
in_deg = wiki_graph.GetNodes() - count
print('IN degree less than 10: ',in_deg)

#####################################
# Question 2

degree = []
node_count = []

CntV = snap.TIntPrV()
snap.GetOutDegCnt(wiki_graph,CntV)
for i in CntV:
    if i.GetVal1()!=0 and i.GetVal2()!=0:
        degree.append(i.GetVal1())
        node_count.append(i.GetVal2())
degree = np.array(degree)
node_count = np.array(node_count)

plt.figure(figsize=(12,8))
ax = plt.gca()
ax.scatter(degree, node_count,alpha=0.5)
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlim([degree.min(), degree.max()])
ax.set_title('Out-degree Distribution', fontsize=30)
ax.set_xlabel('Degree (log)', fontsize=24)
ax.set_ylabel('Count (log)', fontsize=24)
plt.savefig('SNAP_HW0.png')

a,b = np.polyfit(degree,node_count,1)
print('a: ',a)
print('b: ',b)

#Plot line
x = np.array([degree.min(), degree.max()])
y = a*x + b
plt.figure(figsize=(12,8))
plt.plot(degree, node_count, 'ro')
plt.plot(x, y, 'b', linewidth=3)
plt.xlabel('Degree (log)', fontsize=20)
plt.ylabel('Count (log)', fontsize=20)
plt.title('Out-degree Distribution', fontsize=30)

plt.savefig('SNAP_HW0_Q2.png')

###########################################
## Question 3
# Load Wikipedia graph data
stack_overflow_graph = snap.LoadEdgeList(snap.PNGraph,'stackoverflow-Java.txt',0,1)

# Weakly connected components
Components = snap.TCnComV()
snap.GetWccs(stack_overflow_graph, Components)
print("Number of Weakly Connected Components:", Components.Len())

# Edges and Nodes of Weakly connected edges
MxWcc = snap.GetMxWcc(stack_overflow_graph)
print("Number of MxWcc Edges:", MxWcc.GetEdges())
print("Number of MxWcc Nodes:", MxWcc.GetNodes())

PRankH = snap.TIntFltH()
snap.GetPageRank(stack_overflow_graph, PRankH)
PRankH.SortByDat(False)

i = 0
itr = PRankH.BegI()
print("The top 3 most central nodes in the network by PagePank scores:")
while i < 3:
    print("Node:", itr.GetKey())
    itr.Next()
    i += 1
print("")
