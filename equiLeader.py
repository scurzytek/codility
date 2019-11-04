# A non-empty array A consisting of N integers is given.
#
# The leader of this array is the value that occurs in more than half of the elements of A.
#
# An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.
#
# For example, given array A such that:
#
#     A[0] = 4
#     A[1] = 3
#     A[2] = 4
#     A[3] = 4
#     A[4] = 4
#     A[5] = 2
# we can find two equi leaders:
#
# 0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
# 2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
# The goal is to count the number of equi leaders.
#
# Write a function:
#
# def solution(A)
#
# that, given a non-empty array A consisting of N integers, returns the number of equi leaders.
#
# For example, given:
#
#     A[0] = 4
#     A[1] = 3
#     A[2] = 4
#     A[3] = 4
#     A[4] = 4
#     A[5] = 2
# the function should return 2, as explained above.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].


def solution(a):

    if len(a) == 1:
        return 0

    B = a[:]
    B.sort()

    leader = B[len(a) // 2]
    count_leader = len([number for number in a if number == leader])

    if count_leader <= len(a) // 2:
        return 0

    count_left_leader = 0
    equi_leader = 0

    for i in range(0, len(a)):
        if a[i] == leader:
            count_left_leader += 1
        if count_left_leader > (i + 1) // 2 and (count_leader - count_left_leader) > (len(a) - i - 1) // 2:
            equi_leader += 1

    return equi_leader


print(solution([4, 3, 3, 3, 3, 4, 3, 3, 3]))





