#The fuction lm() requires an input of (i,m) and then stores
#those values into varibles and function lm1() computes the
#linear model using slope and interept.
def lm(i, m):
    slope = m
    intercept = i
    def lm1(x):
        number = x
        answer = intercept + (slope*number)
        return answer
    return lm1

#The fuction lm_p() requires an input of (l,p) and then stores
#those values into varibles. The varible 'slope' is the answer of the
#function lm() and function pm1() computes the power transformation of the
#predictive model.
def lm_p(l, p):
    slope = l
    value = p
    def pm1(x):
        number = x
        answer = slope(number**value)
        return answer
    return pm1

#This statement ensures that this module is for import use only and cannot
#be called directly in command-line.
if __name__ == '__main__':
    print('Sorry, not for human consumption')
