import sys
import math
class Point(object) :
    """
        cette classe represente un point avec ses coordonées 
    """
    #----------------constructeur------------------------------------
    def __init__(self, x = 0.0, y = 0.0):
        self.abs = x 
        self.ord = y

    #---------calcul de la distance entre deux points--------------------------------------------
    def calculdistance(self,elmt) :
        return math.sqrt(math.pow((int(elmt.abs) - int(self.abs)),2) + \
                math.pow(int(elmt.ord) - int(self.ord),2)) 

    #---- affichage du point--------------------------------------------------------------------
    def afficherPoint(self) :
        return 'Point <{},{}> '.format(self.abs , self.ord)
    
class Moncercle(Point) :
    """
     cette classe represente un cercle avec son centre, son rayon et sa couleur 
    """
    #-------Constructeur-------------------------------------------------------------------------
    def __init__(self, absX, ordY ,r , couleur ="blanc"):
        self.un_rayon = r
        self.un_coul = couleur
        #---- appelle du constructeur de la classe point-----------------------------------------
        Point.__init__(self,absX,ordY)
    #-----------------affichage------------------------------------------------------------------
    def __str__(self) :
        return 'mon cercle de centre de coordonées  <{},{}>  ,de  rayon {} , et de couleur {} '\
            .format(self.abs, self.ord, self.un_rayon , self.un_coul)
    #-------------- renvois le rayon, abscisse , ordonnee du cercle---------------------------------------------------
    """
        simulation de l'encapsulation en python
        - attribut avec un seul underscore = protected
        - attributs avec 2 undrscore = private 
    """
    @property
    def _getAbs(self) :
        print('son abscisse :')
        return self.abs 
    @property
    def _getOrd(self) :
        print("son ordonnee : \n")
        return self.ord 
    @property
    def _getRayon(self) :
        print(" appelle getRayon() \n")
        return self.un_rayon
    @property
    def _setRayon(self,r) :
        print(" appelle setRayon(),le rayon change de valeur , sa nouvelle valeur est {}".format(r))
        self.un_rayon =r
    @property
    def _setOrd(self, x) :
        print(" appelle setOrd(),la valeur de l'ordonnee a changé , nouvelle valeur est {}".format(x))
        self.ord = x
    @property
    def _setAbs(self,y) :
        print(" appelle setAbs() ,la valeur de l'abscisse achangé, nouvelle valeur est {}".format(y))
        self.abs = y
    mon_accesseurGetter_Abs = property(_getAbs,_setAbs)
    mon_accesseurGetter_Ord = property(_getOrd,_setOrd)
    mon_accesseurGetter_Rayon = property(_getRayon,_setRayon)
    #--------------calcule du perimetre du cercle -----------------------------------------------
    def calcul_perimetre(self) :
        return math.pi*(int(self.un_rayon)*2) 
    #--------------calcul de la surface du cercle -----------------------------------------------
    def calcul_surface(self) :
        return math.pi*(math.pow(int(self.un_rayon),2))
    #--------- verifie si un point appartient au cercle -----------------------------------------
    def appartientPoint(self,element) :
        #element = Point(2,4)
        dists = math.sqrt(math.pow((int(element.abs) - int(self.abs)),2) + \
                math.pow(int(element.ord) - int(self.ord),2))
        if dists <= float(self.un_rayon) :
            return True
        return False
#----------le programme principale---------------------------------------------------------------
if __name__ == "__main__":
    print("le menu de l'application")
    print('donnez un votre abscisse :') 
    xx= input()
    print('donnez vortre ordonne :')
    yy=input()
    print('donner le rayon')
    rr = input()
    centre = Point(xx,yy)
    print(centre.afficherPoint())
    cercle = Moncercle(xx,yy,rr,"noir")
    print(cercle)
    print('son perimetre de {}m \n surface de {} \n'.format(cercle.calcul_perimetre() , cercle.calcul_surface()))
    print('donnez un point :')
    pt_x = input()
    pt_y = input()
    test_point = Point(pt_x,pt_y)
    verif =isinstance(cercle, Moncercle)
    if verif :
        if cercle.appartientPoint(test_point) == True :
            print("le point {} appartenance au cercle".format(test_point.afficherPoint()))
        else :
            print("le point {} n'appartient pas au cercle".format(test_point.afficherPoint()))


