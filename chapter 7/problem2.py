l = ["tanu", "manu","jahnvi",'anu',"tanya"]

for name in l:
    if(name.startswith("t")):
        print(f"hello {name}")

    if name in l:
        if(name.endswith("u")):
            print(f"bye {name}")    