class Client(object) :
    """
        defint une classe client avec les attributs :
        -CIN
        -Nom
        -Prenom
        -Telephone
    """
    #-----------constructeur------------------------------------------------------------------------------
    def __init__(self,cin,nom,prenom,tel) :
        """
            constructeur de la classe client
        """
        self.__cin = cin #private attribut
        self.__nom = nom #private attribut
        self.__prenom = prenom #private attribut
        self.__tel = tel #private attribut
        self.__email = self.__nom + '.' + self.__prenom + '@' + "gmail.com"
    #--------------- accesseurs et mutateurs ------------------------------------------------------------
    def getCin(self) :
        return self.__cin
    def getNon(self) :
        return self.__nom
    def getPrenom(self) :
        return self.__prenom
    def getTel(self) :
        return self.__tel
    def setNom(self,nom) :
        print(" called setNom()")
        self.__nom =nom
    def setPrenom(self,prenom) :
        print("called setPrenom()")
        self.__prenom = prenom
    def setTel(self,tel) :
        print(" called setTel()")
        self.__tel = tel
    def getMail(self) :
        return self.__email
    mon_property = property(getNon,setPrenom)
    #--------------------------verification---------------------------------------------------------
    def verification_cin(self, valeur) :
        """
            verifie l'unicité de cin
        """
        if self.getCin() == valeur :
            return True
        return False
    #-----------------------------affichage----------------------------------------------------------
    def __str__(self) :
        msg = "client:\n CIN: {}\n nom: {}\n prenom: {}\n telephone : {}\n adresse-mail: {}\n"
        return msg.format(self.getCin(),self.getNon(),self.getPrenom(),self.getTel(), self.getMail())
#---------------------classe compte -----------------------------------------------------------------
class Compte(Client) :
    """
        herite de la classe client
        une classe compte caraterisé par son solde et un code incrementé
        - son propriétaire 
    """
    #--------------constructeur----------------------------------------------------------------------
    
    def __init__(self,solde,proprietaire) :
        """
            un compte se definit par son solde et son proprietaire
        """
        global number_compte
        super().__init__(proprietaire.getCin(),proprietaire.getNon()
                        ,proprietaire.getPrenom(),proprietaire.getTel())
        self.__solde =solde
        nobject = Compteur()
        self.__number_compte = nobject.compte_objet 
    #-------------------accesseurs et mutateur-------------------------------------------------------
    def getSolde(self):
        return self.__solde
    def getNumero_compte(self) :
        return self.__number_compte
    def setSolde(self,val) :
        self.__solde = val
    #--------------------credite un compte-----------------------------------------------------------
    def credite_compte(self,valeur) :
        """
            credite un compte en prenant une somme en parametre
        """
        print("le compte a été credité")
        self.setSolde(self.getSolde() + valeur)
    #-------------------effectuer un virement--------------------------------------------------------
    def virement_entre_compte(self,valeure,compte_debite) :
        """
            credite un compte a partir d'un compte passé en parametre 
            et la somme a debite
        """
        print(" virement a été effectué sur le compte {}".format(self.getNumero_compte()))
        self.setSolde(self.getSolde() + valeure)
        print(" la somme de {} a été debité sur le compte {}".format(valeure,compte_debite.getNumero_compte()))
        compte_debite.setSolde(compte_debite.getSolde() - valeure)
    #---------------------debite un compte---------------------------------------------------------------
    def debite_compte(self,valeur) :
        """
            debite un compte avec une somme passé en parametre
        """
        print(" le compte {} a été debité de {}".format(self.getNumero_compte(), valeur))
        self.setSolde(self.getSolde()- valeur)
    #----------------------debite un compte un compte et credite l'autre---------------------------------
    def debite_compte_credite_autre(self,valeur, compte_a_credite) :
        """
            debite le compte courant et credite compte passé en paramettre 
            avec la valeure passé en parametre
        """
        print("le compte {} a été debité de {}".format(self.getNumero_compte(), valeur))
        self.setSolde(self.getSolde()-valeur)
        print(" virement a été effectué sur le compte {}".format(compte_a_credite.getNumero_compte()))
        compte_a_credite.setSolde(compte_a_credite.getSolde() + valeur)       
    #-----------------affichage--------------------------------------------------------------------------
    def __str__(self) :
        msg = "Numero de compte: {}\n solde: {}€\n Proprietaire du compte:\n CIN: {}\n nom: {}\n prenom: {}\n tel: {}\n adresse: {}\n"
        return msg.format(self.__number_compte,self.__solde , self.getCin()
                            , self.getNon(), self.getPrenom(),self.getTel(), self.getMail()) 
#-----------------------------------classe compte--------------------------------------------------------
class Compteur(Compte) :
      compte_objet = 0
      def __init__(self) :
            global compte_objet
            Compteur.compte_objet +=1
#------------------mon programme principale----------------------------------------------------------
if __name__ == "__main__":
    dict={}
    print("Bienvenue a la banque de France \n")
    print("Que voulez-vous faire ? \n")
    bouton = input("choisissez une option <O-ouvertuere_compte> <C-consulter_compte> <V-virement>\n")
    if bouton == 'O':
        cc=int(input("donnez le CIN: "))
        nn=input("donnez le NOM: ")
        pp=input("donnez le Prenom: ")
        tt=int(input("donnez le numero de telephone: "))
    elif bouton == 'C':
        pass
    elif bouton == 'V':
        pass
    elif bouton == 'Q':
        pass
    elif bouton == 'A':
        pass
    else:
        pass
    
    
    
    
    
    
    c = Client("EE1111","komah" ,"mohamed", 19876543)
    c1 =Client("EE1911","komah" ,"amed", 19876544)
    mn_cmpte = Compte(10000,c)
    mn_compte = Compte(2000000,c1)
    mn_compte.credite_compte(3456)
    mn_cmpte.virement_entre_compte(30,mn_compte)
    print(mn_cmpte)
    print(mn_compte)
