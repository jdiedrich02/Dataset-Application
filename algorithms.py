def parseTxt(file):
    data = {'x': [], 'y': []}
    with open(file) as f:
        for line in f:
            line = line.rstrip().split()
            data['x'].append(line[0])
            data['y'].append(line[1])

    return data
    

def parseCSV(file):
    print('Running the algorithm for CSV and returning the data in a proper format')

def parseExcel(file):
    print('Running the algorithm for Excel and returning the data in a proper format')