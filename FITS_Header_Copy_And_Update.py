# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 08:53:45 2022

@author: Lenovo
"""

import os #importing the os module 

#all the files needs to be in the working directory
directory = os.getcwd() #getting the current working directory
print(directory) #prints the current working directory


from astropy.io import fits #importing the fits module

Header1 = fits.getheader('M15.FTS',0) # Gets the header from one FTS/FITS file: M15.FTS
Data, Header2 = fits.getdata("M15_R_Sub.FTS", header=True) # Gets the data and the header from another FTS/FITS File: M15_R_Sub.FTS
Header2['FILTER']  = 'R Red' # Adds filter information to the header of the second FTS/FITS File: M15_R_Sub.FTS
Header2.update(Header1) # Pastes  the header of the first FTS/FITS file: M15.FTS to the header of the second FTS/FITS File: M15_R_Sub.FTS 
fits.writeto('M15_R_Sub_Update.FTS', Data, Header2, overwrite=True) # Updates the header of the second FTS/FITS File: M15_R_Sub.FTS
  


Header1 = fits.getheader('M15.FTS',0) # Gets the header from one FTS/FITS file: M15.FTS
Data, Header2 = fits.getdata("M15_G_Sub.FTS", header=True) # Gets the data and the header from another FTS/FITS File: M15_G_Sub.FTS
Header2['FILTER']  = 'G Green' # Adds filter information to the header of the second FTS/FITS File: M15_G_Sub.FTS   
Header2.update(Header1) # Pastes  the header of the first FTS/FITS file: M15.FTS to the header of the second FTS/FITS File: M15_G_Sub.FTS
fits.writeto('M15_G_Sub_Update.FTS', Data, Header2, overwrite=True) # Updates the header of the second FTS/FITS File: M15_G_Sub.FTS



Header1 = fits.getheader('M15.FTS',0) # Gets the header from one FTS/FITS file: M15.FTS
Data, Header2 = fits.getdata("M15_B_Sub.FTS", header=True) # Gets the data and the header from another FTS/FITS File: M15_B_Sub.FTS
Header2['FILTER']  = 'B Blue' # Adds filter information to the header of the second FTS/FITS File: M15_B_Sub.FTS
Header2.update(Header1) # Pastes  the header of the first FTS/FITS file: M15.FTS to the header of the second FTS/FITS File: M15_B_Sub.FTS
fits.writeto('M15_B_Sub_Update.FTS', Data, Header2, overwrite=True) # Updates the header of the second FTS/FITS File: M15_B_Sub.FTS 

