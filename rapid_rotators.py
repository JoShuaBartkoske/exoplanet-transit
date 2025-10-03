'''
Caclulate the parameters for rapid rotating stars
Author: Joshua Thomas Bartkoske
DoC: Oct 3, 2025
'''

# imports
import numpy as np
import astropy as astpy
import astropy.units as u

# In order to calculate the parameters for rapidly rotating stars, we can use an equation
# Omega_critical = Omega_keplerian * sqrt( 1 - edd_p^(3/2) )
# where the Keplerian angular velocity Omega_keplerian = sqrt(G*M / R_equator^3)
# and the Eddington parameter edd_p = ( k_opacity * L ) / ( 4 * pi * c * G * M)
# where k_opacity is the flux-weighted opacity, L is the luminosity of the star, c is the speed of light,
#   G is the Newtonian gravitational constant, and M is the mass of the star.

# constants
from astropy.constants import G, c, M_sun, R_sun

# first the Omega_keplerian based on parameters for an exoplanet host star
M_star = 1.43*M_sun # F5 IV star 
R_star = 2.13*R_sun
O_kep = np.sqrt((G * M_star) / (R_star**3))
print(O_kep)

# the star's angular rotation
vrot_star = 9.0*u.km/u.s # km/s
w_star = vrot_star.to(u.m/u.s) / R_star
print(w_star)

# angular rotational rate as fraction of critical angular rotation
omega_star = w_star/O_kep
print(omega_star)
