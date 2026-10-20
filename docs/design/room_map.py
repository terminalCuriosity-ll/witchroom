# Room map v9.
# Camera measured from lofi-vibes-4k-h4-147462594.jpg (scaled to 1040x583) by detecting its
# straight edges and finding where they meet: one-point perspective, but the vanishing point
# sits at the far right, VP = (1010, 229). Horizon (eye level) y = 229.
# Back wall: ceiling line y 20, floor line y 480, left corner x 405 (right wall off-frame).
import math, random, sys
W,Hs=1040,583
VX,HY=1010,229
F,H,ZB,C=669,1.5,4.0,2.75
XL,XR=-3.617,0.6
Zn=1.0
def P(X,Y,Z): return (round(VX+F*X/Z,1), round(HY+F*(H-Y)/Z,1))
def pts(*ps): return " ".join(f"{x},{y}" for x,y in ps)
def poly(ps,fill,extra=''): return f'<polygon points="{pts(*ps)}" fill="{fill}" {extra}/>'
def quad(a,b,c,d,fill,extra=''): return poly([P(*a),P(*b),P(*c),P(*d)],fill,extra)
def line(a,b,col,w=1.5,extra=''): return f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="{col}" stroke-width="{w}" {extra}/>'
def box(X0,X1,Y0,Y1,Z0,Z1,top,front,side,extra=''):
    o=[]
    if X0>0: o.append(quad((X0,Y0,Z0),(X0,Y0,Z1),(X0,Y1,Z1),(X0,Y1,Z0),side,extra))
    if X1<0: o.append(quad((X1,Y0,Z0),(X1,Y0,Z1),(X1,Y1,Z1),(X1,Y1,Z0),side,extra))
    if Y1<H: o.append(quad((X0,Y1,Z0),(X1,Y1,Z0),(X1,Y1,Z1),(X0,Y1,Z1),top,extra))
    if Y0>H: o.append(quad((X0,Y0,Z0),(X1,Y0,Z0),(X1,Y0,Z1),(X0,Y0,Z1),top,extra))
    o.append(quad((X0,Y0,Z0),(X1,Y0,Z0),(X1,Y1,Z0),(X0,Y1,Z0),front,extra))
    return ''.join(o)
FONT='font-family="Share Tech Mono, monospace"'
def lab(x,y,n,t,c="#d9d2ff",anchor="start"):
    return f'<text x="{x:.0f}" y="{y:.0f}" text-anchor="{anchor}" {FONT} font-size="13" fill="{c}" paint-order="stroke" stroke="#060214" stroke-width="3.5"><tspan fill="#ffdf00">{n}</tspan> {t}</text>'
s=[]
s.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0d0230"/><stop offset="0.38" stop-color="#2a0f6e"/><stop offset="0.5" stop-color="#6a2299"/><stop offset="0.53" stop-color="#ff1d8c"/><stop offset="0.6" stop-color="#3a1460"/><stop offset="1" stop-color="#160a2e"/></linearGradient>
<radialGradient id="glow"><stop offset="0" stop-color="#fffbce" stop-opacity="0.6"/><stop offset="1" stop-color="#fffbce" stop-opacity="0"/></radialGradient>
<radialGradient id="lampglow"><stop offset="0" stop-color="#fff3b0" stop-opacity="0.42"/><stop offset="0.45" stop-color="#fff3b0" stop-opacity="0.12"/><stop offset="1" stop-color="#fff3b0" stop-opacity="0"/></radialGradient>
<radialGradient id="circleglow"><stop offset="0" stop-color="#ff00ff" stop-opacity="0.38"/><stop offset="1" stop-color="#ff00ff" stop-opacity="0"/></radialGradient>
<radialGradient id="candleglow"><stop offset="0" stop-color="#ffdf00" stop-opacity="0.38"/><stop offset="1" stop-color="#ffdf00" stop-opacity="0"/></radialGradient>
<radialGradient id="greenglow"><stop offset="0" stop-color="#39ff88" stop-opacity="0.3"/><stop offset="1" stop-color="#39ff88" stop-opacity="0"/></radialGradient>
<radialGradient id="cyanglow"><stop offset="0" stop-color="#00e5ff" stop-opacity="0.22"/><stop offset="1" stop-color="#00e5ff" stop-opacity="0"/></radialGradient>
<radialGradient id="moonorb" cx="0.42" cy="0.4" r="0.65"><stop offset="0" stop-color="#fff6e0"/><stop offset="0.55" stop-color="#ffdca8"/><stop offset="1" stop-color="#ffb060"/></radialGradient>
<radialGradient id="moonglow"><stop offset="0" stop-color="#ffcf8a" stop-opacity="0.42"/><stop offset="0.45" stop-color="#ffb070" stop-opacity="0.12"/><stop offset="1" stop-color="#ffb070" stop-opacity="0"/></radialGradient>
<radialGradient id="orb" cx="0.38" cy="0.35" r="0.7"><stop offset="0" stop-color="#ffffff"/><stop offset="0.35" stop-color="#fffbce"/><stop offset="1" stop-color="#ffcf6b"/></radialGradient>
<linearGradient id="haze" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ff7ad9" stop-opacity="0"/><stop offset="0.5" stop-color="#ff7ad9" stop-opacity="0.3"/><stop offset="1" stop-color="#ff7ad9" stop-opacity="0"/></linearGradient>
<linearGradient id="holo" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#00e5ff" stop-opacity="0.2"/><stop offset="1" stop-color="#00e5ff" stop-opacity="0.06"/></linearGradient>
<filter id="neon" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="2.2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<pattern id="scan" width="4" height="3" patternUnits="userSpaceOnUse"><rect width="4" height="1" fill="#00e5ff" opacity="0.13"/></pattern>
<radialGradient id="lavaglow"><stop offset="0" stop-color="#ff4fb8" stop-opacity="0.45"/><stop offset="0.5" stop-color="#ff4fb8" stop-opacity="0.12"/><stop offset="1" stop-color="#ff4fb8" stop-opacity="0"/></radialGradient>
<linearGradient id="lavaglass" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5a1a6e"/><stop offset="1" stop-color="#9a2a7e"/></linearGradient>
<radialGradient id="tealglow"><stop offset="0" stop-color="#3fe0d0" stop-opacity="0.32"/><stop offset="1" stop-color="#3fe0d0" stop-opacity="0"/></radialGradient>
<linearGradient id="streakR" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#00e5ff" stop-opacity="0"/><stop offset="1" stop-color="#00e5ff" stop-opacity="0.7"/></linearGradient>
<linearGradient id="streakL" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ff7ad9" stop-opacity="0.7"/><stop offset="1" stop-color="#ff7ad9" stop-opacity="0"/></linearGradient>
<linearGradient id="megafade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a1d5c"/><stop offset="1" stop-color="#1a1240"/></linearGradient>
</defs>''')
# ---------------------------------------------------------------- shell
s.append(quad((XL,C,Zn),(XR,C,Zn),(XR,C,ZB),(XL,C,ZB),"#0a031c"))          # ceiling
s.append(quad((XL,0,Zn),(XL,0,ZB),(XL,C,ZB),(XL,C,Zn),"#170a36"))          # left wall
s.append(quad((XL,0,Zn),(XR,0,Zn),(XR,0,ZB),(XL,0,ZB),"#0e0722"))          # floor
s.append(quad((XL,C,ZB),(XR,C,ZB),(XR,0,ZB),(XL,0,ZB),"#1c0d3e"))          # back wall
# skirting on the left wall and the back wall
s.append(quad((XL,0,Zn),(XL,0,ZB),(XL,0.1,ZB),(XL,0.1,Zn),"#241248"))
# floor tiles: depth lines run to the vanishing point, cross lines stay level
for X in [-3.0,-2.5,-2.0,-1.5,-1.0,-0.5,0.0]:
    s.append(line(P(X,0,ZB),P(X,0,Zn),"#1f1342",1.4))
for Z in [3.6,3.25,2.95,2.7]:
    s.append(line(P(XL,0,Z),P(XR,0,Z),"#1f1342",1.4))
# a few tiles picked out, like the patchwork floor in the picture
random.seed(8)
for _ in range(9):
    X=random.choice([-3.0,-2.5,-2.0,-1.5,-1.0,-0.5]); zs=[ZB,3.6,3.25,2.95,2.7]; k=random.randrange(len(zs)-1)
    s.append(quad((X,0,zs[k+1]),(X+0.5,0,zs[k+1]),(X+0.5,0,zs[k]),(X,0,zs[k]),random.choice(["#170d33","#1a1038","#140b2c"])))
# ---------------------------------------------------------------- the window
WX0,WX1,WY0=-3.52,-0.82,0.38
(x0,y0),(x1,y1)=P(WX0,C,ZB),P(WX1,WY0,ZB)
WIN=(x0,y0,x1,y1)
s.append(f'<defs><clipPath id="glass"><rect x="{x0}" y="{y0}" width="{x1-x0:.1f}" height="{y1-y0:.1f}"/></clipPath></defs>')
s.append('<g clip-path="url(#glass)">')
s.append(f'<rect x="{x0}" y="{y0}" width="{x1-x0:.1f}" height="{y1-y0:.1f}" fill="url(#sky)"/>')
random.seed(5)
for _ in range(46):
    sx=random.uniform(x0+6,x1-6); sy=random.uniform(y0+22,HY-40)
    s.append(f'<circle cx="{sx:.0f}" cy="{sy:.0f}" r="{random.choice([1.1,1.5,1.9])}" fill="#f3edf3" opacity="{random.choice([0.55,0.85])}"/>')
# a small far planet, left of the megastructures
s.append(f'<circle cx="{x0+322:.0f}" cy="{y0+182:.0f}" r="12" fill="#2f8a7a" opacity="0.9"/><circle cx="{x0+317:.0f}" cy="{y0+178:.0f}" r="4" fill="#5fd0b0" opacity="0.6"/>')
# the moon and its phase (the clock). Its hour path is only implied now, and it is drawn first,
# so it passes behind everything in the city
ax0,ax1,ay,apk=x0+28,x1-28,HY-12,y0+64
cy_=2*apk-ay
def arc(t): return ((1-t)**2*ax0+2*(1-t)*t*(ax0+ax1)/2+t*t*ax1,(1-t)**2*ay+2*(1-t)*t*cy_+t*t*ay)
mx,my=arc(0.3)
# the phase: the dark side stays inside the disc (a faint earthshine), the lit crescent is the disc minus an offset disc
s.append(f'<defs><mask id="phase"><circle cx="{mx:.0f}" cy="{my:.0f}" r="28" fill="#fff"/><circle cx="{mx+13:.0f}" cy="{my-6:.0f}" r="25" fill="#000"/></mask></defs>')
s.append(f'<circle cx="{mx:.0f}" cy="{my:.0f}" r="72" fill="url(#glow)"/>')
s.append(f'<circle cx="{mx:.0f}" cy="{my:.0f}" r="28" fill="#2a1a5c" stroke="#fffbce" stroke-opacity="0.3" stroke-width="1"/>')
s.append(f'<circle cx="{mx:.0f}" cy="{my:.0f}" r="28" fill="#fffbce" mask="url(#phase)"/>')
MOON=(mx,my)
WINC=["#ffdf00","#ffdf00","#ffd27a","#ffd27a","#ff7ad9","#00e5ff","#b4a7d6","#39ff88"]
def windows(bx0,bx1,top,base,cw,chh,gx,gy,p,op,seed):
    # a grid of lit windows on one building face (faces the window, so the grid stays square-on)
    rnd=random.Random(seed); o=[]
    y=top+gy
    while y<base-chh:
        x=bx0+gx*0.8
        while x<bx1-cw-1:
            if rnd.random()<p:
                o.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{cw}" height="{chh}" fill="{rnd.choice(WINC)}" opacity="{op}"/>')
            x+=cw+gx
        y+=chh+gy
    return ''.join(o)
def skyline(top_lo,top_hi,base,wmin,wmax,col,seed,win,tops=None):
    rnd=random.Random(seed); sk=[(x0,base)]; x=x0; o=[]; lit=[]
    while x<x1:
        w=rnd.uniform(wmin,wmax); h=rnd.uniform(top_lo,top_hi)
        if tops is not None: tops.append((x,x+w,h))
        sk+=[(round(x,1),round(h,1)),(round(min(x+w,x1),1),round(h,1))]
        if rnd.random()<0.25 and w>16: o.append(line((round(x+w/2,1),round(h,1)),(round(x+w/2,1),round(h-rnd.uniform(8,22),1)),col,2))
        lit.append(windows(x+1,min(x+w,x1)-1,h,base,*win,seed*100+len(lit)))
        x+=w
    sk+=[(x1,base)]
    return poly(sk,col)+''.join(o)+''.join(lit)
# megastructures: far away, so a little hazy, but towering over everything else
def mega(cx,tiers,seed,col="url(#megafade)"):
    # tiers: list of (half width, top y), widest first, from the ground up. Floors show as faint
    # level bands, which is what makes them read as enormous; windows are sparse pinpricks.
    o=[]; base=y1; rnd=random.Random(seed)
    for hw,top in tiers:
        o.append(f'<rect x="{cx-hw:.1f}" y="{top}" width="{2*hw:.1f}" height="{base-top:.1f}" fill="{col}"/>')
    for i,(hw,top) in enumerate(tiers):
        nxt=tiers[i+1][1] if i+1<len(tiers) else None
        yy=top+5
        while yy<base:
            if nxt is None or True:
                o.append(f'<rect x="{cx-hw+1:.1f}" y="{yy:.1f}" width="{2*hw-2:.1f}" height="0.8" fill="#b4a7d6" opacity="0.16"/>')
            yy+=5
        o.append(windows(cx-hw+2,cx+hw-2,top+2,base,1.6,1.6,3.2,3.4,0.22,0.9,seed+i))
        o.append(f'<rect x="{cx-hw:.1f}" y="{top}" width="{2*hw:.1f}" height="2.2" fill="#ff7ad9" opacity="0.8"/>')
        o.append(f'<rect x="{cx-hw:.1f}" y="{top}" width="1.6" height="{base-top:.1f}" fill="#00e5ff" opacity="0.45"/><rect x="{cx+hw-1.6:.1f}" y="{top}" width="1.6" height="{base-top:.1f}" fill="#00e5ff" opacity="0.25"/>')
    return ''.join(o)
# megastructure one: a stepped arcology standing behind the twin spires, so they and the city hide most of it
MA=x0+391
s.append(mega(MA,[(50,166),(38,134),(26,110)],71,"#33246a"))
s.append(line((MA,110),(MA,92),"#33246a",3)+f'<circle cx="{MA}" cy="92" r="2.4" fill="#ff1d8c"/>')
# megastructure two: twin spires joined by sky bridges
MB=x0+382
s.append(mega(MB-16,[(17,124),(10,96)],83))
s.append(mega(MB+19,[(19,110),(12,66)],89))
for yb in (132,170):
    s.append(f'<rect x="{MB-1}" y="{yb}" width="4" height="5" fill="#2a1d5c"/><rect x="{MB-1}" y="{yb+1.5}" width="4" height="1.5" fill="#ffdf00" opacity="0.9"/>')
s.append(line((MB+19,66),(MB+19,46),"#2a1d5c",2.5)+f'<circle cx="{MB+19}" cy="46" r="2.2" fill="#ff1d8c"/><circle cx="{MB-16}" cy="96" r="2" fill="#ff1d8c"/>')
# city: far towers above the horizon, then the city below us down to the sill
s.append(skyline(HY-92,HY-18,y1,16,40,"#1e1440",3,(2,2,3,4,0.42,0.7)))
s.append(f'<rect x="{x0}" y="{HY-34}" width="{x1-x0:.1f}" height="68" fill="url(#haze)"/>')
def train(xa,xb,y,h,body,dirn,seed):
    # a hover train barrelling sideways: pale cars with a lit window band, a nose, a headlight,
    # a cyan hover-glow underneath and a light trail streaming out behind
    o=[]; n=max(3,int((xb-xa)/(h*4.2))); carw=(xb-xa)/n
    tail=(xa-170,xa) if dirn>0 else (xb,xb+170)
    g="streakR" if dirn>0 else "streakL"
    o.append(f'<rect x="{tail[0]:.0f}" y="{y+h*0.3:.1f}" width="170" height="{max(1.4,h*0.22):.1f}" fill="url(#{g})"/>')
    o.append(f'<rect x="{tail[0]:.0f}" y="{y+h*0.8:.1f}" width="170" height="{max(1,h*0.12):.1f}" fill="url(#{g})" opacity="0.6"/>')
    o.append(f'<rect x="{xa:.1f}" y="{y+h+1.5:.1f}" width="{xb-xa:.1f}" height="{max(1.2,h*0.16):.1f}" fill="#00e5ff" opacity="0.75" filter="url(#neon)"/>')
    nose=h*1.3
    if dirn>0: shape=[(xa,y+h*0.2),(xb-nose,y),(xb,y+h*0.72),(xb,y+h),(xa,y+h)]
    else: shape=[(xb,y+h*0.2),(xa+nose,y),(xa,y+h*0.72),(xa,y+h),(xb,y+h)]
    o.append(poly([(round(a,1),round(b,1)) for a,b in shape],body,'stroke="#060214" stroke-width="0.8"'))
    o.append(f'<rect x="{xa+(2 if dirn>0 else nose):.1f}" y="{y+h*0.3:.1f}" width="{xb-xa-nose-2:.1f}" height="{h*0.32:.1f}" fill="#1a1038"/>')
    wx=xa+(4 if dirn>0 else nose+2)
    while wx<xb-(nose+3 if dirn>0 else 3):
        o.append(f'<rect x="{wx:.1f}" y="{y+h*0.34:.1f}" width="{max(1.6,h*0.3):.1f}" height="{h*0.24:.1f}" fill="#ffd27a"/>')
        wx+=max(2.8,h*0.48)
    for k in range(1,n):
        cxk=xa+k*carw; o.append(line((round(cxk,1),round(y+h*0.1,1)),(round(cxk,1),round(y+h,1)),"#060214",1))
    o.append(f'<rect x="{xa:.1f}" y="{y+h*0.78:.1f}" width="{xb-xa:.1f}" height="{max(0.8,h*0.08):.1f}" fill="#ff1d8c" opacity="0.85"/>')
    hx=xb if dirn>0 else xa
    o.append(f'<circle cx="{hx:.0f}" cy="{y+h*0.7:.1f}" r="{h*1.8:.1f}" fill="url(#glow)"/><circle cx="{hx:.0f}" cy="{y+h*0.7:.1f}" r="{max(1.2,h*0.2):.1f}" fill="#ffffff"/>')
    return ''.join(o)
s.append(train(x0+150,x0+262,HY-40,6,"#8a7fb8",1,1))
s.append(skyline(HY-30,HY+20,y1,20,52,"#120c26",4,(2,3,4,5,0.45,0.85)))
s.append(train(x0+24,x0+190,HY+20,9,"#a89bd0",-1,2))
# the nearest train runs behind the first row of buildings, just high enough to peek over the rooftops
nt=[]; skyline(HY+40,HY+95,y1,26,70,"#0b0818",9,(3,4,5,6,0.5,0.95),nt)
TXA,TXB,TH=x0+236,x0+446,13
roof=sorted(h for a,b,h in nt if b>TXA and a<TXB); TY=round(roof[len(roof)//2]-TH*0.62,1)
s.append(train(TXA,TXB,TY,TH,"#c9bfe6",1,3))
s.append(skyline(HY+40,HY+95,y1,26,70,"#0b0818",9,(3,4,5,6,0.5,0.95)))
s.append('</g>')
# blinds rolled up under the ceiling (night light), with a pull cord
s.append(f'<rect x="{x0}" y="{y0}" width="{x1-x0:.1f}" height="15" fill="#3a2f55"/><rect x="{x0}" y="{y0+15}" width="{x1-x0:.1f}" height="3" fill="#6b6488"/>')
s.append(line((x1-40,y0+18),(x1-40,y0+150),"#b4a7d6",1.5)+f'<circle cx="{x1-40}" cy="{y0+153}" r="3.5" fill="#fffbce"/>')
BLINDS=(x1-40,y0+153)
# ---------------------------------------------------------------- candle shelf behind the bed

s.append(box(-0.72,XR,0.82,0.86,3.84,ZB,"#5a2a6e","#3a1f50","#3a1f50"))
cand=[("sleep","#c9b8f0",0.24),("lock","#9a7fd6",0.3),("log out","#c04fb0",0.2),("reboot","#8a2a6e",0.27),("shut down","#3a0f24",0.23)]
for i,(nm,col,h) in enumerate(cand):
    X=-0.62+i*0.13; a=P(X,0.86,3.92); t=P(X,0.86+h,3.92)
    s.append(f'<circle cx="{a[0]}" cy="{t[1]-4}" r="22" fill="url(#candleglow)"/>')
    s.append(f'<rect x="{a[0]-4.5}" y="{t[1]}" width="9" height="{a[1]-t[1]:.1f}" fill="{col}" stroke="#060214" stroke-width="1"/>')
    s.append(f'<ellipse cx="{a[0]}" cy="{t[1]-6}" rx="3.2" ry="6" fill="{"#ffdf00" if i<4 else "#b4a7d6"}"/>')
CAN=P(-0.62,0.86+0.3,3.92)
# ---------------------------------------------------------------- wi-fi and bluetooth: one round porthole on the left wall

# one round porthole on the left wall, two halves with no border between them: wi-fi above, bluetooth below.
# Every point is projected from the wall's plane, so it follows the same perspective as the shelves.
XW=XL+0.03
PZ,PY,PR,PRO=3.55,1.75,0.36,0.43
def wp(Z,Y): return P(XW,Y,Z)
def circ(r,a0=0,a1=2*math.pi,n=72): return [wp(PZ+r*math.cos(a0+(a1-a0)*k/n),PY+r*math.sin(a0+(a1-a0)*k/n)) for k in range(n+1)]
def chord(Y):
    # the two points where a level line on the wall (a depth line, so it runs to the vanishing point) meets the glass
    d=math.sqrt(max(PR*PR-(Y-PY)**2,0)); return wp(PZ-d,Y),wp(PZ+d,Y)
m=wp(PZ,PY); s.append(f'<ellipse cx="{m[0]}" cy="{m[1]-20}" rx="95" ry="70" fill="url(#cyanglow)"/><ellipse cx="{m[0]}" cy="{m[1]+40}" rx="85" ry="60" fill="url(#tealglow)"/>')
s.append(poly(circ(PRO)+circ(PR)[::-1],"#2d1f46",'stroke="#060214" stroke-width="1"'))     # rim
for k in range(10):
    a=2*math.pi*k/10+0.31; c=wp(PZ+(PR+PRO)/2*math.cos(a),PY+(PR+PRO)/2*math.sin(a)); rr=F*0.012/PZ
    s.append(f'<circle cx="{c[0]}" cy="{c[1]}" r="{rr+0.6:.1f}" fill="#6b6488"/>')
top=circ(PR,0,math.pi); bot=circ(PR,math.pi,2*math.pi)
# wi-fi half: connected, two friends on the call
s.append(poly(top,"#0b1430"))
s.append(poly(top,"url(#scan)"))
for zf,yf,r,colr in [(-0.4,0.42,0.075,"#ff1d8c"),(0.3,0.46,0.066,"#39ff88")]:
    Z=PZ+PR*zf; Yh=PY+PR*yf; c=wp(Z,Yh); rr=F*r/Z
    s.append(f'<ellipse cx="{c[0]}" cy="{c[1]}" rx="{rr*0.82:.1f}" ry="{rr:.1f}" fill="{colr}" opacity="0.9"/>')
    a=wp(Z-0.1,PY+0.005); b=wp(Z+0.1,PY+0.005); tt=wp(Z,Yh-r*1.5)
    s.append(f'<path d="M{a[0]} {a[1]} Q{tt[0]} {tt[1]-6:.1f} {b[0]} {b[1]} Z" fill="{colr}" opacity="0.9"/>')
# bluetooth half, idle: a soft teal glow in level bands, like the round window in the first Drive room
s.append(poly(bot,"#0f3a44"))
for k in range(1,7):
    Y=PY-k*PR/7; a,b=chord(Y); a2,b2=chord(Y-PR/16)
    s.append(poly([a,b,b2,a2],"#3fe0d0",f'opacity="{0.42-0.05*k:.2f}"'))
# no border between the halves: only the outer edge glows, bright above, soft below
s.append(f'<polyline points="{pts(*top)}" fill="none" stroke="#00e5ff" stroke-width="2.6" filter="url(#neon)"/>')
s.append(f'<polyline points="{pts(*bot)}" fill="none" stroke="#3fe0d0" stroke-width="2" opacity="0.7"/>')
FR1=wp(PZ-PRO*0.2,PY+PRO); FR2=wp(PZ,PY-PRO)
# ---------------------------------------------------------------- a small goth altar under the porthole, built into the window ledge
# The altar's long side runs along the left wall, so all its long edges (top, plinth, lace, arch bases,
# the lines of writing in the book) are depth lines and run to the vanishing point. Edges that cross
# the room stay level, as they must in one-point perspective.
AX0,AX1,AZ0,AZ1,AY=XL,XL+0.42,3.18,ZB,0.88
s.append(box(AX0,AX1-0.02,0,0.06,AZ0+0.02,AZ1-0.02,"#140a26","#140a26","#190d2e"))           # plinth
s.append(box(AX0,AX1-0.04,0.06,AY-0.05,AZ0+0.04,AZ1-0.04,"#1f1236","#1f1236","#24163f"))      # body
s.append(box(AX0,AX1,AY-0.05,AY,AZ0,AZ1,"#3a2452","#2a1a40","#2f1d48"))                      # top slab
def arch(pt,zl,zr,yb,ya,n=10):
    # a pointed gothic arch from zl to zr (along the face), base yb, apex ya; pt(z,y) projects onto the face
    w=zr-zl; ys=ya-0.866*w; o=[pt(zl,yb),pt(zl,ys)]
    for k in range(1,n+1):
        a=math.pi-(math.pi/3)*k/n; o.append(pt(zr+w*math.cos(a),ys+w*math.sin(a)))
    for k in range(1,n+1):
        a=(math.pi/3)-(math.pi/3)*k/n; o.append(pt(zl+w*math.cos(a),ys+w*math.sin(a)))
    o.append(pt(zr,yb)); return o
XA=AX1-0.035
side=lambda z,y:P(XA,y,z)
# two full arches on the stretch in front of the ledge, one shorter arch above the ledge where they join
for zl,zr,yb,ya in [(AZ0+0.08,AZ0+0.24,0.14,0.75),(AZ0+0.28,AZ0+0.43,0.14,0.75),(3.68,3.9,0.5,0.78)]:
    s.append(poly(arch(side,zl,zr,yb,ya),"#120822",'stroke="#8a4ab0" stroke-width="1.3"'))
    s.append(poly(arch(side,zl+0.03,zr-0.03,yb+0.04,ya-0.06),"none",'stroke="#5a2a6e" stroke-width="1"'))
    c=P(XA,(yb+ya)/2-0.05,(zl+zr)/2); s.append(f'<circle cx="{c[0]}" cy="{c[1]}" r="{F*0.022/((zl+zr)/2):.1f}" fill="none" stroke="#c04fb0" stroke-width="1"/>')
ZE=AZ0+0.04
endf=lambda x,y:P(x,y,ZE)
s.append(poly(arch(endf,AX0+0.1,AX1-0.14,0.14,0.75),"#120822",'stroke="#8a4ab0" stroke-width="1.3"'))
# a plain white lace runner along the top, hanging straight over the room-side edge
LZ0,LZ1=AZ0+0.06,AZ1-0.06
s.append(quad((AX1-0.25,AY+0.003,LZ0),(AX1+0.012,AY+0.003,LZ0),(AX1+0.012,AY+0.003,LZ1),(AX1-0.25,AY+0.003,LZ1),"#f3edf3",'opacity="0.9"'))
XLc=AX1+0.012
s.append(quad((XLc,AY+0.003,LZ0),(XLc,AY+0.003,LZ1),(XLc,AY-0.075,LZ1),(XLc,AY-0.075,LZ0),"#f3edf3",'opacity="0.92"'))
# the book stand: a wedge, low at the room side, high at the wall side
SZ0,SZ1=3.36,3.74
SXf,SXb,SYf,SYb=AX1-0.06,AX1-0.31,AY+0.04,AY+0.18
gl=P(AX1-0.18,AY+0.12,(SZ0+SZ1)/2); s.append(f'<ellipse cx="{gl[0]}" cy="{gl[1]}" rx="80" ry="55" fill="url(#greenglow)"/>')
s.append(quad((SXf,AY,SZ0),(SXb,AY,SZ0),(SXb,SYb,SZ0),(SXf,SYf,SZ0),"#2d1f46",'stroke="#060214" stroke-width="0.8"'))   # near end
s.append(quad((SXf,AY,SZ0),(SXf,AY,SZ1),(SXf,SYf,SZ1),(SXf,SYf,SZ0),"#3a2850",'stroke="#060214" stroke-width="0.8"'))   # room side
s.append(quad((SXf,SYf,SZ0),(SXf,SYf,SZ1),(SXb,SYb,SZ1),(SXb,SYb,SZ0),"#4a3466",'stroke="#060214" stroke-width="0.8"'))  # slope
def onstand(u,v,lift=0.012):
    # u: 0..1 along the wall (near to far), v: 0..1 up the slope (room side to wall side)
    return P(SXf-(SXf-SXb)*v, SYf+(SYb-SYf)*v+lift, SZ0+(SZ1-SZ0)*u)
s.append(poly([onstand(-0.03,-0.05,0.006),onstand(1.03,-0.05,0.006),onstand(1.03,1.04,0.006),onstand(-0.03,1.04,0.006)],"#1a0f2a",'stroke="#8a4ab0" stroke-width="1"'))  # cover
s.append(poly([onstand(0.02,0.02),onstand(0.5,0.05,0.004),onstand(0.5,0.97,0.004),onstand(0.02,0.96)],"#0e0b1a",'stroke="#39ff88" stroke-width="1.2"'))
s.append(poly([onstand(0.5,0.05,0.004),onstand(0.98,0.02),onstand(0.98,0.96),onstand(0.5,0.97,0.004)],"#0e0b1a",'stroke="#39ff88" stroke-width="1.2"'))
for k in range(5):
    v=0.18+k*0.16
    for ua,ub in [(0.08,0.44),(0.56,0.92 if k<4 else 0.74)]:
        s.append(line(onstand(ua,v),onstand(ub,v),"#39ff88",1.2,'opacity="0.95"'))
rb=onstand(0.62,0.0); rb2=P(SXf+0.004,AY+0.005,SZ0+(SZ1-SZ0)*0.64)
s.append(line(rb,rb2,"#ff1d8c",2))
BOOK=onstand(0.1,0.0)
# a little skull at the near end (the ivy at the far end is drawn with the plants)
sk=P(AX1-0.17,AY,AZ0+0.09); u=F*0.01/(AZ0+0.09)
s.append(f'<g fill="#e8e0f0" stroke="#060214" stroke-width="0.8"><circle cx="{sk[0]}" cy="{sk[1]-u*5.2:.1f}" r="{u*4:.1f}"/><rect x="{sk[0]-u*2.4:.1f}" y="{sk[1]-u*3:.1f}" width="{u*4.8:.1f}" height="{u*3:.1f}" rx="{u:.1f}"/></g><circle cx="{sk[0]-u*1.6:.1f}" cy="{sk[1]-u*4.8:.1f}" r="{u*1.1:.1f}" fill="#060214"/><circle cx="{sk[0]+u*1.6:.1f}" cy="{sk[1]-u*4.8:.1f}" r="{u*1.1:.1f}" fill="#060214"/>')
ALTAR=P(AX1,0.45,AZ0+0.05)
# ---------------------------------------------------------------- the window ledge, one piece with the altar: same wood, arches, trim and lace
SX0=AX1-0.01; SX1=WX1+0.05
s.append(box(SX0,SX1,0,0.06,3.66,ZB,"#140a26","#140a26","#190d2e"))                     # plinth, as on the altar
s.append(box(SX0,SX1,0.06,WY0,3.68,ZB,"#1f1236","#1f1236","#24163f"))                   # body
s.append(box(SX0,SX1,WY0,WY0+0.06,3.62,ZB,"#3a2452","#2a1a40","#2f1d48"))               # top slab
front=lambda x,y:P(x,y,3.68)
n_arch=8; aw=0.21; gap=(SX1-0.04-(SX0+0.06)-n_arch*aw)/(n_arch-1)
for k in range(n_arch):
    xl=SX0+0.06+k*(aw+gap)
    s.append(poly(arch(front,xl,xl+aw,0.1,0.34),"#120822",'stroke="#8a4ab0" stroke-width="1.3"'))
    s.append(poly(arch(front,xl+0.03,xl+aw-0.03,0.13,0.3),"none",'stroke="#5a2a6e" stroke-width="1"'))
# a plain white lace runner hanging straight over the ledge's front edge, the same as on the altar
LY=WY0+0.06; LX0,LX1=SX0+0.03,SX1-0.03
s.append(quad((LX0,LY+0.002,3.615),(LX1,LY+0.002,3.615),(LX1,LY-0.065,3.615),(LX0,LY-0.065,3.615),"#f3edf3",'opacity="0.92"'))
LEDGE=P(-1.6,0.2,3.62)
# ---------------------------------------------------------------- bed, far right, head to the back wall, no headboard

BX0,BZ0=-0.8,1.8
s.append(box(BX0,XR,0,0.3,BZ0,3.98,"#2a1034","#2d1238","#2a1034"))
s.append(box(BX0,XR,0.3,0.55,BZ0,3.98,"#4a1d5c","#3c1850","#43195a"))
s.append(box(BX0+0.06,BX0+0.66,0.55,0.67,3.42,3.9,"#c9bfe6","#a89bd0","#a89bd0"))     # pillows
s.append(box(BX0+0.72,XR-0.04,0.55,0.67,3.42,3.9,"#b4a7d6","#9d90c4","#9d90c4"))
s.append(box(BX0,XR,0.55,0.61,BZ0,3.28,"#5a2470","#4a1d5c","#4a1d5c"))                 # blanket
s.append(quad((BX0,0.61,BZ0),(XR,0.61,BZ0),(XR,0.34,BZ0-0.03),(BX0,0.34,BZ0-0.03),"#4f1f63"))   # blanket draped over the foot
s.append(line(P(BX0,0.612,3.2),P(XR,0.612,3.2),"#7d3a96",2))
BED=P(BX0,0.6,3.05)
# ritual circle on the bed: volume as lit segments, battery as the glow; simple, a little cyber
CXc,CZc,R,YB=-0.28,2.82,0.36,0.615
def bp(r,a): return P(CXc+r*math.cos(a),YB,CZc+r*math.sin(a))
def ring(r,steps=96): return [bp(r,2*math.pi*k/steps) for k in range(steps)]
cc=P(CXc,YB,CZc)
s.append(f'<ellipse cx="{cc[0]}" cy="{cc[1]}" rx="140" ry="50" fill="url(#circleglow)"/>')
s.append(poly(ring(R),"none",'stroke="#ff00ff" stroke-width="2.6" filter="url(#neon)"'))
s.append(poly(ring(R*0.62),"none",'stroke="#ff00ff" stroke-width="1.2"'))
nseg,lit=20,13
for k in range(nseg):
    a0=2*math.pi*(k+0.12)/nseg-math.pi/2; a1=2*math.pi*(k+0.88)/nseg-math.pi/2
    on=k<lit
    seg=[bp(R*0.78,a0+(a1-a0)*j/4) for j in range(5)]+[bp(R*0.9,a1-(a1-a0)*j/4) for j in range(5)]
    s.append(poly(seg,"#ff00ff" if on else "#4a1d5c",f'opacity="{0.95 if on else 0.8}"'))
tri=[bp(R*0.62,-math.pi/2+2*math.pi*k/3) for k in range(3)]
s.append(poly(tri,"none",'stroke="#ff00ff" stroke-width="1.2"'))
for p in tri: s.append(f'<rect x="{p[0]-2.5}" y="{p[1]-2.5}" width="5" height="5" fill="#ff00ff"/>')
s.append(poly(ring(R*0.12,32),"#ff00ff",'opacity="0.9"'))
# the familiar, curled up asleep on the end of the bed
cx,cy=P(-0.64,0.61,2.04); k=F*0.009/2.04
def kp(a,b): return f"{cx+a*k:.1f},{cy+b*k:.1f}"
s.append(f'<ellipse cx="{cx}" cy="{cy-k*1:.1f}" rx="{k*17:.1f}" ry="{k*3:.1f}" fill="#060214" opacity="0.45"/>')   # shadow on the blanket
s.append(f'<path d="M{kp(-14,-1)} C{kp(-16,-12)} {kp(-4,-17)} {kp(5,-15)} C{kp(13,-13)} {kp(17,-7)} {kp(15,-1)} Z" fill="#0e0b1a" stroke="#b4a7d6" stroke-width="1.2"/>')     # body
s.append(f'<path d="M{kp(-13,-1.5)} C{kp(-9,2)} {kp(4,2.5)} {kp(12,-1)}" fill="none" stroke="#0e0b1a" stroke-width="{k*2.6:.1f}" stroke-linecap="round"/>')                  # tail wrapped round the front
s.append(f'<path d="M{kp(-13,-1.5)} C{kp(-9,2)} {kp(4,2.5)} {kp(12,-1)}" fill="none" stroke="#b4a7d6" stroke-width="0.9" opacity="0.6"/>')
s.append(f'<circle cx="{cx+k*10:.1f}" cy="{cy-k*7:.1f}" r="{k*5.6:.1f}" fill="#0e0b1a" stroke="#b4a7d6" stroke-width="1.2"/>')                                         # head, tucked
s.append(f'<polygon points="{kp(6,-11)} {kp(7,-16.5)} {kp(10,-12)}" fill="#0e0b1a" stroke="#b4a7d6" stroke-width="1.1"/><polygon points="{kp(11.5,-12.4)} {kp(15,-16)} {kp(15.4,-10.6)}" fill="#0e0b1a" stroke="#b4a7d6" stroke-width="1.1"/>')
s.append(f'<path d="M{kp(8.6,-7)} q{k*1.4:.1f},{k*1.2:.1f} {k*2.8:.1f},0" stroke="#39ff88" stroke-width="1.3" fill="none"/><path d="M{kp(12.6,-7.4)} q{k*1.2:.1f},{k*1.1:.1f} {k*2.4:.1f},0" stroke="#39ff88" stroke-width="1.3" fill="none"/>')
FAM=(cx,cy)
FAMR=cx+k*17
# her messages, tucked into the bottom-right corner, just clear of her
def bubble(bx,by,w,lines,fill="#f3edf3",tail=False,ink="#060214"):
    h=9+15*len(lines)
    if tail:   # a little tail on the left, pointing back at the familiar
        o=f'<polygon points="{bx},{by} {bx+w},{by} {bx+w},{by+h} {bx},{by+h} {bx},{by+h-7} {bx-11},{by+h-12} {bx},{by+h-17}" fill="{fill}" stroke="#060214" stroke-width="2"/>'
    else:
        o=f'<rect x="{bx}" y="{by}" width="{w}" height="{h}" fill="{fill}" stroke="#060214" stroke-width="2"/>'
    for i,l in enumerate(lines): o+=f'<text x="{bx+8}" y="{by+18+15*i}" font-family="&quot;Goudy Bookletter 1911&quot;, serif" font-size="13" fill="{ink}">{l}</text>'
    return o,h
BW=176; BXr=W-6-BW
b2,h2=bubble(BXr,0,BW,["mrrp! you are allowed","to rest. you're doing well."],tail=True)
b1,h1=bubble(BXr,0,BW,["Ash: are you coming","to the gig tonight?"],fill="#b4a7d6")
y2=Hs-6-h2; y1b=y2-7-h1
s.append(f'<g transform="translate(0,{y1b})">{b1}</g><g transform="translate(0,{y2})">{b2}</g>')
NOTE=(BXr,y1b)
# ---------------------------------------------------------------- six plants, each a different kind, each on its own
def xf(pts_,ox,oy,ang,sc):
    # rotate local leaf points (y up) by ang degrees from vertical, scale, and place at (ox,oy) on screen
    a=math.radians(ang); ca,sa=math.cos(a),math.sin(a)
    return [(round(ox+sc*(x*ca+y*sa),1),round(oy-sc*(-x*sa+y*ca),1)) for x,y in pts_]
def pot(cx,by,u,h,wt,wb,col,band=None):
    # a pot facing us: trapezoid body, a rim, an optional band
    o=poly([(cx-u*wb/2,by),(cx+u*wb/2,by),(cx+u*wt/2,by-u*h),(cx-u*wt/2,by-u*h)],col,'stroke="#060214" stroke-width="0.9"')
    o+=f'<rect x="{cx-u*wt/2-u*0.8:.1f}" y="{by-u*h-u*2:.1f}" width="{u*wt+u*1.6:.1f}" height="{u*2.4:.1f}" fill="{col}" stroke="#060214" stroke-width="0.9"/>'
    if band: o+=f'<rect x="{cx-u*(wt+wb)/4:.1f}" y="{by-u*h*0.55:.1f}" width="{u*(wt+wb)/2:.1f}" height="{u*1.4:.1f}" fill="{band}" opacity="0.85"/>'
    return o
# 1. monstera, on the floor in the corner past the bookshelves, in front of the altar
mb=P(-3.2,0,2.98); u=F*0.0088/2.98
s.append(f'<ellipse cx="{mb[0]}" cy="{mb[1]}" rx="{u*16:.1f}" ry="{u*3:.1f}" fill="#060214" opacity="0.5"/>')
leaf=[]
for i in range(25):
    t=i/24; w=0.5*math.sin(math.pi*min(1,0.12+0.95*t))**0.9
    leaf.append((-w,t))
leaf=[(0.0,0.06)]+leaf+[(-x,y) for x,y in leaf[::-1]]
mt=(mb[0],mb[1]-u*22)
for ang,L,col,sx in [(-62,30,"#24603e",-14),(-30,38,"#2f7a4f",-6),(5,42,"#3f9a5f",0),(38,36,"#2f7a4f",6),(66,30,"#24603e",13),(-8,30,"#3f9a5f",-3)]:
    a=math.radians(ang); ex=mt[0]+u*sx+math.sin(a)*u*L*0.75; ey=mt[1]-math.cos(a)*u*L*0.75
    s.append(f'<path d="M{mt[0]+u*sx*0.2:.1f} {mt[1]:.1f} Q{mt[0]+u*sx:.1f} {ey+u*8:.1f} {ex:.1f} {ey:.1f}" stroke="#2f6b3a" stroke-width="{u*0.9:.1f}" fill="none"/>')
    sz=u*L*0.62; lp=xf(leaf,ex,ey,ang*1.15,sz)
    s.append(poly(lp,col,'stroke="#14361f" stroke-width="0.8"'))
    for tt in [0.3,0.48,0.66,0.82]:
        for sd in (-1,1):
            w=0.5*math.sin(math.pi*min(1,0.12+0.95*tt))**0.9
            seg=xf([(sd*w*1.02,tt),(sd*w*0.42,tt-0.05)],ex,ey,ang*1.15,sz)
            s.append(line(seg[0],seg[1],"#0e0722",1.6))
    mid=xf([(0,0.05),(0,0.9)],ex,ey,ang*1.15,sz); s.append(line(mid[0],mid[1],"#14361f",0.9))
s.append(pot(mb[0],mb[1],u,22,26,20,"#1a1030","#ff1d8c"))
MON=(mb[0],mb[1]-u*60)
# ---------------------------------------------------------------- bookshelves along the left wall (every board runs to the vanishing point)
BXa,BXb,BZa,BZb,BTop=XL,XL+0.36,1.7,2.8,2.6
s.append(quad((BXb,0,BZa),(BXb,0,BZb),(BXb,BTop,BZb),(BXb,BTop,BZa),"#1a1530"))
s.append(quad((BXb,0,BZb),(BXa,0,BZb),(BXa,BTop,BZb),(BXb,BTop,BZb),"#14102a"))
boards=[0.06,0.42,0.78,1.14,1.5,1.86,2.22]
random.seed(11)
HERB=["#2f7a4f","#3f9a5f","#39ff88","#7a5ab0","#4fbf8f"]
POT=["#b0583a","#7a3b2a","#6b6488"]
BOOKC=["#4a1d5c","#b4a7d6","#39ff88","#ff1d8c","#ffdf00","#6b6488","#2d6b8a","#8a2a6e"]
herbshelf=0.42
hgshelf,HGZ=1.86,2.4
pearlshelf,PLZ=1.5,2.6
PEARL=None
lavashelf,LVZ=0.78,2.56
LAVA=None
def lavalamp(lb,u):
    # a gentle lava lamp, drawn face-on (it is round, so it looks the same from any side); u = pixels per cm
    def lvl(h): return round(lb[1]-u*h,1)
    o=f'<ellipse cx="{lb[0]}" cy="{lvl(16)}" rx="{u*14:.1f}" ry="{u*17:.1f}" fill="url(#lavaglow)"/>'
    o+=poly([(lb[0]-u*5,lb[1]),(lb[0]+u*5,lb[1]),(lb[0]+u*2.7,lvl(8)),(lb[0]-u*2.7,lvl(8))],"#6b6488",'stroke="#060214" stroke-width="0.8"')
    o+=poly([(lb[0]-u*2.7,lvl(8)),(lb[0]+u*2.7,lvl(8)),(lb[0]+u*4.2,lvl(14)),(lb[0]+u*2,lvl(27)),(lb[0]-u*2,lvl(27)),(lb[0]-u*4.2,lvl(14))],"url(#lavaglass)",'stroke="#ff7ad9" stroke-width="0.8"')
    for bx,by,rx,ry in [(0,10,2.3,1.4),(-0.7,16,1.5,2.1),(0.8,22,1.1,1.4)]:
        o+=f'<ellipse cx="{lb[0]+u*bx:.1f}" cy="{lvl(by)}" rx="{u*rx:.1f}" ry="{u*ry:.1f}" fill="#ff8ad0"/>'
    o+=poly([(lb[0]-u*2,lvl(27)),(lb[0]+u*2,lvl(27)),(lb[0]+u*1.1,lvl(30)),(lb[0]-u*1.1,lvl(30))],"#6b6488",'stroke="#060214" stroke-width="0.8"')
    return o,(lb[0],lvl(30))
HG=None
for i,Y in enumerate(boards):
    top=boards[i+1] if i+1<len(boards) else BTop
    # board: top or underside depending on eye level, then its front edge
    yy=Y+0.04
    surf=yy if yy<H else Y
    s.append(quad((BXa,surf,BZa),(BXb,surf,BZa),(BXb,surf,BZb),(BXa,surf,BZb),"#6a2b7a" if yy<H else "#3a1a4a"))
    s.append(quad((BXb,Y,BZa),(BXb,Y,BZb),(BXb,yy,BZb),(BXb,yy,BZa),"#b04aba"))
    Z=BZa+0.03
    while Z<BZb-0.06:
        if Y==hgshelf and HGZ-0.06<Z<HGZ+0.1:
            # the hourglass, standing among the books
            hx,hy=P(BXb-0.1,yy,HGZ+0.06); ht=F*0.22/(HGZ+0.06); hw=F*0.055/(HGZ+0.06)
            s.append(f'<ellipse cx="{hx}" cy="{hy-ht*0.55:.1f}" rx="34" ry="34" fill="url(#candleglow)"/>')
            s.append(f'<rect x="{hx-hw-3:.1f}" y="{hy-4:.1f}" width="{2*hw+6:.1f}" height="4" fill="#6b4a2a"/><rect x="{hx-hw-3:.1f}" y="{hy-ht:.1f}" width="{2*hw+6:.1f}" height="4" fill="#6b4a2a"/>')
            s.append(f'<line x1="{hx-hw-1:.1f}" y1="{hy-ht+2:.1f}" x2="{hx-hw-1:.1f}" y2="{hy-2:.1f}" stroke="#6b4a2a" stroke-width="2"/><line x1="{hx+hw+1:.1f}" y1="{hy-ht+2:.1f}" x2="{hx+hw+1:.1f}" y2="{hy-2:.1f}" stroke="#6b4a2a" stroke-width="2"/>')
            s.append(f'<polygon points="{hx-hw:.1f},{hy-ht+4:.1f} {hx+hw:.1f},{hy-ht+4:.1f} {hx},{hy-ht/2:.1f} {hx+hw:.1f},{hy-4:.1f} {hx-hw:.1f},{hy-4:.1f} {hx},{hy-ht/2:.1f}" fill="#1a0c3a" fill-opacity="0.6" stroke="#d9d2ff" stroke-width="1.3"/>')
            s.append(f'<polygon points="{hx-hw*0.62:.1f},{hy-ht+8:.1f} {hx+hw*0.62:.1f},{hy-ht+8:.1f} {hx},{hy-ht/2-3:.1f}" fill="#ffdf00"/><polygon points="{hx-hw*0.85:.1f},{hy-5:.1f} {hx+hw*0.85:.1f},{hy-5:.1f} {hx},{hy-14:.1f}" fill="#ffdf00"/><line x1="{hx}" y1="{hy-ht/2:.1f}" x2="{hx}" y2="{hy-14:.1f}" stroke="#ffdf00" stroke-width="1"/>')
            HG=(hx,hy-ht); Z=HGZ+0.16; continue
        if Y==lavashelf and LVZ-0.04<Z<LVZ+0.12:
            # the lava lamp, standing among the books
            o,LAVA=lavalamp(P(BXb-0.12,yy,LVZ+0.05),F*0.01/(LVZ+0.05))
            s.append(o); Z=LVZ+0.16; continue
        if Y==pearlshelf and PLZ-0.04<Z<PLZ+0.12:
            # a string-of-pearls in a little pot, its strands spilling over the shelf's edge
            pz=PLZ+0.01; pw=0.09; ph=0.07
            s.append(quad((BXb-0.03,yy,pz),(BXb-0.03,yy,pz+pw),(BXb-0.03,yy+ph,pz+pw+0.006),(BXb-0.03,yy+ph,pz-0.006),"#2d1f46",'stroke="#060214" stroke-width="0.8"'))
            s.append(quad((BXb-0.03,yy+ph,pz-0.006),(BXb-0.03,yy+ph,pz+pw+0.006),(BXb-0.03,yy+ph+0.012,pz+pw+0.006),(BXb-0.03,yy+ph+0.012,pz-0.006),"#6b6488"))
            rnd=random.Random(41)
            for j in range(9):
                z=pz+0.01+j*(pw-0.02)/8; c=P(BXb-0.03,yy+ph+0.02+0.012*math.sin(j),z)
                s.append(f'<circle cx="{c[0]}" cy="{c[1]}" r="{F*0.007/z+0.4:.1f}" fill="#7fd38a" stroke="#1d4a2a" stroke-width="0.5"/>')
            for j,(dz,L) in enumerate([(-0.01,0.22),(0.015,0.34),(0.04,0.27),(0.065,0.4),(0.09,0.19),(0.105,0.3)]):
                z0=pz+dz; pts_=[(BXb-0.03,yy+ph+0.01,z0),(BXb+0.006,yy+0.03,z0+0.004)]
                n=int(L/0.022)
                for q in range(1,n+1): pts_.append((BXb+0.008,yy+0.03-q*0.022,z0+0.006+0.01*math.sin(q*0.7+j)))
                pp=[P(*a) for a in pts_]
                s.append(f'<polyline points="{pts(*pp)}" fill="none" stroke="#2f6b3a" stroke-width="0.8"/>')
                for c in pp[1:]: s.append(f'<circle cx="{c[0]}" cy="{c[1]}" r="{F*0.0065/z0+0.3:.1f}" fill="#8fe39a" stroke="#1d4a2a" stroke-width="0.4"/>')
            PEARL=P(BXb+0.008,yy-0.25,pz+0.05)
            Z=pz+pw+0.04; continue
        if Y==herbshelf and Z>2.4:
            # a few herb pots tucked among the books: the file manager
            w=0.1; ph=0.1
            s.append(quad((BXb-0.03,yy,Z),(BXb-0.03,yy,Z+w),(BXb-0.03,yy+ph,Z+w-0.01),(BXb-0.03,yy+ph,Z+0.01),random.choice(POT)))
            c=P(BXb-0.03,yy+ph+0.07,Z+w/2); r=F*0.06/(Z+w/2); col=random.choice(HERB)
            s.append(f'<ellipse cx="{c[0]}" cy="{c[1]}" rx="{r*0.75:.1f}" ry="{r:.1f}" fill="{col}" opacity="0.92"/><ellipse cx="{c[0]-r*0.5:.1f}" cy="{c[1]+r*0.45:.1f}" rx="{r*0.45:.1f}" ry="{r*0.6:.1f}" fill="{col}" opacity="0.75"/><ellipse cx="{c[0]+r*0.5:.1f}" cy="{c[1]+r*0.4:.1f}" rx="{r*0.45:.1f}" ry="{r*0.6:.1f}" fill="{col}" opacity="0.75"/>')
            Z+=w+0.04; continue
        if random.random()<0.1:
            # a short stack lying flat
            for k in range(3):
                hh=0.028; s.append(quad((BXb-0.03,yy+k*hh,Z),(BXb-0.03,yy+k*hh,Z+0.16),(BXb-0.03,yy+(k+1)*hh,Z+0.16),(BXb-0.03,yy+(k+1)*hh,Z),random.choice(BOOKC),'stroke="#060214" stroke-width="0.6"'))
            Z+=0.19; continue
        dz=random.uniform(0.026,0.05); h=random.uniform(0.62,0.92)*(top-yy-0.03)
        col=random.choice(BOOKC); op=random.choice([0.7,0.85,1])
        s.append(quad((BXb-0.03,yy,Z),(BXb-0.03,yy,Z+dz),(BXb-0.03,yy+h,Z+dz),(BXb-0.03,yy+h,Z),col,f'opacity="{op}" stroke="#060214" stroke-width="0.6"'))
        Z+=dz+random.uniform(0.004,0.02)
SHELF=P(BXb,1.5,2.2); HERBS=P(BXb,herbshelf+0.04,2.45)
# ---------------------------------------------------------------- plants, continued
# 3. english ivy, in a pot on the far end of the altar, trailing over its edge
ib=P(AX1-0.1,AY,AZ1-0.12); u=F*0.01/(AZ1-0.12)
ivyleaf=[(0,0),(-0.3,0.12),(-0.52,0.4),(-0.26,0.46),(-0.3,0.78),(0,1),(0.3,0.78),(0.26,0.46),(0.52,0.4),(0.3,0.12)]
rnd=random.Random(23)
for j,(dz,L) in enumerate([(-0.08,0.3),(-0.02,0.38),(0.04,0.26)]):
    z0=AZ1-0.12+dz
    path3=[(AX1-0.1,AY+0.07,z0),(AX1-0.03,AY+0.03,z0+0.01),(AX1+0.016,AY-0.01,z0+0.015)]
    for q in range(1,int(L/0.06)+1): path3.append((AX1+0.018,AY-0.01-q*0.06,z0+0.015+0.015*math.sin(q*1.1+j)))
    pp=[P(*a_) for a_ in path3]
    s.append(f'<polyline points="{pts(*pp)}" fill="none" stroke="#2f5a2a" stroke-width="1"/>')
    for q,c in enumerate(pp[1:]):
        lp=xf(ivyleaf,c[0],c[1],(140 if q%2 else 220)+rnd.uniform(-15,15),u*4.6*(1-0.2*q/len(pp)))
        s.append(poly(lp,rnd.choice(["#2f6b3a","#24603e","#3f7a45"]),'stroke="#c9e8b0" stroke-width="0.5"'))
s.append(pot(ib[0],ib[1],u,8,10,7,"#2d1f46","#8a4ab0"))
for k in range(6):
    a_=math.pi*(0.15+0.7*k/5); c=(ib[0]+math.cos(a_)*u*5.5,ib[1]-u*9.5-math.sin(a_)*u*3)
    lp=xf(ivyleaf,c[0],c[1],-70+28*k,u*4.4)
    s.append(poly(lp,"#2f6b3a" if k%2 else "#3f7a45",'stroke="#c9e8b0" stroke-width="0.5"'))
IVY=(ib[0],ib[1]-u*14)
# 4. pothos, hanging in a macrame sling in front of the window's left edge
hp=P(-2.72,2.28,3.25); u=F*0.01/3.25
s.append(line((hp[0],0),(hp[0],round(hp[1]-u*30,1)),"#b4a7d6",1.1))
for dx in (-8,0,8):
    s.append(line((hp[0],round(hp[1]-u*30,1)),(round(hp[0]+u*dx,1),round(hp[1]-u*12,1)),"#b4a7d6",1.1))
s.append(pot(hp[0],hp[1],u,12,17,12,"#3a2850","#39ff88"))
heart=[(0,0),(-0.45,0.35),(-0.42,0.75),(-0.2,0.95),(0,0.82),(0.2,0.95),(0.42,0.75),(0.45,0.35)]
rnd=random.Random(17)
for dx,L,sw in [(-8,46,-1),(-4,62,1),(1,38,-1),(5,56,1),(8,30,1),(-1,24,-1)]:
    x=hp[0]+u*dx; y=hp[1]-u*12; vine=[(round(x,1),round(y,1))]
    for q in range(1,int(L/5)+1):
        vine.append((round(x+u*sw*2.2*math.sin(q*0.9+dx),1),round(y+u*5*q,1)))
    s.append(f'<polyline points="{pts(*vine)}" fill="none" stroke="#2f6b3a" stroke-width="1"/>')
    for q,(vx,vy) in enumerate(vine[1:]):
        side=1 if q%2 else -1
        lp=xf([(a*1.0,b) for a,b in heart],vx,vy,180+side*55,u*5.6)
        s.append(poly(lp,rnd.choice(["#3f9a5f","#4fbf8f","#2f7a4f","#9ad06a"]),'stroke="#14361f" stroke-width="0.6"'))
POTH=(hp[0],hp[1])
# 5. boston fern, hanging high in the corner above the head of the bed
fp=P(-0.05,1.72,3.7); u=F*0.01/3.7
s.append(line((fp[0],0),(fp[0],round(fp[1]-u*26,1)),"#b4a7d6",1.1))
for dx in (-9,9):
    s.append(line((fp[0],round(fp[1]-u*26,1)),(round(fp[0]+u*dx,1),round(fp[1]-u*13,1)),"#b4a7d6",1.1))
fr_base=(fp[0],fp[1]-u*13)
for ang,L in [(-100,40),(-75,48),(-45,40),(-20,30),(0,26),(20,30),(45,40),(75,48),(100,40),(-130,30),(130,30)]:
    # each frond arcs out and droops; little leaflets down both sides
    a=math.radians(ang); fr=[]
    for q in range(13):
        t=q/12; d=u*L*t
        fr.append((fr_base[0]+math.sin(a)*d, fr_base[1]-math.cos(a)*d*0.8+u*0.012*(L*t)**2))
    s.append(f'<polyline points="{pts(*[(round(x,1),round(y,1)) for x,y in fr])}" fill="none" stroke="#2f7a4f" stroke-width="1.1"/>')
    for q in range(1,12):
        (xa,ya),(xb,yb)=fr[q],fr[q+1]; dx_,dy_=xb-xa,yb-ya; n=math.hypot(dx_,dy_) or 1
        nx,ny=-dy_/n,dx_/n; lw=u*3.2*(1-q/13)
        for sd in (-1,1):
            s.append(line((round(xa,1),round(ya,1)),(round(xa+sd*nx*lw+dx_*0.5,1),round(ya+sd*ny*lw+dy_*0.5,1)),"#4fbf8f",1.2))
s.append(pot(fp[0],fp[1],u,13,20,15,"#1a1030","#ff7ad9"))
FERN=(fp[0],fp[1])
# ---------------------------------------------------------------- the light: a glowing moon pendant, top right

# the moon lamp from the purple bedroom picture, hung on one plain cord where the light was
LmX,LmY,LmZ=-0.42,2.1,3.1
lc=P(LmX,LmY,LmZ); lr=F*0.11/LmZ
s.append(f'<ellipse cx="{lc[0]}" cy="{lc[1]+20}" rx="200" ry="160" fill="url(#moonglow)"/>')
s.append(line((lc[0],0),(lc[0],round(lc[1]-lr-6,1)),"#4a3a6c",2))
s.append(f'<rect x="{lc[0]-5}" y="{lc[1]-lr-8:.1f}" width="10" height="5" rx="1.5" fill="#8a4a6a"/>')
s.append(f'<circle cx="{lc[0]}" cy="{lc[1]}" r="{lr+8:.1f}" fill="#ffcf8a" opacity="0.22"/>')
s.append(f'<circle cx="{lc[0]}" cy="{lc[1]}" r="{lr:.1f}" fill="url(#moonorb)" stroke="#ff9d3d" stroke-width="2"/>')
for dx,dy,rx,ry,op in [(-0.35,-0.25,0.32,0.22,0.35),(0.25,-0.4,0.22,0.15,0.3),(0.2,0.2,0.36,0.24,0.32),(-0.3,0.42,0.22,0.14,0.28),(0.5,0.05,0.12,0.18,0.25)]:
    s.append(f'<ellipse cx="{lc[0]+dx*lr:.1f}" cy="{lc[1]+dy*lr:.1f}" rx="{rx*lr:.1f}" ry="{ry*lr:.1f}" fill="#d9a066" opacity="{op}"/>')
LAMP=(lc[0]+lr,lc[1])
# ---------------------------------------------------------------- the reading, on a little hologram at the very top of the screen
HX0,HX1,HY0,HY1=434,858,2,37
_h0=len(s)
s.append(f'<g><rect x="{HX0}" y="{HY0}" width="{HX1-HX0}" height="{HY1-HY0}" fill="#060214" opacity="0.55"/><rect x="{HX0}" y="{HY0}" width="{HX1-HX0}" height="{HY1-HY0}" fill="url(#holo)"/><rect x="{HX0}" y="{HY0}" width="{HX1-HX0}" height="{HY1-HY0}" fill="url(#scan)"/>')
s.append(f'<rect x="{HX0}" y="{HY0}" width="{HX1-HX0}" height="{HY1-HY0}" fill="none" stroke="#00e5ff" stroke-width="1.5" filter="url(#neon)"/>')
s.append('</g>')
cw,ch,cy0=18,27,HY0+5
# the deck, on the reading's left
dx0=HX0+10
for k in range(3): s.append(f'<rect x="{dx0+k*1.2:.1f}" y="{cy0+2.4-k*1.2:.1f}" width="{cw}" height="{ch}" fill="#4a1d5c" stroke="#00e5ff" stroke-width="1"/>')
dk=dx0+3.6
s.append(f'<rect x="{dk:.1f}" y="{cy0-0.8:.1f}" width="{cw}" height="{ch}" fill="#4a1d5c" stroke="#ff00ff" stroke-width="1.4"/><polygon points="{dk+cw/2:.1f},{cy0+5:.1f} {dk+cw/2+3.5:.1f},{cy0+12.5:.1f} {dk+cw/2:.1f},{cy0+20:.1f} {dk+cw/2-3.5:.1f},{cy0+12.5:.1f}" fill="none" stroke="#ff00ff" stroke-width="1.3"/>')
DECK=(dk,cy0+ch)
s.append(f'<line x1="{dx0+32}" y1="{cy0}" x2="{dx0+32}" y2="{cy0+ch}" stroke="#00e5ff" stroke-width="1" opacity="0.5"/>')
syms=["☽","✦","♀","♡"]
rx0=dx0+52
for k in range(4):
    x=rx0+k*(cw+6)
    s.append(f'<rect x="{x}" y="{cy0}" width="{cw}" height="{ch}" fill="#f3edf3" fill-opacity="0.93" stroke="#00e5ff" stroke-width="1.2"/><rect x="{x+2}" y="{cy0+2}" width="{cw-4}" height="{ch-4}" fill="none" stroke="#060214" stroke-width="0.6"/><text x="{x+cw/2}" y="{cy0+ch/2+4}" text-anchor="middle" font-size="10" fill="#ff00ff">{syms[k]}</text>')
xg=rx0+4*(cw+6)
s.append(f'<rect x="{xg}" y="{cy0}" width="{cw}" height="{ch}" fill="none" stroke="#00e5ff" stroke-width="1" stroke-dasharray="3 3" opacity="0.8"/><text x="{xg+cw/2}" y="{cy0+ch/2+4}" text-anchor="middle" {FONT} font-size="11" fill="#00e5ff" opacity="0.85">+</text>')
SPREAD=(rx0,cy0+ch)
s.append(f'<text x="{rx0-10}" y="{cy0+ch/2+4}" text-anchor="middle" font-family="Staatliches, sans-serif" font-size="11" fill="#ffdf00">I</text>')
# the other workspaces' readings, face-down
ox=xg+cw+24
s.append(f'<line x1="{ox-14}" y1="{cy0}" x2="{ox-14}" y2="{cy0+ch}" stroke="#00e5ff" stroke-width="1" opacity="0.5"/>')
for name,n in [("II",2),("III",3),("IV",1)]:
    s.append(f'<text x="{ox}" y="{cy0+ch/2+4}" font-family="Staatliches, sans-serif" font-size="11" fill="#6b6488">{name}</text>')
    for k in range(n): s.append(f'<rect x="{ox+16+k*12}" y="{cy0+5}" width="10" height="17" fill="#4a1d5c" stroke="#b4a7d6" stroke-width="0.8" opacity="0.8"/>')
    ox+=16+n*12+16
OTHER=(xg+cw+24,cy0+ch)
# shrink the whole hologram by 20%, keeping it centred over the window and pinned to the top edge
HS=0.8; HCX=(HX0+HX1)/2
def ht(p): return (round(HCX*(1-HS)+HS*p[0],1),round(HY0*(1-HS)+HS*p[1],1))
grp=''.join(s[_h0:]); del s[_h0:]
s.append(f'<g transform="translate({HCX*(1-HS):.1f},{HY0*(1-HS):.1f}) scale({HS})">{grp}</g>')
DECK=ht(DECK); SPREAD=ht(SPREAD); OTHER=ht(OTHER)
HX0s=ht((HX0,HY0))[0]
# ---------------------------------------------------------------- window-manager tiles, as faint holographic outlines
# Each tile stops at the edge of the thing it belongs to, and no two tiles overlap:
# shelves end at the bookcase's front edge, the right wall starts just past the window frame.
SHX=round(P(BXb,0,BZb)[0])          # right edge of the bookcase, on screen
TW=(round(WIN[0]+4),round(WIN[1]+24),round(WIN[2]-4),round(WIN[3]-4))
TS=(5,5,SHX-6,Hs-5)
TR=(round(WIN[2])+6,TW[1],W-5,TW[3])
TF=(SHX+6,TW[3]+8,W-5,Hs-5)
def trect(t): return f'<rect x="{t[0]}" y="{t[1]}" width="{t[2]-t[0]}" height="{t[3]-t[1]}"/>'
s.append('<g fill="none" stroke="#00e5ff" stroke-width="1.3" stroke-dasharray="6 6" opacity="0.38">'+''.join(trect(t) for t in (TS,TW,TR,TF))+'</g>')
s.append(f'<g {FONT} font-size="11" fill="#00e5ff" opacity="0.85" paint-order="stroke" stroke="#060214" stroke-width="3"><text x="10" y="572">tile: shelves</text><text x="{TF[0]+6}" y="572">tile: floor</text><text x="{TR[2]-6}" y="{TR[3]-6}" text-anchor="end">tile: right wall</text><text x="{TW[0]+6}" y="{TW[3]-6}">tile: window</text></g>')
# ---------------------------------------------------------------- labels

L=[]
L.append(lab(MOON[0]-28,MOON[1]+46,1,"moon","#fffbce"))
L.append(lab(WIN[0]+300,WIN[1]+214,2,"sky"))
L.append(lab(HX0s-6,HY0+19,3,"deck","#d9d2ff","end"))
L.append(lab(SPREAD[0]+16,SPREAD[1]+22,4,"reading"))
L.append(lab(CAN[0]-6,CAN[1]-34,5,"candles"))
L.append(lab(BLINDS[0]-14,BLINDS[1]+18,6,"blinds","#d9d2ff","end"))
L.append(lab(BOOK[0]-14,BOOK[1]-4,7,"spellbook","#39ff88","end"))
L.append(lab(FAM[0]-58,FAM[1]+30,8,"familiar"))
L.append(lab(cc[0]-92,cc[1]+12,9,"circle","#ff00ff","end"))
L.append(lab(LAMP[0]-80,LAMP[1]+64,10,"light","#ffcf8a"))
L.append(lab(FR1[0]-30,FR1[1]-8,11,"wi-fi","#00e5ff"))
L.append(lab(FR2[0]-46,FR2[1]+22,12,"bluetooth","#3fe0d0"))
L.append(lab(HG[0]+20,HG[1]+14,13,"hourglass"))
L.append(lab(SHELF[0]+8,SHELF[1]+4,14,"books"))
L.append(lab(10,552,15,"holo tiles","#00e5ff"))
def plain(x,y,t,anchor="start",c="#b4a7d6"):
    return f'<text x="{x:.0f}" y="{y:.0f}" text-anchor="{anchor}" {FONT} font-size="11" fill="{c}" paint-order="stroke" stroke="#060214" stroke-width="3">{t}</text>'
L.append(plain(HERBS[0]-4,HERBS[1]+30,"herbs","end"))
L.append(plain(OTHER[0],OTHER[1]+22,"other spreads"))
L.append(plain(BED[0]+4,BED[1]+4,"bed"))
L.append(plain(ALTAR[0]+6,ALTAR[1],"altar"))
L.append(plain(LAVA[0]+16,LAVA[1]+14,"lava lamp","start","#ff8ad0"))
L.append(plain(MON[0]+56,MON[1]+40,"monstera","start","#9ad06a"))
L.append(plain(IVY[0]+14,IVY[1]+4,"english ivy","start","#9ad06a"))
L.append(plain(POTH[0]-24,POTH[1]+30,"pothos","end","#9ad06a"))
L.append(plain(FERN[0]-40,FERN[1]+36,"fern","end","#9ad06a"))
L.append(plain(PEARL[0]-14,PEARL[1]+44,"string of pearls","end","#9ad06a"))
s+=L
svg=f'<svg width="{W}" height="{Hs}" viewBox="0 0 {W} {Hs}" style="position: absolute; left: 0; top: 0; display: block">'+'\n'.join(s)+'</svg>'
open(sys.argv[1] if len(sys.argv)>1 else 'room.svg','w').write(svg)
open('geo.txt','w').write(repr({'VP':(VX,HY),'back':[P(XL,C,ZB),P(XR,C,ZB),P(XR,0,ZB),P(XL,0,ZB)],'win':WIN,'tiles':{'shelves':TS,'window':TW,'right':TR,'floor':TF}}))
