#!/usr/bin/env python3
"""Ambience + simple warm music bed (NO voice), 295s mono WAV. Voice is added by a human."""
import numpy as np, wave
SR=44100; DUR=295.0; n=int(SR*DUR); t=np.arange(n)/SR
mix=np.zeros(n, dtype=np.float64)
rng=np.random.default_rng(7); noise=rng.standard_normal(n)
b=1-np.exp(-2*np.pi*120/SR); lp=np.zeros(n); prev=0.0
for i in range(n):
    prev=prev+b*(noise[i]-prev); lp[i]=prev
mix += lp/(np.max(np.abs(lp))+1e-9)*0.06
def note(freq,start,dur,amp=0.12):
    s=int(start*SR); e=min(n,int((start+dur)*SR)); L=e-s
    if L<=0: return
    tt=np.arange(L)/SR; env=np.minimum(tt/0.04,1.0)*np.exp(-tt*1.6)
    mix[s:e]+=(np.sin(2*np.pi*freq*tt)+0.3*np.sin(4*np.pi*freq*tt))*env*amp
C=261.63; D=293.66; E=329.63; G=392.0; A=440.0
for f,st in [(C,0.5),(E,1.6),(G,2.7),(A,4.0),(G,5.4)]: note(f,st,1.6,0.11)
note(C,8.5,3.0,0.08); note(E,9.0,3.0,0.06)
for f,st in [(G,18.5),(A,19.6),(G,20.7),(E,21.8),(G,23.4),(C,25.0)]: note(f,st,1.3,0.10)
note(C,191.0,3.5,0.07); note(G,193.0,3.5,0.05)
for f,st in [(C,221.0),(E,222.2),(G,223.4),(A,225.0),(G,226.6),(E,228.2),(C,230.5)]: note(f,st,1.5,0.12)
for f,st in [(G,236.0),(A,238.0),(G,240.0),(C,243.0)]: note(f,st,1.6,0.09)
for f,st in [(C,281.0),(G,282.4),(E,283.8),(C,285.5)]: note(f,st,2.2,0.10)
note(C,288.0,4.0,0.06)
mix=np.tanh(mix*1.2); mix=mix/(np.max(np.abs(mix))+1e-9)*0.85
pcm=(mix*32767).astype(np.int16)
with wave.open("audio.wav","w") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
print("audio.wav written", DUR, "s")
