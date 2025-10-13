def shortestWordDistance(l:list, w1, w2)->int:
    i1 = -1 
    i2 = -1
    ans = float("inf")

    for i in range(len(l)):
        if l[i] == w1:
            i1 = i
        if l[i] == w2:
            i2 = i
        if i1 != -1 and i2 != -1:
            ans = min(ans, abs(i1-i2))
    
    return ans


if __name__ == "__main__":
    l1 =["practice", "makes", "perfect", "coding", "makes"]
    assert shortestWordDistance(l1, "practice", "coding") == 3
    assert shortestWordDistance(l1, "coding", "makes") == 1 