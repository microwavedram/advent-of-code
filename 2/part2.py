# x=rock y=paper z=scissors
beats = {"X":"Z","Y":"X","Z":"Y"}
loses = {"Z":"X","X":"Y","Y":"Z"}
scores = {"X":1,"Y":2,"Z":3}

score = 0
with open("input.txt") as f:
    for strat in f.read().split("\n"):
        strat = strat.replace("A","X")
        strat = strat.replace("B","Y")
        strat = strat.replace("C","Z")

        split = strat.split(" ")

        if split[1] == "X":
            m = beats[split[0]]
        elif split[1] == "Y":
            m = split[0]
        elif split[1] == "Z":
            m = loses[split[0]]



        win = beats[m] == split[0]
        lose = beats[split[0]] == m
        draw = m == split[0]
        
        rscore = scores[m]
        if win == True:
            rscore += 6
        elif draw == True:
            rscore += 3

        print(split,win,lose,draw,rscore)
        score += rscore
    
print(score)
