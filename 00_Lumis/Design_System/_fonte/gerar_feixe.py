"""Gera artefato/feixe_capa.svg. Rodar da pasta Design_System."""
import math, random
random.seed(7)
W, H = 1240, 560
cx, cy = 150, H - 80
VITAL, PULSO, PROF = "#3DBE93", "#2BA6C9", "#0F2D3A"


def ecg(t):
    """Um batimento (t de 0 a 1) como soma de gaussianas: ondas P, Q, R, S e T."""
    g = lambda c, a, w: a * math.exp(-((t - c) / w) ** 2)
    return g(.18, -12, .035) + g(.37, 9, .012) + g(.41, -118, .014) + g(.45, 32, .013) + g(.66, -24, .055)


def beat(x0, L, n=400):
    return [(x0 + L * i / n, cy + ecg(i / n)) for i in range(n + 1)]


def by_length(pts, step):
    """Amostra pontos a distância constante ao longo da curva, para os pontos desenharem o batimento."""
    out, acc = [pts[0]], 0.0
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        acc += math.hypot(x2 - x1, y2 - y1)
        if acc >= step:
            out.append((x2, y2)); acc = 0.0
    return out


P = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
     '<defs>',
     f'<radialGradient id="fundo" cx="{cx/W:.3f}" cy="{cy/H:.3f}" r="1.1" fx="{cx/W:.3f}" fy="{cy/H:.3f}">'
     '<stop offset="0" stop-color="#17404F"/><stop offset=".55" stop-color="#0F2D3A"/><stop offset="1" stop-color="#0B2330"/></radialGradient>',
     f'<radialGradient id="halo"><stop offset="0" stop-color="{VITAL}" stop-opacity=".45"/><stop offset="1" stop-color="{VITAL}" stop-opacity="0"/></radialGradient>',
     f'<linearGradient id="vp" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{VITAL}"/><stop offset="1" stop-color="{PULSO}"/></linearGradient>',
     '<filter id="grao" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" stitchTiles="stitch"/>'
     '<feColorMatrix values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .05 0"/></filter>',
     '</defs>',
     f'<rect width="{W}" height="{H}" fill="url(#fundo)"/>']

# Arcos de sinal: espaçamento que cresce, opacidade que cai, alguns pontilhados (o sinal vira leitura)
r = 64
for i in range(13):
    op = max(.05, .34 - i * .024) * random.uniform(.85, 1.1)
    if i == 4:
        P.append(f'<circle cx="{cx}" cy="{cy}" r="{r:.0f}" fill="none" stroke="url(#vp)" stroke-width="1.8" stroke-opacity=".9"/>')
    elif i in (2, 7, 10):
        P.append(f'<circle cx="{cx}" cy="{cy}" r="{r:.0f}" fill="none" stroke="#FFFFFF" stroke-opacity="{op+.08:.2f}" '
                 f'stroke-width="2" stroke-dasharray="0 {9 + i}" stroke-linecap="round"/>')
    else:
        P.append(f'<circle cx="{cx}" cy="{cy}" r="{r:.0f}" fill="none" stroke="#FFFFFF" stroke-opacity="{op:.2f}" stroke-width="{1.1 if i % 3 else 1.6}"/>')
    r = r * 1.19 + 14

# Halo do ponto vital
P.append(f'<circle cx="{cx}" cy="{cy}" r="120" fill="url(#halo)"/>')

# Primeiro batimento: linha contínua (saúde)
L = 300
b1 = [(cx, cy), (cx + 120, cy)] + beat(cx + 120, L)
P.append('<path d="M' + " L".join(f"{x:.1f},{y:.1f}" for x, y in b1) +
         f'" fill="none" stroke="{VITAL}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>')

# Batimentos seguintes: o mesmo traçado, agora em pontos (dados), do verde ao ciano, cada vez mais leves
x0 = cx + 120 + L
for k, (step, rad, op) in enumerate(((11, 3.2, .95), (15, 2.6, .7), (21, 2.0, .45))):
    pts = by_length(beat(x0, L), step)
    for x, y in pts:
        t = (x - (cx + 120 + L)) / (3 * L)
        col = VITAL if t < .3 else PULSO
        P.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rad}" fill="{col}" fill-opacity="{op}"/>')
    x0 += L

P.append(f'<circle cx="{cx}" cy="{cy}" r="20" fill="{VITAL}"/>')
P.append(f'<rect width="{W}" height="{H}" filter="url(#grao)"/>')
P.append('</svg>')
open('artefato/feixe_capa.svg', 'w').write("\n".join(P))
print("ok")
