# Subroutine to return state of water given temperature in degrees celsius

def State(t):
    if t >= 100:
        return 'gaseous'
    elif t >=1 and t<=99:
        return 'liquid'
    else:
        return 'solid'
    

        

