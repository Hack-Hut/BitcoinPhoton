import requests, json, time

'''
This program calculates the current Bitcoin block every minute (plus the time taken to make the request) over a 12 hour period.
'''

def getBlock():
    results = list() ##where the results are stored
    for minutes in range(0, 720): ##queryies the bitcoin network ever minute for 12 hours to see if a new block has been propegated
        try:
            current_blockcount = requests.get("https://blockexplorer.com/api/status?q=getBlockCount")
            # gets current blockcount for bitcoin network
            block_json = json.loads(current_blockcount.text)
            # converts to JSON
        except ValueError:
            print("Json value error")
        current_block = str(block_json['blockcount'])
        print("Current block:" + current_block + " Current time:" + str(minutes))
        time.sleep(60)
        if minutes == 0:
            starting_block = str(block_json['blockcount'])

        if current_block == previous_block:
            results.append(str(0))
        if current_block == (int(previous_block) + 1):
            results.append(str(1))
        if current_block == (int(previous_block) + 2):
            results.append(str(2))

        previous_block = current_block

    fin_block = str(block_json['blockcount'])
    block_elasped = int(fin_block) - int(starting_block)

    # output results
    print("starting_block: " + str(starting_block))
    print("finishing_block: " + str(fin_block))
    print("Time_elaspased: 12 hours/720 mins")
    print("blocks_elasped: " + str(block_elasped))
    print("expected_number_of_blocks: 72")

    print(*results, sep=",")


getBlock()

