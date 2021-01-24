from functools import reduce


def AddFullName(di):
    FullName = di["first_name"] + " " + di["last_name"]
    di["full_name"] = FullName
    return di


def AddPerMonthSalary(di1):
    MonthSalary = di1["per_year_salary"] / 12
    di1["per_month_salary"] = MonthSalary
    return di1


def FilterBySalary(di):
    if di["per_month_salary"] > 80000:
        return True
    return False


def CalculateAllYearSalary(a, b):
    if isinstance(a, dict):
        sumi = a["per_year_salary"] + b["per_year_salary"]
    else:
        sumi = a + b["per_year_salary"]
    return sumi


def GetAverageYearSalary(data):
    AllSalary = reduce(CalculateAllYearSalary, data)
    return AllSalary / len(data)


peoples = [
    {
        "first_name": "yerassyl",
        "last_name": "Tleugazy",
        "per_year_salary": 800000,
    },
    {
        "first_name": "Vadim",
        "last_name": "Zemtsov",
        "per_year_salary": 1000000,
    },
    {
        "first_name": "ABCD",
        "last_name": "DCBA",
        "per_year_salary": 1200000,
    },
    {
        "first_name": "EFGH",
        "last_name": "HGFE",
        "per_year_salary": 1400000,
    },
]

peoples1 = list(map(AddFullName, peoples))
print(peoples1)
peoples2 = list(map(AddPerMonthSalary, peoples))
print(peoples2)
peoples3 = list(filter(FilterBySalary, peoples2))
print(peoples3)
AllYearSalary2 = GetAverageYearSalary(peoples2)
AllYearSalary3 = GetAverageYearSalary(peoples3)
print(AllYearSalary2)
print(AllYearSalary3)
# CTRL + ALT + L
