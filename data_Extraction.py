#Program to exrtact data 
import pandas as pd 
import numpy as np
import math


#read the files and name the columns
lp1 = pd.read_csv('D:\padipu\MSc\AI_ML\Assignment\lp1.csv',skiprows = 0, names = ['LP1_Y', 'X_Fx', 'X_Fy', 'X_Fz', 'X_Tx', 'X_Ty', 'X_Tz'])
lp2 = pd.read_csv('D:\padipu\MSc\AI_ML\Assignment\lp2.csv',skiprows = 0, names = ['LP2_Y', 'X_Fx', 'X_Fy', 'X_Fz', 'X_Tx', 'X_Ty', 'X_Tz'])
lp3 = pd.read_csv('D:\padipu\MSc\AI_ML\Assignment\lp3.csv',skiprows = 0, names = ['LP3_Y', 'X_Fx', 'X_Fy', 'X_Fz', 'X_Tx', 'X_Ty', 'X_Tz'])
lp4 = pd.read_csv('D:\padipu\MSc\AI_ML\Assignment\lp4.csv',skiprows = 0, names = ['LP4_Y', 'X_Fx', 'X_Fy', 'X_Fz', 'X_Tx', 'X_Ty', 'X_Tz'])
lp5 = pd.read_csv('D:\padipu\MSc\AI_ML\Assignment\lp5.csv',skiprows = 0, names = ['LP5_Y', 'X_Fx', 'X_Fy', 'X_Fz', 'X_Tx', 'X_Ty', 'X_Tz'])

# #Give numerical values to the labels

lp1.replace(to_replace={"normal" : 0, "collision": 1, "fr_collision": 2, "obstruction": 3}, inplace = True)
lp2.replace(to_replace={"normal": 0, "front_col": 1, "back_col": 2, "right_col": 3, "left_col": 4}, inplace = True)
lp3.replace(to_replace={"ok": 0, "slightly_moved": 1, "moved": 2, "lost": 3}, inplace = True)
lp4.replace(to_replace={"normal": 0, "collision": 1, "obstruction": 2}, inplace = True)
lp5.replace(to_replace={"normal": 0, "bottom_collision": 1, "bottom_obstruction": 2, "collision_in_part": 3, "collision_in_tool": 4}, inplace = True)

#Convert pandas dataframes to numpy arrays for better processing

lp1_numpy = lp1.to_numpy()
lp2_numpy = lp2.to_numpy()
lp3_numpy = lp3.to_numpy()
lp4_numpy = lp4.to_numpy()
lp5_numpy = lp5.to_numpy()

#Python list initialisation to copy the extracted input and label values
Y_lp1 = []
Y_lp2 = []
Y_lp3 = []
Y_lp4 = []
Y_lp5 = []
X_lp1 = []
X_lp2 = []
X_lp3 = []
X_lp4 = []
X_lp5 = []

#extract input and label values from the python list
for i in range(len(lp1_numpy)):
    if (i==0 or i%18==0):
        Y_lp1.append(lp1_numpy[i,0])
    else:
        X_lp1.append(lp1_numpy[i, 1:7])
        
for i in range(len(lp2_numpy)):
    if (i==0 or i%18==0):
        Y_lp2.append(lp2_numpy[i,0])
    else:
        X_lp2.append(lp2_numpy[i, 1:7])    
        

for i in range(len(lp3_numpy)):
    if (i==0 or i%18==0):
        Y_lp3.append(lp3_numpy[i,0])
    else:
        X_lp3.append(lp3_numpy[i, 1:7])    
 
for i in range(len(lp4_numpy)):
    if (i==0 or i%18==0):
        Y_lp4.append(lp4_numpy[i,0])
    else:
        X_lp4.append(lp4_numpy[i, 1:7])
    
for i in range(len(lp5_numpy)):
    if (i==0 or i%18==0):
        Y_lp5.append(lp5_numpy[i,0])
    else:
        X_lp5.append(lp5_numpy[i, 1:7])
 
#Saving the input values X in csv files
np.savetxt("X_lp1.csv", X_lp1, delimiter = ',', header = "Fx_lp1,Fy_lp1,Fz_lp1,Tx_lp1,Ty_lp1,Tz_lp1", comments = "", encoding= 'utf-8')
np.savetxt("X_lp2.csv", X_lp2, delimiter = ',', header = "Fx_lp2,Fy_lp2,Fz_lp2,Tx_lp2,Ty_lp2,Tz_lp2", comments = "", encoding= 'utf-8')
np.savetxt("X_lp3.csv", X_lp3, delimiter = ',', header = "Fx_lp3,Fy_lp3,Fz_lp3,Tx_lp3,Ty_lp3,Tz_lp3", comments = "", encoding= 'utf-8')
np.savetxt("X_lp4.csv", X_lp4, delimiter = ',', header = "Fx_lp4,Fy_lp4,Fz_lp4,Tx_lp4,Ty_lp4,Tz_lp4", comments = "", encoding= 'utf-8')
np.savetxt("X_lp5.csv", X_lp5, delimiter = ',', header = "Fx_lp5,Fy_lp5,Fz_lp5,Tx_lp5,Ty_lp5,Tz_lp5", comments = "", encoding= 'utf-8')
      
#Saving the label values Y in csv files
np.savetxt("Y_lp1.csv", Y_lp1, delimiter = ',', header = "Y_lp1", comments = "", encoding= 'utf-8')
np.savetxt("Y_lp2.csv", Y_lp2, delimiter = ',', header = "Y_lp2", comments = "", encoding= 'utf-8')
np.savetxt("Y_lp3.csv", Y_lp3, delimiter = ',', header = "Y_lp3", comments = "", encoding= 'utf-8')
np.savetxt("Y_lp4.csv", Y_lp4, delimiter = ',', header = "Y_lp4", comments = "", encoding= 'utf-8')
np.savetxt("Y_lp5.csv", Y_lp5, delimiter = ',', header = "Y_lp5", comments = "", encoding= 'utf-8')

