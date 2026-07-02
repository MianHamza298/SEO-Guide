clicks = [120,150,170,210,260,300,340,380,420,470,510,560]
impressions = [40,52,60,75,88,95,110,125,140,150,168,182]
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

W, H = 600, 200
pad_l, pad_r, pad_t, pad_b = 10, 10, 10, 24
plot_w = W - pad_l - pad_r
plot_h = H - pad_t - pad_b

def points(data):
    mx = max(data)
    mn = 0
    pts = []
    n = len(data)
    for i, v in enumerate(data):
        x = pad_l + i/(n-1)*plot_w
        y = pad_t + plot_h - (v-mn)/(mx-mn)*plot_h
        pts.append((x,y))
    return pts

def polyline_str(pts):
    return " ".join(f"{x:.1f},{y:.1f}" for x,y in pts)

pc = points(clicks)
pi = points(impressions)
print("CLICKS POLYLINE:", polyline_str(pc))
print("IMPR POLYLINE:", polyline_str(pi))

# area path (clicks)
def area_path(pts):
    d = f"M{pts[0][0]:.1f},{pad_t+plot_h:.1f} "
    d += "L" + " L".join(f"{x:.1f},{y:.1f}" for x,y in pts)
    d += f" L{pts[-1][0]:.1f},{pad_t+plot_h:.1f} Z"
    return d
print("CLICKS AREA:", area_path(pc))

# x labels positions
for i,m in enumerate(months):
    x = pad_l + i/(len(months)-1)*plot_w
    print(m, f"{x:.1f}")
