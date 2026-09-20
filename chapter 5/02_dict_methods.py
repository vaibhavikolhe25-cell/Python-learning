m = {
    "tanuuu": 200,
    "soham": 100,
    "bugya":50,
    50 :"bugya"
}
print(m.items())
print(m.keys())
print(m.values())
m.update({"bugya":100,"didi":50})
print(m)
print(m.get("didi2"))#output none
# print(m["didi2"]) returns an error