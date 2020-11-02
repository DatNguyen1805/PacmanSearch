 # Extracts the amount of whitespace regions in the number.
    def getRegions(features):
        regions = []

        # Loop every pixel in the image
        for x in range(DIGIT_DATUM_WIDTH):
            for y in range(DIGIT_DATUM_HEIGHT):
                # Get information about the pixel
                pixel = (x, y)
                value = features[pixel]

                # If the pixel is white, it can be processed
                if value == 0:
                    # Get all neighboring pixels
                    topPixel = (x, y - 1)
                    rightPixel = (x + 1, y)
                    bottomPixel = (x, y + 1)
                    leftPixel = (x - 1, y)

                    # Keep track of whether the current pixel was added to a region
                    added = False
                    for region in regions:
                        # Check if a neighboring pixel is part of a region
                        if topPixel in region or rightPixel in region or bottomPixel in region or leftPixel in region:
                            # If so, this pixel must logically be part of the same region so add it
                            region.append(pixel)
                            added = True
                    
                    # Check if the pixel wasn't added to an existing region
                    if not added:
                        # If so, the pixel will be part of a new region
                        regions.append([pixel])

        # Add the actual feature
        for i in range(1, 3):
            # The feature has a weight of 6
            for w in range(1, 6):
                features[(w, "regions", i)] = len(regions) == i

    # Extracts the way pixels are divided over the image.
    def getDivision(features):
        # Keep track of the amount of black pixels per region
        leftBlacks = 0
        rightBlacks = 0
        topBlacks = 0
        bottomBlacks = 0

        # Loop all pixels in the image
        for x in range(DIGIT_DATUM_WIDTH):
            for y in range(DIGIT_DATUM_HEIGHT):
                # Check if the current pixel is black
                if features[(x, y)] == 1:
                    # Check if it is part of the left half
                    if(x < DIGIT_DATUM_WIDTH / 2):
                        leftBlacks += 1
                    else:
                        rightBlacks += 1

                    # Check if it is part of the top half
                    if(y < DIGIT_DATUM_WIDTH / 2):
                        topBlacks += 1
                    else:
                        bottomBlacks += 1
        
        # 0 = left side has more pixels
        # 1 = right side has more pixels
        # The feature has a weight of 2
        for w in range(1, 2):
            features[(w, "horizontalDivision")] = topBlacks > bottomBlacks

        # 0 = top side has more pixels
        # 1 = bottom side has more pixels
        # The feature has a weight of 2
        for w in range(1, 2):
            features[(w, "verticalDivision")] = leftBlacks > rightBlacks

    # Retrieves the relation between pixels in using the values in the features.
    def getPixelRelations(features, datum):
        # Loop all pixels in the image
        for x in range(DIGIT_DATUM_WIDTH):
            for y in range(DIGIT_DATUM_HEIGHT):
                # Add the actual features, where the value is the relation between the current pixel and the one preceding it
                features[("horizontalPixelRelations", (x, y))] = features[(x, y)] > features[(x - 1, y)]
                features[("verticalPixelRelations", (x, y))] = features[(x, y)] > features[(x, y - 1)]

    # Retrieves the relation between pixels in using the values in the datum.
    def getPixelRelations2(features):
        # Loop all pixels in the image
        for x in range(DIGIT_DATUM_WIDTH):
            for y in range(DIGIT_DATUM_HEIGHT):
                # Add the actual features, where the value is the relation between the current pixel and the one preceding it
                features[("horizontalPixelRelations2", (x, y))] = datum.getPixel(x, y) > datum.getPixel(x - 1, y)
                features[("verticalPixelRelations2", (x, y))] = datum.getPixel(x, y) > datum.getPixel(x, y - 1)

    # Apply mutations to the features variable
    ##getRegions(features)
    ##getDivision(features)
    getPixelRelations(features, datum)
    getPixelRelations2(features)
    
    return features

