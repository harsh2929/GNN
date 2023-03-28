

from texttable import Texttable

def tcb(args):
   
    args = vars(args)
    keys = sorted(args.keys())
    t = Texttable() 
    t.add_rows([["Parameter", "Value"]])
    t.add_rows([[k.replace("_", " ").capitalize(), args[k]] for k in keys])
    print(t.draw())

def cmc(node_properties):

    return {value:i for i, value in enumerate(node_properties)}
'''
def tcb(args):
    """
    Prints a table with the parameter names and their values.
    """
    args = vars(args)
    keys = sorted(args.keys())
    t = Texttable() 
    t.add_rows([["Parameter", "Value"]])
    t.add_rows([[f"{k.replace('_', ' ').capitalize()}", args[k]] for k in keys])
    print(t.draw())

'''
