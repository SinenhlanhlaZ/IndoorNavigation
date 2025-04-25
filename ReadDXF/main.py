def parse_dxf(file_path):
    # open file in read mode
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    i = 0
    entities = [] # store entities (lines, walls)

    # loop through lines in drawing
    while i<len(lines):
        line = lines[i].strip()

        if line == 'LINE':
            entity = {'type':'LINE'} # create dictionary to store line info

            #keep looping to extract all properties of LINE entity
            while True:
                i+=1
                if i >= len(lines): break #preventing index out of bounds

                code = lines[i].strip() # group code (10, 20, 11 etc.)
                i+=1
                value = lines[i].strip()

                # Map coordinates based on group codes
                if code == '10':
                    entity['x1'] = float(value) #start point x
                elif code == '20':
                    entity['y1'] = float(value) # start point y
                elif code == '11':
                    entity['x2'] = float(value) #end point x
                elif code == '21':
                    entity['y2'] = float(value) #end point y
                elif code == '0':
                    # new entity begines, so we go back one step and break
                    i -= 1
                    break
            
            entities.append(entity) #store this LINE entity
        
        # Move to the next line
        i += 1

    return entities # return all LINE entities parsed

walls = parse_dxf('GroundFloor.dxf')

# print each wall (line) as a dictionary with coordinates
for wall in walls:
    print(wall)