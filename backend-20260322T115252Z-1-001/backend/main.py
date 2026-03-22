# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Set, Tuple
from collections import defaultdict, deque

app = FastAPI()

# Allow frontend localhost
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Pipeline(BaseModel):
    nodes: List[Dict]
    edges: List[Dict]

@app.get('/')
def read_root():
    return {'Ping': 'Pong'}

def is_dag_func(nodes, edges: Set[Tuple[str, str]]):
    graph = defaultdict(list)
    indegree = {node['id']: 0 for node in nodes}

    for src, tgt in edges:  # unpack tuple here
        if src in indegree and tgt in indegree:
            graph[src].append(tgt)
            indegree[tgt] += 1

    queue = deque([node_id for node_id, deg in indegree.items() if deg == 0])
    visited = 0

    while queue:
        current = queue.popleft()
        visited += 1
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return visited == len(nodes)

@app.post('/pipelines/parse')
def parse_pipeline(pipeline: Pipeline):
    nodes = pipeline.nodes
    edges = pipeline.edges

    # count unique edges
    unique_edges: Set[Tuple[str, str]] = set()
    for edge in edges:
        src = edge.get('source')
        tgt = edge.get('target')
        if src and tgt and src != tgt:  # ignore self-loops
            unique_edges.add((src, tgt))

    num_nodes = len(nodes)
    num_edges = len(unique_edges)
    is_dag = is_dag_func(nodes, unique_edges)  # now works

    return {
        'num_nodes': num_nodes,
        'num_edges': num_edges,
        'is_dag': is_dag
    }