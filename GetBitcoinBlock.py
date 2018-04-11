with open('old.txt', 'r') as f:
    lines = f.readlines()
    previous_block = '507101'
    num_of_ones = 0
    num_of_zeros = 0
    total_line = 0
    results = []
    loop = 5
    for line in lines:
        line.strip('\n')
        if previous_block == line:
            num_of_zeros += 1
            results.append('0')
        else:
            num_of_ones += 1
            results.append('1')
        previous_block=line
        total_line += 1

    print("There are " + str(total_line) + " lines")
    print("Estimated number of block for 10 min interval: " + str(total_line/10))
    print("Actual number of blocks: " + str(num_of_ones))

    cumulative = 0
    cum = []
    for x in range(0, len(results)):
        if results[x] == '0':
            pass
            #print(cumulative)
        elif results[x] == '1':
            cumulative += 1
            # print(cumulative)
        else:
            print('error')

        cum.append(cumulative)

    n = 0
    temp = 0
    number_of_blocks_in_10_mins = [0,0,0,0,0]
    for y in range(0, len(cum)):
        n = n + 1
        temp = temp + (cum[y] - cum[y-1])
        #print(temp)
        if n % 10 == 0:
            print(temp)
            if temp >= 0:
                number_of_blocks_in_10_mins[temp] = number_of_blocks_in_10_mins[temp] + 1
            temp = 0
    print(number_of_blocks_in_10_mins)