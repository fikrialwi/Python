from TopologiIndex import TopologiIndex
from Graph import Graph


class Graf:
    def __init__(self) -> None:
        pass

    def run(self, **option):
        validOption = ["topologi", "graf"]
        topologi = {
            "narumi katayama": "NarumiKatayama",
            "first zagreb multiple": "firstMultipleZagreb",
            "second zagreb multiple": "secondMultipleZagreb"
        }
        for i in option:
            if i not in validOption:
                return 'error option --option yang anda pilih tidak tersedia'

            if i == "graf":
                print(option[i][1])
                if self.cekGraf(option[i][1]):
                    g = Graph(option[i][0], option[i][1])
                    e = g.edges()
                    v = g.vertecies()
                    o = g.orde()
                    s = g.size()
                    print(
                        f"graf : {option['graf'][1]} pada ring {option['graf'][0]}")
                    print(f"simpul dari graf : {v}")
                    print(f"sisi dari graf : {e}")
                    print(f"orde dari graf : {o}")
                    print(f"size dari graf : {s}")
            if i == "topologi":
                if self.cekTopologi(option[i]):
                    t = TopologiIndex(g)
                    if option[i] == "first zagreb multiple":
                        tli = [t.firstMultipleZagreb(
                            1), t.firstMultipleZagreb(2)]
                    else:
                        tli = t.topologi[option[i]]()
                    print(f"indeks {option['topologi']}: {tli}")
            else:
                print("ok")

    def cekGraf(self, graf):
        validGraf = ["annihaltor", ""]
        return graf in validGraf

    def cekTopologi(self, topologi):
        validTopologi = ["narumi katayama"]
        return topologi in validTopologi
