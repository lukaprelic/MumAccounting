from decimal import *

output = ""
getcontext().rounding = ROUND_05UP
roundd = lambda f: Decimal(f).quantize(Decimal('.001'), rounding=ROUND_HALF_UP)
combinations = 0
correctValues = []


def execCalc(expectedResult, krouns, ExchangeRate,
             xApproximate,yApproximate, zApproximate,
             exchangeIncrement, yIncrement, zIncrement,
             exchangeDiviation, yDiviation, zDiviation,equalstolerance):
    global output
    output = ""
    global combinations
    global correctValues
    combinations = 0
    correctValues = []
    value = ('NO VALUE FOUND', 'NO VALUE FOUND', 'NO VALUE FOUND')
    expectedResult = roundd(expectedResult)
    xExchangeRate = roundd(ExchangeRate)
    xApproximate = roundd(xApproximate)
    exchangeDiviation = roundd(exchangeDiviation)
    exchangeIncrement = roundd(exchangeIncrement)
    krouns = krouns
    exchangeLowerBound = roundd(xApproximate - exchangeDiviation)
    exchangeUpperBound = roundd(xApproximate + exchangeDiviation)
    xPossible = roundd(exchangeLowerBound)

    yLowerBound = yApproximate - yDiviation
    yUpperBound = yApproximate + yDiviation

    zLowerBound = zApproximate - zDiviation
    zUpperBound = zApproximate + zDiviation
    lastResultDiff = float('inf')
    lastResult = float('inf')
    while xPossible <= exchangeUpperBound:
        strr = "changed x=" + str(xPossible)
        printAndOuput(strr)
        xPossible = roundd(xPossible)
        yPossible = yLowerBound
        while yPossible <= yUpperBound:
            zPossible = zLowerBound
            while zPossible <= zUpperBound:
                combinations += 1
                result = runCalc(xPossible, yPossible, zPossible, krouns, xExchangeRate)
                resultDiff = abs(expectedResult - result)

                if resultDiff <= lastResultDiff:
                    printAndOuput("x=", xPossible, " y=", yPossible, " z=", zPossible, "result=", result, "diff=",
                                  resultDiff,
                                  " diff", resultDiff, "<", lastResultDiff, " result=", result, "lastresult=",
                                  lastResult,
                                  "curr diff=", resultDiff)
                    lastResult = result
                    lastResultDiff = resultDiff
                    value = {'x': str(xPossible), 'y': yPossible, 'z': zPossible,'diff':str(resultDiff)}
                    if resultDiff < equalstolerance:
                        printAndOuput("!!!!x=", xPossible, " y=", yPossible, " z=", zPossible, "result=", result,
                                      "diff=",
                                      resultDiff,
                                      " diff", resultDiff, "<", lastResultDiff, " result=", result, "lastresult=",
                                      lastResult,
                                      "curr diff=", resultDiff)
                        correctValues.append(value)
                zPossible += zIncrement
            yPossible += yIncrement

        xPossible += exchangeIncrement
    printAndOuput("Run Completed -------- combinations", combinations, "possiblities=", len(correctValues))
    # for val in correctValues:
    #    printAndOuput("x=", val[0], " y=", val[1], " z=", val[2], "result=", lastResult, "diff=", lastResultDiff)
    return output


def runCalc(xthis, ythis, zthis, krouns, exchangeRate):
    result = roundd(krouns / roundd(xthis)) + \
             roundd(ythis / roundd(exchangeRate)) + \
             roundd(zthis / roundd(exchangeRate))
    return result


def printAndOuput(*string):
    global output
    line = ""
    for strr in string:
        line += str(strr) + " "
    #print(line)
    line += "<br/>"
    output += line
