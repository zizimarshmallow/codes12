### YOUR CODE FOR chocolatePrice() FUNCTION GOES HERE ###
def chocolatePrice(ali_budget,bashir_budget):
    if ali_budget<bashir_budget:
        smaller_budget=ali_budget
    else:
        smaller_budget=bashir_budget
    for a in range(1, smaller_budget + 1):
        if((ali_budget % a == 0)and (bashir_budget % a == 0)):
            chocolate=a
    return chocolate


#### End OF MARKER





### YOUR CODE FOR calculateProfit() FUNCTION GOES HERE ###

def calculateProfit(ali_budget, bashir_budget):
    if ali_budget == 0 or bashir_budget == 0:
        return ("Not Possible")
    if type(ali_budget) == str or type(bashir_budget) == str:
        return ("Not Possible")
    if ali_budget <= 0 or bashir_budget <= 0:
        return ("Not Possible")
    else:
        ali_budget = round(ali_budget)
        bashir_budget = round(bashir_budget)
        single=chocolatePrice(ali_budget, bashir_budget)
        bashir_chocolate= bashir_budget//single
        alichocolates= ali_budget//single
        if ali_chocolate>bashir_chocolate:
            aliprofit=round(ali_chocolate * single * 0.3)
            bashirprofit=round(bashir_chocolate * single * 0.2)
            if bashirprofit<aliprofit:
                return aliprofit
            else:
                return bashirprofit
        else:
            aliprofit=round(ali_chocolate * single * 0.2)
            bashirprofit=round(bashir_chocolate * single * 0.5)
            if bashirprofit<aliprofit:
                return aliprofit
            else:
                return bashirprofit


#### End OF MARKER


