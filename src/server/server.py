from flask import Flask, request, render_template
from server.helper.fileinput import read
from server.helper.astar import aStarAlgorithm
from server.helper.parser import graph_to_json, arr_of_dict_to_graph
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/compute-path", methods=["POST"])
def compute_path():
    body = request.json

    graph = arr_of_dict_to_graph(body["graph"])

    path_string_arr = aStarAlgorithm(body["start"], body["end"], graph)

    path = []
    for path_string in path_string_arr:
        splitted = path_string.split(": ")
        path.append({
            "name": splitted[0],
            "weight": float(splitted[1])
        })

    return {"path": path}
