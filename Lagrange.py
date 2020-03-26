class Lagrange:

    def __init__(self, nodes, values):
        self.nodes = nodes
        for i in range(len(nodes)):
            for j in range(len(nodes)):
                if j != i:
                    values[i] = values[i] / (nodes[i] - nodes[j])
        self.dividers = values

    def get_val(self, x):
        values = self.dividers
        s = 0
        for i in range(len(self.dividers)):
            for j in range(len(self.dividers)):
                if j != i:
                    values[i] *= (x - self.nodes[j])
            s += values[i]
        return s
