import pandas as pd
df = pd.read_csv("/data/training/studentlist.csv")
df.drop("studentEmail",axis=1,inplace=True)
df2 = pd.read_csv("/data/training/quiz/quiz1.csv")
df3 = pd.read_csv("/data/training/quiz/quiz2.csv")
df2.index.name = "index"
df2.rename(columns={"Firstname":"studentName"},inplace=True)
df3.rename(columns={"Firstname":"studentName"},inplace=True)
quiz1 = []
quiz2 = []
for i in range(1,20):
    df1 = pd.read_csv("/data/training/batchwiselist/"+str(i)+".csv")
    result1 = pd.merge(df1,df2,on="studentName",how = 'inner')
    result2 = pd.merge(df1,df3,on="studentName",how = 'inner')
    quiz1.append(result1)
    quiz2.append(result2)

for i in quiz1:
    i["Grade/10.00"] = pd.to_numeric(i["Grade/10.00"],errors='coerce')
for j in quiz2:
    j["Grade/10.00"] = pd.to_numeric(j["Grade/10.00"],errors='coerce')
lessthan50 = []
btw50and60 = []
btw60and70 = []
btw70and80 = []
greatthan80 = []
a = 0
b = 0
c = 0
d = 0
e = 0
for i in quiz1:
    for k in i["Grade/10.00"]:
        if k<5:
            a = a+1
        elif k>=5 and k<6:
            b = b+1
        elif k>=6 and k<7:
            c= c+1
        elif k>=7 and k<8:
            d = d+1
        elif k >= 8 and k<=10:
            e = e+1
        else:
            break
    lessthan50.append(a)
    btw50and60.append(b)
    btw60and70.append(c)
    btw70and80.append(d)
    greatthan80.append(e)
a = 0
b = 0
c = 0
d = 0
e = 0
for j in quiz2:
    for k in j["Grade/10.00"]:
        if k<5:
            a = a+1
        elif k>=5 and k<6:
            b = b+1
        elif k>=6 and k<7:
            c= c+1
        elif k>=7 and k<8:
            d = d+1
        elif k >= 8 and k<=10:
            e = e+1
        else:
            break
    lessthan50.append(a)
    btw50and60.append(b)
    btw60and70.append(c)
    btw70and80.append(d)
    greatthan80.append(e)
stats = ["noofpresent", "lessthan50", "between50and60", "between60and70", "between70and80", "greaterthan80"]
stat = pd.DataFrame(columns=stats)
f = open("/data/training/testcaseStudent.txt","r")
m = int(f.readline())
df2["Grade/10.00"] = pd.to_numeric(df2["Grade/10.00"],errors='coerce')
df3["Grade/10.00"] = pd.to_numeric(df3["Grade/10.00"],errors='coerce')
for i in range(m):
    a = 0
    b = 0
    file = f.readline()
    value = f.readline()
    data = pd.read_csv("/data/training/batchwiselist/"+file[:-1])
    result1 = pd.merge(data,df2,on="studentName")
    result2 = pd.merge(data,df3,on="studentName")
    if value[:-1] == "lessthan50":
        for j in result1["Grade/10.00"]:
            if j < 5:
                a = a+1
        for t in result2["Grade/10.00"]:
            if t < 5:
                b = b+1
    elif value[:-1] == "between50and60":
        for j in result1["Grade/10.00"]:
            if j >= 5 and j < 6:
                a = a+1
        for t in result2["Grade/10.00"]:
            if t >= 5 and t < 6:
                b = b+1
    elif value[:-1] == "between60and70":
        for j in result1["Grade/10.00"]:
            if j >= 6 and j < 7:
                a = a+1
        for t in result2["Grade/10.00"]:
            if t >= 6 and t < 7:
                b = b+1
    elif value[:-1] == "between70and80":
        for j in result1["Grade/10.00"]:
            if j >= 7 and j < 8:
                a = a+1
        for t in result2["Grade/10.00"]:
            if t >= 7 and t < 8:
                b = b+1            
    elif value[:-1] == "greaterthan80":
        for j in result1["Grade/10.00"]:
            if j >= 8:
                a = a+1
        for t in result2["Grade/10.00"]:
            if t >= 8:
                b = b+1
    else:
        a = result1["admissionNumber"].count()
        b = result2["admissionNumber"].count()
    fileout = open("/code/output"+str(i+1)+".txt","w")
    fileout.write(str(a)+"\n")
    fileout.write(str(b))
    fileout.close()
