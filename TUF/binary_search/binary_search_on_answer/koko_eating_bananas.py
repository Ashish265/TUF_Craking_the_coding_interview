"""
Docstring for TUF.binary_search.binary_search_on_answer.koko_eating_bananas
Problem Statement: A monkey Koko is given ‘n’ piles of bananas, whereas the 'ith' pile has ‘a[i]’ bananas. An integer ‘h’ is also given, which denotes the time (in hours) for all the bananas to be eaten.

Each hour, the monkey chooses a non-empty pile of bananas and eats ‘k’ bananas. If the pile contains less than ‘k’ bananas, then the monkey consumes all the bananas and won’t eat any more bananas in that hour.

Find the minimum number of bananas ‘k’ to eat per hour so that the monkey can eat all the bananas within ‘h’ hours.

Input: N = 4, a[] = {7, 15, 6, 3}, h = 8
Output: 5
Explanation:  If Koko eats 5 bananas/hr, he will take 2, 3, 2, and 1 hour to eat the piles accordingly. So, he will take 8 hours to complete all the piles.  
Input: N = 5, a[] = {25, 12, 8, 14, 19}, h = 5
Output: 25
Explanation: If Koko eats 25 bananas/hr, he will take 1, 1, 1, 1, and 1 hour to eat the piles accordingly. 

"""
def calculate_total_hours(piles, k):
    total_hours = 0
    for pile in piles:
        total_hours += (pile + k - 1) // k  # Ceiling division to account for partial hours
    return total_hours

def min_eating_speed(piles, h):
    left, right = 1, max(piles)
    result = right

    while left <= right:
        mid = left + (right - left) // 2
        total_hours = calculate_total_hours(piles, mid)

        if total_hours <= h:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

# Example usage:
if __name__ == "__main__":
    piles = [7, 15, 6, 3]
    h = 8
    print(min_eating_speed(piles, h))  # Output: 5

    piles = [25, 12, 8, 14, 19]
    h = 5
    print(min_eating_speed(piles, h))  # Output: 25

    piles = [30, 11, 23, 4, 20]
    h = 6
    print(min_eating_speed(piles, h))  # Output: 23