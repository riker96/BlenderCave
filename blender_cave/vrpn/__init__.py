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

import blender_cave.base
import blender_cave.exceptions

try:
    from . import local_devices
    from . import tracker
    from . import analog
    from . import button
    from . import text
except ImportError:
    _VRPN_NOT_AVAILABLE = True
else:
    _VRPN_NOT_AVAILABLE = False

class VRPN(blender_cave.base.Base):
    def __init__(self, parent,  configuration):
        super(VRPN, self).__init__(parent)

        self._devices = []

        if not 'processor_configuration' in configuration:
            return

        self._processor = configuration['module'].Processor(self, configuration['processor_configuration'])

        try:
            device_types = {'button'        : button.Button,
                            'analog'        : analog.Analog,
                            'tracker'       : tracker.Tracker,
                            'text'          : text.Text,
                            'local_devices' : local_devices.LocalDevices}
        except NameError:
            pass
        else:
            for key, className in device_types.items():
                try:
                    elements = configuration[key]
                    del(configuration[key])
                except KeyError:
                    continue
                for element in elements:
                    try:
                        self._devices.append(className(self, element))
                    except blender_cave.exceptions.VRPN_Invalid_Device as method:
                        self.getLogger().warning(method)
        self._available = True

    def start(self):
        for index in range(len(self._devices)):
            self._devices[index].start()
        if hasattr(self, '_processor'):
            self._processor.start()

    def run(self):
        for index in range(len(self._devices)):
            self._devices[index].run()
        if hasattr(self, '_processor'):
            self._processor.idle()

    def getProcessor(self):
        if hasattr(self, '_processor'):
            return self._processor
        return None