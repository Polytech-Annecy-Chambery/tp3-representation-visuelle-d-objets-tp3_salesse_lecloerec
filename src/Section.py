# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import OpenGL.GL as gl

class Section:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: position of the wall 
        # width: width of the wall - mandatory
        # height: height of the wall - mandatory
        # thickness: thickness of the wall
        # color: color of the wall        

        # Sets the parameters
        self.parameters = parameters
        
        # Sets the default parameters
        if 'position' not in self.parameters:
            self.parameters['position'] = [0, 0, 0]        
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')   
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')   
        if 'orientation' not in self.parameters:
            self.parameters['orientation'] = 0              
        if 'thickness' not in self.parameters:
            self.parameters['thickness'] = 0.2    
        if 'color' not in self.parameters:
            self.parameters['color'] = [0.5, 0.5, 0.5]       
        if 'edges' not in self.parameters:
            self.parameters['edges'] = False             
            
        # Objects list
        self.objects = []

        # Generates the wall from parameters
        self.generate()   
        
    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self     

    # Defines the vertices and faces 
    def generate(self):
        self.vertices = [ 
                [0,0,0],
                [0,0,self.parameters['height']],
                [self.parameters['width'], 0, self.parameters['height']],
                [self.parameters['width'], 0, 0],
                [0,self.parameters['thickness'],0],
                [0,self.parameters['thickness'],self.parameters['height']],
                [self.parameters['width'],self.parameters['thickness'] , self.parameters['height']],
                [self.parameters['width'],self.parameters['thickness'] , 0]
                
                ]
                # Définir ici les sommets
        self.faces = [
                [0,1,2,3],
                [0,4,5,1],
                [4,5,6,7],
                [6,2,3,7],
                [1,5,6,2],
                [0,4,7,3],
                # définir ici les faces
                ]   

    # Checks if the opening can be created for the object x
    def canCreateOpening(self, x):
        # A compléter en remplaçant pass par votre code
        pass      
        
    # Creates the new sections for the object x
    def createNewSections(self, x):
        # A compléter en remplaçant pass par votre code
        pass              
        
    # Draws the edges
    def drawEdges(self):
        # A compléter en remplaçant pass par votre code
        for i in self.faces:
            gl.glPushMatrix()
            gl.glTranslatef(0.0,0.0,0.0)
            gl.glRotatef(self.parameters['orientation'],0,0,1)
            gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_LINE)
            gl.glBegin(gl.GL_QUADS)
            gl.glColor3fv([0, 255, 0])
            gl.glVertex3fv(self.vertices[i[0]])
            gl.glVertex3fv(self.vertices[i[1]])
            gl.glVertex3fv(self.vertices[i[2]])
            gl.glVertex3fv(self.vertices[i[3]])
            gl.glEnd()
            gl.glPopMatrix()           
                    
    # Draws the faces
    def draw(self):
        # A compléter en remplaçant pass par votre code
        if self.parameters['edges'] == True :
            self.drawEdges()
        for i in self.faces:
            gl.glPushMatrix()
            gl.glTranslatef(self.parameters['position'][0],self.parameters['position'][1],self.parameters['position'][2])
            gl.glRotatef(self.parameters['orientation'],0,0,1)
            gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL)
            gl.glBegin(gl.GL_QUADS)
            gl.glColor3fv([0.5, 0.5, 0.5])
            gl.glVertex3fv(self.vertices[i[0]])
            gl.glVertex3fv(self.vertices[i[1]])
            gl.glVertex3fv(self.vertices[i[2]])
            gl.glVertex3fv(self.vertices[i[3]])
            gl.glEnd()
            gl.glPopMatrix()
        
  