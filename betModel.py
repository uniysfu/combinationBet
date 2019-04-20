
from expectation import *
from info import *
def getProbabilities( ratioA, ratioB):
    rAwin = ratioA[0]
    rAdraw = ratioA[1]
    rAlose = ratioA[2]
    sumA = rAwin + rAlose + rAdraw
    pAwin = rAlose/sumA
    pAdraw = rAdraw / sumA
    pAlose = rAwin / sumA
    probabilityA = [pAwin, pAdraw, pAlose]

    rBwin = ratioB[0]
    rBdraw = ratioB[1]
    rBlose = ratioB[2]
    sumB = rBwin + rBlose + rBdraw
    pBwin = rBlose / sumB
    pBdraw = rBdraw/ sumB
    pBlose = rBwin / sumB
    probabilityB = [pBwin, pBdraw, pBlose]

    probabilities = [probabilityA, probabilityB]
    return probabilities


def findMin(result):
    tempMin = 0;
    dic={}
    for key, value in result.items():
        if value <= tempMin:
            tempMin = value
            dic.clear()
            dic[key] = value

    return dic


if __name__ == '__main__':
    teamA = "Cardiff"
    teamB = "Arsenal"
    teams = [teamA, teamB]

    ratioA = [17, 7, 1.17]
    ratioB = [1.5, 4.33, 6.5]
    ratios = [ratioA, ratioB]

    probabilities = getProbabilities(ratioA, ratioB)

    temp = 0
    info = Info()
    for bAwin in range(0.1, 1.1, 0.1):
        for bAdraw in range(0.1, 1.1, 0.1):
            for bAlose in range(0.1, 1.1, 0.1):
                for bBwin in range(0.1, 1.1, 0.1):
                    for bBdraw in range(0.1, 1.1, 0.1):
                        for bBlose in range(0.1, 1.1, 0.1):
                            betA = [bAwin, bAdraw, bAlose]
                            betB = [bBwin, bBdraw, bBlose]
                            bets = [betA, betB]
                            result = buildExpectations(teams, probabilities, ratios, bets)
                            dic = findMin(result)








