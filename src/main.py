from server.helper.astar import aStarAlgorithm, isNodeValid, print_lintasan
from server.helper.fileinput import read
from server.helper.node import Node
from server.server import app

import sys

if len(sys.argv) == 1:
    app.run(port=5000, debug=True)

else:
    if sys.argv[1] == "cli":
        filename = input("Masukkan nama file input: ")
        graf = read(filename)
        awal = input("Node awal : ")
        akhir = input("Node akhir : ")

        if isNodeValid(awal, graf) and isNodeValid(akhir, graf):
            lintasan = aStarAlgorithm(awal, akhir, graf)
            print("Lintasan dari "+awal+" ke "+akhir+" tercepat :")
            print(lintasan)
        else:
            print("Node input tidak valid.")

    elif sys.argv[1] == "server":
        app.run(port=5000, debug=True)

    else:
        print("invalid command")
