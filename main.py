#parse month should take in the text of the month and return the number 
#as a string
#January -> 1 (as a string)
'''
Parsing Dates Lab:  
You may work with others on this lab.  

Write a program that reads a date as January 18, 2024 and outputs the date formatted as MM/DD/YYYY (01/18/2024). Fix the provided functions to produce this output.

Notes:
- Continue reading dates until -1 is entered.
- Assume the dates entered are correctly formatted.

Example:  
Input  
March 1, 1990  
April 2, 1995  
December 13, 2003  
-1

Output  
03/01/1990  
04/02/1995  
12/13/2003
yay
'''
#YOU MAY USE THIS FUNCTION IF YOU WANT TO OR YOU MAY REMOVE IT
def parse_month(month):
    months = ['Gen', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    a = str(months.index(month))
    if int(a) < 10:
        a = '0' + a

    return a

#REMOVE PASS AND FIX THIS FUNCTION
#parse_date function should return the date formated as MM/DD/YYYY
#DO NOT REMOVE THIS FUNCTION
def parse_date(user_string):
    
    dates = user_string.split()
    month = parse_month(dates[0])
    if dates[1][-1] == ',':
        dAy = dates[1][:-1]
    else:
        dAy = dates[1]
    
    if int(dAy) < 10:
        day = "0" + dAy
    else:
        day = dAy
    year = dates[2]

    date = month + "/" + day + "/" + year
    
    return date


#REMOVE PASS AND YOUR CODE GOES HERE
if __name__ == '__main__':
    
    imp = input()
    imps = []
    while imp != "-1":
        print(imp + ', ' + (imp == -1))
        imps.append(imp)
        imp = input()

    print(parse_date(imps))


