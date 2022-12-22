import pandas as pd
df = pd.read_csv("req.csv", header=None)
#print(df)
newstr = '="'
#dff= pd.DataFrame()
#print(newstr)
for i in df[0]:
    i=i.replace("==", newstr)
    i = i + '"'
    print(i)
    #dff.append(i)
#print(df)
#df.to_csv("reqto.csv")