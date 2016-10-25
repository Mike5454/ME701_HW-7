#-*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

plt.ioff()
exp = np.exp

def Q(rho_e, rho_h) :
    return rho_e + rho_e **2*( exp ( -1.0/ rho_e ) -1.0) + \
    rho_h + rho_h **2*( exp ( -1.0/ rho_h ) -1.0)
        
def sig_Q(rho_e, rho_h) :
    a = rho_e **2 + 2.* rho_e **3*( exp ( -1.0/ rho_e ) -1) + \
    0.5* rho_e **3*(1 - exp ( -2.0/ rho_e ))
    b = rho_h **2 + 2.* rho_h **3*( exp ( -1.0/ rho_h ) -1) + \
    0.5* rho_h **3*(1 - exp ( -2.0/ rho_h )) 
    c = 2.* rho_e * rho_h + 2.* rho_e **2* rho_h *( exp ( -1.0/ rho_e ) -1) + \
    2.* rho_h **2* rho_e *( exp ( -1.0/ rho_h ) -1)  
    d = 2.*( rho_e * rho_h )**2/( rho_e - rho_h )*( exp ( -1.0/ rho_e ) - exp ( -1.0/ rho_h ))
    return np.sqrt( a + b + c +d - Q( rho_e , rho_h )**2)
    
def R (rho_e, rho_h) :
    return 100*sig_Q(rho_e, rho_h )/Q(rho_e, rho_h )
    
n = 2000
H = np.logspace ( -1 , 2 , n )
E = np.logspace ( -1 , 2 , n )

H,E = np.meshgrid(H, E, sparse = False, indexing ='ij')
res = R(E, H)
# plot Contours
cont = (0.1, 0.2, 0.5, 1, 2, 5, 10, 15, 20, 30, 40)

plt.figure(figsize =(10, 10))
# labels for the y axis
plt.text(115, 70, '0.1%', fontsize=12)
plt.text(115, 47, '0.2%', fontsize=12)
plt.text(115, 24, '0.5%', fontsize=12)
plt.text(115, 12, '1%', fontsize=12)
plt.text(115, 6.7, '2%', fontsize=12)
plt.text(115, 2.6, '5%', fontsize=12)
plt.text(115, 1.1, '10%', fontsize=12)
plt.text(115, 0.75, '15%', fontsize=12)
plt.text(115, 0.56, '20%', fontsize=12)
plt.text(115, 0.28, '30%', fontsize=12)
plt.text(115, 0.16, '40%', fontsize=12)
# labels for the y axis
plt.text(0.15, 115, '40%', fontsize=12)
plt.text(0.26, 115, '30%', fontsize=12)
plt.text(0.47, 115, '20%', fontsize=12)
plt.text(0.78, 115, '15%', fontsize=12)

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Electron Extraction Factor', fontsize=18)
plt.ylabel('Hole Extraction Factor', fontsize=16)
plt.contour(E, H, res, cont, colors ='k')
plt.savefig('new_contour.png')
plt.show()