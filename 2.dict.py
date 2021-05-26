dict={"1":50,"2":60,"3":70}
def maxvalue(dict):
    m=max(dict,key=dict.get)
    k=dict[m]
    print(m,":",k)
maxvalue(dict)
