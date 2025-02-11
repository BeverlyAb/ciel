
from pprint import PrettyPrinter
from ciel.public.references import SWURLReference

class RefPrettyPrinter(PrettyPrinter):

    def format(self, obj, context, maxlevels, level):
        if isinstance(obj, SWURLReference):
            return (str(obj), False, False)
        else:
            return PrettyPrinter.format(self, obj, context, maxlevels, level)

def sw_pprint(obj, **args):

    pprinter = RefPrettyPrinter(**args)
    pprinter.pprint(obj)

