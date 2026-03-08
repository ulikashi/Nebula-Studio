from PIL import Image, ImageDraw, ImageFilter, ImageOps, ImageEnhance
from urllib.request import urlopen, Request
import os, io, random

W, H = 1600, 1000
OUT = "/Users/uliana/creative_dgi/Nebula-Studio/assets/images"
os.makedirs(OUT, exist_ok=True)

CASES = [
    ("project-1.webp", "AURORA LABS", "SaaS Platform", "laptop,minimal,technology,workspace", (63, 230, 255), (12, 20, 39)),
    ("project-2.webp", "PULSE ZERO", "Wearables Brand", "smartwatch,fitness,product,studio", (255, 102, 224), (30, 14, 36)),
    ("project-3.webp", "ATLAS MOTION", "B2B Campaign", "billboard,city,advertising,night", (118, 255, 203), (8, 24, 30)),
    ("project-4.webp", "LUMEN HOUSE", "Fashion E-commerce", "fashion,editorial,model,studio", (255, 177, 116), (43, 17, 14)),
    ("project-5.webp", "NOVA GRID", "Digital Strategy", "creative,direction,planning,office", (134, 194, 255), (11, 24, 40)),
    ("project-6.webp", "DRIFT AUDIO", "Music Campaign", "headphones,vinyl,music,neon", (204, 132, 255), (23, 12, 39)),
    ("project-7.webp", "FLUX CAPITAL", "Fintech Website", "finance,corporate,city,architecture", (120, 202, 255), (11, 24, 36)),
    ("project-8.webp", "ECHO FOODS", "FMCG Launch", "food,packaging,product,green", (127, 255, 168), (13, 32, 23)),
]

FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"

def font(path, size):
    try:
        from PIL import ImageFont
        return ImageFont.truetype(path, size)
    except Exception:
        from PIL import ImageFont
        return ImageFont.load_default()

F_BIG = font(FONT_BOLD, 76)
F_SUB = font(FONT_REG, 28)
F_TAG = font(FONT_BOLD, 18)


def fetch_photo(query, lock):
    url = f"https://loremflickr.com/{W}/{H}/{query}?lock={lock}"
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=25) as r:
        data = r.read()
    return Image.open(io.BytesIO(data)).convert("RGB").resize((W, H), Image.Resampling.LANCZOS)


def duotone(img, dark, accent):
    gray = ImageOps.grayscale(img)
    mapped = ImageOps.colorize(gray, black=tuple(max(0, c - 22) for c in dark), white=accent)
    mapped = ImageEnhance.Contrast(mapped).enhance(1.18)
    mapped = ImageEnhance.Color(mapped).enhance(1.24)
    return mapped


def add_texture(base, accent, dark, seed):
    random.seed(seed)
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)

    # Soft bloom lights
    for _ in range(6):
        cx = random.randint(-120, W + 120)
        cy = random.randint(-120, H + 120)
        r = random.randint(180, 420)
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(*accent, random.randint(20, 48)))

    # Angled translucent forms for editorial look
    for i in range(5):
        x = random.randint(-200, W)
        y = random.randint(-150, H)
        w = random.randint(280, 620)
        h = random.randint(120, 300)
        poly = [(x, y), (x + w, y - 70), (x + w + 90, y + h), (x - 90, y + h + 60)]
        d.polygon(poly, fill=(255, 255, 255, random.randint(10, 24)))

    layer = layer.filter(ImageFilter.GaussianBlur(20))
    comp = Image.alpha_composite(base.convert("RGBA"), layer)

    # Vignette
    vignette = Image.new("L", (W, H), 0)
    vd = ImageDraw.Draw(vignette)
    vd.ellipse((-250, -170, W + 250, H + 180), fill=220)
    vignette = vignette.filter(ImageFilter.GaussianBlur(110))
    dark_fill = Image.new("RGBA", (W, H), (*dark, 255))
    comp = Image.composite(comp, dark_fill, vignette)

    # Fine grain
    noise = Image.effect_noise((W, H), 10).convert("L")
    noise = noise.point(lambda p: int(p * 0.28))
    grain = Image.new("RGBA", (W, H), (255, 255, 255, 0))
    grain.putalpha(noise)
    comp = Image.alpha_composite(comp, grain)

    return comp


def circle_cutout(src, size=500):
    src = src.resize((size, size), Image.Resampling.LANCZOS)
    mask = Image.new("L", (size, size), 0)
    md = ImageDraw.Draw(mask)
    md.ellipse((0, 0, size, size), fill=255)
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    out.paste(src, (0, 0), mask)
    return out


def render_case(fname, title, subtitle, query, accent, dark, idx):
    try:
        photo = fetch_photo(query, 900 + idx)
    except Exception:
        photo = Image.new("RGB", (W, H), dark)

    base = duotone(photo, dark, accent)
    canvas = add_texture(base, accent, dark, idx * 27)
    d = ImageDraw.Draw(canvas, "RGBA")

    # Main object crop
    focal = photo.crop((280, 90, 1320, 960))
    focal = ImageEnhance.Contrast(focal).enhance(1.08)
    bubble = circle_cutout(focal, 630)
    canvas.paste(bubble, (870, 210), bubble)

    # Offset ring and frame
    d.ellipse((840, 180, 1510, 850), outline=(*accent, 190), width=4)
    d.rounded_rectangle((28, 28, W - 28, H - 28), radius=28, outline=(255, 255, 255, 68), width=2)

    # Header chip
    d.rounded_rectangle((64, 62, 460, 104), radius=16, fill=(255, 255, 255, 34), outline=(255, 255, 255, 84), width=1)
    d.text((82, 74), "NEBULA STUDIO / SELECTED WORK", font=F_TAG, fill=(236, 245, 255, 242))

    # Type block
    d.text((66, 170), title, font=F_BIG, fill=(246, 251, 255, 250))
    d.text((70, 262), subtitle, font=F_SUB, fill=(219, 235, 248, 245))

    # Minimal brand cue icons (no graphs)
    d.rounded_rectangle((66, 340, 136, 410), radius=14, fill=(255, 255, 255, 24))
    d.rounded_rectangle((148, 340, 218, 410), radius=14, fill=(255, 255, 255, 24))
    d.rounded_rectangle((230, 340, 300, 410), radius=14, fill=(255, 255, 255, 24))
    d.ellipse((86, 360, 116, 390), fill=(*accent, 220))
    d.rectangle((166, 360, 200, 390), fill=(*accent, 220))
    d.polygon([(248, 390), (282, 390), (265, 358)], fill=(*accent, 220))

    # Bottom glass strip for premium feel
    d.rounded_rectangle((62, 860, W - 62, 942), radius=20, fill=(255, 255, 255, 20), outline=(255, 255, 255, 64), width=1)

    # Stylish diagonals
    for i in range(-5, 14):
        x = i * 180
        d.line((x, 0, x + 460, H), fill=(255, 255, 255, 14), width=1)

    canvas = canvas.filter(ImageFilter.UnsharpMask(radius=1.7, percent=130, threshold=2))
    canvas.convert("RGB").save(os.path.join(OUT, fname), "WEBP", quality=92, method=6)


for i, case in enumerate(CASES, 1):
    render_case(*case, idx=i)

print("Regenerated in new style without charts")
