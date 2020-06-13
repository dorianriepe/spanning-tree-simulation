file = open('graph.txt', 'rt').read()
lines = file.split('\n')

nodes = {}

for line in lines:
    line = line.strip()

    if '=' in line:
        name, weight = line.split('=')
        name = name.strip()
        weight = int(weight.replace(';','').strip())
        nodes[name] = {'weight': weight,'name': name,'root': name,'cost': 0,'nextHop': name,'neighbours': {}}

    if ':' in line and '-' in line:
        node, weight = line.split(':')
        node1, node2 = node.split('-')
        node1 = node1.strip()
        node2 = node2.strip()
        weight = int(weight.replace(';','').strip())
        nodes[node1]['neighbours'][node2] = nodes[node2]['neighbours'][node1] = weight

for i in range(0, 10):
    
    nodesNameList = list(nodes.keys()) 

    for nodeName in nodesNameList:

        # 'Send message' to neighbours
        neighbours = list(nodes[nodeName]['neighbours'])
        for neighbourName in neighbours:
            
            senderRoot = nodes[nodeName]['root']
            neighbourRoot = nodes[neighbourName]['root']
            senderRootWeight = nodes[senderRoot]['weight']
            neighbourRootWeight = nodes[neighbourRoot]['weight']

            # Check if path is shorter, if root of sender and recipient are the same
            if senderRoot is neighbourRoot:
                senderCost = nodes[nodeName]['cost']+nodes[nodeName]['neighbours'][neighbourName]
                neighbourCost = nodes[neighbourName]['cost']
                if senderCost < neighbourCost:
                    nodes[neighbourName]['cost'] = nodes[nodeName]['cost']+nodes[nodeName]['neighbours'][neighbourName]
                    nodes[neighbourName]['nextHop'] = nodeName

            # Check if root weight is better than neighbour's root weight
            if senderRootWeight < neighbourRootWeight:
                nodes[neighbourName]['root'] = nodes[nodeName]['root']
                nodes[neighbourName]['cost'] = int(nodes[nodeName]['cost'])+int(nodes[nodeName]['neighbours'][neighbourName])
                nodes[neighbourName]['nextHop'] = nodeName

out = "Spanning-Tree {\n\n    Root: "+nodes['A']['root']+";\n"
nodesNameList = list(nodes.keys()) 
for name in nodesNameList:
    if name is not nodes['A']['root']:
        out = out+"    "+name+" - "+nodes[name]['nextHop']+";\n"
out = out + "}"
file = open("result.txt", "w")
file.write(out)
file.close()
