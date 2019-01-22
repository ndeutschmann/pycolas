"""A module to handle the json output of MadNkLO runs
TODO DOC
"""
from math import sqrt

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
        self.name = string(result_dict["name"])
        self.timestamp = string(result_dict["timestamp"])
        self.unit = string(result_dict["unit"])
        self.order = string(result_dict["order"])

    def __add__(self, other):
        """TODO DOC """
        if isinstance(other,Result):
            if self.unit != other.unit:
                print "WARNING YOU ARE ADDING APPLES AND BANANAS !!! ({}+{})".format(self.unit,other.unit)

            return Result(
                {
                    "Cross section": self.value+other.value,
                    "MC uncertainty": sqrt(self.uncertainty**2+other.uncertainty**2),
                    "name": self.name+"+"+other.name,
                    "order": self.order+"+"+other.order,
                    "timestamp": self.timestamp+"+"+other.timestamp,
                    "unit": self.unit
                }
            )
    def __sub__(self, other):
        """TODO DOC """
        if isinstance(other,Result):
            if self.unit != other.unit:
                print "WARNING YOU ARE SUBTRACTING APPLES AND BANANAS !!! ({}+{})".format(self.unit,other.unit)

            return Result(
                {
                    "Cross section": self.value-other.value,
                    "MC uncertainty": sqrt(self.uncertainty**2+other.uncertainty**2),
                    "name": self.name+"-"+other.name,
                    "order": self.order+"-"+other.order,
                    "timestamp": self.timestamp+"-"+other.timestamp,
                    "unit": self.unit
                }
            )

    def str(self):
        return "{:e.4} +/- {:e.4}".format(self.value,self.uncertainty)