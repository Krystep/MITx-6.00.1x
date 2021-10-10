# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 13:19:26 2021

@author: ja
"""

import math
 
def polysum (n, s):
    """ takes 2 arguments: n - number of sides and s - lenght of one side. 
    returns the sum of the area and square of the perimeter rounded to 4 decimal places"""
    
    area = (0.25 * n * s**2) / (math.tan(math.pi/n))
    perimeter = s*n
    
    return round((area + perimeter**2), 4)



    