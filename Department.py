import gc

class Department(object):
    """ Parent class for all departments.  """

    def __init__(self, budget, name = None, supervisor = None, employee_count = None):
        self.employees = set()
        self.__name = name
        self.__supervisor = supervisor
        self.__employee_count = employee_count
        self.__employees = set()
        self.__budget = budget
        self.all_budgets = list()
        self.__meeting_count = 0

        for obj in gc.get_objects():
            if isinstance(obj, Department):
                self.all_budgets.append([obj.name, obj.budget])

    ##################################################
    ##################  Properties ###################
    ##################################################

    # Name Property ----------------------------------------------------------------------
    @property
    def name(self):
        try:
            return self.__name
        except AttributeError:
            return ""

    @name.setter
    def name(self, val):
        if not isinstance(val, str):
            raise TypeError('Please provide a string value for the department name')

        if val is not "" and len(val) > 1:
            self.__name = val
        else:
            raise ValueError("Please provide a department name")


    # Supervisor Property ----------------------------------------------------------------
    @property
    def supervisor(self):
        if self.__supervisor is None:
            raise ValueError("No supervisor found!")

        try:
            return self.__supervisor
        except AttributeError:
            print("No supervisor found for the " + self.name + " department.")
            return ""

    @supervisor.setter
    def supervisor(self, val):
        if not isinstance(val, str):
            raise TypeError('Please provide a string value for the supervisor name')

        if val is not "" and len(val) > 3:
            self.__supervisor = val
        else:
            raise ValueError("Please provide a supervisor name")
    # Employees Property ----------------------------------------------------------------
    @property
    def employees(self):
        if self.__employees:
            try:
                return self.__employees
            except:
                raise ValueError("Employees set is empty!")
        else:
            raise ValueError("Employees set is empty!")

    @employees.setter
    def employees(self, vals):
        if not isinstance(vals, set):
            raise TypeError("Employees must be a set().")
        else:
            self.__employees = vals

    @property
    def employee_count(self):
        try:
            return self.__employee_count
        except:
            raise ValueError("Employee Count not found")

    @employee_count.setter
    def employee_count(self, val):
        if not isinstance(val, int):
            raise TypeError("Value must be an integer")
        if not val == 0:
            self.__employee_count = val
        else:
            raise ValueError("Value cannot be 0")

    @property
    def budget(self):
        try:
            return self.__budget
        except:
            raise ValueError("Budget not found")

    @budget.setter
    def budget(self, val):
        if not isinstance(val, float):
            raise TypeError("Budget must be a number")
        if val > 5000 and val > 0:
            try:
                self.__budget = val
            except:
                raise ValueError("Couldnt find self.budget!")

    @property
    def meeting_count(self):
        try:
            return self.__meeting_count
        except:
            raise ValueError("No meeting count found")

    @meeting_count.setter
    def meeting_count(self, val):
        if not isinstance(val, int):
            raise TypeError('Not an integer')
        else:
            try:
                self.__meeting_count = val
            except:
                raise ValueError("Needs to be an intefer")



    ##################################################
    ####################  Methods ####################
    ##################################################



    def meet(self):
        self.meeting_count += 1
        print("Everyone meet in {}'s office.".format(self.supervisor))







