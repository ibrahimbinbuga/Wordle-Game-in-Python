import sys
WoD=sys.argv[1]
print("The length of word must be five!")
tries=["Try1:" ,"Try2:" ,"Try3:" ,"Try4:" ,"Try5:" ,"Try6:"]
suffixes=["1.","2.","3.","4.","5.","6."]
while True:
    for j in tries:
        x=input(j)
        if not len(x)==5:
            print("The length of word must be five!")
        if len(x)==5:
            for k in range(5):
                if WoD[k]==x[k]:
                    print(suffixes[k], "letter exists and located right position.")
                else:
                    if x[k] in WoD:
                        print(suffixes[k], "letter exists but located wrong position.")
                    if not x[k] in WoD:
                        print(suffixes[k], "letter does not exists.")
            if x==(WoD):
                s=tries.index(j)
                print("Congratulations!", "You guess right in", suffixes[s], "shot!")
                sys.exit()
    if j>"6":
        print("You are failed!")
        sys.exit()