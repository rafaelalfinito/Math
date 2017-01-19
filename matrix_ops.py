import numpy as np


class estrutura(object):
    def __init__(self, struct):
        self.structure = struct
        self.b = self.init_b(self.structure)
        self.w = self.init_w(self.structure)

    def init_b(self, struct):
        b = []
        for i in range(1, len(struct)):
            b.append(np.random.randn(struct[i]))

        return b

    def init_w(self, struct):
        w = []
        for i in range(len(struct)-1):
            w.append(np.transpose(np.random.randn(struct[i+1], struct[i])))
        return w

    def prop_fwd(self, inputs):
        a = []
        a.append(inputs)
        # print('Array A:')
        # print(a)
        for layer in range(1, len(self.structure)):
            outputs = []
            #print('layer %s'.format(self.w[layer]), layer)
            for i in range(0, self.structure[layer]):
                w_prime = list(map(list, zip((self.w[layer - 1])[:, i])))
                # print('a:')
                # print(a[layer-1])
                # print('w')
                # print(w_prime)
                # print('b')
                # print(self.b[layer-1])
                # print(np.dot(a[layer-1],w_prime))
                x = (np.dot(a[layer-1],w_prime) + self.b[layer-1][i])
                # print('x:')
                # print(x)
                outputs.append(signal(x))
            a.append(list(outputs))
            #print(self.b[layer])
            #print(outputs)
            #print(a)
        return a

def signal(x):
    result = float(1/(1+np.exp(-x)))
    return result

np.random.seed(0)
struct = estrutura(np.array([4, 3, 2]))
#
print(struct.structure)
print(struct.b)
print(struct.w)
print(struct.prop_fwd(np.transpose([0,0,0,0])))
