tot_mins=int(input())
if tot_mins>=100 and tot_mins<=550:
    h=tot_mins//60
    m=tot_mins%60
    print(h,"Hours and",m, "Minutes")