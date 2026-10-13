"""qlab: Rick's quantum lab — statevector sim, optimizers v1-v3, approximate QFT, calibrated noise twin."""
import os,sys
_here=os.path.dirname(os.path.abspath(__file__)); _root=os.path.dirname(_here)
for _p in (_root,_here):
    if _p not in sys.path: sys.path.insert(0,_p)
