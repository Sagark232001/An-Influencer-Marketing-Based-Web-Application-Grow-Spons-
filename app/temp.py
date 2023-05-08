d={"A":19,"B":2,"C":45,"D":23}
nd=dict(sorted(d.items(),key=lambda x:x[1], reverse=True))
print(nd)