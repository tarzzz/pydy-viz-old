try:
	from IPython.core.display import HTML,display
except ImportError:	
    HTML = None
    

class html(object):
    """
    Defines an HTML Object for utilization in the visualization process.
    
    Examples:
    =========
    
    a = html()
    a.outline(body = AnotherHTMLObject)
    
    
    
    """
    
    
    def __init__(self,html = ''):
        """
        Returns the Default HTML if it is initialized, Otherwise
        
        """
        if html is '':
            self.content = '''
                    <!DOCTYPE html>
                    <html>
                    <head>
                        <meta charset="utf-8" />
                        
                    </head>
                    <script type="text/javascript">%s</script>
                    <body>%s</body>
                    
                    </html>'''
            self.body = ''
            self.js = ''      
            self.wrap = ''
        else:
            self.content = html         
            self.body = ''      
            self.js = ''
            self.wrap = ''
                    
        
        
    def set_main_content(self,content = ''):
        """
        Initializes the body of the HTML, which is mergeable in htmlwrap
        function.Returns the body string
        
        a = html()
        p = a.set_main()
        p = a.set_js()
        s = a.htmlwrap(body=p,js=p)
                        
        
        """
        self.body = content
        return self.body
        
#    def set_js(self,js = ''):
		
    
    
    def htmlwrap(self,body = '',js=''):
        html = self.content
        if body is '' and js is '':
            
            self.wrap = self.content%(self.js,self.body)
            
        else:
            self.wrap = self.content%(js,body)
            
                
                        
    def visualize(self):
		if not HTML:
			raise NotImplementedError('This feature works only on IPython')
		else:	
			vis = HTML(self.wrap)
			display(vis)
		    
    
