employees=[{"id":1,"first_name":"Man","gender":"Genderqueer"},
{"id":2,"first_name":"Kathlin","gender":"Female"},
{"id":3,"first_name":"Jule","gender":"Male"},
{"id":4,"first_name":"Palm","gender":"Male"},
{"id":5,"first_name":"Rosamund","gender":"Bigender"},
{"id":6,"first_name":"Muriel","gender":"Female"},
{"id":7,"first_name":"Rosemary","gender":"Female"},
{"id":8,"first_name":"Scarlett","gender":"Female"},
{"id":9,"first_name":"Chuck","gender":"Male"},
{"id":10,"first_name":"Jeanne","gender":"Female"},
{"id":11,"first_name":"Xenos","gender":"Male"},
{"id":12,"first_name":"Alfonso","gender":"Male"},
{"id":13,"first_name":"Misti","gender":"Female"},
{"id":14,"first_name":"Diana","gender":"Female"},
{"id":15,"first_name":"Tabina","gender":"Female"},
{"id":16,"first_name":"Chuck","gender":"Male"},
{"id":17,"first_name":"Lynn","gender":"Female"},
{"id":18,"first_name":"Noak","gender":"Male"},
{"id":19,"first_name":"Dick","gender":"Male"},
{"id":20,"first_name":"Carolann","gender":"Female"},
{"id":21,"first_name":"Karlie","gender":"Female"},
{"id":22,"first_name":"Dolly","gender":"Female"},
{"id":23,"first_name":"Darsey","gender":"Female"},
{"id":24,"first_name":"Javier","gender":"Male"},
{"id":25,"first_name":"Sukey","gender":"Polygender"},
{"id":26,"first_name":"Shirley","gender":"Bigender"},
{"id":27,"first_name":"Kristel","gender":"Female"},
{"id":28,"first_name":"Cam","gender":"Polygender"},
{"id":29,"first_name":"Bartolemo","gender":"Male"},
{"id":30,"first_name":"Culver","gender":"Male"},
{"id":31,"first_name":"Thaddus","gender":"Male"},
{"id":32,"first_name":"Bibi","gender":"Genderfluid"},
{"id":33,"first_name":"Brien","gender":"Male"},
{"id":34,"first_name":"Cullin","gender":"Male"},
{"id":35,"first_name":"Pearline","gender":"Female"},
{"id":36,"first_name":"Darryl","gender":"Female"},
{"id":37,"first_name":"Jeremy","gender":"Male"},
{"id":38,"first_name":"Adham","gender":"Male"},
{"id":39,"first_name":"Walliw","gender":"Female"},
{"id":40,"first_name":"Malissia","gender":"Female"},
{"id":41,"first_name":"Tessa","gender":"Agender"},
{"id":42,"first_name":"Jermayne","gender":"Male"},
{"id":43,"first_name":"Josias","gender":"Male"},
{"id":44,"first_name":"Ferdie","gender":"Male"},
{"id":45,"first_name":"Arch","gender":"Male"},
{"id":46,"first_name":"Teodoor","gender":"Male"},
{"id":47,"first_name":"Skipp","gender":"Agender"},
{"id":48,"first_name":"Jandy","gender":"Female"},
{"id":49,"first_name":"Hurleigh","gender":"Male"},
{"id":50,"first_name":"Craggie","gender":"Male"},
{"id":51,"first_name":"Stesha","gender":"Polygender"},
{"id":52,"first_name":"Winslow","gender":"Male"},
{"id":53,"first_name":"Jay","gender":"Male"},
{"id":54,"first_name":"Delmer","gender":"Male"},
{"id":55,"first_name":"Marsiella","gender":"Polygender"},
{"id":56,"first_name":"Sheff","gender":"Male"},
{"id":57,"first_name":"Luciano","gender":"Male"},
{"id":58,"first_name":"Horatio","gender":"Male"},
{"id":59,"first_name":"Sheeree","gender":"Female"},
{"id":60,"first_name":"Gerta","gender":"Non-binary"},
{"id":61,"first_name":"Ag","gender":"Female"},
{"id":62,"first_name":"Lil","gender":"Female"},
{"id":63,"first_name":"Oliver","gender":"Male"},
{"id":64,"first_name":"Samuel","gender":"Male"},
{"id":65,"first_name":"Rick","gender":"Male"},
{"id":66,"first_name":"Margareta","gender":"Female"},
{"id":67,"first_name":"Berton","gender":"Genderfluid"},
{"id":68,"first_name":"Teirtza","gender":"Female"},
{"id":69,"first_name":"Bertram","gender":"Male"},
{"id":70,"first_name":"Rolf","gender":"Male"},
{"id":71,"first_name":"Isiahi","gender":"Male"},
{"id":72,"first_name":"Nichole","gender":"Female"},
{"id":73,"first_name":"Horatio","gender":"Male"},
{"id":74,"first_name":"Minne","gender":"Bigender"},
{"id":75,"first_name":"Baudoin","gender":"Male"},
{"id":76,"first_name":"Garv","gender":"Male"},
{"id":77,"first_name":"Leodora","gender":"Genderqueer"},
{"id":78,"first_name":"Cameron","gender":"Male"},
{"id":79,"first_name":"Shalna","gender":"Female"},
{"id":80,"first_name":"Britteny","gender":"Female"},
{"id":81,"first_name":"Luise","gender":"Female"},
{"id":82,"first_name":"Dulsea","gender":"Female"},
{"id":83,"first_name":"Paola","gender":"Female"},
{"id":84,"first_name":"Shaw","gender":"Male"},
{"id":85,"first_name":"Mahmud","gender":"Agender"},
{"id":86,"first_name":"Randell","gender":"Male"},
{"id":87,"first_name":"Leonid","gender":"Male"},
{"id":88,"first_name":"Jada","gender":"Female"},
{"id":89,"first_name":"Zacherie","gender":"Male"},
{"id":90,"first_name":"Marlo","gender":"Male"},
{"id":91,"first_name":"Karlan","gender":"Male"},
{"id":92,"first_name":"Leila","gender":"Female"},
{"id":93,"first_name":"Melisande","gender":"Female"},
{"id":94,"first_name":"Carmelina","gender":"Female"},
{"id":95,"first_name":"Mechelle","gender":"Female"},
{"id":96,"first_name":"Brittaney","gender":"Non-binary"},
{"id":97,"first_name":"Elora","gender":"Female"},
{"id":98,"first_name":"Thatch","gender":"Male"},
{"id":99,"first_name":"Darn","gender":"Male"},
{"id":100,"first_name":"Arturo","gender":"Male"}]

""""
for num in employees:
    print(num["first_name"])

    for num in employees:
        if num["gender"]=="Male":
            print(num["first_name"])
            
    for num in employees:
        if num["gender"]=="Female":
            print(num["first_name"])
    count=0
    for num in employees:
        if num["gender"]=="Female":
            count=count+1
    print(count)    
i=0
while i<=len(employees)-1:  
    print(employees[i]["first_name"])
    i=i+1;

i=0
while i<=len(employees)-1:  
    if employees[i]["gender"]=="Female":
     print(employees[i]["first_name"])
    i=i+1;"""
i=0
while i<=len(employees)-1:  
    if employees[i]["gender"]=="Male":
     print(employees[i]["first_name"])
    i=i+1;
"""i=0
j=0
while i<=len(employees)-1:  
    if employees[i]["gender"]=="Male":
     j=j+1
    i=i+1
print(j)"""
# i=0
# j=0
# while i<=len(employees)-1:  
#     if employees[i]["gender"]=="Female":
#      j=j+1
#     i=i+1
# print(j)