"""Reusable geometry/pin checks (mm)."""
import math
def r(p): return math.hypot(*p)
def in_circle(p,R,c=(0,0)): return math.hypot(p[0]-c[0],p[1]-c[1])<=R
def in_annulus(p,r0,r1): return r0<=r(p)<=r1
def in_rect(p,w,h,c=(0,0)): return abs(p[0]-c[0])<=w/2 and abs(p[1]-c[1])<=h/2
def clearance(a,b,ra=0,rb=0): return math.dist(a,b)-ra-rb
def min_clearance(items,others,ra=0,rb=0):
    return min((clearance(a,b,ra,rb),na,nb) for na,a in items.items() for nb,b in others.items())
def mux_coverage(n_channels,n_mux,ch_per_mux): return n_mux*ch_per_mux>=n_channels, n_mux*ch_per_mux
def check_seal(points,r0,r1): return [n for n,p in points.items() if in_annulus(p,r0,r1)]
def check_outside(points,R): return [n for n,p in points.items() if not in_circle(p,R)]
