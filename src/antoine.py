import numpy as np
def antoine( a, T):
    """    
        Ps = antoine( a, T)
        
        Uses Antoine's equation to obtain the vapor pressure of a substance given
        the coefficients of the equation:
        Ps = a1 - a2/(a3+T)
        
        INPUTS:
            a - the antoine coefficients with coeffients in columns and species in
                rows. Coefficients from NIST expect units of bar and K.
            T - the temperature at which the vapor pressure is evaluated (K)
                tempUnit - OPTIONAL the unit of temperature used
        
        OUTPUT:
            Ps - row vector of species vapor pressures at the specified temperature,
                typically in bar.
        
        The units depend on the units used for the coefficients. The user is
        responsible for maintaining consistency with units. NIST uses bar and K.

        Code originally by: James C. Sutherland
        Modified by: Tyler R. Josephson
    """
    try:
        a = np.array(a)
        if a.ndim == 1:
            Ps = 10.0**( a[0] - a[1] / ( a[2] + T ) )
        elif a.ndim == 2:
            Ps = 10.0**( a[:,0] - a[:,1] / ( a[:,2] + T ) )
        else:
            Ps = 'a'
        Ps/1.0
    except TypeError:
        print("Invalid array type. Must be 1-d or 2-d as in docstring.")

         
    #Ps = 10.0**( a[:,0] - a[:,1] / ( a[:,2] + T ) )
    
    #Ps = 10.0**( a[:,0] - a[:,1] / ( a[:,2] + T ) )
    return Ps
