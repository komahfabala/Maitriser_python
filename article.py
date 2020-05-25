import sys
class Article(object) :
        """
            cette classe décris un article avec : 
            -non de l'article
            -sa reference
            -designation
            -son prix hort taxe
            -calcule son prix TTC
            ces attributs sont accessible que par les mutateurs et accesseurs
        """
        taux_TVA = 1.196
        #--------constructeur --------------------------------------------------------------------------
        def __init__(self, nom,ref , design , prix_HT) :
            global taux_TVA   
            self.__nom = nom  #privée accessible dans les sous classes
            self.__ref = ref
            self.__design = design
            self.__prix_HT = prix_HT
            self.__prix_TTC = float(self.__prix_HT) * Article.taux_TVA 
        #-------------------les accesseurs et mutateurs--------------------------------------------------
        """ accessseur et mutateur """
        def set_Nom(self,nom) :
            print(" appelle set_Nom()")
            self.__nom = nom
        def get_Nom(self) :
            print(" appelle get_Nom()")
            return self.__nom
        def del_Nom(self) :
            print(" attention supression du nom")
            del self.__nom
        def set_Ref(self,ref) :
            print(" appelle set_Ref()")
            self.__ref = ref
        def get_Ref(self) :
            return self.__ref
        def set_Desgn(self,dsgn) :
            print(" appelle set_Desgn()")
            self.__design = dsgn
        def set_prixHT(self,pTH) :
            print(" appelle set_prixHT")
            self.__prix_HT =pTH
        mon_property = property(get_Nom, set_Nom, del_Nom)
        
        #----------------------------affichage------------------------------------------------------------
        def __str__(self) :
            msg = ' article: {} \n non: {} \n reference : {} \n designation :{}\n prix hors taxe :{}\n prix_TTC :{} \n'
            v = Compteur_objet()
            return (msg.format(v.compte_objet,self.get_Nom(),self.get_Ref() \
                ,self.__design,self.__prix_HT, self.__prix_TTC))
        #-------------------- methode de recherche ---------------------------------------------------------
        def recherche_article(self,reference) :
            """ cette methode recherche un article avec sa reference renvoi true or false"""
            if int(reference) == self.get_Ref():
                print(self)
                return True
            return False,print("No article existed")
        #-------------------------methode de recherche par nom-------------------------------------------
        def recherche_article_nom(self,name) :
            """ cette methode recherche un article par un nom donner renvoi true or false """
            if name == self.get_Nom() :
                return True
            return False
        #------------------------methode de recherche par iterval de prix--------------------------------
        def recherche_inter_prix(self,basse_prix, haut_prix) :
            """ cette methode recherche un article par interval de prix renvoi true or false """
            if self.__prix_HT >= basse_prix or self.__prix_HT <= haut_prix :
                return True
            return False
        #-----------------------methode de suppression d'article par reference----------------------------
        def suppression_article_ref(self, reference) :
            """ cette methode supprime un article par reference """
            if self.get_Ref == reference:
                del self
                print(" article supprimer")
        #-----------------------modifier un article------------------------------------------------------
        def modifier_article(self,reference,nval1,nval2,nval3) :
            """ cette methode modifie un article par sa reference """
            self.set_Ref(nval1)
            self.set_Desgn(nval2)
            self.set_prixHT(nval3)
            print("article modifier\n")
#---------------------------------------classe compteur d'objet------------------------------------------
class Compteur_objet(Article) :
        """ une classe qui compte les objects """
        compte_objet =0
        def __init__(self) :
            global compte_objet
            Compteur_objet.compte_objet +=1
#-------------- le programme principale ------------------------------------------------------------------
if __name__ == "__main__":
    print("Menu de l'application")
    print(" 1-rechercher un article par reference\n 2-Ajouter un artciele au stock en verifiant l'unicité\n \
    3-Supprimer un article par reference\n 4-Modifier un article par reference\n 5-Rechercher un article par nom\n \
    6-Rechercher un article par intervalle de prix de vente\n 7-afficher tous les articles\n 8-quitter")  
    ma_list = []
    arret = ''
    while arret != 's' :
        print(" Que voulez vous faire? <8-quitter> <autre-continuer> ")
        boutton = int(input("choisissez un chiffre entre 1 et 8 \n"))
        if boutton == 1:
            print("la recherche d'un article par reference.....:\n")
            rhr= int(input("donnez la reference de l'article:\n"))
            for x in range(len(ma_list)):
                if ma_list[x].recherche_article(rhr) == True :
                    print(ma_list[x])
                    break
        elif boutton == 2:
            q=''
            while q != 'T':    
                print("Enregistrement des articles")
                name = input("donnez le nom de l'article\n")
                rr= int(input("donnez la reference\n"))
                dd = input(" donner la designation \n")
                pHT = int(input("donner son prix hors taxe \n"))  
                art = Article(name,rr,dd,pHT)
                ma_list.append(art)
                del art
                print("voulez ajouter un autre article <T(quitter) , autre(continuer) >\n")
                q = input()
        elif boutton == 3:
            print("suppression d'article par reference") 
            art_ref= input("donnez la reference de l'article\n")
            for x in range(len(ma_list)):
               if ma_list[x].suppression_article_ref(art_ref) == True :
                    print(ma_list[x])
                    break 
            print(" la reference n'existe pas \n")
        elif boutton == 4:
            print("modifier")
            ancienne_ref = input("donez la nouvelle reference de l'article:\n")            
            nouv_ref = input("donez la nouvelle reference de l'article:\n")
            nouv_dsgn = input("donez la nouvelle designation de l'article:\n")
            nouv_prixHT = input("donez la nouveau prixHT de l'article:\n")
            for x in range(len(ma_list)):
                if ma_list[x].get_Ref == ancienne_ref :
                    ma_list[x].modifier_article(ancienne_ref,nouv_ref,nouv_dsgn,nouv_prixHT)
        elif boutton == 5:
            print("recherche par nom")
            nn = input("donnez un nom d'article:\n")
            for x in range(len(ma_list)):
                if ma_list[x].recherche_article_nom(nn) == True :
                    print(ma_list[x])
                    break
        elif boutton == 6:
            print("recherche par interval de prix\n")
            basse_p1 = int(input("donnez le prix minimum:\n"))
            haut_p2 = int(input("donnez le prix maximum:\n"))
            for x in range(len(ma_list)):
                if ma_list[x].recherche_inter_prix(basse_p1, haut_p2)  == True :
                    print(ma_list[x])
                    break
        elif boutton == 7:
            print("tous les articles de la listes")
            for x in range(len(ma_list)):
                print("---------------------")
                print(ma_list[x])
                print("---------------------")
        else:
            print("quitter")
        print(" voulez vous continuer <s-stop|autre-continuer")
        arret = input()
    print(" Bye Bye")
#-------------------------------fin programme-------------------------------------------------------------