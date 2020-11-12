class Solution:
    def intToRoman(self, num: int) -> str:
        d = {}
        d[1] = 'I'
        d[2] = 'II'
        d[3] = 'III'
        d[4] = 'IV'
        d[5] = 'V'
        d[6] = 'VI'
        d[7] = 'VII'
        d[8] = 'VIII'
        d[9] = 'IX'
        d[10] = 'X'
        d[20] = 'XX'
        d[30] = 'XXX'
        d[40] = 'XL'
        d[50] = 'L'
        d[60] = 'LX'
        d[70] = 'LXX'
        d[80] = 'LXXX'
        d[90] = 'XC'
        d[100] = 'C'
        d[200] = 'CC'
        d[300] = 'CCC'
        d[400] = 'CD'
        d[500] = 'D'
        d[600] = 'DC'
        d[700] = 'DCC'
        d[800] = 'DCCC'
        d[900] ='CM'
        d[1000] = 'M'
        d[2000] = 'MM'
        d[3000] = 'MMM'

        base = 1
        v = ''
        while num > 0:
            ans = num % 10 * base
            if ans > 0:
                v = d[ans] + v
            num = num // 10
            base = base * 10
            
        return v