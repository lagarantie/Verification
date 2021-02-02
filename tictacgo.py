import random
import numpy as np



def valeurmax(a,b):
    if (a>b):
        return a
    else:
        return b
    
    

def compteur(N, colonne, lignes, hrz, vrt, pion,grille):
    nb=1
    tmpcolonne=colonne+hrz
    tmplignes=lignes+vrt

    while (tmpcolonne<N and tmpcolonne>=0 and tmplignes<N and tmplignes>=0):
        if ((grille[tmpcolonne][tmplignes]==pion)):
           
            nb=nb+1
            
        else:
            break
        
        tmpcolonne=tmpcolonne+hrz
        tmplignes=tmplignes+vrt

    return nb

def deplacement(N, colonne, lignes, hrz, vrt, pion, grille):
  

    max=compteur(N, colonne, lignes, 0, 1, pion, grille)
    max=valeurmax(max,compteur(N,colonne, lignes, 1, 0, pion, grille)+compteur(N,colonne, lignes, -1, 0, pion,grille)-1)
    #print ("max1:"+str(max))
    max=valeurmax(max,compteur(N,colonne, lignes, 1, 1, pion,grille)+compteur(N,colonne, lignes, -1, -1, pion, grille)-1)
    #print ("max2:"+str(max))
    max=valeurmax(max,compteur(N,colonne, lignes, 1, -1, pion,grille)+compteur(N,colonne, lignes, -1, 1, pion,grille)-1)
    #print ("max3:"+str(max))
    
    
    return max
   
def agagne(N, colonne, lignes, hrz, vrt, pion, grille):
    if (deplacement(N, colonne,lignes,hrz,vrt, pion, grille)>=3):
        return 1
  
    return 0

parties=0
J1_win=0
J2_win=0
egalite=0
partie=0
while (parties<1000):
    n = 3
    grille = [[0] * n for i in range(n)]

    gagne=0

    pion=1
    pion_pose=0
    while (gagne==0 and pion_pose<9):
        pion_place=False

        while(pion_place==False):
            val1=random.randint(0,2)
            val2=random.randint(0,2)
            

            if (grille[val1][val2]==0):
                pion_pose+=1
                pion_place=True
                #print (val1_utilise)
                #print (val2_utilise)
                grille[val1][val2]=pion
                #print (grille[val1][val2])
                gagne=agagne(n,val1,val2,1,1,pion,grille)
                """
                for i in range(0,3):
                    print (grille[i])
                """
                if gagne!=1:
                    if (pion==1):
                        pion=2
                    else:
                        pion=1
                else:
                    if pion==1:
                        J1_win+=1
                    elif pion==2:
                        J2_win+=1
                    else:
                        egalite+=1
        
    parties+=1

print (J1_win)
print(J2_win)
print (egalite)



    
