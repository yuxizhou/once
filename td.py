def calc(lidao, qijin, dongcha, huixin, huishang, mingzhong, waigong, neigong):
    h = 0.53 - 0.1    # hui xin
    s = 1.23      # hui shang
    m = 2 - 1.0     # ming zhong
    A = 1700            # wai gong
    a = 750             # nei gong

    # ## zhenwu ##
    # h = 0.466 - 0.336    # hui xin
    # s = 1.168           # hui shang
    # m = 1.703 - 1.13     # ming zhong
    # A = 1811            # wai gong
    # a = 1220             # nei gong

    if m > 1.0:
        m = 1.0

    standard = (h * s + 1) * (m * A + a)
    print 'standard:', standard

    h += huixin
    s += huishang
    m += mingzhong
    A += waigong
    a += neigong

    h += dongcha * 0.0002
    s += qijin * 0.00005
    m += dongcha * 0.0002
    A += lidao * 0.65
    a += qijin * 0.4
    a += dongcha * 0.1

    if m > 1.0:
        m = 1.0

    e = (h * s + 1) * (m * A + a)
    print 'param-->: ({} * {} + 1) * ({} * {} + {})'.format(h, s, m, A, a)
    print 'withplus:', e
    print 'withdiff:', e - standard
    print
    return e


FENG_HUA_6 = [116, 212, 155, 37, 29, 0.1088, 0.0486, 0.0]
LUO_HOU_6 =  [166, 170, 113, 72, 39, 0.0912, 0.0353, 0.0264]
LIU_DU_6 =   [104, 98,  169, 63, 35, 0.0807, 0.0324, 0.0782]
BEI_HUI_6 =  [205, 104, 180, 127,10, 0.0468, 0.0081, 0.0442]
LIE_FENG_6 = [190, 113, 109, 87, 45, 0.0324, 0.0342, 0.0376]

BEI_HUI_7 = [291, 167, 268, 127, 21, 0.0468, 0.0258, 0.0442]
LIE_FENG_7 = [322, 140, 151, 110, 45, 0.1020, 0.0342, 0.0664]

BEI_HUI_8 = [360, 213, 322, 229, 41, 0.0816, 0.0727, 0.073]
LIE_FENG_8 = [420, 185, 196, 215, 69, 0.1368, 0.0698, 0.0664]

FENG_HUA_7 = [130, 311, 215, 37, 51, 0.1436, 0.0840, 0.0288]
FENG_HUA_8 = [161, 395, 307, 105,64, 0.2284, 0.1264, 0.0576]

LIU_DU_7 = [141, 140, 219, 86, 57, 0.0904, 0.0501, 0.0860]
LIU_DU_8 = [195, 171, 288, 154, 57, 0.2365, 0.0925, 0.1148]

LUO_HOU_7 = [216, 297, 173, 72, 62, 0.0912, 0.0530, 0.0264]
LUO_HOU_8 = [270, 358, 212, 154, 93, 0.1372, 0.0919, 0.0642]




def calc_xin_fa(a, b, c):
    x = [
        a[0] + 0.6 * b[0] + 0.3 * c[0],
        a[1] + 0.6 * b[1] + 0.3 * c[1],
        a[2] + 0.6 * b[2] + 0.3 * c[2],
        a[3] + 0.6 * b[3] + 0.3 * c[3],
        a[4] + 0.6 * b[4] + 0.3 * c[4],
        a[5] + 0.6 * b[5] + 0.3 * c[5],
        a[6] + 0.6 * b[6] + 0.3 * c[6],
        a[7] + 0.6 * b[7] + 0.3 * c[7],
    ]
    return calc(x[0], x[1], x[2], x[6], x[7], x[5], x[3], x[4])


def calc_all_xin_fa():
    all = ['BEI_HUI', 'FENG_HUA', 'LUO_HOU', 'LIU_DU', 'LIE_FENG']
    level = ['_6', '_7', '_8']
    spec_level = ['_6', '_7', '_7']
    rank = {}

    import itertools

    # for a, b, c in list(itertools.permutations(all, 3)):
    #     for l1 in level:
    #         for l2 in level:
    #             for l3 in level:
    #                 r = calc_xin_fa(globals()[a+l1], globals()[b+l2], globals()[c+l3])
    #                 rank[r] = (a+l1, b+l2, c+l3)

    for a, b, c in list(itertools.permutations(all, 3)):
        for l1, l2, l3 in list(itertools.permutations(spec_level, 3)):
            r = calc_xin_fa(globals()[a+l1], globals()[b+l2], globals()[c+l3])
            rank[r] = (a+l1, b+l2, c+l3)

    for i in sorted(rank.keys(), reverse=True):
        a = 0
        for j in rank[i]:
            a += int(j.split('_')[-1])
        if a < 25:
            print i, rank[i]

print '###########################################################################'
print

# fenghua beihui changtian jiuying
calc(271, 292, 295, 0.05346, 0.02652, 0.13683, 113, 35)
# fenghua beihui jiuying changtian
calc(278, 300, 338, 0.06585, 0.02652, 0.15501, 120, 35)
# fenghua xiuluo jiuying changtian
calc(228, 291, 341, 0.08025, 0.04236, 0.18309, 43, 29)
# fenghua jiuying xiuluo changtian
calc(225, 290, 349, 0.08301, 0.02118, 0.17319, 50, 29)

# fenghua beihui xiuluo changtian
calc(309, 301, 330, 0.06309, 0.0477, 0.16491, 113, 35)
# beihui fenghua xiuluo jiuying
calc(345, 257, 328, 0.04689, 0.06538, 0.14013, 149, 27)

# beihui luohou xiuluo jiuying
calc(375, 232, 303, 0.03891, 0.08122, 0.1296, 170, 33)
# luohou beihui xiuluo jiuying
calc(347, 259, 276, 0.04979, 0.0741, 0.14736, 148, 45)

# beihui xiuluo bairen jiuying
calc(374, 188, 351, 0.02799, 0.08656, 0.13246, 155, 10)
# beihui bairen xiuluo jiuying
calc(394, 191, 328, 0.01899, 0.06538, 0.13389, 183, 10)
# beihui liudu xiuluo jiuying
calc(337, 189, 336, 0.03717, 0.1123, 0.1233, 164, 31)

print '###########################################################################'
print

calc(16, 0, 16, 0, 0, 0, 0, 0)
calc(0, 16, 16, 0, 0, 0, 0, 0)
calc(0, 0, 28, 0, 0, 0, 0, 0)

print '###########################################################################'
print

calc(100, 0, 0, 0, 0, 0, 0, 0)
calc(0, 100, 0, 0, 0, 0, 0, 0)
calc(0, 0, 100, 0, 0, 0, 0, 0)


