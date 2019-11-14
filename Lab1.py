from TravellingSalesmanProblem import getCostOfRoute, readCSV 

'''
    Lab instructions:
        https://vle.aston.ac.uk/bbcswebdav/pid-1674349-dt-content-rid-10821790_1/xid-10821790_1
'''

def runTSP_1(routes, cityList) : 
    bestRoute = []
    bestCost = 100
    for route in routes :
        routeCost = getCostOfRoute(route, cityList)
        if (routeCost < bestCost) :
            bestCost = routeCost
            bestRoute = route
    print('best route - ', bestRoute, ' cost: ', bestCost)


def permuteRoutes(cityList) :
    return list(itertools.permutations(range(len(cityList))))

runTSP_1(permuteRoutes(cityList), readCSV())