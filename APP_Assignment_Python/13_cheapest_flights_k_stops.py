def cheapest_price(n, flights, src, dst, k):
    inf = float("inf")
    prices = [inf] * n
    prices[src] = 0
    for _ in range(k + 1):
        updated = prices.copy()
        for a, b, cost in flights:
            if prices[a] != inf:
                updated[b] = min(updated[b], prices[a] + cost)
        prices = updated
    return -1 if prices[dst] == inf else prices[dst]

if __name__ == "__main__":
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    print(cheapest_price(4, flights, 0, 3, 1))
