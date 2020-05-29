import time
from datetime import date
class Personne(object):
    """
        definit une classe personne avec les attributs :
        -nom
        -prenom
        -date de naissance
    """
    #--------------------constructeur----------------------------------------------------------------------
    def __init__(self,personne_nom,personne_prenom,personne_date_Naissance):
        """
            constructeur de la classe personne
        """
        self.__personne_nom = personne_nom
        self.__personne_prenom = personne_prenom
        self.__personne_date_Naissance = personne_date_Naissance
    #------------------accesseur et getter-----------------------------------------------------------------
    #surcharge de fonction
    @property
    def name(self):
        return self.__personne_nom
    @name.setter
    def name(self,value) :
        self.__personne_nom = value
    @name.deleter
    def name(self,value) :
        print("suppression........")
        del self.__personne_nom
    @property
    def prenom(self) :
        return self.__personne_prenom
    @prenom.setter
    def prenom(self,valeur) :
        self.__personne_prenom = valeur
    def getDateNaissance(self) :
        return self.__personne_date_Naissance
    #-------------------affichage--------------------------------------------------------------------------
    def __str__(self) :
        msg = "Information sur la personne: \n nom: {}\n prenom: {}\n date de naissance: {}\n"
        return msg.format(self.__personne_nom,self.__personne_prenom,self.__personne_date_Naissance)
        
#------------------------------classe emplyer--------------------------------------------------------------
class Employer(Personne) :
    """
        definit un enploer de la banque un attribut salaire
    """
    #----------------constructeur-------------------------------------------------------------------------
    def __init__(self,salaire,personne_employer) :
        #appelle du constructeur de la classe personne
        super().__init__(personne_employer.name(),personne_employer.prenom(),personne_employer.personne_date_Naissance)
        self.__salaire = salaire
    #-----------------------------accesseur et mutateur --------------------------------------------------
    def getSalaire(self) :
        return self.__salaire
    #--------------------------------affichage-----------------------------------------------------------
    def __str__(self) :
        msg = "Information sur l'employé: \n nom: {}\n prenom: {}\n date de naissance: {}\n salaire: {}\n"
        return msg.format(self.name(),self.prenom(),self.getDateNaissance(),self.__salaire)
#------------------------classe chef -----------------------------------------------------------------------
class Chef_service(Employer):
    """
        definit une classe chef qui herite de la classe employer avec un attribut service
    """
    def __init__(self, service,chef) :
        super().__init__(chef.getSalaire(),chef)
        self.__service = service
    #---------------------accesseur et mutateur ---------------------------------------------------
    @property
    def serv_chef(self):
        return self.__service
    @serv_chef.setter
    def serv_chef(self,valeur) :
        print("attention modificateur")
        self.__service =valeur
    @serv_chef.deleter
    def serv_chef(self) :
        print("suppression")
        del self.__service
#-----------------------------classe Directeur--------------------------------------------------------------
class Directeur(Chef_service) :
    """
        definit une classe directeur qui herite de chef_service avec un attribut banque 
    """
    def __init__(self,nom_banque,employer_banque) :
        super().__init__(employer_banque.serv_chef(),employer_banque)
        self.__nom_banque = nom_banque
    #-------------------accesseur et mutateur-------------------------------------------------------------
    def getNon_banque(self) :
        return self.__nom_banque
    def setNon_banque(self,valeur):
        self.__nom_banque = valeur
    
#------------------------------------classe client----------------------------------------------------------
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
    #numero_compte=0
    def __init__(self,solde,proprietaire) :
        """
            un compte se definit par son solde et son proprietaire
        """
        #global number_compte
        super().__init__(proprietaire.getCin(),proprietaire.getNon()
                        ,proprietaire.getPrenom(),proprietaire.getTel())
        self.__solde =solde
        nobject = Compteur()
        self.__number_compte = bin(nobject.compte_objet) #numero de compte a convertir en binaire 
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
        print(" la somme de {} a été debité sur le compte {}".format(valeure,compte_debite.getNumero_compte()))
        compte_debite.setSolde(compte_debite.getSolde() - valeure)
        print("virement en cours ........")
        time.sleep(20)
        #temps = time.localtime()
        named_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
        print(" virement a été effectué sur le compte numero {} aujourd'hui le {}"\
            .format(self.getNumero_compte() ,time_string))
        self.setSolde(self.getSolde() + valeure)
        
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
    #--------------------afficher un compte connaissant le nom------------------------------------------
    def rechercher_compte_par_nom(self,nom) :
        if self.getNon == nom :
            print(self)
        else:
            print("le compte n'existe pas ") 
    def rechercher_compte_par_numeroCompte(self,num) :
        if self.getNumero_compte == num:
            return self
#-----------------------classe compte epargne------------------------------------------------------------
class Epargne(Compte,Client) :
    """
    definit un compte epargne avec un attribut taux-d'interet et une methode calculinteret() qui permet de mettre 
    à jour le solde en fonction du taux
    Arguments:
        Compte {[type]} -- [description]
    """
    def __init__(self,taux_interet,epargne_solde,proprietaire) :
        super().__init__(epargne_solde,proprietaire)
        self.__taux_interet = taux_interet
    #----------------methode de calcul du taux d'interet------------------------------------------------------
    def calcul_taux_interet(self) :
        tauxIn = self.getSolde * int(self.__taux_interet * 24)
        self.setSolde(self.getSolde() + tauxIn)
#-----------------------------------classe compteur--------------------------------------------------------
class Compteur(Compte) :
      compte_objet = 0
      def __init__(self) :
            global compte_objet
            Compteur.compte_objet +=1
#------------------mon programme principale----------------------------------------------------------
if __name__ == "__main__":
    base_des_comptes={}# une listes des comptes temporaire
    liste_des_comptes = [] #un dictionnaire pour stocker tous les comptes definitivement
    print("Bienvenue a la banque de Fabala \n")
    print("Que voulez-vous faire ? \n")
    bouton = input("choisissez une option:<O-ouvertuere_compte><D-prelever-surCompte><C-consulter_compte><V-virement> <A-affichage des comptes>\n")
    while bouton !='q' :
        if bouton == 'O':
            out= ''
            while out != 'q' :
                cc=input("donnez le CIN: ")
                nn=input("donnez le NOM: ")
                pp=input("donnez le Prenom: ")
                tt=int(input("donnez le numero de telephone: "))
                premier_depot= int(input("versez une première somme : \n"))
                client_1 = Client(cc,nn,pp,tt)
                compte_creer = Compte(premier_depot,client_1)
                liste_des_comptes.append(compte_creer)
                base_des_comptes={k:v for k,v in enumerate(liste_des_comptes)} #utilisation de dictionnaire comprehension
                out=input("voulez vous ouvrir un autre compte ? <q-quitter|autre-continuer> ")
        elif bouton == 'C':
            quitter= ''
            while quitter !='q':
                rechCompte = input("Donnez le nom du proprietaire de compte ")
                for elts in liste_des_comptes:
                    elts.rechercher_compte_par_nom(rechCompte)
                    break
                quitter=input("voulez vous continuer ou quitter <autre-continuer> <q-quitter> ")
        elif bouton == 'V':
            sortir =''
            while sortir !='q' :
                vir = input("Vous avez optez pour un virement alors donner le numero de compte a debité : ")
                sme = int(input("donnez la somme a debité: "))
                cmpte_credite_num = input("Donnez le numero de compte a credite : ")
                vari=Client("EEE1234","nom","prenom",23456987)
                cmpte_credite = Compte(0,vari)
                temps_compte = Compte(0,vari)
                for e  in liste_des_comptes :
                    tmps_compte = e.rechercher_compte_par_numeroCompte(vir) #compte debité
                    cmpte_credite = e.rechercher_compte_par_numeroCompte(cmpte_credite_num) #compte credité
                    cmpte_credite.virement_entre_compte(sme,temps_compte) #virement
                    break
                sortir = input(" voulez vous faire un autre virement ? <q-quitter><autre-continuer> : ")
        elif bouton == 'D':
            print("voulez-vous prelever sur un montant sur un compte : ")
            ss= int(input("donnez la somme à prelever: "))
            numCpte = input("donnez le numero de compte: ")
            for e in liste_des_comptes :
                cpte_adebiter = e.rechercher_compte_par_numeroCompte(numCpte) 
                cpte_adebiter.debite_compte(ss)
                break
        elif bouton == 'A':
            print("Affichage de tous les comptes : \n")
            for k,v in base_des_comptes.items() :
                print("compte numero {} : \n".format(k))
                print(v)
        else:
            print(" aurevoir")
        bouton = input("choisissez une option <O-ouvertuere_compte> <A-affichage des comptes><C-consulter_compte> <V-virement><q-quitter>\n")