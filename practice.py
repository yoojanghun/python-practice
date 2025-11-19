N, S, E, M = map(int, input().split())    # 0 ~ N-1 까지 도시 존재
cost = []
for _ in range(M):
    start, end, price = map(int, input().split())
    cost.append((start, end, -price))

city_money = []
for _ in range(N):
    money = int(input())
    city_money.append(money)

