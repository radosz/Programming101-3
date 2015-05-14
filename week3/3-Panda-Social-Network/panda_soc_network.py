from validate_email import validate_email
from BFS_level import connection_level as bfs_l
from copy import deepcopy
import json


class Panda:

    def __init__(self, name, mail, gender):
        self.__name = name
        self.__mail = mail
        self.__gender = gender

    def json_panda_repr(self):
        name = '"name":"{}"'.format(self.__name)
        mail = '"mail": "{}"'.format(self.__mail)
        gender = '"gender":"{}"'.format(self.__gender)
        return "{{\n {},\n{},\n{} \n}}".format(name, gender, mail)

    def getGender(self):
        return self.__gender

    def isMail(self):
        return validate_email(self.__mail)

    def validate_gender(self):
        validate_str = str(self.__gender).upper()
        return validate_str == "MALE" or validate_str == "FEMALE"

    def name(self):
        return self.__name

    def email(self):
        return self.__mail

    def isMale(self):
        return self.__gender == "male"

    def isFemale(self):
        return self.__gender == "female"

    def __eq__(self, other):
        b1 = self.__name == other.__name
        b2 = self.__mail == other.__mail
        b3 = self.__gender == other.__gender
        return b1 and b2 and b3

    def __hash__(self):
        hash_str = self.__name + self.__mail + self.__gender
        return(hash(hash_str))

    def __str__(self):
        return self.__name

    def __repr__(self):
        return self.json_panda_repr()


class PandaSocialNetwork:

    def __init__(self):
        self.network = {}
        #self.exc = Errors("PandaAlreadyThere","Panda alredy there")

# TODO : Add error messages
    def add_panda(self, panda):
        # if panda in self.pandas :
            #raise PandaAlreadyThere
        self.network[panda] = []

    def has_panda(self, panda):
        return panda in self.network

    def make_friends(self, panda1, panda2):

        if not self.has_panda(panda1):
            self.add_panda(panda1)

        if not self.has_panda(panda2):
            self.add_panda(panda2)

        self.network[panda1].append(panda2)
        # TODO : Raise PandasAlreadyFriend

    def are_friends(self, panda1, panda2):
        return panda2 in self.network[panda1]

    def friends_of(self, panda):
        return self.network[panda]

    def connection_level(self, panda1, panda2):
        return bfs_l(self.network, panda1, panda2)

    def are_connected(self, panda1, panda2):
        return panda2 in self.network[panda1]

    def panda_genders(self, set_pandas, gender):
        counter = 0
        for p in set_pandas:
            if p.getGender() == gender:
                counter += 1
        return counter

    def how_many_gender_in_network(self, level, panda, gender):
        end_level = 0
        start_level = level
        all_pandas = [panda for panda in self.network[panda]]
        if level == 1:
            return self.panda_genders(all_pandas, gender)
        level -= 1
        while level != 0:
            for pnd in set(all_pandas):
                all_pandas += [x for x in self.network[pnd] if x != panda]
            end_level += 1
            level -= 1

        # TODO: Make level exception for this case
        if start_level != end_level + 1:
            raise Exception("Level exception")

        return self.panda_genders(set(all_pandas), gender)

    def __str__(self):
        return str(self.network)

    def pandas_to_json(self):
        result = []
        for k, v in self.network.items():
            result.append(
                "{} : {}".format(k.json_panda_repr(), v))
        return ",".join(result)

    def save(self):
        pass

    def load(self):
        pass


# TODO : write  this later
class Errors(Exception):

    def __init__(self, message, errors):

        # Call the base class constructor with the parameters it needs
        super(ValidationError, self).__init__(message)

        # Now for your custom code...
        self.errors = errors
