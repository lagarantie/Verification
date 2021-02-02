i1=1
i2=4
import numpy as np
import random

nb_exe=1000000
resultat=0

for i in np.arange(i1,i2,((i2-i1)/nb_exe)):
    value=random.randint(i1,i2)
    resultat+=value**3-5*value**2+20


intégrale=(i2-i1)*float(resultat/nb_exe)
print (intégrale)