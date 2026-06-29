#!/usr/bin/env bash
# Rebuild EP-001 Animatic v1 (rough frames + audio bed, no voice).
# Deterministic: frames + audio regenerate identically; voice is added later by a human.
set -e
python3 render_frames.py        # -> frames/f01..f19.png  (1280x720)
python3 synth_audio.py          # -> audio.wav            (295s ambience + music)
DUR=(18 17 20 20 20 15 15 13 14 10 8 20 15 15 15 20 20 5 15)
: > list.txt
for i in $(seq 1 19); do
  printf "file '%s/frames/f%02d.png'\nduration %s\n" "$PWD" "$i" "${DUR[$((i-1))]}" >> list.txt
done
printf "file '%s/frames/f19.png'\n" "$PWD" >> list.txt
ffmpeg -y -f concat -safe 0 -i list.txt -i audio.wav \
  -vf "fps=25,scale=1280:720,format=yuv420p,fade=t=in:st=0:d=0.6,fade=t=out:st=294:d=1.0" \
  -c:v libx264 -preset medium -crf 21 -c:a aac -b:a 128k -movflags +faststart -shortest \
  STORY-001-ball-animatic-v1.mp4
echo "Built STORY-001-ball-animatic-v1.mp4 (~4:55)"
