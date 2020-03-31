class Lagrange:
    def __init__(self, nodes, values):
        self.nodes = nodes
        val = values
        for i in range(len(nodes)):
            for j in range(len(nodes)):
                if j != i:
                    val[i] = val[i] / (nodes[i] - nodes[j])
        self.dividers = val

    def get_val(self, x):
        values = self.dividers
        s = 0
        for i in range(len(self.dividers)):
            k = 1
            for j in range(len(self.dividers)):
                if j != i:
                    k *= (x - self.nodes[j])
            s += values[i] * k
        return s


