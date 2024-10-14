'''
    WAP to convert integers into numbers
        suppose, the user input num = 673, then the output should
            be like :- six hundred seventy 3 .......and so on .
                the input should be of 5 digits(maximum)
                    and minimum as much you want.  :))
'''
num = input("Enter a number : ")
dig = {1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE"}
ten = {0:"TEN",1:"ELEVEN",2:"TWELVE",3:"THIRTEEN",4:"FOURTEEN",5:"FIFTEEN",6:"SIXTEEN",7:"SEVENTEEN",8:"EIGHTEEN",9:"NINETEEN"}
tt = {2:"TWENTY",3:"THIRTY",4:"FOURTY",5:"FIFTY",6:"SIXTY",7:"SEVENTY",8:"EIGHTY",9:"NINTY"}

d = 0
for i in range(len(num),0,-1):
    dg = int(num[d])
    if i == 5:
        print(tt[dg], end = ' ')
    if i == 4:
        print(dig[dg]+ " THOUSAND", end = ' ')
    elif i == 3:
        print(dig[dg]+ " HUNDRED", end = ' ')
    elif i == 2:
        if dg > 1:
            print(tt[dg] + " " + dig[int(num[d+1])])
        elif dg == 1:
            print(ten[int(num[d+1])])
        else:
            print(ten[int(num[d+1])])
    d += 1
