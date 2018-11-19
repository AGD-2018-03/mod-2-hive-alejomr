
from __future__ import print_function
from IPython.core.magic import (Magics, 
                                magics_class, 
                                line_magic,
                                cell_magic, 
                                line_cell_magic)
import pexpect

CMD = 'hive --silent ' ## para suprimir toda la salida
CMD = '/home/caamartinezre/apache-hive-3.1.0-bin/bin/hive'

@magics_class
class CodeMagic(Magics):

    def __init__(self, shell):
        super(CodeMagic, self).__init__(shell)
        self.child = pexpect.spawn(CMD, timeout=300)
        self.child.expect('hive> ')
        print(self.child.before.decode())

    @cell_magic
    def hive(self, line, cell):
        x = cell.split('\n')
        for y in x:
            self.child.sendline(y)
            result = self.child.expect(['\r\n    > ', '\r\nhive> '])
            print(self.child.before.decode())          
        return None        
        

__ip = get_ipython()
codemagic = CodeMagic(__ip)
__ip.register_magics(codemagic)

