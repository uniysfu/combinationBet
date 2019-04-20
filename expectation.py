
def buildExpectations(teams, probabilities, ratios, bets):
    teamA = teams[0]
    teamB = teams[1]

    probabilityA = probabilities[0]
    pAwin = probabilityA[0]
    pAdraw = probabilityA[1]
    pAlose = probabilityA[2]

    probabilityB = probabilities[1]
    pBwin = probabilityB[0]
    pBdraw = probabilityB[1]
    pBlose = probabilityB[2]

    ratioA = ratios[0]
    rAwin = ratioA[0]
    rAdraw = ratioA[1]
    rAlose = ratioA[2]

    ratioB = ratios[1]
    rBwin = ratioB[0]
    rBdraw = ratioB[1]
    rBlose = ratioB[2]

    betA = bets[0]
    bAwin = betA[0]
    bAdraw = betA[1]
    bAlose = betA[2]

    betB = bets[1]
    bBwin = betB[0]
    bBdraw = betB[1]
    bBlose = betB[2]

    profitAwin = (rAwin - 1) * bAwin - bAdraw - bAlose
    profitAdraw = (rAdraw - 1) * bAdraw - bAwin - bAlose
    profitAlose = (rAlose - 1) * bAlose - bAwin - bAdraw

    profitBwin = (rBwin - 1) * bBwin - bBdraw - bBlose
    profitBdraw = (rBdraw - 1) * bBdraw - bBwin - bBlose
    profitBlose = (rBlose - 1) * bBlose - bBwin - bBdraw

    situationsA = ["win", "draw", "lose"]
    situationsB = ["win", "draw", "lose"]

    expectations = {}
    for sA in situationsA:
        if sA.lower() == "win":
            for sB in situationsB:
                if sB.lower() == "win":
                    margin = profitAwin * pAwin + profitBwin * pBwin
                    expectations[sA + '|' + sB] = margin
                if sB.lower() == "draw":
                    margin = profitAwin * pAwin + profitBdraw * pBdraw
                    expectations[sA + '|' + sB] = margin
                if sB.lower() == "lose":
                    margin = profitAwin * pAwin + profitBlose * pBlose
                    expectations[sA + '|' + sB] = margin

        elif sA.lower() == "draw":
            for sB in situationsB:
                if sB.lower() == "win":
                    margin = profitAdraw * pAdraw + profitBwin * pBwin
                    expectations[sA + '|' + sB] = margin
                if sB.lower() == "draw":
                    margin = profitAdraw * pAdraw + profitBdraw * pBdraw
                    expectations[sA + '|' + sB] = margin
                if sB.lower() == "lose":
                    margin = profitAdraw * pAdraw + profitBlose * pBlose
                    expectations[sA + '|' + sB] = margin

        elif sA.lower() == "lose":
            for sB in situationsB:
                if sB.lower() == "win":
                    margin = profitAlose * pAlose + profitBwin * pBwin
                    expectations[sA + '|' + sB] = margin
                if sB.lower() == "draw":
                    margin = profitAdraw * pAdraw + profitBdraw * pBdraw
                    expectations[sA + '|' + sB] = margin
                if sB.lower() == "lose":
                    margin = profitAlose * pAlose + profitBlose * pBlose
                    expectations[sA + '|' + sB] = margin
    return expectations

