#Task 1 Elmira Orujova SE-2008
def recursive_perm(str, start, end):
    if start == end:
        print("'"+"".join(str) + "'")  #outputs the result of permutation
        
    else:
        for i in range(start, end + 1):
            str[start], str[i] = str[i], str[start]  #swapping 
            recursive_perm(str, start + 1, end)
            str[i], str[start] = str[start], str[i] # swapping back

input = input("enter your input: ")
recursive_perm(list(input), 0, len(input)-1) #calling the function