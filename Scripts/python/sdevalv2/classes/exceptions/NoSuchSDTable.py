class NoSuchSDTable(Exception):
    """
    If a requested SDTable by the user is not there, this exception is raised.
    
    @author:  Albert Heinle
    @contact: albert.heinle@rwth-aachen.de
    """
    def __init__(self, value):
        self.value = value
         
    def __str__(self):
        return repr(self.value)