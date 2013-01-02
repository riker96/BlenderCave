## Copyright © LIMSI-CNRS (2011)
##
## contributor(s) : Jorge Gascon, Damien Touraine, David Poirier-Quinot,
## Laurent Pointal, Julian Adenauer, 
## 
## This software is a computer program whose purpose is to distribute
## blender to render on CAVE(TM) device systems.
## 
## This software is governed by the CeCILL  license under French law and
## abiding by the rules of distribution of free software.  You can  use, 
## modify and/ or redistribute the software under the terms of the CeCILL
## license as circulated by CEA, CNRS and INRIA at the following URL
## "http://www.cecill.info". 
## 
## As a counterpart to the access to the source code and  rights to copy,
## modify and redistribute granted by the license, users are provided only
## with a limited warranty  and the software's author,  the holder of the
## economic rights,  and the successive licensors  have only  limited
## liability. 
## 
## In this respect, the user's attention is drawn to the risks associated
## with loading,  using,  modifying and/or developing or reproducing the
## software by the user in light of its specific status of free software,
## that may mean  that it is complicated to manipulate,  and  that  also
## therefore means  that it is reserved for developers  and  experienced
## professionals having in-depth computer knowledge. Users are therefore
## encouraged to load and test the software's suitability as regards their
## requirements in conditions enabling the security of their systems and/or 
## data to be ensured and,  more generally, to use and operate it in the 
## same conditions as regards security. 
## 
## The fact that you are presently reading this means that you have had
## knowledge of the CeCILL license and that you accept its terms.
## 

from . import base

class Computer(base.Base):
 
    def __init__(self, parent, attrs):
        super(Computer, self).__init__(parent, attrs)

    def startElement(self, name, attrs):
        child = None
        if name == 'screen':
            from . import screen
            child = screen.Screen(self, attrs)
        return self.addChild(child)

    def display(self, indent):
        super(Computer, self).display(indent)

    def getConfiguration(self):
        if len(self._children['screen']) == 0:
            self.raise_error('No screen defined for this computer', False)
        if self.getParser().getOnlyScreens():
            screens = {}
            for screenName in self._children['screen']:
                screens[screenName] = self._children['screen'][screenName].getConfiguration()
            return screens
        screen = self.getParser().getScreen()
        if screen is None:
            if len(self._children['screen']) != 1:
                self.raise_error('Undefined screen !\nYou must at least define BLENDER_CAVE_CONF_SCREEN environment variable or --config as an argument !', False)
            screenObject = self._children.dict['screen'].itervalues().next()
        else:
            try:
                screenObject = self._children['screen'][screen]
            except KeyError:
                self.raise_error('Cannot find screen "' + screen + '" for this computer', False)
        return screenObject

    def addScreenAndGetItsID(self, screen):
        return self._parent.addScreenAndGetItsID(screen)