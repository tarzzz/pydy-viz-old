#This module includes some of the basic functions(javascrpt)
#Which are required by WebGL to work properly.

class JS(object):
	def __init__(self,js= ''):
		if js is '':
			self.jswrap = ''

def InitGL(canvas):
    """
    Takes the Canvas HTML id as the input and returns
    the code for the same in JavaScript, 
    also 'gl' object can be returned as well
    """
	
    js_var = '''var gl;
        function initGL(%s) 
        {
        try {
           gl = canvas.getContext("webgl") | canvas.getContext("experimental-webgl");
           gl.viewportWidth = canvas.width;
           gl.viewportHeight = canvas.height;
            } 
        catch (e) 
            {
            alert(e);
            }
        if (!gl) 
            {
            alert("Could not initialise WebGL, sorry :-(");
            }
            }'''%(canvas)
	self.jswrap+=js_var

def InitShaders():
