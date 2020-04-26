



def person(name,**data):
    print(name)
    print(data)



#person("umang",20,"mumbai",255556)


person(name="umang",age=20,city="mumbai",phone_no=255556)


def per(name,**data):
    print(name)

    for i,j in data:
        
        print(i,j)



#person("umang",20,"mumbai",255556)


per(name="umang",age=20,city="mumbai",phone_no=255556)
