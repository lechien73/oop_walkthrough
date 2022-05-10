class Employee:
    """
    A class describing an Employee for an employee management system

    Properties:
        first_name: string, the first name of the employee
        last_name: string, the last name of the employee
        salary: int, the employee's salary

    Methods:
        calculate_raise: calculates the employee's raise
        apply_raise: applies the employee's raise
    """

    def __init__(self, first_name="", last_name="", salary=0):
        """ Initialises the properties """
        self._first_name = first_name
        self._last_name = last_name
        self._salary = salary

    @property
    def first_name(self):
        """ first_name getter """
        if self._first_name:
            return self._first_name
        else:
            return "First name not set"
      
    @first_name.setter
    def first_name(self, new_value):
        """
        first_name setter method
        
        Args:
            new_value: string specifying the new first name
        
        Returns:
            None
            
        Raises:
            ValueError: if the new string has a zero length
        """
        if len(new_value) > 0:
            self._first_name = new_value
        else:
            raise ValueError("Cannot set the value!")
    
    @property
    def last_name(self):
        """ last_name getter """
        if self._last_name:
            return self._last_name
        else:
            return "Last name not set"
      
    @last_name.setter
    def last_name(self, new_value):
        """
        last_name setter method
        
        Args:
            new_value: string specifying the new last name
        
        Returns:
            None
            
        Raises:
            ValueError: if the new string has a zero length
        """
        if len(new_value) > 0:
            self._last_name = new_value
        else:
            raise ValueError("Cannot set the value!")
    
    @property
    def salary(self):
        """  salary getter """
        return self._salary
    
    @salary.setter
    def salary(self, new_value):
        """
        salary setter method
        
        Args:
            new_value: string specifying the new salary
        
        Returns:
            None
            
        Raises:
            Exception: if the new salary is less than zero
            ValueError: if the new salary is not an integer
        """
        if isinstance(new_value, int):
            if new_value < 0:
                raise Exception("The salary cannot be less than zero")
            else:
                self._salary = new_value
        else:
            raise ValueError("The new value must be a whole number!")
    
    def calculate_raise(self):
        """
        calculate_raise method

        Args:
            None
        
        Returns:
            int of 10% of the current salary

        Raises:
            None
        """
        return int(self.salary * 0.1)
    
    def apply_raise(self):
        """
        apply_raise method

        Args:
            None
        
        Returns:
            int of current salary plus the calculated raise

        Raises:
            None
        """

        self.salary += self.calculate_raise()
        return self.salary
    
    def __str__(self):
        """ String representation of the object """
        return f'Employee({self.first_name},{self.last_name},{self.salary})'


class Developer(Employee):
    """
    A class describing a Developer for an employee management system
    Subclass of Employee

    Properties:
        language: string, the programming language the developer uses
    """

    def __init__(self, first_name="", last_name="", salary=0):
        """ Initialises the properties """
        super().__init__(first_name, last_name, salary)
        self._language = ""
        self._language_list = ["php", "python", "javascript"]
    
    @property
    def language(self):
        """ language getter """
        if self._language:
            return self._language
        else:
            return "Language not set"

    @language.setter
    def language(self, new_value):
        """
        language setter method
        
        Args:
            new_value: string specifying the new language
        
        Returns:
            None
            
        Raises:
            ValueError: if the new string is not in the permitted list
        """
        if new_value.lower() not in self._language_list:
            raise Exception("Error: language must be in the list")
        else:
            self._language = new_value
    
    def calculate_raise(self):
        """
        calculate_raise polymorphic method

        Args:
            None
        
        Returns:
            int of a percentage of the current salary

        Raises:
            Exception: if the language is not set
        """
        if self.language.lower() == "php":
            rate = 0.15
        elif self.language.lower() == "javascript":
            rate = 0.2
        elif self.language.lower() == "python":
            rate = 0.25
        else:
            raise Exception("Error: language not set")
        
        return int(self.salary * rate)
    
    def __str__(self):
        """ String representation of the object """
        return f'Developer({self.first_name},{self.last_name},{self.salary},{self.language})'
    
