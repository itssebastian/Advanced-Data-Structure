graph = { "a" : ["c "],
          "b" : ["c" ,"e"],
          "c" : ["a" , "b", "e", "d"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : [],
          "g" : []}


edges = []
for i in  graph.values():
    for j in   i:
        if not (j  in  edges):
            edges.append(j)
print(edges)
print(len(edges))
for i in graph:
    if graph[i] == []:
        print(i,"is isolated vertex")
