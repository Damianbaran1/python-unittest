#Jakie inne narzędzia udostępnia python wbudowane w składnie Pythona

"""
Narzędzie assert

assert dowolne wyrażenie
sprawdza pod względem prawdziwości True albo False
Podnosi assert error gdy wyrażenie = False

np.
assert 0
zwróci nam AssertionError ze względu, że 0 ma wartość False
"""

condition = False

#Ta logika odpowiada kodowi assert condition

#if not condition:
#    raise AssertionError('Assertion message.')

assert condition, 'Assertion message'


