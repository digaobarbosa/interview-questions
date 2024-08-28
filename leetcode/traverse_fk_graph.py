from typing import *
from collections import deque

def normalize_graph(graph:dict):
    keys = list(graph.keys())
    for key in keys:
        fks = graph.get(key,set())
        for fk in fks:
            fk_set = graph.get(fk)
            if fk_set is None:
                graph[fk] = set([key])
            else:
                fk_set.add(key)



def traverse(graph:dict,start: str,end:str) -> List[str]:
    normalize_graph(graph)
    q = deque([(start,[start])])
    visited = set()
    while q:
        table,path = q.pop()
        fks = graph.get(table,[])
        if table == end:
            return path
        for fk in fks:
            if fk not in visited:
                q.append((fk,path+[fk]))
        visited.add(table)


if __name__ == '__main__':
    g = {"a":set(["b"]),
         "b":set(["c","d"]),
         "c":set(["x","y"]),
         "d":set(["e","f"]),
         }
    print(traverse(g,"a","e"))
    g = {"a":set(["b"]),
         "b":set(["c","d","a"]),
         "c":set(["x","y","c"]),
         "d":set(["e","f","a"]),
         }
    print(traverse(g,"a","e"))

    g = {"a":set(["b"]),
         "b":set(["c","d","a"]),
         "c":set(["x","y","c"]),
         "d":set(["e","f","a"]),
         }
    print(traverse(g,"e","a"))

    g = {"a":set(["b"]),
         "b":set(["c","d"]),
         "c":set(["x","y"]),
         "d":set(["e","f"]),
         }
    print(traverse(g,"a","e"))