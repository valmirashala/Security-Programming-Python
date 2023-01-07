import pickle
x=open("","rb")
y=pickle.load(x)
print(y)
x.close()