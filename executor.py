# import sys
import __main__

import dropin

with open('executed.py', 'rb') as f:
    code = compile(f.read(), '', 'exec')
    dropin.dropin_cb(None)
    globals = __main__.__dict__
    locals = __main__.__dict__
    exec(code, globals, locals)