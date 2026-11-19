"""Monta o vídeo pitch da GS: slide grande à esquerda, câmera de quem fala à direita."""
import os, re, subprocess, sys, json
import pymupdf as fitz

ROOT = "D:/001_PESSOAL/GS_Video"
BRUTOS = f"{ROOT}/brutos"
WORK = f"{ROOT}/work"
DECK = "D:/001_PESSOAL/02_FIAP/GS_2026-2_CitizenTech/GS_Prosa_Pitch_Deck_v2.pdf"
FFMPEG = sys.argv[1]
OUT = sys.argv[2] if len(sys.argv) > 2 else f"{ROOT}/GS_Prosa_Video_rascunho.mp4"
os.makedirs(WORK, exist_ok=True)
import shutil
for _f in ("georgia.ttf", "calibri.ttf", "calibrib.ttf"):
    shutil.copy(f"C:/Windows/Fonts/{_f}", f"{WORK}/{_f}")
os.chdir(WORK)

FONT_SERIF = "georgia.ttf"
FONT_SANS = "calibri.ttf"
FONT_SANS_B = "calibrib.ttf"
PROFUNDO, VITAL, PAPEL, NEVOA = "0x0F2D3A", "0x3DBE93", "0xEEF7F3", "0x9FB3BB"

# Layout 1920x1080
SX, SY, SW, SH = 40, 150, 1440, 810      # slide
CX, CY, CW, CH = 1520, 150, 360, 480     # câmera (3:4)

# (arquivo, pessoa, cabeçalho, [(slide, fração_inicial)], pausas detectadas)
CLIPS = [
    ("1a_Mafe_cidadao.mp4", "Maria Fernanda Costa Barros", "1 · O cidadão", [(2, 0.0)]),
    ("1b_Mafe_solucao.mp4", "Maria Fernanda Costa Barros", "2 · A solução", [(4, 0.0), (7, None)]),
    ("2a_Gustavo_negocio.mp4", "Gustavo Halfen Simon", "3 · O negócio", [(3, 0.0), (6, None)]),
    ("2b_Gustavo_controle.mp4", "Gustavo Halfen Simon", "4 · O controle", [(7, 0.0), (8, None)]),
    ("3_Felipe_pedido.mov","Felipe Alef dos Santos Dias", "5 · Para quem e o pedido", [(11, 0.0), (12, None)]),
]
# Corte entre slides: fração do texto do roteiro (palavras) antes da troca, ajustada à maior pausa próxima
SPLIT_FRAC = {
    "1b_Mafe_solucao.mp4": None,     # calculado: antes de "Cada uma tem limite"
    "2a_Gustavo_negocio.mp4": None,  # antes de "Fizemos a conta"
    "2b_Gustavo_controle.mp4": None, # antes de "Classificamos o risco"
    "3_Felipe_pedido.mp4": None,     # antes de "A Prosa conecta-se aos ODS"
}
ROTEIRO = open("D:/001_PESSOAL/02_FIAP/GS_2026-2_CitizenTech/GS_Roteiro_Video_Pitch_v2.md", encoding="utf-8").read()

def frac_before(section_title, marker):
    sec = ROTEIRO.split(section_title, 1)[1].split("\n## ", 1)[0]
    sec = sec.split("\n", 1)[1]
    body = sec.split("---")[0]
    i = body.index(marker)
    w = lambda s: len(re.findall(r"\w+", s))
    return w(body[:i]) / w(body)

SPLIT_FRAC["1b_Mafe_solucao.mp4"] = frac_before("## 2. A solução", "Cada uma tem limite")
SPLIT_FRAC["2a_Gustavo_negocio.mp4"] = frac_before("## 3. O negócio", "Fizemos a conta")
SPLIT_FRAC["2b_Gustavo_controle.mp4"] = frac_before("## 4. O controle", "Classificamos o risco")
SPLIT_FRAC["3_Felipe_pedido.mov"] = frac_before("## 5. Para quem", "A Prosa conecta-se")

# Tratamento extra por gravação (antes do recorte da câmera / antes do loudnorm)
EXTRA_V = {
    "3_Felipe_pedido.mov": "hqdn3d=2:1.5:4:4,eq=contrast=1.06:saturation=1.04:gamma=0.98,colorbalance=rs=-0.03:gs=0:bs=0.03,",
}
EXTRA_A = {
    "3_Felipe_pedido.mov": "highpass=f=80,afftdn=nf=-25,",
}

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        print(r.stderr[-3000:]); raise SystemExit(1)
    return r.stderr

def probe(path):
    out = run([FFMPEG, "-hide_banner", "-i", path, "-af", "silencedetect=n=-32dB:d=0.25", "-f", "null", "-"])
    dur = float(re.findall(r"time=(\d+):(\d+):([\d.]+)", out)[-1][2]) + 60*int(re.findall(r"time=(\d+):(\d+):([\d.]+)", out)[-1][1])
    st = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", out)]
    en = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", out)]
    pauses = list(zip(st, en))
    vs = re.search(r"Video: \w+.*?, (\d{3,5})x(\d{3,5})", out)
    return dur, pauses, int(vs.group(1)), int(vs.group(2))

def textfile(name, text):
    p = f"{WORK}/{name}.txt"
    open(p, "w", encoding="utf-8").write(text)
    return f"{name}.txt"

# 1. Slides em PNG
doc = fitz.open(DECK)
for n in {s for c in CLIPS for s, _ in c[3]}:
    pix = doc[n-1].get_pixmap(matrix=fitz.Matrix(SW/doc[n-1].rect.width, SH/doc[n-1].rect.height))
    pix.save(f"{WORK}/slide{n:02d}.png")

segments, log = [], []
# 2. Abertura (3 s)
intro = f"{WORK}/seg00_intro.mp4"
t1, t2, t3, t4 = (textfile("i1", "Prosa"), textfile("i2", "O agrônomo que cabe no WhatsApp do pequeno produtor"),
                  textfile("i3", "Global Solution 2026.2 · CitizenTech · FIAP"),
                  textfile("i4", "Felipe Alef dos Santos Dias (RM 574450) · Gustavo Halfen Simon (RM 575052)\nMaria Fernanda Costa Barros (RM 576110)"))
vf = (f"drawtext=fontfile={FONT_SERIF}:textfile={t1}:fontsize=150:fontcolor=white:x=(w-tw)/2:y=330,"
      f"drawbox=x=(iw-160)/2:y=520:w=160:h=6:color={VITAL}:t=fill,"
      f"drawtext=fontfile={FONT_SANS}:textfile={t2}:fontsize=48:fontcolor={PAPEL}:x=(w-tw)/2:y=570,"
      f"drawtext=fontfile={FONT_SANS}:textfile={t3}:fontsize=32:fontcolor={NEVOA}:x=(w-tw)/2:y=680,"
      f"drawtext=fontfile={FONT_SANS}:textfile={t4}:fontsize=32:fontcolor={PAPEL}:x=(w-tw)/2:y=850:line_spacing=14:text_align=center,"
      f"fade=t=in:st=0:d=0.6,fade=t=out:st=3.6:d=0.4")
run([FFMPEG, "-y", "-f", "lavfi", "-i", f"color=c={PROFUNDO}:s=1920x1080:r=30:d=4",
     "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo", "-t", "4", "-vf", vf,
     "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-shortest", intro])
segments.append(intro)

# 3. Trechos
k = 1
for fname, person, header, slides in CLIPS:
    src = f"{BRUTOS}/{fname}"
    if not os.path.exists(src):
        log.append(f"FALTA {fname}"); continue
    dur, pauses, vw, vh = probe(src)
    # corta silêncio do começo/fim (deixa 0,15 s)
    t0 = max(0.0, pauses[0][1] - 0.15) if pauses and pauses[0][0] < 0.3 else 0.0
    tend = min(dur, pauses[-1][0] + 0.15) if pauses and pauses[-1][1] > dur - 0.3 else dur
    cuts = [t0]
    if len(slides) > 1:
        target = t0 + SPLIT_FRAC[fname] * (tend - t0)
        near = [p for p in pauses if abs((p[0]+p[1])/2 - target) < 5 and t0 < p[0] < tend - 1]
        best = max(near, key=lambda p: (p[1]-p[0]) - 0.08*abs((p[0]+p[1])/2 - target)) if near else (target, target)
        cuts.append((best[0]+best[1])/2)
    cuts.append(tend)
    # recorte 3:4 central da câmera
    cw = int(vh*3/4)//2*2
    cam = (f"{EXTRA_V.get(fname, '')}crop={cw}:{vh}:(iw-{cw})/2:0,scale={CW}:{CH}:flags=lanczos"
           + (",unsharp=5:5:0.5" if vh >= 1000 else ""))
    tp, th = textfile(f"p{k}", person), textfile(f"h{k}", header)
    for j, (sn, _) in enumerate(slides):
        a, b = cuts[j], cuts[j+1]
        seg = f"{WORK}/seg{k:02d}_{j}.mp4"
        afades = []
        if j == 0: afades.append("afade=t=in:st=0:d=0.12")
        if j == len(slides)-1: afades.append(f"afade=t=out:st={max(0,b-a-0.25):.3f}:d=0.25")
        fc = (f"[0:v]{cam}[cam];"
              f"color=c={PROFUNDO}:s=1920x1080:r=30[bg];"
              f"[1:v]scale={SW}:{SH}[sl];"
              f"[bg][sl]overlay={SX}:{SY}[t1];"
              f"[t1]drawbox=x={CX-4}:y={CY-4}:w={CW+8}:h={CH+8}:color={VITAL}:t=fill[t2];"
              f"[t2][cam]overlay={CX}:{CY}:shortest=1[t3];"
              f"[t3]drawtext=fontfile={FONT_SERIF}:textfile={th}:fontsize=52:fontcolor=white:x={SX}:y=58,"
              f"drawbox=x={SX}:y=128:w=120:h=5:color={VITAL}:t=fill,"
              f"drawtext=fontfile={FONT_SANS}:text='Prosa':fontsize=30:fontcolor={NEVOA}:x=1880-tw:y=74,"
              f"drawtext=fontfile={FONT_SANS_B}:textfile={tp}:fontsize=30:fontcolor=white:x={CX}:y={CY+CH+24}:"
              f"line_spacing=6,"
              f"drawtext=fontfile={FONT_SANS}:text='GS 2026.2 · CitizenTech · FIAP':fontsize=24:fontcolor={NEVOA}:x={SX}:y=1000,"
              f"fps=30,format=yuv420p[v];"
              f"[0:a]aresample=48000,aformat=channel_layouts=stereo,{EXTRA_A.get(fname, '')}loudnorm=I=-16:TP=-1.5:LRA=11"
              f"{(',' + ','.join(afades)) if afades else ''}[a]")
        run([FFMPEG, "-y", "-ss", f"{a:.3f}", "-to", f"{b:.3f}", "-i", src,
             "-loop", "1", "-i", f"{WORK}/slide{sn:02d}.png",
             "-filter_complex", fc, "-map", "[v]", "-map", "[a]", "-t", f"{b-a:.3f}",
             "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-c:a", "aac", "-b:a", "160k", "-ar", "48000", seg])
        segments.append(seg)
        log.append(f"{fname}: slide {sn} de {a:.2f}s a {b:.2f}s ({b-a:.1f}s)")
    k += 1

# 4. Concatena
lst = f"{WORK}/lista.txt"
open(lst, "w", encoding="utf-8").write("".join(f"file '{s}'\n" for s in segments))
run([FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", "-movflags", "+faststart", OUT])
out = subprocess.run([FFMPEG.replace("ffmpeg.exe", "ffprobe.exe"), "-v", "error", "-show_entries", "format=duration",
                      "-of", "csv=p=0", OUT], capture_output=True, text=True).stdout.strip()
print("\n".join(log))
print("Duração final (s):", out)
print("Saída:", OUT)
