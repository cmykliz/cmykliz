import math
#Figure out unrounded signatures (/16)
#If decimal is >0.3 then round down with no blanks
#If decimal is <0.3 then round up with blanks
#Calculate blanks
#Give warning if more than 6 blank pages

#Input from user on current page count
page_count = int (input("Current page count: "))
signatures = 0

#calculate extent
def extent (page_count):
    return signatures*16

#calculate blanks
def blanks (signatures, unroundedSig):
    remainder = signatures-unroundedSig
    return int(remainder*16)

#If already a multiple of 16 then yay
if page_count % 16 == 0:
        print (f"Yay, your extent is {page_count}pp exactly!")

else:
    unroundedSig = float (page_count/16)
    roundability = math.trunc(unroundedSig)
    decimals = unroundedSig-roundability
    if decimals <=0.3:
        signatures = math.floor(unroundedSig)
        print (f"Ugh. You need to track back to {extent(page_count)}pp.")
    else:
        signatures = math.ceil(unroundedSig)
        print (f"The extent is {extent (page_count)}pp with {blanks (signatures, unroundedSig)} blank pages.")
    

