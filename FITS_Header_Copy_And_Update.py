# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 08:53:45 2022

 This code gets the Header from one FTS/FITS file, the Data from another FTS/FITS file, and writes them to a new FTS/FITS file  
"""

import os #importing the os module 

#all the files needs to be in the working directory
directory = os.getcwd() #getting the current working directory
print(directory) #prints the current working directory


from astropy.io import fits #importing the fits module

# This code gets the Header from the First FTS/FITS file named: File_Name_1.FTS, the Data from the Second FTS/FITS named: File_Name_2.FTS, and writes them to a New FTS/FITS file named: File_Name_3.FTS
Header1 = fits.getheader('File_Name_1.FTS',0) # Gets the header from the First FTS/FITS file: File_Name_1.FTS
Data, Header2 = fits.getdata("File_Name_2.FTS", header=True) # Gets the data and the header from Second FTS/FITS File: File_Name_2.FTS
Header2['FILTER']  = 'Any Color' # Adds any filter information to the header of the Second FTS/FITS File: File_Name_2.FTS. 
Header2.update(Header1) # Pastes the header of the First FTS/FITS file:File_Name_1.FTS to the header of the Second FTS/FITS File: File_Name_2.FTS 
fits.writeto('File_Name_3.FTS', Data, Header2, overwrite=True) # Writes the updated header and the original Data of the Second FTS/FITS File: File_Name_2.FTS to a New file: File_Name_3.FTS

'''
Exemple with the files: M15.FTS, M15_R_Sub.FTS, M15_G_Sub.FTS, M15_B_Sub.FTS

# This code gets the Header from the First FTS/FITS file, the Data from the Second FTS/FITS file, and writes them to a New FTS/FITS file  
Header1 = fits.getheader('M15.FTS',0) # Gets the header from the First FTS/FITS file: M15.FTS
Data, Header2 = fits.getdata("M15_R_Sub.FTS", header=True) # Gets the data and the header from the Second FTS/FITS File: M15_R_Sub.FTS
Header2['FILTER']  = 'R Red' # Adds filter information to the header of the second FTS/FITS File: M15_R_Sub.FTS
Header2.update(Header1) # Pastes  the header of the First FTS/FITS file: M15.FTS to the header of the Second FTS/FITS File: M15_R_Sub.FTS 
fits.writeto('M15_R_Sub_Update.FTS', Data, Header2, overwrite=True) # Writes the updated header and the original Data of the Second FTS/FITS File: M15_R_Sub.FTS to a New file: M15_R_Sub_Update.FTS

# This code gets the Header from the First FTS/FITS file, the Data from the Second FTS/FITS file, and writes them to a New FTS/FITS file 
Header1 = fits.getheader('M15.FTS',0) # Gets the header from the First FTS/FITS file: M15.FTS
Data, Header2 = fits.getdata("M15_G_Sub.FTS", header=True) # Gets the data and the header from  the Second FTS/FITS File: M15_G_Sub.FTS
Header2['FILTER']  = 'G Green' # Adds filter information to the header of the Second FTS/FITS File: M15_G_Sub.FTS   
Header2.update(Header1) # Pastes  the header of the First FTS/FITS file: M15.FTS to the header of the Second FTS/FITS File: M15_G_Sub.FTS
fits.writeto('M15_G_Sub_Update.FTS', Data, Header2, overwrite=True) # Writes the updated header and the original Data of the Second FTS/FITS File: M15_G_Sub.FTS to a New file: M15_G_Sub_Update.FTS

# This code gets the Header from the First FTS/FITS file, the Data from the Second FTS/FITS file, and writes them to a New FTS/FITS file 
Header1 = fits.getheader('M15.FTS',0) # Gets the header from the First FTS/FITS file: M15.FTS
Data, Header2 = fits.getdata("M15_B_Sub.FTS", header=True) # Gets the data and the header fromthe Second FTS/FITS File: M15_B_Sub.FTS
Header2['FILTER']  = 'B Blue' # Adds filter information to the header of the Second FTS/FITS File: M15_B_Sub.FTS
Header2.update(Header1) # Pastes  the header of the First FTS/FITS file: M15.FTS to the header of the Second FTS/FITS File: M15_B_Sub.FTS
fits.writeto('M15_B_Sub_Update.FTS', Data, Header2, overwrite=True) # Writes the updated header and the original Data of the Second FTS/FITS File: M15_B_Sub.FTS to a New file: M15_B_Sub_Update.FTS
'''
