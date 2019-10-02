# Write a function:
#
# def solution(A)
#
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
#
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
#
# Given A = [1, 2, 3], the function should return 4.
#
# Given A = [−1, −3], the function should return 1.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].



def solution_1(A):

    A.sort()
    missing = 1

    for element in A:

        if element == missing:
            missing = element + 1

    return missing


def solution_2(A):

    return min(set(range(1, len(A)+2)).difference(set(A)))


# print(solution_2([4,5]))