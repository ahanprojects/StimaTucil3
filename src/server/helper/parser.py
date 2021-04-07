import json
from server.helper.node import Node


def graph_to_json(graph):
    retval = {
        "nodes": []
    }
    for node in graph:
        retval["nodes"].append({
            "name": node.name,
            "position": {
                "lat": node.position[1],
                "lng": node.position[0]
            },
            "connected": [{"name": c[0], "weight": c[1]} for c in node.connected]
        })

    print(retval)
    return retval


def arr_of_dict_to_graph(arr_of_dict):
    retval = []
    for d in arr_of_dict:
        pos = (d["position"]["lng"], d["position"]["lat"])
        name = d["name"]
        conns = d["connected"]

        new_node = Node(name, pos, None)
        new_node.connected = [(conn["name"], float(conn["weight"]))
                              for conn in conns]

        retval.append(new_node)

    return retval
