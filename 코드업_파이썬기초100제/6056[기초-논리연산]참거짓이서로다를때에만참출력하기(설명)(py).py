a, b = map(int, input().split())
c = bool(a)
d = bool(b)
print(c != d)

'''
XOR 연산 - (A&&!B)||(!A&&B)를 파이썬에서 구현하려면
(A and (not B)) or ((not A) and B)를 이용하여
print((c and (not d)) or ((not c) and d)) 로도 구현 가능
'''