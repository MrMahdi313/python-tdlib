from .utils import Type, Method, factorize
from .. import constructors

# monkey patching constructors table
from .table import constructors as cs
for k in cs.keys(): cs[k] = getattr(constructors, k)
