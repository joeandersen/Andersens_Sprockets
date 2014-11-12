###############################
#
# A secret santa application
#
#
# By Joe Andersen
#
# 12/11/14
#
##############################

class Family(object):
    def __init__(self,fname):
        self._fname = fname
        self._people = dict()

    def get_fname(self):
        return self._fname

    def update_fname(self,fname):
        self._fname = fname

    def get_people(self):
        return self._people

    def add_person(self,person):
        self._people[person.get_name()]=person

    def remove_person(self,person):
        del self._people[person.get_name()]
        
    def __repr__(self):
        return 'Family. Name: '+self.get_fname()+ ' People: '+ str(self.get_people().keys() )     

class Person(object):
    def __init__(self,name,family=None):
        self._name = name
        self._is_buying_for = ''
        
        if family<>None:
            self._using_family = True
            self._family = family
            self._family.add_person(self)
        else:
            self._using_family = False
            self ._family = 'none'              
        

    def get_name(self):
        return self._name

    def update_name(self,name):
        self._name = name

    def get_family(self):
        return self._family

    def update_family(self,family):
        if self._using_family:
            self.get_family.remove_person(self)
            self._family = family
            self.get_family.add_person(self)

    def set_is_buying_for(self,other):
        self._is_buying_for = other

    def get_is_buying_for(self):
        return self._is_buying_for

    def __repr__(self):
        if self._using_family:
            return 'Person: name: '+self.get_name()+', in family: '+ self.get_family().get_fname()+'. They are buying for: '+str(self.get_is_buying_for())
        else:
            return 'Person: name: '+self.get_name()+ '. They are buying for: '+str(self.get_is_buying_for())

    def __str__(self):
        return self.get_name()





def create_families(names):
    families = dict()
    for family_name in names:
        families[family_name] = (Family(family_name))
    return families

def create_person(name,using_families):
    if using_families

def get_family_names():
    names = []
    name = raw_input('First Family name: ')
    while name <>'':
        names.append(name)
        name = raw_input('Next Family name: ')
    return names

def interact():
    
    print 'Welcome to Secret Santa Generator'
    print
    print
    using_families =  raw_input('Will you be using families? (y/n) ')
    while using_families<>True and using_families<>False:
        if using_families == 'y':
            using_families = True
        elif using_families =='n':
            using_families = False
        else:
            print 'y and n are the only input I understand here'
            using_families =  raw_input('Will you be using families? (y/n) ')
    

    if using_families:
        fnames = get_family_names()
        families = create_families(fnames)
        

    print 'Create People'
    print
    
    
    

        





    


if __name__ == '__main__':
    interact()
