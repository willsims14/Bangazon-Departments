from Department import Department

# Human Resources Class
class HumanResources(Department):
    '''
    
    Class: Inherites from Department, but adds the policies property

    '''

    def __init__(self, name, supervisor = None, employee_count = None):
        super().__init__(name, supervisor, employee_count)
        self.__policies = set()

    @property
    def policies(self):
        try:
            return self.__policies
        except:
            raise ValueError("Policies does not exist for " + self.name)

    @policies.setter
    def policies(self, vals):
        if not isinstance(vals, set):
            raise TypeError("Value is not a set!")
        else:
            try:
                self.__policies = vals
            except:
                raise ValueError("Could not set policies")

# Marketing Class
class Marketing(Department):
    '''

    Class: Inherits from department class, but adds the advertisements property

    '''
    def __init__(self, name, supervisor = None, employee_count = None):
        super().__init__(name, supervisor, employee_count)
        self.__advertisements = list()

        @property
        def advertisements(self):
            try:
                return self.__advertisements
            except:
                raise ValueError("No advertisements found!")

        @advertisements.setter
        def advertisements(self, vals):
            if not isinstance(vals, list):
                raise TypeError("Vals is not a list!")
            else:
                try:
                    self.__advertisements = vals
                except:
                    raise ValueError("Could not set advertisements!")