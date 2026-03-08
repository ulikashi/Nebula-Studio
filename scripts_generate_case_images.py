from PIL import Image, ImageDraw, ImageFilter, ImageOps
import os, random

W, H = 1600, 1000
OUT = "/Users/uliana/creative_dgi/Nebula-Studio/assets/images"
os.makedirs(OUT, exist_ok=True)

cases = [
    ("project-1.webp", "saas", ((14, 25, 44), (55, 118, 255))),
    ("project-2.webp", "wearable", ((33, 14, 43), (201, 88, 255))),
    ("project-3.webp", "campaign", ((10, 32, 35), (35, 173, 156))),
    ("project-4.webp", "fashion", ((46, 19, 16), (243, 111, 83))),
    ("project-5.webp", "strategy", ((13, 28, 44), (81, 156, 255))),
    ("project-6.webp", "audio", ((25, 14, 44), (165, 85, 255))),
    ("project-7.webp", "fintech", ((11, 30, 42), (50, 138, 226))),
    ("project-8.webp", "food", ((13, 35, 24), (58, 188, 122))),
]


def bg(c1, c2):
    img = Image.new("RGB", (W, H), c1)
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / (H - 1)
        r = int(c1[0] * (1 - t) + c2[0] * t)
        g = int(c1[1] * (1 - t) + c2[1] * t)
        b = int(c1[2] * (1 - t) + c2[2] * t)
        d.line((0, y, W, y), fill=(r, g, b))
    return img


def glass(d, x1, y1, x2, y2, r=22):
    d.rounded_rectangle((x1, y1, x2, y2), radius=r, fill=(255, 255, 255, 22), outline=(255, 255, 255, 85), width=2)


def draw_saas(d):
    # Laptop
    glass(d, 160, 180, 1120, 760)
    d.rounded_rectangle((240, 250, 1040, 640), radius=18, fill=(10, 17, 30, 210), outline=(160, 215, 255, 120), width=2)
    d.polygon([(190, 760), (1080, 760), (1160, 840), (120, 840)], fill=(210, 230, 255, 80))
    # Website blocks
    d.rounded_rectangle((280, 290, 440, 610), radius=12, fill=(255, 255, 255, 18))
    for i in range(7):
        y = 315 + i * 40
        d.rounded_rectangle((300, y, 420, y + 24), radius=6, fill=(120, 205, 255, 120))
    d.rounded_rectangle((470, 290, 1000, 440), radius=12, fill=(255, 255, 255, 16))
    points = [(500, 420), (570, 390), (650, 400), (730, 340), (810, 355), (900, 310), (980, 330)]
    d.line(points, fill=(130, 255, 220, 230), width=6)
    d.rounded_rectangle((470, 470, 660, 610), radius=12, fill=(255, 255, 255, 16))
    d.rounded_rectangle((680, 470, 840, 610), radius=12, fill=(255, 255, 255, 16))
    d.rounded_rectangle((860, 470, 1000, 610), radius=12, fill=(255, 255, 255, 16))


def draw_wearable(d):
    # Watch
    glass(d, 140, 140, 900, 860)
    d.rounded_rectangle((430, 210, 620, 790), radius=45, fill=(18, 14, 28, 235), outline=(255, 205, 245, 170), width=3)
    d.rounded_rectangle((460, 330, 590, 660), radius=24, fill=(255, 255, 255, 24), outline=(255, 225, 250, 110), width=2)
    d.arc((475, 410, 575, 510), start=25, end=330, fill=(255, 145, 228, 255), width=9)
    d.ellipse((510, 445, 540, 475), fill=(255, 245, 255, 240))
    # Product shots
    for i in range(3):
        x = 980 + i * 180
        glass(d, x, 260, x + 150, 550, 18)
        d.ellipse((x + 32, 330, x + 118, 416), fill=(255, 255, 255, 45), outline=(255, 225, 250, 80), width=2)
        d.rounded_rectangle((x + 48, 416, x + 102, 500), radius=12, fill=(255, 255, 255, 35))


def draw_campaign(d):
    # Street + billboard
    d.polygon([(0, 760), (W, 680), (W, H), (0, H)], fill=(20, 30, 34, 180))
    glass(d, 140, 160, 860, 700)
    d.rounded_rectangle((220, 230, 780, 560), radius=18, fill=(255, 255, 255, 20), outline=(180, 255, 230, 130), width=2)
    d.polygon([(420, 315), (420, 475), (560, 395)], fill=(210, 255, 240, 170))
    d.rectangle((320, 700, 380, 900), fill=(255, 255, 255, 50))
    d.rectangle((620, 700, 680, 900), fill=(255, 255, 255, 50))
    # Ad cards
    for i in range(3):
        x = 940 + i * 190
        glass(d, x, 250, x + 160, 600, 16)
        d.rounded_rectangle((x + 20, 290, x + 140, 470), radius=10, fill=(255, 255, 255, 20))


def draw_fashion(d):
    # Clothes rack + editorial cards
    glass(d, 140, 160, 980, 840)
    d.line((220, 300, 900, 300), fill=(255, 220, 190, 180), width=8)
    for i in range(6):
        x = 260 + i * 110
        d.line((x, 300, x, 520), fill=(255, 230, 210, 140), width=4)
        d.polygon([(x - 40, 350), (x + 40, 350), (x + 26, 480), (x - 26, 480)], fill=(255, 185 + i * 8, 155 + i * 5, 120))
    for r in range(2):
        for c in range(2):
            x = 1080 + c * 210
            y = 250 + r * 290
            glass(d, x, y, x + 180, y + 250, 16)
            d.rectangle((x + 24, y + 22, x + 156, y + 175), fill=(255, 255, 255, 40))


def draw_strategy(d):
    # Team board/table
    glass(d, 120, 170, 1480, 860)
    d.rounded_rectangle((220, 280, 1380, 740), radius=24, fill=(255, 255, 255, 18), outline=(180, 220, 255, 130), width=2)
    notes = [
        (280, 340, (255, 220, 135)),
        (520, 320, (130, 210, 255)),
        (760, 360, (146, 255, 220)),
        (1000, 330, (255, 190, 170)),
        (460, 520, (220, 190, 255)),
        (760, 520, (180, 230, 255)),
    ]
    for x, y, c in notes:
        d.rounded_rectangle((x, y, x + 230, y + 140), radius=12, fill=(*c, 180), outline=(255, 255, 255, 160), width=1)
    d.line((390, 410, 620, 390), fill=(230, 245, 255, 210), width=4)
    d.line((870, 430, 1120, 400), fill=(230, 245, 255, 210), width=4)
    d.line((640, 590, 880, 590), fill=(230, 245, 255, 210), width=4)


def draw_audio(d):
    # Turntable + headphones
    glass(d, 130, 150, 990, 850)
    d.ellipse((260, 240, 860, 840), fill=(255, 255, 255, 15), outline=(230, 180, 255, 130), width=3)
    d.ellipse((380, 360, 740, 720), fill=(14, 10, 24, 240), outline=(220, 170, 255, 160), width=3)
    d.ellipse((510, 490, 610, 590), fill=(255, 255, 255, 50))
    d.arc((270, 250, 850, 830), start=210, end=330, fill=(255, 165, 245, 230), width=16)
    for i in range(36):
        x = 1040 + i * 14
        h = 80 + ((i * 31) % 180)
        d.rounded_rectangle((x, 780 - h, x + 10, 780), radius=4, fill=(225, 160, 255, 220))


def draw_fintech(d):
    # Bank tower + card/payments
    glass(d, 120, 140, 940, 860)
    d.polygon([(260, 330), (530, 200), (800, 330)], fill=(255, 255, 255, 45))
    for i in range(5):
        x = 300 + i * 95
        d.rectangle((x, 330, x + 50, 740), fill=(255, 255, 255, 40))
    d.rectangle((260, 740, 840, 790), fill=(255, 255, 255, 55))
    glass(d, 1030, 260, 1460, 560, 20)
    d.rounded_rectangle((1080, 320, 1410, 500), radius=18, fill=(255, 255, 255, 25), outline=(185, 225, 255, 140), width=2)
    d.rectangle((1108, 372, 1380, 412), fill=(255, 255, 255, 45))


def draw_food(d):
    # Plate + packaging shelf
    glass(d, 120, 150, 950, 860)
    d.ellipse((240, 240, 840, 840), fill=(255, 255, 255, 28), outline=(205, 255, 220, 145), width=3)
    d.ellipse((350, 350, 730, 730), fill=(110, 195, 120, 140))
    d.ellipse((430, 430, 520, 520), fill=(255, 120, 90, 200))
    d.ellipse((560, 500, 650, 590), fill=(255, 210, 95, 200))
    d.ellipse((480, 560, 580, 660), fill=(145, 225, 140, 220))
    for i in range(3):
        x = 1060 + i * 170
        glass(d, x, 300, x + 140, 720, 14)
        d.rectangle((x + 28, 380, x + 112, 520), fill=(150, 240, 170, 155))


scene = {
    "saas": draw_saas,
    "wearable": draw_wearable,
    "campaign": draw_campaign,
    "fashion": draw_fashion,
    "strategy": draw_strategy,
    "audio": draw_audio,
    "fintech": draw_fintech,
    "food": draw_food,
}

for i, (name, kind, pal) in enumerate(cases, start=1):
    img = bg(pal[0], pal[1])
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer, "RGBA")

    # subtle lights
    random.seed(i * 13)
    for _ in range(6):
        x = random.randint(-200, W + 200)
        y = random.randint(-200, H + 200)
        r = random.randint(180, 420)
        d.ellipse((x - r, y - r, x + r, y + r), fill=(255, 255, 255, random.randint(12, 30)))

    scene[kind](d)

    # border and light lines
    d.rounded_rectangle((28, 28, W - 28, H - 28), radius=24, outline=(255, 255, 255, 62), width=2)
    for j in range(-5, 14):
        x = j * 180
        d.line((x, 0, x + 460, H), fill=(255, 255, 255, 10), width=1)

    out = Image.alpha_composite(img.convert("RGBA"), layer)
    out = out.filter(ImageFilter.UnsharpMask(radius=1.4, percent=120, threshold=2))
    out = ImageOps.autocontrast(out.convert("RGB"), cutoff=1)
    out.save(os.path.join(OUT, name), "WEBP", quality=92, method=6)

print("Generated clear business-specific illustrations")
