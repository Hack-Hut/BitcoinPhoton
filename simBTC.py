def blocksize_increase_per_year(blocksize, blockintervel):
    #returns the blocksize increase of a year in MB
    #result = int(blocksize * (525600/blockintervel)/1000)
    result = int(blocksize * (525600/(blockintervel/60))/1000)
    return(result)

def bandwidth_useage(blocksize, blockintervel):
    #returns the network bandwidth requirements based on the blocksize and blockinterval
    result = float((blocksize*1000)/(blockintervel))
    return(result)

def transactions_per_sec(blocksize, blockintervel):
    #returns the transaction per second given the set peramiterization
    result = float(((blocksize*1000000)/250)*(1/(blockintervel)))
    return(result)


## populating test permameters into a list
blocksize = []
block_interval = []

for x in range(0, 9):
    blocksize.append(x)

for i in range(0, 11):
    block_interval.append(i * 60)


print("blocksize  |  block interval  |   blocksize increase over a year  |   bandwidth  |  throughput")
print(200*"-")
## calculates the results of changing the blocksize
for sizes in blocksize :
    if sizes == 0:
        continue
    x = blocksize_increase_per_year(blocksize[sizes], 600)
    y = bandwidth_useage(blocksize[sizes], 600)
    z = transactions_per_sec(blocksize[sizes], 600)


    string = "{} Mb     |      600sec           |       {} Gb y                    |    {} Kbps   |   {} Tps"
    #print(string.format(sizes, x, round(y, 1), round(z, 1)))
    print(round(z,1))

## calculates the results of changing the block interval
for blockinterval in range(0, 610):
    try:
        x = blocksize_increase_per_year(1, block_interval[blockinterval])
        y = bandwidth_useage(1, block_interval[blockinterval])
        z = transactions_per_sec(1, block_interval[blockinterval])
    except:
        continue
    string = "1 Mb     |      {}sec           |       {} Gb y                    |    {} Kbps   |   {} Tps"
    #print(string.format(blockinterval*60, x, round(y, 1), round(z, 1)))
    #outputs the results
    print(round(z,1))
