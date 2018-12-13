from City_JSON_Obj import City_JSON_Obj
import csv

def Sort_City_Id(cities=None):
    if cities==None:
        City_List=sorted(City_JSON_Obj(),key=lambda x:x['id'])
        return(City_List)
    else:
        City_List = sorted(City_JSON_Obj(cities), key=lambda x: x['id'])
        return (City_List)

#print(Sort_City_Id(['bekasi','jakarta']))
#print(type(Sort_City_Id())) # type : LIST
#for row in Sort_City_Id():
#    print(type(row))

def data_to_csv():
    berkas = open('test.csv','w')
    for row in (Sort_City_Id()):
        berkas.writelines([str(row)])
        berkas.write(',')
    berkas.close()

#data_to_csv()