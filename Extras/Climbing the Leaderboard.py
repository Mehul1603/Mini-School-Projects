#https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

def climbingLeaderboard(scores, alice):
    res = []
    for a in alice:
        scor = list(scores)
        scor += [a]
        scor.sort(reverse=True)
        ind = scor.index(a)
        rank = [1]
        for i in range(1,ind+1):
            if scor[i] == scor[i-1]:
                rank += [rank[i-1]]
            else:
                rank += [rank[i-1]+1]
        res += [rank[ind]]
    return res