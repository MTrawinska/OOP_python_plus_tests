class SurfingBoard:
    sup_weight = None
    user_weight = None
    gear_weight = None

    def __init__(self, sup_weight, user_weight, gear_weight):
        self.sup_weight = sup_weight
        self.user_weight = user_weight
        self.gear_weight = gear_weight

    def __repr__(self):
        return ("Surfing board weight: {} kg "\
                "User weight: {} kg, where total "\
                "weight with gear is {}kg".format(self.sup_weight, \
                                   self.user_weight, \
                                   self.total_weight_incl_gear(self.sup_weight,self.user_weight, self.gear_weight)))

    @staticmethod
    def total_weight_incl_gear(sup_weight, user_weight, gear_weight):
        return sup_weight + user_weight + gear_weight

    def print_info(self):
        print("Sup weight", self.sup_weight)
        print("User weight", self.user_weight)
        print("Gear weight", self.gear_weight)

class SUP(SurfingBoard):
    _max_sup_weight = 11
    _max_user_weight = 130
    _max_user_number = 2
    _sup_type = ["epoxy", "inflatable", "soft_top", "other"]

    def __init__(self, sup_weight, user_weight, gear_weight, user_number, model):
        super(SUP, self).__init__(sup_weight, user_weight, gear_weight)
        self.user_number = user_number
        self._sup_type = model

    def __iter__(self):
        self.counter = 0
        model = ["epoxy", "inflatable", "soft_top", "other"]
        while True:
            yield model

    def __next__(self):
        if self.counter >=4:
            raise StopIteration
        generate = self._sup_type
        for gen in generate:
            return gen

    def __str__(self):
        describtion = "Max SUP weight: {} kg / "\
                      "max user weight {} kg/ \n"\
                      "Chosen SUP weight {} kg / "\
                      " chosen user weight {} kg /\n"\
                      "Number of users {}/ max user number "\
                      "per SUP is {}. SUP type is {} ".format(self._max_sup_weight, \
                                                              self._max_user_weight, self.sup_weight, \
                                                              self.user_weight, \
                                                              self.user_number, \
                                                              self._max_user_number, self._sup_type)
        return(describtion)

    def print_info(self):
        super(SUP, self).print_info()
        print("User number", self.user_number)
        print("Sup type", self._sup_type)

    @property
    def sup_weight(self):
        return self._sup_weight

    @sup_weight.setter
    def sup_weight(self, sup_weight):
         if not isinstance(sup_weight, int):
            raise TypeError('Weight of SUP must be whole number')
         if not 5 <= sup_weight <= self._max_sup_weight:
            raise ValueError("Weight of SUP must be above 5kg and below {} kg".format(self._max_sup_weight))
         else:
            self._sup_weight = sup_weight

    @property
    def user_weight(self):
            return self._user_weight

    @user_weight.setter
    def user_weight(self, user_weight):
        if not isinstance(user_weight, (int, float)):
            error_msg = 'User weight must be numeric'
            raise TypeError(error_msg)
        if not 15 < user_weight <= self._max_user_weight:
            raise ValueError("User weight is below 15 kg or it is over {}kg" \
                       " and can not use SUP".format(self._max_user_weight))
        else:
            self._user_weight = user_weight

    @property
    def user_number(self):
        return self._user_number

    @user_number.setter
    def user_number(self, user_number):
        if not isinstance(user_number, int):
            raise TypeError('Number of users has to be an integer.')
        if not 1 <= user_number <= self._max_user_number:
            raise ValueError("Max number of user is {}".format(self._max_user_number))
        else:
            self._user_number = user_number

    @property
    def sup_type(self):
        return self._sup_type

    @sup_type.setter
    def sup_type(self, model):
        if not isinstance(model, str):
            raise TypeError("Must be string not numeric.")
        if model in ("epoxy", "inflatable", "soft_top", "other"):
            self._sup_type = model
        else:
            raise ValueError("Incorrect SUP type please type: epoxy/ inflatable/ soft_top /other")

    @classmethod
    def individual_baby_SUP(cls):
        individual = cls
        individual._max_user_weight = 35
        individual._max_user_number = 4
        individual._max_sup_weight = 8
        return individual

    @property
    def total_SUP_mass(self):
        return self.sup_weight + ((self.user_weight + self.gear_weight) * self.user_number)

print('\n')
print("---Surfing board information (parent)---")
print('\n')
board = SurfingBoard(8, 43, 4)
print(board)
print("---Static method: total weight---")
print(board.total_weight_incl_gear(8,43,4))
print("---General information (method)---")
print(board.print_info())
print('\n')
print("---SUP information (child)---")
print('\n')
sup = SUP(8,48,1,1,"epoxy")
print("---General information (string method)---")
print(sup.__str__())
print("---General information (method parent)---")
print(sup.print_info())
print("---Static method from parent class: total weight---")
print(sup.total_weight_incl_gear(8,43,4))
print("---Selection of SUP types (iterated)---")
my_iter = iter(sup)
print(my_iter.__next__())
print("---Show SUP type---")
type=sup.sup_type
print(type)
# sup.sup_type ="mess"
# print(sup.sup_type) -> Just to show setter: ValueError: Incorrect SUP type please type: epoxy/ inflatable/ soft_top /other
print("---SUP property: calculated total mass---")
print(sup.total_SUP_mass)
print("---SUP class method for individual SUP---")
individual_baby_SUP = SUP.individual_baby_SUP()
print(individual_baby_SUP(6,32,2,1,"baby sup"))
print("---More about testing and validation in file SUP_OOP_test.py---")
