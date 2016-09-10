import sys
from IPython.core.magic import Magics, magics_class, line_magic, cell_magic
from IPython.core.magic import line_cell_magic
from IPython.core.display import HTML                                
 
@magics_class
class CustomMagics(Magics):
 
    @cell_magic
    def CS(self, line, cell):
        """
        Defines command ``%%CS``.
        """
        if not sys.platform.startswith("win"):
            raise Exception("Works only on Windows.")
         
        from clrfunction import create_cs_function
        if line is not None:
            spl = line.strip().split(" ")
            name = spl[0]
            deps = " ".join(spl[1:]) if len(spl) > 1 else ""
            deps = deps.split(";")
             
        if name == "-h": 
            print(  "Usage: "
                    "   %%CS function_name dependency1;dependency2"
                    "   function code")
        else :
            try:
                f = create_cs_function(name, cell, deps)
            except Exception as e :
                print(e)
                return
            if self.shell is not None:
                self.shell.user_ns[name] = f
            return f
 
def register_magics():
    """
    register magics function, can be called from a notebook
    """
    ip = get_ipython()
    ip.register_magics(CustomMagics)

register_magics()
