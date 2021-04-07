from server.helper.node import Node
from math import sqrt

# apakah nama node ada pada graf


def isNodeValid(nama, graf):
    for node in graf:
        if nama == node.getName():
            return True
    return False

# print array lintasan


def print_lintasan(lintasan):
    for i in range(len(lintasan)):
        print("("+lintasan[i]+")", end=' ')
        if i != len(lintasan) - 1:
            print("->", end=' ')

# ----------------- A* ALGORITHM ----------------------- #

# mencari node berdasarkan nama dari fileinput


def cariNode(nama, graf):
    for node in graf:
        if nama == node.getName():
            return node

# menghitung jarak heuristik dengan euclidean


def jarakheuristik(node1, node2):
    coord1 = node1.getCoord()
    coord2 = node2.getCoord()
    x = (coord1[0] - coord2[0])**2
    y = (coord1[1] - coord2[1])**2
    return sqrt(x + y)

# memeriksa apakah tetangga boleh dimasukkan ke opened


def opened_add(tetangga, opened):
    for node in opened:
        if (tetangga.f > node.f and tetangga == node):
            return False
    return True


def aStarAlgorithm(strfirst, strlast, graf):
    # first, last : node. graf, opened, closed : array of node
    first = cariNode(strfirst, graf)
    no_parent = Node("$", None, None)
    first.setParent(no_parent)
    last = cariNode(strlast, graf)

    # List kosong opened dan closed
    opened = []
    closed = []

    # masukkan first node ke opened
    opened.append(first)

    # selama masih ada node pada list opened
    while len(opened) > 0:
        # urutkan opened berdasarkan f(n)
        opened.sort()
        # pilih node dengan f(n) terkecil, lalu hapus dari opened
        cekNode = opened.pop(0)
        # masukan cekNode ke closed (node di tutup)
        closed.append(cekNode)

        # check apakah sudah sampai node last
        if cekNode == last:
            # array lintasannya
            lintasan = []
            # selama current node bukan first
            while cekNode != first:
                lintasan.append(cekNode.getName() + ': ' + str(cekNode.getg()))

                # pindah ke parent dari current node
                cekNode = cekNode.getParent()

            # masukkan first node ke lintasan
            lintasan.append(first.getName() + ': ' + str(first.getg()))

            # kembalikan lintasan yang dibalik
            return lintasan[::-1]

        # Memeriksa semua tetangga dari ceknode
        # tupl adalah elemen pada atribut connected, format (Nama,Bobot)
        for tupl in cekNode.getConnected():

            # cek tetangga
            tetangga = cariNode(tupl[0], graf)

            # jika tetangga belum punya parent
            if tetangga.getParent() is None:
                tetangga.setParent(cekNode)

            # skip jika tetangga sudah ada pada closed
            if(tetangga in closed):
                continue

            # hitung dan masukan nilai g(n), h(n), f(n) ke atribut tetangga
            tetangga.setg(cekNode.getg() + tupl[1])            # hitung g(n)
            tetangga.seth(jarakheuristik(tetangga, last))        # hitung h(n)
            tetangga.setf(tetangga.getg() + tetangga.geth())    # hitung f(n)

            # periksa apakah tetangga ada pada list opened
            # dan memiliki f(n) lebih kecil, jika iya masukkan ke opened
            if opened_add(tetangga, opened):
                opened.append(tetangga)

    # jika lintasan tidak ditemukan
    return None
