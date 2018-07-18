# coded by MOHD ASYRAF BIN RUSLAAN (B16CS0006)
# TIME SLOT JB
TS1_JB = "1800-1900"
TS2_JB = "2000-2300"
TS3_JB = "1100-1300"
TS4_JB = "1400-1600"
TS5_JB = "1630-1830"
TS6_JB = "2000-2200"

# TIME SLOT KL
TS1_KL = "1400-1600"
TS2_KL = "1630-1830"
TS3_KL = "2000-2200"
TS4_KL = "0830-1030"
TS5_KL = "1100-1300"
TS6_KL = "1400-1600"

# TIME SLOT PP
TS1_PP = "1400-1600"
TS2_PP = "1630-1830"
TS3_PP = "2000-2200"
TS4_PP = "0830-1030"
TS5_PP = "1100-1300"
TS6_PP = "1400-1600"

# GROUP
G1 = "GROUP 1"
G2 = "GROUP 2"
G3 = "GROUP 3"


class JB(object):
    def __init__(self, date, timeslot, group):
        self.date = date
        self.timeslot = timeslot
        self.group = group


class KL(object):
    def __init__(self, date, timeslot, group):
        self.date = date
        self.timeslot = timeslot
        self.group = group


class PP(object):
    def __init__(self, date, timeslot, group):
        self.date = date
        self.timeslot = timeslot
        self.group = group


# Timetable JB
jb1 = JB("8 Sept", (TS3_JB, TS4_JB, TS5_JB, TS6_JB), G1)
jb2 = JB("15 Sept", (TS3_JB, TS4_JB, TS5_JB, TS6_JB), G2)
jb3 = JB("22 Sept", (TS3_JB, TS4_JB, TS5_JB, TS6_JB), G3)
jb4_1 = JB("28 Sept", (TS1_JB, TS2_JB), G1)
jb4_2 = JB("29 Sept", (TS4_JB, TS5_JB, TS6_JB), G1)
jb5_1 = JB("5 Oct", (TS1_JB, TS2_JB), G2)
jb5_2 = JB("6 Oct", (TS3_JB, TS4_JB, TS5_JB, TS6_JB), G2)
jb6_1 = JB("12 Oct", (TS1_JB, TS2_JB), G3)
jb6_2 = JB("13 Oct", (TS3_JB, TS4_JB, TS5_JB), G3)
jb7_1 = JB("19 Oct", (TS1_JB, TS2_JB), G1)
jb7_2 = JB("20 Oct", (TS3_JB, TS4_JB, TS5_JB, TS6_JB), G1)
jb8 = JB("27 Oct", (TS3_JB, TS4_JB, TS5_JB, TS6_JB), G2)
jb9 = JB("3 Nov", (TS3_JB, TS4_JB, TS5_JB, TS6_JB), G3)
jb11_1 = JB("16 Nov", (TS1_JB, TS2_JB), G3)
jb11_2 = JB("17 Nov", (TS3_JB, TS4_JB, TS5_JB, TS6_JB), G3)
jb12_1 = JB("23 Nov", (TS1_JB, TS2_JB), G2)
jb12_2 = JB("24 Nov", (TS3_JB, TS4_JB, TS5_JB, TS6_JB), G2)
jb13_1 = JB("30 Nov", (TS1_JB, TS2_JB), G1)
jb13_2 = JB("1 Dis", (TS3_JB, TS4_JB, TS5_JB, TS6_JB), G1)
jb14 = JB("8 Dis", (TS3_JB, TS4_JB, TS5_JB, TS6_JB), G2)
jb15 = JB("15 Dis", (TS3_JB, TS4_JB, TS5_JB, TS6_JB), G3)

# Timetable KL
KL2 = KL("15 Sept", (TS1_KL, TS2_KL, TS3_KL), G1)
KL3_1 = KL("22 Sept", (TS1_KL, TS2_KL, TS3_KL), G2)
KL3_2 = KL("23 Sept", (TS4_KL, TS5_KL, TS6_KL), G3)
KL4_1 = KL("29 Sept", (TS1_KL, TS2_KL, TS3_KL), G1)
KL4_2 = KL("30 Sept", (TS4_KL, TS5_KL, TS6_KL), G1)
KL5_1 = KL("6 Oct", (TS1_KL, TS2_KL, TS3_KL), G2)
KL5_2 = KL("7 Oct", (TS4_KL, TS5_KL, TS6_KL), G2)
KL6_1 = KL("13 Oct", (TS1_KL, TS2_KL, TS3_KL), G3)
KL6_2 = KL("14 Oct", (TS4_KL, TS5_KL, TS6_KL), G3)
KL7_1 = KL("20 Oct", (TS1_KL, TS2_KL, TS3_KL), G1)
KL7_2 = KL("21 Oct", (TS4_KL, TS5_KL, TS6_KL), G2)
KL8_1 = KL("27 Oct", (TS1_KL, TS2_KL, TS3_KL), G3)
KL8_2 = KL("28 Oct", (TS4_KL, TS5_KL, TS6_KL), G3)
KL9_1 = KL("3 Nov", (TS1_KL, TS2_KL, TS3_KL), G1)
KL9_2 = KL("4 Nov", (TS4_KL, TS5_KL, TS6_KL), G1)
KL11_1 = KL("17 Nov", (TS1_KL, TS2_KL, TS3_KL), G2)
KL11_2 = KL("18 Nov", (TS4_KL, TS5_KL, TS6_KL), G2)
KL12_1 = KL("24 Nov", (TS1_KL, TS2_KL, TS3_KL), G3)
KL12_2 = KL("25 Nov", (TS4_KL, TS5_KL, TS6_KL), G1)
KL13_1 = KL("1 Dis", (TS1_KL, TS2_KL, TS3_KL), "Only SCSJ/SCJ 2154 OOP")
KL13_2 = KL("2 Dis", (TS4_KL, TS5_KL, TS6_KL), G2)
KL14_1 = KL("8 Dis", (TS1_KL, TS2_KL, TS3_KL), G3)
KL14_2 = KL("9 Dis", (TS4_KL, TS5_KL, TS6_KL), "Only SCS*/SC* 3104 AD")

# Timetable PP
pp3 = PP("22 Sept", (TS1_PP, TS2_PP, TS3_PP), G1)
pp4_1 = PP("29 Sept", (TS1_PP, TS2_PP, TS3_PP), G2)
pp4_2 = PP("30 Sept", (TS4_PP, TS5_PP, TS6_PP), G3)
pp5_1 = PP("6 Oct", (TS1_PP, TS2_PP, TS3_PP), G1)
pp5_2 = PP("7 Oct", (TS4_PP, TS5_PP, TS6_PP), G1)
pp6_1 = PP("13 Oct", (TS1_PP, TS2_PP, TS3_PP), G2)
pp6_2 = PP("14 Oct", (TS4_PP, TS5_PP, TS6_PP), G2)
pp7_1 = PP("20 Oct", (TS1_PP, TS2_PP, TS3_PP), G3)
pp7_2 = PP("21 Oct", (TS4_PP, TS5_PP, TS6_PP), G3)
pp8_1 = PP("27 Oct", (TS1_PP, TS2_PP, TS3_PP), G1)
pp8_2 = PP("28 Oct", (TS4_PP, TS5_PP, TS6_PP), G1)
pp9_1 = PP("3 Nov", (TS1_PP, TS2_PP, TS3_PP), G2)
pp9_2 = PP("4 Nov", (TS4_PP, TS5_PP, TS6_PP), G2)
pp11_1 = PP("17 Nov", (TS1_PP, TS2_PP, TS3_PP), G3)
pp11_2 = PP("18 Nov", (TS4_PP, TS5_PP, TS6_PP), G3)
pp12_1 = PP("24 Nov", (TS1_PP, TS2_PP, TS3_PP), G1)
pp12_2 = PP("25 Nov", (TS4_PP, TS5_PP, TS6_PP), G1)
pp13_1 = PP("1 Dis", (TS1_PP, TS2_PP, TS3_PP), G3)
pp13_2 = PP("2 Dis", (TS4_PP, TS5_PP, TS6_PP), G3)
pp14_1 = PP("8 Dis", (TS1_PP, TS2_PP, TS3_PP), G2)
pp14_2 = PP("9 Dis", (TS4_PP, TS5_PP, TS6_PP), G2)

# Counter untuk check clash
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0
counter6 = 0
counter7 = 0
counter8 = 0
counter9 = 0
counter10 = 0
counter11 = 0
counter12 = 0
counter13 = 0
counter14 = 0
counter15 = 0
counter16 = 0
counter17 = 0
counter18 = 0
counter19 = 0
counter20 = 0
counter21 = 0
counter22 = 0
counter23 = 0
counter24 = 0
counter25 = 0
counter26 = 0
counter27 = 0




print("------------------------")
print("Clash between JB and KL")
print("------------------------")
print("Group 1 JB and Group 1 KL")
for x in (jb1, jb2, jb3, jb4_1, jb4_2, jb5_1, jb5_2, jb6_1, jb6_2, jb7_1, jb7_2, jb8, jb9, jb11_1, jb11_2, jb12_1,
          jb12_2, jb13_1, jb13_2, jb14, jb15):

    for y in (KL2, KL3_1, KL3_1, KL4_1, KL4_2, KL5_1, KL5_2, KL6_1, KL6_2, KL7_1, KL7_2, KL8_1, KL8_2, KL9_1, KL9_2,
              KL11_1, KL11_2, KL12_1, KL12_2, KL13_1, KL13_2, KL14_1, KL14_2):

        if (x.group == G1 and y.group == G1) and (x.date == y.date):
            print(x.date)
            counter1 += 1

if counter1 == 0:
    print("No clash")


print("")
print("Group 1 JB and Group 2 KL")
for x in (jb1, jb2, jb3, jb4_1, jb4_2, jb5_1, jb5_2, jb6_1, jb6_2, jb7_1, jb7_2, jb8, jb9, jb11_1, jb11_2, jb12_1,
          jb12_2, jb13_1, jb13_2, jb14, jb15):

    for y in (KL2, KL3_1, KL3_1, KL4_1, KL4_2, KL5_1, KL5_2, KL6_1, KL6_2, KL7_1, KL7_2, KL8_1, KL8_2, KL9_1, KL9_2,
              KL11_1, KL11_2, KL12_1, KL12_2, KL13_1, KL13_2, KL14_1, KL14_2):

        if (x.group == G1 and y.group == G2) and (x.date == y.date):
            print(x.date)
            counter10 += 1

if counter10 == 0:
    print("No clash")


print("")
print("Group 1 JB and Group 3 KL")
for x in (jb1, jb2, jb3, jb4_1, jb4_2, jb5_1, jb5_2, jb6_1, jb6_2, jb7_1, jb7_2, jb8, jb9, jb11_1, jb11_2, jb12_1,
          jb12_2, jb13_1, jb13_2, jb14, jb15):

    for y in (KL2, KL3_1, KL3_1, KL4_1, KL4_2, KL5_1, KL5_2, KL6_1, KL6_2, KL7_1, KL7_2, KL8_1, KL8_2, KL9_1, KL9_2,
              KL11_1, KL11_2, KL12_1, KL12_2, KL13_1, KL13_2, KL14_1, KL14_2):

        if (x.group == G1 and y.group == G3) and (x.date == y.date):
            print(x.date)
            counter11 += 1

if counter11 == 0:
    print("No clash")

print("")
print("Group 2 JB and Group 1 KL")
for x in (jb1, jb2, jb3, jb4_1, jb4_2, jb5_1, jb5_2, jb6_1, jb6_2, jb7_1, jb7_2, jb8, jb9, jb11_1, jb11_2, jb12_1,
          jb12_2, jb13_1, jb13_2, jb14, jb15):

    for y in (KL2, KL3_1, KL3_1, KL4_1, KL4_2, KL5_1, KL5_2, KL6_1, KL6_2, KL7_1, KL7_2, KL8_1, KL8_2, KL9_1, KL9_2,
              KL11_1, KL11_2, KL12_1, KL12_2, KL13_1, KL13_2, KL14_1, KL14_2):

        if (x.group == G2 and y.group == G1) and (x.date == y.date):
            print(x.date)
            counter2 += 1

if counter2 == 0:
    print("No clash")

print("")
print("Group 2 JB and Group 2 KL")
for x in (jb1, jb2, jb3, jb4_1, jb4_2, jb5_1, jb5_2, jb6_1, jb6_2, jb7_1, jb7_2, jb8, jb9, jb11_1, jb11_2, jb12_1,
          jb12_2, jb13_1, jb13_2, jb14, jb15):

    for y in (KL2, KL3_1, KL3_1, KL4_1, KL4_2, KL5_1, KL5_2, KL6_1, KL6_2, KL7_1, KL7_2, KL8_1, KL8_2, KL9_1, KL9_2,
              KL11_1, KL11_2, KL12_1, KL12_2, KL13_1, KL13_2, KL14_1, KL14_2):

        if (x.group == G2 and y.group == G2) and (x.date == y.date):
            print(x.date)
            counter12 += 1

if counter12 == 0:
    print("No clash")

print("")
print("Group 2 JB and Group 3 KL")
for x in (jb1, jb2, jb3, jb4_1, jb4_2, jb5_1, jb5_2, jb6_1, jb6_2, jb7_1, jb7_2, jb8, jb9, jb11_1, jb11_2, jb12_1,
          jb12_2, jb13_1, jb13_2, jb14, jb15):

    for y in (KL2, KL3_1, KL3_1, KL4_1, KL4_2, KL5_1, KL5_2, KL6_1, KL6_2, KL7_1, KL7_2, KL8_1, KL8_2, KL9_1, KL9_2,
              KL11_1, KL11_2, KL12_1, KL12_2, KL13_1, KL13_2, KL14_1, KL14_2):

        if (x.group == G2 and y.group == G3) and (x.date == y.date):
            print(x.date)
            counter13 += 1

if counter13 == 0:
    print("No clash")

print("")
print("Group 3 JB and Group 1 KL")
for x in (jb1, jb2, jb3, jb4_1, jb4_2, jb5_1, jb5_2, jb6_1, jb6_2, jb7_1, jb7_2, jb8, jb9, jb11_1, jb11_2, jb12_1,
          jb12_2, jb13_1, jb13_2, jb14, jb15):

    for y in (KL2, KL3_1, KL3_1, KL4_1, KL4_2, KL5_1, KL5_2, KL6_1, KL6_2, KL7_1, KL7_2, KL8_1, KL8_2, KL9_1, KL9_2,
              KL11_1, KL11_2, KL12_1, KL12_2, KL13_1, KL13_2, KL14_1, KL14_2):

        if (x.group == G3 and y.group == G1) and (x.date == y.date):
            print(x.date)
            counter14 += 1

if counter14 == 0:
    print("No clash")

print("")
print("Group 3 JB and Group 2 KL")
for x in (jb1, jb2, jb3, jb4_1, jb4_2, jb5_1, jb5_2, jb6_1, jb6_2, jb7_1, jb7_2, jb8, jb9, jb11_1, jb11_2, jb12_1,
          jb12_2, jb13_1, jb13_2, jb14, jb15):

    for y in (KL2, KL3_1, KL3_1, KL4_1, KL4_2, KL5_1, KL5_2, KL6_1, KL6_2, KL7_1, KL7_2, KL8_1, KL8_2, KL9_1, KL9_2,
              KL11_1, KL11_2, KL12_1, KL12_2, KL13_1, KL13_2, KL14_1, KL14_2):

        if (x.group == G3 and y.group == G2) and (x.date == y.date):
            print(x.date)
            counter15 += 1

if counter15 == 0:
    print("No clash")

print("")
print("Group 3 JB and Group 3 KL")
for x in (jb1, jb2, jb3, jb4_1, jb4_2, jb5_1, jb5_2, jb6_1, jb6_2, jb7_1, jb7_2, jb8, jb9, jb11_1, jb11_2, jb12_1,
          jb12_2, jb13_1, jb13_2, jb14, jb15):

    for y in (KL2, KL3_1, KL3_1, KL4_1, KL4_2, KL5_1, KL5_2, KL6_1, KL6_2, KL7_1, KL7_2, KL8_1, KL8_2, KL9_1, KL9_2,
              KL11_1, KL11_2, KL12_1, KL12_2, KL13_1, KL13_2, KL14_1, KL14_2):

        if (x.group == G3 and y.group == G3) and (x.date == y.date):
            print(x.date)
            counter16 += 1

if counter16 == 0:
    print("No clash")

print("")
print("------------------------")
print("Clash between JB and PP")
print("------------------------")
print("Group 1 JB group 1 PP")
for x in (jb1, jb2, jb3, jb4_1, jb4_2, jb5_1, jb5_2, jb6_1, jb6_2, jb7_1, jb7_2, jb8, jb9, jb11_1, jb11_2, jb12_1,
          jb12_2, jb13_1, jb13_2, jb14, jb15):

    for y in (pp3, pp4_1, pp4_2, pp5_1, pp5_2, pp6_1, pp6_2, pp7_1, pp7_2, pp8_1, pp8_2, pp9_1, pp9_2, pp11_1, pp11_2,
              pp12_1, pp12_2, pp13_1, pp13_2, pp14_1, pp14_2):

        if (x.group == G1 and y.group == G1) and (x.date == y.date):
            print(x.date)
            counter4 += 1

if counter4 == 0:
    print("No clash")

print("")
print("Group 1 JB and Group 2 PP")
for x in (jb1, jb2, jb3, jb4_1, jb4_2, jb5_1, jb5_2, jb6_1, jb6_2, jb7_1, jb7_2, jb8, jb9, jb11_1, jb11_2, jb12_1,
          jb12_2, jb13_1, jb13_2, jb14, jb15):

    for y in (pp3, pp4_1, pp4_2, pp5_1, pp5_2, pp6_1, pp6_2, pp7_1, pp7_2, pp8_1, pp8_2, pp9_1, pp9_2, pp11_1, pp11_2,
              pp12_1, pp12_2, pp13_1, pp13_2, pp14_1, pp14_2):

        if (x.group == G1 and y.group == G2) and (x.date == y.date):
            print(x.date)
            counter17 += 1

if counter17 == 0:
    print("No clash")

print("")
print("Group 1 JB and Group 3 PP")
for x in (jb1, jb2, jb3, jb4_1, jb4_2, jb5_1, jb5_2, jb6_1, jb6_2, jb7_1, jb7_2, jb8, jb9, jb11_1, jb11_2, jb12_1,
          jb12_2, jb13_1, jb13_2, jb14, jb15):

    for y in (pp3, pp4_1, pp4_2, pp5_1, pp5_2, pp6_1, pp6_2, pp7_1, pp7_2, pp8_1, pp8_2, pp9_1, pp9_2, pp11_1, pp11_2,
              pp12_1, pp12_2, pp13_1, pp13_2, pp14_1, pp14_2):

        if (x.group == G1 and y.group == G3) and (x.date == y.date):
            print(x.date)
            counter18 += 1

if counter18 == 0:
    print("No clash")


print("")
print("Group 2 JB and Group 1 PP")
for x in (jb1, jb2, jb3, jb4_1, jb4_2, jb5_1, jb5_2, jb6_1, jb6_2, jb7_1, jb7_2, jb8, jb9, jb11_1, jb11_2, jb12_1,
          jb12_2, jb13_1, jb13_2, jb14, jb15):

    for y in (pp3, pp4_1, pp4_2, pp5_1, pp5_2, pp6_1, pp6_2, pp7_1, pp7_2, pp8_1, pp8_2, pp9_1, pp9_2, pp11_1, pp11_2,
              pp12_1, pp12_2, pp13_1, pp13_2, pp14_1, pp14_2):

        if (x.group == G2 and y.group == G1) and (x.date == y.date):
            print(x.date)
            counter5 += 1

if counter5 == 0:
    print("No clash")

print("")
print("Group 2 JB and Group 2 PP")
for x in (jb1, jb2, jb3, jb4_1, jb4_2, jb5_1, jb5_2, jb6_1, jb6_2, jb7_1, jb7_2, jb8, jb9, jb11_1, jb11_2, jb12_1,
          jb12_2, jb13_1, jb13_2, jb14, jb15):

    for y in (pp3, pp4_1, pp4_2, pp5_1, pp5_2, pp6_1, pp6_2, pp7_1, pp7_2, pp8_1, pp8_2, pp9_1, pp9_2, pp11_1, pp11_2,
              pp12_1, pp12_2, pp13_1, pp13_2, pp14_1, pp14_2):

        if (x.group == G2 and y.group == G2) and (x.date == y.date):
            print(x.date)
            counter19 += 1

if counter19 == 0:
    print("No clash")

print("")
print("Group 2 JB and Group 3 PP")
for x in (jb1, jb2, jb3, jb4_1, jb4_2, jb5_1, jb5_2, jb6_1, jb6_2, jb7_1, jb7_2, jb8, jb9, jb11_1, jb11_2, jb12_1,
          jb12_2, jb13_1, jb13_2, jb14, jb15):

    for y in (pp3, pp4_1, pp4_2, pp5_1, pp5_2, pp6_1, pp6_2, pp7_1, pp7_2, pp8_1, pp8_2, pp9_1, pp9_2, pp11_1, pp11_2,
              pp12_1, pp12_2, pp13_1, pp13_2, pp14_1, pp14_2):

        if (x.group == G2 and y.group == G3) and (x.date == y.date):
            print(x.date)
            counter20 += 1

if counter20 == 0:
    print("No clash")


print("")
print("Group 3 JB and Group 1 PP")
for x in (jb1, jb2, jb3, jb4_1, jb4_2, jb5_1, jb5_2, jb6_1, jb6_2, jb7_1, jb7_2, jb8, jb9, jb11_1, jb11_2, jb12_1,
          jb12_2, jb13_1, jb13_2, jb14, jb15):

    for y in (pp3, pp4_1, pp4_2, pp5_1, pp5_2, pp6_1, pp6_2, pp7_1, pp7_2, pp8_1, pp8_2, pp9_1, pp9_2, pp11_1, pp11_2,
              pp12_1, pp12_2, pp13_1, pp13_2, pp14_1, pp14_2):

        if (x.group == G3 and y.group == G1) and (x.date == y.date):
            print(x.date)
            counter6 += 1

if counter6 == 0:
    print("No clash")

print("")
print("Group 3 JB and Group 2 PP")
for x in (jb1, jb2, jb3, jb4_1, jb4_2, jb5_1, jb5_2, jb6_1, jb6_2, jb7_1, jb7_2, jb8, jb9, jb11_1, jb11_2, jb12_1,
          jb12_2, jb13_1, jb13_2, jb14, jb15):

    for y in (pp3, pp4_1, pp4_2, pp5_1, pp5_2, pp6_1, pp6_2, pp7_1, pp7_2, pp8_1, pp8_2, pp9_1, pp9_2, pp11_1, pp11_2,
              pp12_1, pp12_2, pp13_1, pp13_2, pp14_1, pp14_2):

        if (x.group == G3 and y.group == G2) and (x.date == y.date):
            print(x.date)
            counter21 += 1

if counter21 == 0:
    print("No clash")

print("")
print("Group 3 JB and Group 3 PP")
for x in (jb1, jb2, jb3, jb4_1, jb4_2, jb5_1, jb5_2, jb6_1, jb6_2, jb7_1, jb7_2, jb8, jb9, jb11_1, jb11_2, jb12_1,
          jb12_2, jb13_1, jb13_2, jb14, jb15):

    for y in (pp3, pp4_1, pp4_2, pp5_1, pp5_2, pp6_1, pp6_2, pp7_1, pp7_2, pp8_1, pp8_2, pp9_1, pp9_2, pp11_1, pp11_2,
              pp12_1, pp12_2, pp13_1, pp13_2, pp14_1, pp14_2):

        if (x.group == G3 and y.group == G3) and (x.date == y.date):
            print(x.date)
            counter22 += 1

if counter22 == 0:
    print("No clash")

print("")
print("------------------------")
print("Clash between KL and PP")
print("------------------------")
print("Group 1 KL and Group 1 PP")
for x in (KL2, KL3_1, KL3_1, KL4_1, KL4_2, KL5_1, KL5_2, KL6_1, KL6_2, KL7_1, KL7_2, KL8_1, KL8_2, KL9_1, KL9_2,
          KL11_1, KL11_2, KL12_1, KL12_2, KL13_1, KL13_2, KL14_1, KL14_2):

    for y in (pp3, pp4_1, pp4_2, pp5_1, pp5_2, pp6_1, pp6_2, pp7_1, pp7_2, pp8_1, pp8_2, pp9_1, pp9_2, pp11_1, pp11_2,
              pp12_1, pp12_2, pp13_1, pp13_2, pp14_1, pp14_2):

        if (x.group == G1 and y.group == G1) and (x.date == y.date):
            print(x.date)
            counter7 += 1

if counter7 == 0:
    print("No clash")


print("")
print("Group : 1 KL and Group 2 PP")
for x in (KL2, KL3_1, KL3_1, KL4_1, KL4_2, KL5_1, KL5_2, KL6_1, KL6_2, KL7_1, KL7_2, KL8_1, KL8_2, KL9_1, KL9_2,
          KL11_1, KL11_2, KL12_1, KL12_2, KL13_1, KL13_2, KL14_1, KL14_2):

    for y in (pp3, pp4_1, pp4_2, pp5_1, pp5_2, pp6_1, pp6_2, pp7_1, pp7_2, pp8_1, pp8_2, pp9_1, pp9_2, pp11_1, pp11_2,
              pp12_1, pp12_2, pp13_1, pp13_2, pp14_1, pp14_2):

        if (x.group == G1 and y.group == G2) and (x.date == y.date):
            print(x.date)
            counter23 += 1

if counter23 == 0:
    print("No clash")

print("")
print("Group 1 KL and Group 3 PP")
for x in (KL2, KL3_1, KL3_1, KL4_1, KL4_2, KL5_1, KL5_2, KL6_1, KL6_2, KL7_1, KL7_2, KL8_1, KL8_2, KL9_1, KL9_2,
          KL11_1, KL11_2, KL12_1, KL12_2, KL13_1, KL13_2, KL14_1, KL14_2):

    for y in (pp3, pp4_1, pp4_2, pp5_1, pp5_2, pp6_1, pp6_2, pp7_1, pp7_2, pp8_1, pp8_2, pp9_1, pp9_2, pp11_1, pp11_2,
              pp12_1, pp12_2, pp13_1, pp13_2, pp14_1, pp14_2):

        if (x.group == G1 and y.group == G3) and (x.date == y.date):
            print(x.date)
            counter23 += 1

if counter23 == 0:
    print("No clash")

print("")
print("Group 2 KL and Group 1 PP")
for x in (KL2, KL3_1, KL3_1, KL4_1, KL4_2, KL5_1, KL5_2, KL6_1, KL6_2, KL7_1, KL7_2, KL8_1, KL8_2, KL9_1, KL9_2,
          KL11_1, KL11_2, KL12_1, KL12_2, KL13_1, KL13_2, KL14_1, KL14_2):

    for y in (pp3, pp4_1, pp4_2, pp5_1, pp5_2, pp6_1, pp6_2, pp7_1, pp7_2, pp8_1, pp8_2, pp9_1, pp9_2, pp11_1, pp11_2,
              pp12_1, pp12_2, pp13_1, pp13_2, pp14_1, pp14_2):

        if (x.group == G2 and y.group == G1) and (x.date == y.date):
            print(x.date)
            counter8 += 1

if counter8 == 0:
    print("No clash")

print("")
print("Group 2 KL and Group 2 PP")
for x in (KL2, KL3_1, KL3_1, KL4_1, KL4_2, KL5_1, KL5_2, KL6_1, KL6_2, KL7_1, KL7_2, KL8_1, KL8_2, KL9_1, KL9_2,
          KL11_1, KL11_2, KL12_1, KL12_2, KL13_1, KL13_2, KL14_1, KL14_2):

    for y in (pp3, pp4_1, pp4_2, pp5_1, pp5_2, pp6_1, pp6_2, pp7_1, pp7_2, pp8_1, pp8_2, pp9_1, pp9_2, pp11_1, pp11_2,
              pp12_1, pp12_2, pp13_1, pp13_2, pp14_1, pp14_2):

        if (x.group == G2 and y.group == G2) and (x.date == y.date):
            print(x.date)
            counter24 += 1

if counter24 == 0:
    print("No clash")

print("")
print("Group 2 KL and Group 3 PP")
for x in (KL2, KL3_1, KL3_1, KL4_1, KL4_2, KL5_1, KL5_2, KL6_1, KL6_2, KL7_1, KL7_2, KL8_1, KL8_2, KL9_1, KL9_2,
          KL11_1, KL11_2, KL12_1, KL12_2, KL13_1, KL13_2, KL14_1, KL14_2):

    for y in (pp3, pp4_1, pp4_2, pp5_1, pp5_2, pp6_1, pp6_2, pp7_1, pp7_2, pp8_1, pp8_2, pp9_1, pp9_2, pp11_1, pp11_2,
              pp12_1, pp12_2, pp13_1, pp13_2, pp14_1, pp14_2):

        if (x.group == G2 and y.group == G3) and (x.date == y.date):
            print(x.date)
            counter25 += 1

if counter25 == 0:
    print("No clash")

print("")
print("Group 3 KL and Group 1 PP")
for x in (KL2, KL3_1, KL3_1, KL4_1, KL4_2, KL5_1, KL5_2, KL6_1, KL6_2, KL7_1, KL7_2, KL8_1, KL8_2, KL9_1, KL9_2,
          KL11_1, KL11_2, KL12_1, KL12_2, KL13_1, KL13_2, KL14_1, KL14_2):

    for y in (pp3, pp4_1, pp4_2, pp5_1, pp5_2, pp6_1, pp6_2, pp7_1, pp7_2, pp8_1, pp8_2, pp9_1, pp9_2, pp11_1, pp11_2,
              pp12_1, pp12_2, pp13_1, pp13_2, pp14_1, pp14_2):

        if (x.group == G3 and y.group == G1) and (x.date == y.date):
            print(x.date)
            counter9 += 1

if counter9 == 0:
    print("No clash")

print("")
print("Group 3 KL and Group 2 PP")
for x in (KL2, KL3_1, KL3_1, KL4_1, KL4_2, KL5_1, KL5_2, KL6_1, KL6_2, KL7_1, KL7_2, KL8_1, KL8_2, KL9_1, KL9_2,
          KL11_1, KL11_2, KL12_1, KL12_2, KL13_1, KL13_2, KL14_1, KL14_2):

    for y in (pp3, pp4_1, pp4_2, pp5_1, pp5_2, pp6_1, pp6_2, pp7_1, pp7_2, pp8_1, pp8_2, pp9_1, pp9_2, pp11_1, pp11_2,
              pp12_1, pp12_2, pp13_1, pp13_2, pp14_1, pp14_2):

        if (x.group == G3 and y.group == G2) and (x.date == y.date):
            print(x.date)
            counter26 += 1

if counter26 == 0:
    print("No clash")

print("")
print("Group 3 KL and Group 3 PP")
for x in (KL2, KL3_1, KL3_1, KL4_1, KL4_2, KL5_1, KL5_2, KL6_1, KL6_2, KL7_1, KL7_2, KL8_1, KL8_2, KL9_1, KL9_2,
          KL11_1, KL11_2, KL12_1, KL12_2, KL13_1, KL13_2, KL14_1, KL14_2):

    for y in (pp3, pp4_1, pp4_2, pp5_1, pp5_2, pp6_1, pp6_2, pp7_1, pp7_2, pp8_1, pp8_2, pp9_1, pp9_2, pp11_1, pp11_2,
              pp12_1, pp12_2, pp13_1, pp13_2, pp14_1, pp14_2):

        if (x.group == G3 and y.group == G3) and (x.date == y.date):
            print(x.date)
            counter27 += 1

if counter27 == 0:
    print("No clash")

exit()
