"""A module to handle the json output of MadNkLO runs
TODO DOC
"""
from math import sqrt
import json

class Result(object):
    """A class that contains a single MadNkLO results
    """
    def __init__(self,result_dict):
        """Get a dictionnary with the following keys:
        -TODO

        :param result_dict:
        :type result_dict:
        """
        #TODO Input sanitization

        self.value = float(result_dict["Cross section"])
        self.uncertainty = float(result_dict["MC uncertainty"])
        self.name = str(result_dict["name"])
        self.timestamp = str(result_dict["timestamp"])
        self.unit = str(result_dict["unit"])
        self.order = str(result_dict["order"])

    def __add__(self, other):
        """TODO DOC """
        if isinstance(other,Result):
            if self.unit != other.unit:
                print "WARNING YOU ARE ADDING APPLES AND BANANAS !!! ({}+{})".format(self.unit,other.unit)
            result = Result(
                {
                    "Cross section": self.value+other.value,
                    "MC uncertainty": sqrt(self.uncertainty**2+other.uncertainty**2),
                    "name": self.name+"+"+other.name,
                    "order": self.order+"+"+other.order,
                    "timestamp": self.timestamp+"+"+other.timestamp,
                    "unit": self.unit
                }
            )
            return result
        elif isinstance(other,float) or isinstance(other,int):
            result = Result(
                {
                    "Cross section": self.value+other,
                    "MC uncertainty": self.uncertainty,
                    "name": self.name+"+"+str(other),
                    "order": self.order,
                    "timestamp": self.timestamp,
                    "unit": self.unit
                }
            )
            return result

    def __radd__(self, other):
        return self.__add__(other)


    def __sub__(self, other):
        """TODO DOC """
        if isinstance(other,Result):
            if self.unit != other.unit:
                print "WARNING YOU ARE SUBTRACTING APPLES AND BANANAS !!! ({}+{})".format(self.unit,other.unit)

            result = Result(
                {
                    "Cross section": self.value-other.value,
                    "MC uncertainty": sqrt(self.uncertainty**2+other.uncertainty**2),
                    "name": self.name+"-"+other.name,
                    "order": self.order+"-"+other.order,
                    "timestamp": self.timestamp+"-"+other.timestamp,
                    "unit": self.unit
                }
            )
            return result
        elif isinstance(other,float) or isinstance(other,int):
            result = Result(
                {
                    "Cross section": self.value-other,
                    "MC uncertainty": self.uncertainty,
                    "name": self.name+"+"+str(other),
                    "order": self.order,
                    "timestamp": self.timestamp,
                    "unit": self.unit
                }
            )
            return result

    def __str__(self):
        return "{:4.4e} +/- {:4.4e}".format(self.value,self.uncertainty)

    def __repr__(self):
        return ('{} {}='.format(type(self),self.name))+self.__str__()


class ResultDict(object):
    """A dictionnary of Results initialized from a JSON file"""
    def __init__(self,json_path=None):
        self._dict = {}
        if json_path!=None:
            #TODO add exception handling
            with open(json_path,"r") as my_json_file:
                json_dict = json.loads(my_json_file.read())
            for key in json_dict:
                self._dict[key]=Result(json_dict[key])

    def __getitem__(self, item):
        return self._dict[item]

    def __setitem__(self, key, value):
        self._dict[key] = value
