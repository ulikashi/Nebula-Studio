from PIL import Image, ImageDraw, ImageFilter, ImageOps
import os, random

W, H = 1600, 1000
OUT = "/Users/uliana/creative_dgi/Nebula-Studio/assets/images"
os.makedirs(OUT, exist_ok=True)

cases = [
    ("project-1.webp", "SaaS", ((13, 24, 52), (47, 112, 255), (105, 255, 222))),
    ("project-2.webp", "Wearable", ((35, 15, 46), (184, 78, 255), (255, 130, 220))),
    ("project-3.webp", "Campaign", ((9, 34, 38), (20, 170, 160), (128, 255, 214))),
    ("project-4.webp", "Fashion", ((49, 18, 16), (247, 100, 78), (255, 198, 148))),
    ("project-5.webp", "Strategy", ((14, 28, 44), (66, 150, 255), (138, 220, 255))),
    ("project-6.webp", "Audio", ((24, 16, 44), (165, 84, 255), (255, 140, 230))),
    ("project-7.webp", "Fintech", ((12, 30, 44), (34, 134, 227), (120, 208, 255))),
    ("project-8.webp", "FMCG", ((13, 38, 28), (44, 184, 128), (174, 255, 150))),
]


def gradient(c1, c2):
    img = Image.new("RGB", (W, H), c1)
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / (H - 1)
        r = int(c1[0] * (1 - t) + c2[0] * t)
        g = int(c1[1] * (1 - t) + c2[1] * t)
        b = int(c1[2] * (1 - t) + c2[2] * t)
        d.line([(0, y), (W, y)], fill=(r, g, b))
    return img


def add_lights(img, accent_a, accent_b, seed):
    random.seed(seed)
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    for _ in range(7):
        cx = random.randint(-100, W + 100)
        cy = random.randint(-100, H + 100)
        r = random.randint(180, 460)
        col = accent_a if random.random() > 0.5 else accent_b
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(*col, random.randint(20, 58)))
    layer = layer.filter(ImageFilter.GaussianBlur(35))
    return Image.alpha_composite(img.convert("RGBA"), layer)


def glass_card(d, x, y, w, h):
    d.rounded_rectangle((x, y, x + w, y + h), radius=30, fill=(255, 255, 255, 24), outline=(255, 255, 255, 80), width=2)


def grain(img):
    n = Image.effect_noise((W, H), 12).convert("L")
    n = n.point(lambda p: int(p * 0.30))
    g = Image.new("RGBA", (W, H), (255, 255, 255, 0))
    g.putalpha(n)
    return Image.alpha_composite(img.convert("RGBA"), g)


def scene_saas(d, p):
    glass_card(d, 90, 130, 980, 740)
    d.rounded_rectangle((130, 220, 900, 580), radius=22, fill=(10, 20, 34, 180), outline=(140, 210, 255, 130), width=2)
    d.rounded_rectangle((160, 255, 280, 540), radius=14, fill=(255, 255, 255, 16))
    for i in range(6):
        y = 280 + i * 42
        d.rounded_rectangle((180, y, 260, y + 24), radius=8, fill=(130, 225, 255, 95))
    d.rounded_rectangle((310, 255, 860, 375), radius=14, fill=(255, 255, 255, 14))
    points = [(340, 350), (420, 320), (500, 335), (580, 280), (660, 300), (740, 250), (820, 270)]
    d.line(points, fill=(108, 255, 220, 235), width=6)
    for x, y in points:
        d.ellipse((x - 7, y - 7, x + 7, y + 7), fill=(240, 255, 252, 240))
    for i, txt in enumerate(["MRR", "Users", "Churn"]):
        x = 310 + i * 185
        d.rounded_rectangle((x, 405, x + 165, 540), radius=12, fill=(255, 255, 255, 17))
        d.text((x + 16, 430), txt, fill=(220, 245, 255, 230))
    d.ellipse((1020, 190, 1440, 610), fill=(120, 255, 230, 80), outline=(180, 255, 242, 180), width=3)
    d.rounded_rectangle((1110, 300, 1330, 460), radius=30, fill=(10, 20, 35, 220), outline=(180, 245, 255, 140), width=2)


def scene_wearable(d, p):
    d.ellipse((120, 120, 980, 920), fill=(255, 255, 255, 14), outline=(255, 255, 255, 90), width=2)
    d.rounded_rectangle((520, 200, 760, 820), radius=50, fill=(18, 15, 28, 220), outline=(255, 190, 245, 160), width=3)
    d.rounded_rectangle((560, 320, 720, 690), radius=28, fill=(255, 255, 255, 22), outline=(255, 220, 248, 120), width=2)
    d.arc((585, 410, 695, 520), start=20, end=330, fill=(255, 150, 225, 255), width=9)
    d.ellipse((610, 438, 670, 498), fill=(35, 24, 50, 255), outline=(255, 210, 245, 155), width=2)
    for i in range(3):
        x = 880 + i * 200
        glass_card(d, x, 220, 170, 230)
        d.ellipse((x + 36, 270, x + 134, 368), fill=(255, 255, 255, 45))
    d.polygon([(260, 780), (410, 430), (520, 760)], fill=(255, 255, 255, 65))
    d.rectangle((280, 760, 505, 840), fill=(255, 255, 255, 40))


def scene_campaign(d, p):
    glass_card(d, 90, 140, 1400, 720)
    d.polygon([(220, 530), (470, 420), (470, 640)], fill=(255, 255, 255, 70))
    d.rectangle((170, 500, 240, 560), fill=(255, 255, 255, 80))
    for i in range(4):
        x = 520 + i * 230
        d.rounded_rectangle((x, 220, x + 180, 130 + 220 + i * 35), radius=18, fill=(255, 255, 255, 18), outline=(200, 255, 240, 120), width=2)
        d.polygon([(x + 70, 280), (x + 70, 340), (x + 120, 310)], fill=(180, 255, 235, 190))
    d.line((240, 710, 1360, 710), fill=(220, 255, 240, 170), width=4)
    for i in range(5):
        cx = 300 + i * 255
        d.ellipse((cx - 11, 699, cx + 11, 721), fill=(130, 255, 212, 230))


def scene_fashion(d, p):
    glass_card(d, 80, 120, 1450, 760)
    d.rounded_rectangle((130, 180, 780, 820), radius=22, fill=(255, 255, 255, 15), outline=(255, 220, 190, 125), width=2)
    d.polygon([(300, 270), (420, 250), (510, 340), (540, 470), (460, 650), (350, 690), (250, 620), (220, 430)], fill=(255, 230, 200, 90))
    d.rectangle((330, 360, 470, 710), fill=(255, 205, 180, 80))
    for r in range(2):
        for c in range(3):
            x = 860 + c * 215
            y = 230 + r * 290
            d.rounded_rectangle((x, y, x + 180, y + 250), radius=18, fill=(255, 255, 255, 18), outline=(255, 215, 185, 110), width=2)
            d.rectangle((x + 24, y + 20, x + 156, y + 170), fill=(255, 255, 255, 45))
            d.rectangle((x + 44, y + 46, x + 136, y + 140), fill=(250, 170, 130, 120))


def scene_strategy(d, p):
    glass_card(d, 90, 140, 1400, 720)
    d.rounded_rectangle((150, 220, 950, 780), radius=20, fill=(255, 255, 255, 14), outline=(180, 225, 255, 130), width=2)
    notes = [((200, 280), (250, 170, 120)), ((420, 260), (130, 210, 255)), ((650, 320), (140, 255, 220)), ((380, 500), (255, 210, 120)), ((700, 540), (210, 190, 255))]
    for (x, y), col in notes:
        d.rounded_rectangle((x, y, x + 210, y + 140), radius=14, fill=(*col, 185), outline=(255, 255, 255, 160), width=1)
    d.line((220, 350, 420, 330), fill=(220, 245, 255, 200), width=4)
    d.line((620, 390, 510, 570), fill=(220, 245, 255, 200), width=4)
    d.line((760, 610, 840, 720), fill=(220, 245, 255, 200), width=4)
    d.polygon([(1110, 240), (1410, 390), (1110, 540)], fill=(255, 255, 255, 20), outline=(180, 225, 255, 120), width=2)
    d.ellipse((1160, 300, 1360, 500), outline=(170, 240, 255, 170), width=6)


def scene_audio(d, p):
    glass_card(d, 90, 140, 1400, 720)
    d.ellipse((230, 210, 850, 830), fill=(255, 255, 255, 14), outline=(225, 180, 255, 120), width=2)
    d.ellipse((360, 340, 720, 700), fill=(20, 12, 40, 230), outline=(230, 190, 255, 140), width=3)
    d.ellipse((455, 435, 625, 605), fill=(255, 255, 255, 30))
    d.arc((260, 240, 820, 800), start=205, end=335, fill=(255, 170, 245, 230), width=22)
    for i in range(48):
        x = 920 + i * 11
        h = 80 + (i * 37 % 180)
        d.rounded_rectangle((x, 680 - h, x + 8, 680), radius=3, fill=(215, 150, 255, 220))
    d.rounded_rectangle((890, 280, 1450, 620), radius=20, fill=(255, 255, 255, 12), outline=(230, 180, 255, 110), width=2)


def scene_fintech(d, p):
    glass_card(d, 90, 140, 1400, 720)
    d.polygon([(220, 360), (500, 220), (780, 360)], fill=(255, 255, 255, 40))
    for i in range(5):
        x = 255 + i * 100
        d.rectangle((x, 360, x + 50, 700), fill=(255, 255, 255, 36))
    d.rectangle((210, 700, 790, 750), fill=(255, 255, 255, 40))
    d.rounded_rectangle((900, 210, 1430, 760), radius=24, fill=(255, 255, 255, 12), outline=(170, 225, 255, 120), width=2)
    bars = [100, 180, 120, 230, 280, 260, 320]
    for i, b in enumerate(bars):
        x = 940 + i * 65
        d.rounded_rectangle((x, 710 - b, x + 44, 710), radius=10, fill=(120, 205, 255, 220))
    d.line((940, 640, 1000, 600, 1080, 620, 1160, 540, 1240, 510, 1330, 430), fill=(140, 255, 235, 235), width=5)


def scene_fmcg(d, p):
    glass_card(d, 90, 140, 1400, 720)
    d.rounded_rectangle((170, 250, 1470, 770), radius=24, fill=(255, 255, 255, 12), outline=(175, 255, 205, 120), width=2)
    for i in range(4):
        x = 230 + i * 300
        d.rounded_rectangle((x, 330, x + 210, 360), radius=10, fill=(255, 255, 255, 26))
        d.rounded_rectangle((x + 20, 390, x + 190, 700), radius=20, fill=(255, 255, 255, 28), outline=(210, 255, 220, 145), width=2)
        d.rectangle((x + 46, 440, x + 164, 585), fill=(140, 245, 175, 155))
        d.polygon([(x + 105, 476), (x + 130, 520), (x + 86, 520)], fill=(245, 255, 245, 220))
    d.ellipse((1140, 170, 1380, 410), fill=(160, 255, 190, 85), outline=(205, 255, 220, 170), width=2)
    d.polygon([(1230, 220), (1265, 270), (1200, 270)], fill=(245, 255, 245, 220))


scene_map = {
    "SaaS": scene_saas,
    "Wearable": scene_wearable,
    "Campaign": scene_campaign,
    "Fashion": scene_fashion,
    "Strategy": scene_strategy,
    "Audio": scene_audio,
    "Fintech": scene_fintech,
    "FMCG": scene_fmcg,
}

for idx, (fname, kind, pal) in enumerate(cases, start=1):
    base = gradient(pal[0], pal[1])
    comp = add_lights(base, pal[1], pal[2], idx * 19)
    d = ImageDraw.Draw(comp, "RGBA")

    # border + diagonal lines for designer look
    d.rounded_rectangle((24, 24, W - 24, H - 24), radius=26, outline=(255, 255, 255, 56), width=2)
    for i in range(-6, 16):
        x = i * 170
        d.line((x, 0, x + 470, H), fill=(255, 255, 255, 12), width=1)

    scene_map[kind](d, pal)

    comp = grain(comp).filter(ImageFilter.UnsharpMask(radius=1.8, percent=130, threshold=2))
    comp = ImageOps.autocontrast(comp.convert("RGB"), cutoff=1)
    comp.save(os.path.join(OUT, fname), "WEBP", quality=93, method=6)

print("Generated", len(cases), "business-specific designer images")
