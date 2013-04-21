#These functions returns the basic functions from the WebGL 
#in the form of IPython.core.display.Javascript objects.
try:
    from IPython.core.display import Javascript
except:
    Javascript = None

def InitShaders():
    if not Javascript:
        raise NotImplementedError('This script requires IPython module to work')
    


