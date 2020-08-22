g = {}
g['s'] = {}
g['s']['a'] = 5
g['s']['b'] = 2
g['a'] = {}
g['a']['d'] = 2
g['a']['c'] = 4
g['b'] = {}
g['b']['a'] = 8
g['b']['d'] = 7
g['c'] = {}
g['c']['d'] = 6
g['c']['f'] = 3
g['d'] = {}
g['d']['f'] = 1

inf = float('inf')
costs = {}
costs ['a'] = 5
costs ['b'] = 2
costs ['f'] = inf

p = {}
p['a'] = 's'
p['b'] = 's'
p['in'] = None

processed = []

def find_l_c_n(costs):
    l_cost = float('inf')
    l_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < l_cost and node not in processed:
            l_cost = cost
            l_cost_node = node
    return l_cost_node

node = find_l_c_n(costs)
while node is not None:
    cost = costs[node]
    neighbors = g[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        print("n=" ,n)
        print("neighbors[n] = {vnc} and type = {tnc}".format(vnc = neighbors[n], tnc = type(neighbors[n])))

        print("new_cost = {vnc} and type = {tnc}".format(vnc = new_cost, tnc = type(new_cost)))
        print("costs[n] = {n1c} and type = {nc}".format(n1c = costs[n], nc = type(costs[n])))

        if costs[n] > new_cost:
            costs[n] = new_cost
            p[n] = node
    processed.append(node)
    node = find_l_c_n(costs)