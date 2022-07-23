
# Today you decided to go to the gym. You currently have energy equal to E units. There are N exercises in
# the gym. Each of these exercises drains Ai amount of energy from your body.
# You feel tired if your energy reaches 0 or below. Calculate the minimum number of exercises you have
# to perform such that you become tired. Every unique exercise can only be performed at most 2 times as
# others also have to use the machines.
# If performing all the exercises does not make you feel tired, return -1.

# Parameters:
# E :: INTEGER
# The first line contains an integer, E, denoting the Energy.
# E :: 1 -> 10^5
# N :: INTEGER
# The next line contains an integer, N, denoting the number of exercises.
# N :: 1 -> 10^5
# A :: INTEGER ARRAY
# Each line i of the N subsequent lines (where 0 ≤ i < N) contains an integer describing the amount of
# energy drained by i-th exercise.
# A[i] :: 1 -> 10^5

# Test Cases
# Case#: 1
# Input:
# 6
# 2
# 1
# 2
# Output:
# 4
# E = 6
# Do 1st exercise 2 times
# Do 2nd exercise 2 times
# Hence, total exercises done 4.


def minEx(e, a):
    # print(e)
    # print(a)
    amount = {}
    exercises = 0

    for i in a:
        if i in amount:
            amount[i] += 2
        amount[i] = 2
    # print(amount)
    
    while e > 0:
        amax = max(amount)
        # print("Max of e = ", amax)
        for k,v in amount.items():
            if e == k*v:
                return v
        if e >= amax:
            # print(e," >= ",amax)
            exercises += 1
            e -= amax
            amount[amax] -= 1
            if amount[amax] < 1:
                amount.pop(amax)
        elif e in amount:
            # print(e," in ", amount)
            exercises += 1
            amount[e] -= 1
            if amount[e] < 1:
                amount.pop(e)
            e -= e
        else:
            k = max(amount)
            if k <= e:
                # print(k, " <= ", e)
                exercises += 1
                e -= k
                amount[k] -= 1
                if amount[k] < 1:
                    amount.pop(k)
            amount.pop(k)
        
        # print(amount)
        # print ("***** E = ",e,"**** Exercise = ",exercises,"******")
        
        if not amount and e>0:
            # print(amount)
            return -1

    return exercises


energy = 6
amount = [2,3,5]

print(minEx(energy,amount))