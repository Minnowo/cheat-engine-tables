

def get_fingerprint(aob):
    
    if len(aob) < 2:
        raise "The fingerprint aob list must have 2 or more items"

    out = ""
    for i in range(len(aob[0])):

        flag = False

        for k in aob[1:]:

            if k[i] == aob[0][i]:
                continue

            flag = True
            break

        if flag:
            out += "?"
        else:
            out += aob[0][i]

    while out.startswith("??") or out.startswith(" "):
        out = out.lstrip("??")
        out = out.lstrip(" ")

    while out.endswith("??") or out.endswith(" "):
        out = out.rstrip("??")
        out = out.rstrip(" ")
    print(out)
    print("byte count: " + str(hex(int(len(out.replace(" ",""))/2))))
