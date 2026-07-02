import math

def donut(data, colors, cx, cy, r, r_inner, labels):
    total = sum(v for _, v in data)
    start = -90
    paths = []
    for (name, v), color in zip(data, colors):
        angle = v/total*360
        end = start + angle
        def pt(a, rad):
            rad_a = math.radians(a)
            return cx + rad*math.sin(rad_a), cy - rad*math.cos(rad_a)
        x1,y1 = pt(start, r)
        x2,y2 = pt(end, r)
        x3,y3 = pt(end, r_inner)
        x4,y4 = pt(start, r_inner)
        large = 1 if angle > 180 else 0
        d = f"M{x1:.2f},{y1:.2f} A{r},{r} 0 {large} 1 {x2:.2f},{y2:.2f} L{x3:.2f},{y3:.2f} A{r_inner},{r_inner} 0 {large} 0 {x4:.2f},{y4:.2f} Z"
        paths.append(f'<path d="{d}" fill="{color}"/>')
        start = end
    return "\n".join(paths)

# Pillars donut
pillars = [("On-Page",34),("Off-Page",33),("Technical",33)]
colors1 = ["#FF5A3C","#0E9C90","#E39B33"]
print("PILLARS DONUT")
print(donut(pillars, colors1, 130, 130, 110, 68, None))
print()

# Local donut
local = [("GBP Signals",30),("Reviews",20),("Backlinks & Citations",20),("On-Page Local",18),("Behavioral",12)]
colors2 = ["#FF5A3C","#0E9C90","#E39B33","#15202E","#8C6D3F"]
print("LOCAL DONUT")
print(donut(local, colors2, 130, 130, 110, 68, None))
