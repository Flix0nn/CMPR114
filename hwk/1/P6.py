def calculatepackages():
    hdperpack = 10
    bunsperpack = 8
    attending = int(input("How many people are attending the cookout?: "))
    hdperperson = int(input("How many hotdogs per person?: "))

    totalhdneeded = attending * hdperperson
    packagesofhd = (totalhdneeded + hdperpack - 1) // hdperpack
    packagesofbuns = (totalhdneeded + bunsperpack - 1) // bunsperpack

    totalhd = packagesofhd * hdperpack
    totalbuns = packagesofbuns * bunsperpack

    hdleft = totalhd - totalhdneeded
    bunsleft = totalbuns - totalhdneeded

    print(f"The minimum amount of packges of hot dogs required: {packagesofhd}")
    print(f"The minimum amount of packages of buns required: {packagesofbuns}")
    print(f"Number of hot dogs leftover: {hdleft}")
    print(f"Number of buns leftover: {bunsleft}")

calculatepackages()