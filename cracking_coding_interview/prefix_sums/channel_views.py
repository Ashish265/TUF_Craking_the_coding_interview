"""Imagine you are given an array of integers representing the daily views for a YouTube channel. 
You are then asked to answer multiple queries, 
each asking for the total number of views between two specific days. 

Input:
An array views[], where views[i] is the number of views on day i.
An array periods[], where each element is a pair [l,r] with 0 <= l <= r < n

Return an array, results of integers with length p where result[i] is the number of views during that period """

views = [3, 5, 4, 8, 7, 2, 5, 3, 2, 3]
periods = [[0, 1], [0, 5], [5, 8], [3, 3] ]

def channel_views(views, periods):
    res = []

    prefix_sum = [0] * len(views)

    for i in range(1, len(views)):
        prefix_sum[i] = prefix_sum[i-1] + views[i]

    for l, r in periods:

        if l == 0:
            res.append(prefix_sum[r])

        else:
            res.append(prefix_sum[r] - prefix_sum[l-1])
    return res


print(channel_views(views, periods))
