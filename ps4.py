# Problem Set 4
# Name: 
# Collaborators: 
# Time: 

#
# Problem 1
#
from decimal import Decimal

def nestEggFixed(salary, save, growthRate, years):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: the annual percent increase in your investment account (an
      integer between 0 and 100).
    - years: the number of years to work.
    - return: a list whose values are the size of your retirement account at
      the end of each year.
    """
    # TODO: Your code here.
    retirementYear = []
    retirementYear.append(salary * save * 0.01)
    for x in range(1,years):
        retirementYear.append((retirementYear[x-1] *(1 + (0.01 * growthRate))) + retirementYear[0])
        #print retirementYear
    return retirementYear

def testNestEggFixed():
    salary     = 10000
    save       = 10
    growthRate = 15
    years      = 5
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print savingsRecord
    # Output should have values close to:
    # [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]

    # TODO: Add more test cases here.

#
# Problem 2
#

def nestEggVariable(salary, save, growthRates):
    # TODO: Your code here.
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: a list of the annual percent increases in your investment
      account (integers between 0 and 100).
    - return: a list of your retirement account value at the end of each year.
    """
    retirementFund = []
    if not growthRates:
        assert 'No growth rates given'
    retirementFund.append(salary * save * 0.01)
    for x in range(0,len(growthRates)-1):
        retirementFund.append((retirementFund[x] *(1 + (0.01 * growthRates[x]))) + retirementFund[0])
    return retirementFund

def testNestEggVariable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print savingsRecord
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]

    # TODO: Add more test cases here.

#
# Problem 3
#

def postRetirement(savings, growthRates, expenses):
    """
    - savings: the initial amount of money in your savings account.
    - growthRate: a list of the annual percent increases in your investment
      account (an integer between 0 and 100).
    - expenses: the amount of money you plan to spend each year during
      retirement.
    - return: a list of your retirement account value at the end of each year.
    """
    # TODO: Your code here.
    retirementFund = []
    retirementFund.append((savings * (1 + (0.01 * growthRates[0]))) - expenses)
    for x in range(1,len(growthRates)):
        retirementFund.append((retirementFund[x-1] * (1 + (0.01 * growthRates[x]))) - expenses)
    return retirementFund

def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print savingsRecord
    # Output should have values close to:
    # [80000.000000000015, 54000.000000000015, 24000.000000000015,
    # -4799.9999999999854, -34847.999999999985]

    # TODO: Add more test cases here.

#
# Problem 4
#

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - preRetireGrowthRates: a list of annual growth percentages on investments
      while you are still working.
    - postRetireGrowthRates: a list of annual growth percentages on investments
      while you are retired.
    - epsilon: an upper bound on the absolute value of the amount remaining in
      the investment fund at the end of retirement.
    """
    # TODO: Your code here.
    accountYearList = []
    accountYearList = nestEggVariable(salary, save, preRetireGrowthRates)
    preRetirementAccount = accountYearList[len(accountYearList)-1]
    highExp = preRetirementAccount + epsilon
    lowExp = 0.0
    counter = 100
    while counter > 0:
        testExp = (lowExp + highExp)/2.0
        temp = postRetirement(preRetirementAccount, postRetireGrowthRates, testExp)
        if abs(temp[len(temp)-1]) < epsilon:
            return testExp
        if temp[len(temp)-1] >= epsilon:
            lowExp = testExp
        elif temp[len(temp)-1] < epsilon:
            highExp = testExp
    return "Error. Unable to find exact value."
    
def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print expenses
    # Output should have a value close to:
    # 1229.95548986

    # TODO: Add more test cases here.
