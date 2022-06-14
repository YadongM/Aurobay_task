# Coding for the Aurobay interview 
# Coding start 14-Jun-2022

def read_csv(filePath: str, column: bool = True) -> list[list[str]]:
    """Read csv file

    Args:
        filePath (str): Path of csv file.
        column_name (bool, optional): Determine whether the returned list contains headers.
                                      If Ture, the frist factor of sublist is heaer.

    Returns:
        list[list]: Secondary list, each sublist contains a column in the csv.
                    The factor of sublist is str.
    """
    
    with open(filePath) as csv_file:
        columnHeader = csv_file.readline().split(',')
        numColumn = len(columnHeader)

        data = [list() for _ in range(numColumn)]
        if column:
            # Add header to the list
            for idx in range(numColumn):
                data[idx].append(columnHeader[idx].replace('\n', ''))
                
        # Add contain to list
        for line in csv_file:
            line = line.split(',')
            for idx in range(numColumn):
                data[idx].append(line[idx].replace('\n', ''))
    
    return data

