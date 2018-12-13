import City_Weather,json

def City_JSON_Obj(cities=None):
    INDONESIA_20 = []
    if cities==None:
        for object in City_Weather.get_city_based_on_name_value(cities):
            read = (json.loads(object))
            INDONESIA_20.append(read)
        return (INDONESIA_20)

    else:
        for object in City_Weather.get_city_based_on_name_value(cities):
            read = (json.loads(object))
            INDONESIA_20.append(read)
        return (INDONESIA_20)

#print(City_JSON_Obj(['bekasi','jakarta']))