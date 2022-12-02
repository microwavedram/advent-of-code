# x=rock y=paper z=scissors
beats = {"X":"Z","Y":"X","Z":"Y"}
scores = {"X":1,"Y":2,"Z":3}

score = 0
with open("input.txt") as f:
    for strat in f.read().split("\n"):
        strat = strat.replace("A","X")
        strat = strat.replace("B","Y")
        strat = strat.replace("C","Z")

        split = strat.split(" ")
        win = beats[split[0]] == split[1]
        lose = beats[split[1]] == split[0]
        draw = split[0] == split[1]
        
        rscore = scores[split[0]]
        if win == True:
            rscore += 6
        elif draw == True:
            rscore += 3

        print(split,win,lose,draw,rscore)
        score += rscore
    
print(score)
