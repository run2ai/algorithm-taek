# https://www.acmicpc.net/problem/12891

import sys
S, P = [int(x) for x in sys.stdin.readline().split()] 
dna = list(sys.stdin.readline())[:-1]
eles = ["A", "C", "G", "T"]
min_nums = [int(x) for x in sys.stdin.readline().split()]

window = dna[:P]
ans = 0

cnt_list = [
    window.count('A'),
    window.count('C'),
    window.count('G'),
    window.count('T'),
]

idx_dict = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3
}

ans = 0
for i in range(S - P + 1):
    if all([cnt >= min_num for cnt, min_num in zip(cnt_list, min_nums)]):
        ans += 1
    if i < S - P:
        cnt_list[idx_dict[dna[i]]] -= 1
        cnt_list[idx_dict[dna[i + P]]] += 1
# print(cnt_list, dna[i:i + P], ans)
# if all([cnt >= min_num for cnt, min_num in zip(cnt_list, min_nums)]):
#     ans += 1
print(ans)