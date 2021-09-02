# import datetime

# d1 = datetime.datetime(2018, 5, 3)
# d2 = datetime.datetime(2018, 6, 1)

# print(d1>d2)
# print(d1<d2)
# print(d1!=d2)

'''-------------------------------------'''

# str1 = "10-02-2019"
# str2 = "12-03-2022"

# l1 = str1.split("-")
# l2 = str2.split("-")

'''------------------------------------------'''

# d1 = "20170101"
# d2 = "20170102"

# print(d2>d1)
# print(d2<d1)
# print(d2==d1)

'''----------------------------------------------'''

# def compare(date1, date2):
#     date1_parts = date1.split('/')
#     d1, m1, y1 = int(date1_parts[0]), int(date1_parts[1]), int(date1_parts[2])

#     date2_parts = date2.split('/')
#     d2, m2, y2 = int(date2_parts[0]), int(date2_parts[1]), int(date2_parts[2])

#     return (y1, m1, d1) > (y2, m2, d2)

# compare("25/01/2017","12/12/2017")

'''-----------------------------------------------------------'''

def compare(dateOne, dateTwo):
    #Break up the date into its components
    day = int(dateOne[0:2])
    month = int(dateOne[3:5])
    year = int(dateOne[6:10])

    dayTwo = int(dateTwo[0:2])
    monthTwo = int(dateTwo[3:5])
    yearTwo = int(dateTwo[6:10])

    #Compare the years first
    if(year > yearTwo):
        return True
    elif(year < yearTwo):
        return False
    else:
        #If the years are equal, then compare the months
        if(month > monthTwo):
            return True
        elif(month < monthTwo):
            return False
        else:
            #If the days are equal, return False since it's strictly greater, else, return the appropriate value. 
            if(day > dayTwo):
                return True
            else:
                return False

compare("25/01/2017","12/12/2017")

