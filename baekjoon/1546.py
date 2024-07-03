# https://www.acmicpc.net/problem/1546

N = int(input())
scores = input()
score_list = scores.split(" ")

score_list = [int(x) for x in score_list]
max_score = max(score_list)
fixed_score_list = [x * 100 / max_score for x in score_list]

print(sum(fixed_score_list) / len(fixed_score_list))