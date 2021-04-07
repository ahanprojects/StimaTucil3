from server.helper.node import Node
from math import sqrt
# Program membaca file input

# menghitung jarak heuristik dengan euclidean
def euclidean(node1, node2):
    coord1 = node1.getCoord()
    coord2 = node2.getCoord()
    x = (coord1[0] - coord2[0])**2
    y = (coord1[1] - coord2[1])**2
    return round(sqrt(x + y), 2)

def read(filename):
    file1 = open(filename, 'r')

    # bikin array of node kosong
    graf = []
    # baca baris pertama file yaitu jumlah node
    jmlNode = int(file1.readline())
    # loop sebanyak jumlah node, masukin ke array of node
    for i in range(jmlNode):
        line = file1.readline().rstrip("\n").split(" ")
        x = float(line[0])
        y = float(line[1])
        name = line[2]
        graf.append(Node(name, (x, y), None))

    # mengisi atribut connected
    for i in range(jmlNode):
        # menghasilkan array line dengan len = jmlNode
        line = file1.readline().rstrip("\n").split(" ")
        for j in range(len(line)):
            if line[j] != '0':
                # masukkan ke connected, contoh format (A,2)
                name = graf[j].getName()
                bobot = euclidean(graf[i],graf[j])
                graf[i].appendToconnected((name, bobot))

    return graf
