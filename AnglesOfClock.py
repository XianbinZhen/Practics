# Given a time in the format of hour and minute,
# calculate the angle of the hour and minute hand on a clock.
#
# def calcAngle(h, m):
#   # Fill this in.
#
# print calcAngle(3, 30)
# # 75
# print calcAngle(12, 30)
# # 165

def calcAngle(h, m):
    def get_h_angle(h, m):
        return (h + m / 60) / 12 * 360 % 360

    def get_m_angle(m):
        return m / 60 * 360

    return get_m_angle(m) - get_h_angle(h, m)


print(calcAngle(3, 30))
# 75
print(calcAngle(12, 30))
# 165
