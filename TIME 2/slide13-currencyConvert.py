GDPtUSD = 1.24 
GBPtYUAN = 8.89
GBPtEUR = 1.14
GBPtYEN = 185.84

def cnvrt(Pounds, Currency):
    if Currency == 'USD':
        return Pounds * GBPtUSD
    elif Currency == 'YUAN':
        return Pounds * GBPtYUAN
    elif Currency == 'EURO':
        return Pounds * GBPtEUR
    elif Currency == 'YEN':
        return Pounds * GBPtYEN