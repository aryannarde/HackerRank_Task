if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Find the maximum score
    max_score = max(arr)
    
    # remove maximum score
    while max_score in arr:
        arr.remove(max_score)
    
    # Find runner up
    runner_up_score = max(arr)
    print(runner_up_score)