import string , os
if not os.path.exists("letters") :
    os.makedirs("letters")

for ff in string.ascii_uppercase:
    with open(ff + ".txt", "w") as f:
        f.writelines(ff)
