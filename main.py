l = [1,1,0,-1,-1]

negs = [v for v in l if v < 0]
poss = [v for v in l if v > 0]
zeros = [v for v in l if v == 0]

print(l)

print(f'{len(poss)/len(l):.6f}')
print(f'{len(negs)/len(l):.6f}')
print(f'{len(zeros)/len(l):.6f}')
