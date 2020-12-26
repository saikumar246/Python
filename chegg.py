'''
data.txt:
Report Date,FIPS,Locality,VDH Health District,TotalCases,Hospitalizations,Deaths
03/17/2020,51001,Accomack,Eastern Shore,0,0,0
03/17/2020,51003,Albemarle,Thomas Jefferson,0,0,0
03/17/2020,51011,Appomattox,Central Virginia,0,0,0
03/17/2020,51013,Arlington,Arlington,13,1,0
03/17/2020,51015,Augusta,Central Shenandoah,0,0,0
03/17/2020,51017,Bath,Central Shenandoah,0,0,0
03/17/2020,51019,Bedford,Central Virginia,0,0,0
03/17/2020,51021,Bland,Mount Rogers,0,0,0

OUTPUT:
Enter the cityAccomack
Report Date  :  03/17/2020

FIPS  :  51001

Locality  :  Accomack

VDH Health District  :  Eastern Shore

TotalCases  :  0

Hospitalizations  :  0

Deaths  :  0
'''
list=[]
def main():
    city=str(input("Enter the city"))
    fp=open("data.txt","r")
    list=fp.readlines()
    for i in range(len(list)):
        list[i] = list[i].split(",")
    fp.close()
    for i in range(len(list)):
        if list[i][2]==city:
            t=list[0][6]
            list[0][6]=t[:-1]
            h=list[0]
            d=list[i]
    res=dict(zip(h,d))
    for x in res:
        print(x," : ",res[x],"\n")

if __name__=="__main__":
    main()