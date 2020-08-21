'''
day: ([01]\d|2\d|3[01])
month: (0\d|1[012])

YEARS:
leap: (\d{2}(0[48]|[2468][048]|[13579][26])|(0[48]|[2468][048]|[13579][26])00)
    all numb div by 400: (0[48]|[2468][048]|[13579][26])00
    all numb div by 4 and not 100: \d{2}(0[48]|[2468][048]|[13579][26])
not leap: (\d{2}(0[^048]|[2468][^048]|[13579][^26])|(0[^048]|[2468][^048]|[13579][^26])00)
    not div by 4: \d{2}(0[^048]|[2468][^048]|[13579][^26])
    div by 4 and 100 (or just 100) but not 400: (0[^048]|[2468][^048]|[13579][^26])00


DAYS AND MONTHS:
days up to 30: (0[1-9]|[12]\d|30)
    4
    6
    9
    11
    Reg: (0[1-9]|[12]\d|30)\.(0[469]|11)

days up to 31: ([012]\d|3[01])
    1 31
    3 31
    5 31
    7 31
    8 31
    10 31
    12 31
    Reg: (0[1-9]|[12]\d|3[01])\.(0[13578]|1[02])
(0[1-9]|[12]\d|3[01])\.(0[13578]|1[02])

2

days up to 28: (0[1-9]|1\d|2[0-8])\.02
days up to 29: (0[1-9]|[12]\d)\.02

leap: ((0[1-9]|[12]\d|30)\.(0[469]|11)|(0[1-9]|[12]\d|3[01])\.(0[13578]|1[02])|(0[1-9]|[12]\d)\.02)
not leap: ((0[1-9]|[12]\d|30)\.(0[469]|11)|(0[1-9]|[12]\d|3[01])\.(0[13578]|1[02])|(0[1-9]|1\d|2[0-8])\.02)

----
LEAP: ((0[1-9]|[12]\d|30)\.(0[469]|11)|(0[1-9]|[12]\d|3[01])\.(0[13578]|1[02])|(0[1-9]|[12]\d)\.02)\.(\d{2}(0[48]|[2468][048]|[13579][26])|(0[48]|[2468][048]|[13579][26])00)
NOT LEAP: ((0[1-9]|[12]\d|30)\.(0[469]|11)|(0[1-9]|[12]\d|3[01])\.(0[13578]|1[02])|(0[1-9]|1\d|2[0-8])\.02)\.(\d{2}(0[^048]|[2468][^048]|[13579][^26])|(0[^048]|[2468][^048]|[13579][^26])00)


ALL:
^(((0[1-9]|[12]\d|30)\.(0[469]|11)|(0[1-9]|[12]\d|3[01])\.(0[13578]|1[02])|(0[1-9]|[12]\d)\.02)\.(\d{2}(0[48]|[2468][048]|[13579][26])|(0[48]|[2468][048]|[13579][26])00)|((0[1-9]|[12]\d|30)\.(0[469]|11)|(0[1-9]|[12]\d|3[01])\.(0[13578]|1[02])|(0[1-9]|1\d|2[0-8])\.02)\.(\d{2}(0[^048]|[2468][^048]|[13579][^26])|(0[^048]|[2468][^048]|[13579][^26])00))$
'''
date_validator = (
    r'((('
    r'(0[1-9]|1\d|2[0-8])\.(0[1-9]|1[012])|'
    r'(29|30)\.(0[13-9]|1[012])|'
    r'(31\.(0[13578]|1[02])))\.'
    r'([1-9]\d{3}|\d{3}[1-9]))|'
    r'(29\.02\.('
    r'\d\d([2468][048]|[13579][26]|0[48])|'
    r'([2468][048]|[13579][26]|0[48])00'
    r')))$')
