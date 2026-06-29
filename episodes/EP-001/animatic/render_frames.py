#!/usr/bin/env python3
"""EP-001 Animatic v1 — rough frame renderer (real stills, not final character art)."""
from PIL import Image, ImageDraw, ImageFilter
import os, math

W, H = 1280, 720
FLOOR = 540
OUT = "frames"
os.makedirs(OUT, exist_ok=True)

paper=(244,239,227); WALL=(238,231,214); FLOORC=(214,196,162)
INK=(58,55,47); BALL=(232,162,61); WOOD=(201,138,82)
WARM=(242,200,121); COOL=(120,140,165); CREAM=(248,244,236)

def base(tint=None, wall=WALL, floorc=FLOORC):
    img = Image.new("RGB",(W,H),wall); d = ImageDraw.Draw(img)
    d.rectangle([0,FLOOR,W,H], fill=floorc); d.line([0,FLOOR,W,FLOOR], fill=(0,0,0), width=2)
    return img
def apply_tint(img, color, alpha):
    ov = Image.new("RGBA",(W,H),color+(int(alpha*255),))
    return Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB")
def rcap_line(d, p0, p1, w, fill):
    d.line([p0,p1], fill=fill, width=w); r=w//2
    for p in (p0,p1): d.ellipse([p[0]-r,p[1]-r,p[0]+r,p[1]+r], fill=fill)
def face(d, cx, cy, r, mood, look=False):
    ex = r*0.32; ey = cy - r*0.12; er = max(3,int(r*0.16))
    for sx in (-1,1):
        d.ellipse([cx+sx*ex-er, ey-er, cx+sx*ex+er, ey+er], fill=CREAM); pr=max(1,er//2)
        px = cx+sx*ex + (0 if look else sx*er*0.3); d.ellipse([px-pr,ey-pr,px+pr,ey+pr], fill=INK)
    my = cy + r*0.42
    if mood=="smile": d.arc([cx-r*0.4,my-r*0.5,cx+r*0.4,my+r*0.35],20,160,fill=CREAM,width=max(3,int(r*0.12)))
    elif mood=="sad": d.arc([cx-r*0.4,my-r*0.1,cx+r*0.4,my+r*0.7],200,340,fill=CREAM,width=max(3,int(r*0.12)))
    elif mood=="surprise":
        rr=int(r*0.22); d.ellipse([cx-rr,my-rr,cx+rr,my+rr], fill=CREAM)
    else: d.line([cx-r*0.25,my,cx+r*0.25,my], fill=CREAM, width=max(2,int(r*0.1)))
def draw_max(d, cx, base_y, scale=1.0, mood="neutral", armL=None, armR=None, look=False):
    r=int(40*scale); bw=int(66*scale); bh=int(150*scale); by=base_y-bh; hcy=by-r+int(8*scale)
    d.rounded_rectangle([cx-bw//2,by,cx+bw//2,by+bh], radius=int(28*scale), fill=INK)
    if armL: rcap_line(d,(cx-bw//2+6,by+int(40*scale)),tuple(armL),int(16*scale),INK)
    if armR: rcap_line(d,(cx+bw//2-6,by+int(40*scale)),tuple(armR),int(16*scale),INK)
    d.ellipse([cx-r,hcy-r,cx+r,hcy+r], fill=INK); face(d,cx,hcy,r,mood,look)
def draw_eva(d, cx, base_y, scale=1.0, mood="neutral", armL=None, armR=None, look=False, sock=False, tilt=0):
    r=int(34*scale); bw=int(56*scale); bh=int(126*scale); by=base_y-bh; hcy=by-r+int(7*scale)
    d.rounded_rectangle([cx-bw//2,by,cx+bw//2,by+bh], radius=int(24*scale), fill=INK)
    if armL: rcap_line(d,(cx-bw//2+5,by+int(34*scale)),tuple(armL),int(14*scale),INK)
    if armR: rcap_line(d,(cx+bw//2-5,by+int(34*scale)),tuple(armR),int(14*scale),INK)
    d.ellipse([cx-r,hcy-r,cx+r,hcy+r], fill=INK)
    er=int(11*scale); d.ellipse([cx+r-er,hcy-r-er//2,cx+r+er,hcy-r+er*3//2], fill=INK)
    if sock: d.polygon([(cx-r,hcy-r+4),(cx,hcy-r-int(28*scale)),(cx+r,hcy-r+4)], fill=COOL)
    face(d,cx,hcy,r,mood,look)
def ball(d, cx, cy, r):
    d.ellipse([cx-r,cy-r,cx+r,cy+r], fill=BALL)
    d.arc([cx-r*0.5,cy-r*0.7,cx+r*0.3,cy],200,330,fill=(255,255,255),width=max(2,r//6))
def toypile(d, x, y):
    d.rounded_rectangle([x,y-50,x+64,y],radius=8,fill=WOOD)
    d.rounded_rectangle([x+54,y-96,x+110,y],radius=8,fill=COOL)
    d.rounded_rectangle([x+104,y-40,x+176,y],radius=8,fill=(150,120,90))
    d.polygon([(x+18,y-50),(x+50,y-104),(x+82,y-50)], fill=BALL)
def boxdoor(d, x, y, s=1.0):
    w=int(190*s); h=int(150*s); d.rounded_rectangle([x,y,x+w,y+h],radius=int(14*s),fill=WOOD)
    d.pieslice([x+int(0.28*w),y+int(0.18*h),x+int(0.72*w),y+int(1.4*h)],180,360,fill=(42,36,16))
    d.rectangle([x+int(0.28*w),y+int(0.55*h),x+int(0.72*w),y+h],fill=(42,36,16))
    d.ellipse([x+int(0.6*w),y+int(0.62*h),x+int(0.6*w)+10,y+int(0.62*h)+10],fill=CREAM)
def shelf(d, x, y):
    d.line([x,y,x+220,y],fill=INK,width=10); d.arc([x+70,y-46,x+150,y+34],180,360,fill=WOOD,width=12)
def book(d, x, y, c=COOL):
    d.rounded_rectangle([x,y,x+78,y+56],radius=6,fill=c); d.line([x+39,y,x+39,y+56],fill=paper,width=4)
def slipper(rot=0):
    s=Image.new("RGBA",(220,120),(0,0,0,0)); sd=ImageDraw.Draw(s)
    sd.ellipse([10,40,150,110],fill=WOOD); sd.ellipse([90,20,210,100],fill=WOOD)
    return s.rotate(rot, expand=True, center=(110,80))
def window(d, x, y):
    d.rounded_rectangle([x,y,x+190,y+150],radius=12,fill=WARM)
    d.line([x+95,y,x+95,y+150],fill=WALL,width=8); d.line([x,y+75,x+190,y+75],fill=WALL,width=8)
def sunbeam(img, x, y, ln, w=120):
    ov=Image.new("RGBA",(W,H),(0,0,0,0)); od=ImageDraw.Draw(ov)
    od.line([x,y,x+ln,y+ln],fill=WARM+(90,),width=w); ov=ov.filter(ImageFilter.GaussianBlur(28))
    return Image.alpha_composite(img.convert("RGBA"),ov).convert("RGB")
def luma(d, warm=True):
    body=WOOD if warm else (96,108,128)
    d.polygon([(490,FLOOR),(490,300),(640,200),(790,300),(790,FLOOR)],fill=body)
    d.line([(490,300),(640,200),(790,300)],fill=INK,width=4,joint="curve")
    for wx in (545,690):
        d.rounded_rectangle([wx,360,wx+70,450],radius=8,fill=WARM)
        d.line([wx+35,360,wx+35,450],fill=body,width=5); d.line([wx,405,wx+70,405],fill=body,width=5)

def p1():
    img=base(); d=ImageDraw.Draw(img); window(d,940,150); draw_max(d,480,FLOOR)
    return apply_tint(sunbeam(img,120,120,260),WARM,0.08)
def p2():
    img=base(); d=ImageDraw.Draw(img); draw_max(d,440,FLOOR,armR=[620,470]); ball(d,720,560,52)
    return apply_tint(img,WARM,0.06)
def p3():
    img=base(); d=ImageDraw.Draw(img); toypile(d,840,FLOOR); d.arc([560,360,860,560],200,360,fill=BALL,width=4)
    draw_max(d,470,FLOOR,mood="sad",armR=[600,460]); return img
def p4():
    img=base(); d=ImageDraw.Draw(img); toypile(d,180,FLOOR); book(d,1000,520)
    draw_max(d,600,FLOOR,mood="sad",armL=[440,560]); return apply_tint(img,COOL,0.16)
def p5():
    img=base(); d=ImageDraw.Draw(img); d.rectangle([0,150,70,FLOOR],fill=(150,140,120)); toypile(d,560,FLOOR)
    draw_eva(d,150,FLOOR,tilt=8,armR=[280,470]); draw_max(d,860,FLOOR,mood="sad"); return img
def p6():
    img=base(); d=ImageDraw.Draw(img); draw_max(d,470,FLOOR,mood="sad")
    draw_eva(d,720,FLOOR,mood="smile",look=True,armR=[860,470]); return img
def p7():
    img=base(); d=ImageDraw.Draw(img); boxdoor(d,430,360,1.2)
    for bx,c in [(840,BALL),(930,COOL),(1010,(150,120,90))]: d.rounded_rectangle([bx,480,bx+64,544],radius=8,fill=c)
    return img
def p8():
    img=base(); d=ImageDraw.Draw(img); boxdoor(d,180,400)
    draw_eva(d,700,FLOOR,mood="smile",look=True,armL=[520,470]); draw_max(d,980,FLOOR,armL=[900,470])
    d.rounded_rectangle([872,452,916,496],radius=6,fill=BALL); return img
def p9():
    img=base(); d=ImageDraw.Draw(img); boxdoor(d,560,380,1.1); draw_max(d,470,FLOOR,mood="smile",armR=[620,450])
    d.rounded_rectangle([600,430,648,478],radius=6,fill=BALL); return img
def p10():
    img=base(); d=ImageDraw.Draw(img); draw_max(d,440,FLOOR,mood="smile"); draw_eva(d,760,FLOOR,mood="smile",sock=True)
    return apply_tint(img,WARM,0.05)
def p11():
    img=base(); d=ImageDraw.Draw(img); shelf(d,520,300); book(d,600,250,c=BALL)
    draw_max(d,380,FLOOR,mood="smile",armR=[520,330]); draw_eva(d,860,FLOOR,mood="smile",armL=[700,330]); return img
def p12():
    img=base(floorc=BALL); d=ImageDraw.Draw(img); boxdoor(d,960,420,0.9); book(d,240,520)
    draw_max(d,560,FLOOR,mood="surprise",armR=[720,450]); return apply_tint(img,WARM,0.05)
def p13():
    img=base(); d=ImageDraw.Draw(img); draw_max(d,470,FLOOR+120,scale=1.7,mood="surprise")
    draw_eva(d,1000,FLOOR,mood="smile"); return img
def p14():
    img=base(); d=ImageDraw.Draw(img); s=slipper(0); img.paste(s,(840,470),s)
    draw_max(d,470,FLOOR,look=True,armR=[600,470]); return img
def p15():
    img=base(); d=ImageDraw.Draw(img); s=slipper(-18); img.paste(s,(560,470),s); ball(d,760,540,46)
    draw_max(d,430,FLOOR,mood="smile",armR=[580,460]); return apply_tint(sunbeam(img,1000,140,200,90),WARM,0.10)
def p16():
    img=base(); d=ImageDraw.Draw(img); draw_max(d,420,FLOOR,mood="smile",armR=[560,500]); ball(d,640,560,42)
    draw_eva(d,840,FLOOR,mood="smile",armL=[700,500]); return apply_tint(img,WARM,0.06)
def p17():
    img=base(); d=ImageDraw.Draw(img); d.rectangle([1200,150,W,FLOOR],fill=(150,140,120)); boxdoor(d,480,400)
    draw_max(d,640,FLOOR,armL=[520,470]); return img
def p18():
    img=base(); d=ImageDraw.Draw(img); boxdoor(d,560,400); book(d,300,520); return apply_tint(sunbeam(img,980,140,200,80),WARM,0.05)
def p19():
    img=base(wall=(150,160,180),floorc=(120,130,150)); d=ImageDraw.Draw(img); luma(d,warm=True); return apply_tint(img,COOL,0.20)

PANELS=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19]
for i,fn in enumerate(PANELS,1): fn().save(f"{OUT}/f{i:02d}.png")
print("rendered", len(PANELS), "frames")
