def visualize(sortedlist, table):
    from PIL import Image, ImageFont, ImageDraw
    boximg = Image.open('.\\icons\\boxicon.png')
    arrowimg = Image.open('.\\icons\\arrowicon.png')
    size = 100, 100
    width = 6000 #defauit
    height = 14000 #default
    columnumber = 0
    rownumber = 0


    width = 100*table.__len__()
    layout = Image.new('RGBA', (width, height), color ='white')

    tbl = table.values.tolist()
    
    for row in tbl:
        for bin in row:
            if str(bin) == "nan":
                continue
            img = boximg.copy()         
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype(".\\fonts\\bahnschrift.ttf", 16)
            draw.text((19,80),str(bin),(10,10,10), font = font)
            layout.paste(img,(size[0]*rownumber,size[1]*columnumber))
            columnumber = columnumber + 1
        columnumber = 0
        rownumber += 1

    table = table.transpose()
    arrowcoordinates = []

    X = 0
    Y = 0

    for bin in sortedlist:
        
        tmp = table.where(table==bin[0]).dropna(how='all').dropna(axis=1)
        if tmp.__len__()>0:
            X = tmp.index[0]
        Y = table.columns.get_loc(tmp.columns[0])

        arrowcoordinates.append((X,Y))

    for coordinate in arrowcoordinates:
        img = arrowimg.copy()

        newX = int(coordinate[0])
        newY = int(coordinate[1])

        if newX>X and newY>Y:
            img = img.rotate(-45, resample=Image.BICUBIC)
            layout.paste(img, (newY*100 + 40,newX*100), mask = img)
        elif newX>X and newY<Y:
            img = img.rotate(-135,resample=Image.BICUBIC)
            layout.paste(img, (newY*100 + 75,newX*100 - 22), mask = img)
        elif newX==X and newY==Y:
            pass
        elif newX>X and newY==Y:
            img = img.rotate(-90)
            layout.paste(img, (newY*100 + 27,newX*100 - 19), mask = img)
        elif newX==X and newY>Y+1:
            pass
        elif newX==X and newY<Y:
            img = img.rotate(180)
            layout.paste(img, (newY*100 + 68,newX*100 + 25), mask = img)
        elif newX==X and newY>Y:
            layout.paste(img, (newY*100 - 18,newX*100 + 20), mask = img)
        elif newX<X and newY>Y:
            img = img.rotate(45,resample=Image.BICUBIC)
            layout.paste(img, (newY*100 - 25,newX*100 + 72), mask = img)        
        X = newX
        Y = newY

    layout.save('layout.png')