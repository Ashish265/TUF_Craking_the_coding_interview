"""
A YouTuber has fetched the number of likes and dislikes of a video each day since its publication.
We say a day is positive if it has more likes than dislikes.

We are given:

Two arrays, likes and dislikes, of length n, representing the likes and dislikes on each day.
An array periods of length p, where each element is a pair [l, r] with 0 ≤ l ≤ r < n. Each pair represents a time period from day l to day r inclusive.
Return an array, results, of length p, where results[i] is the number of positive days during period[i].

Example:
likes    = [6, 3, 4, 8, 7, 2, 6, 5, 0, 1]
dislikes = [6, 0, 8, 0, 0, 0, 1, 8, 0, 2]
periods  = [[0, 1], [0, 5], [5, 8], [3, 3]]

Output: [1, 4, 2, 1]
For instance, element 0 (for the period [0, 1]) is 1 because
day 0 doesn't have more likes than dislikes, but day 1 does.
"""


def good_reception_score(likes, dislikes, periods):
    positive_days = [0] * len(likes)

    for i in range(len(likes)):
        if likes[i] > dislikes[i]:
            positive_days[i] = 1
    
    prefix_sum = [0] * len(likes)
    prefix_sum[0] = positive_days[0]

    for i in range(1,len(positive_days)):
        prefix_sum[i] = prefix_sum[i-1] + positive_days[i]
    
    res = []

    for l, r in periods:
        if l == 0:
            res.append(prefix_sum[r])
        else:
            res.append(prefix_sum[r] - prefix_sum[l-1])
    return res



likes    = [6, 3, 4, 8, 7, 2, 6, 5, 0, 1]
dislikes = [6, 0, 8, 0, 0, 0, 1, 8, 0, 2]
periods  = [[0, 1], [0, 5], [5, 8], [3, 3]]

print(good_reception_score(likes, dislikes, periods))