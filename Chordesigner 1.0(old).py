print("Chordesigner 1.0--create simple chords")
count=0
notn=0
while True:
    count=count + 1
    print("chord #",count)
    rootnote=input("input root note(C D E F G A B")
    if rootnote == "C":
        chdb = "C E G"
        num=3
    elif rootnote == "D":
        chdb = "D F A"
        num=4
    elif rootnote == "E":
        chdb = "E G B"
        num=5
    elif rootnote == "F":
        chdb = "F A C"
        num=6
    elif rootnote == "G":
        chdb = "G B D"
        num=7
    elif rootnote =="A":
        chdb = "A C E"
        num=1
    elif rootnote == "B":
        chdb = "B D F"
        num=2
    else:
        print("error")
        
    addnota=input("addition note(7th,9th,3up,3down,skip")
    if addnota=="7th":
        if num == 1:
            notn=7
        else:
            notn=num-1
    elif addnota=="9th":
        if num == 7:
            notn=1
        else:
            notn=num+1
    elif addnota=="3up":
        anote = rootnote
        print("Chord #",count,": ",chdb," ",anote,"5")       
    elif addnota=="3down":
        anote = rootnote
        print("Chord #",count,": ",chdb," ",anote,"3")    
    else:
        print("Chord #",count,": ",chdb)
    if notn == 1:
        lasadd="A"
    elif notn == 2:
        lasadd="B"
    elif notn == 3:
        lasadd="C"
    elif notn == 4:
        lasadd="D"
    elif notn == 5:
        lasadd="E"
    elif notn == 6:
        lasadd="F"
    else:
        lasadd="G"
    if addnota == "7th":
        print("Chord #",count,": ",chdb," ",lasadd)
    elif addnota == "9th":
        print("Chord #",count,": ",chdb," ",lasadd)
