import numpy as np
import matplotlib.pyplot as plt

c64b = np.array([800772864,800773120,800772292,800773187,800773375,
		800772676,800773854,800773318,800665344,800772934])
c64p = np.array([12512079,12512077,12512064,12512076,12512084,
		12512070,12512086,12512079,12510393,12512080])
c128b = np.array([967048384,800772292,800772292,967048128,967050948,
		967051524,967050642,967049820,967050950,967050520])
c128p = np.array([7555066,7555090,7555066,7555065,7555086,
		7555095,7555081,7555077,7555086,7555086])
c512b = np.array([1029123334,1029122756,1029126208,1029123712,1029122560,
		1029125059,800773854,800773318,1029128668,1029118464])
c512p = np.array([2010008,2010008,2010011,2010010,2010005,
		2010019,2010018,2010004,2010025,2009997])
c1024b = np.array([902783174,902751428,902755292,902776600,902789514,
		902753874,902750406,871739584,902746112,902772932])
c1024p = np.array([881628,881594,881606,881625,881634,
		881601,881593,851311,881589,881616])
java64b = np.array([322437145,321513522,322613341,310798381,294293688,
		303284224,322017395,322502656,322420736,321638444])
java64p = np.array([5038080,5023648,5040832,4856224,4598336,
		4738816,5031520,5039104,5037824,5025600])
java128b = np.array([639356806,587153408,643317695,640827313,643088165,
		641163167,664846297,641351564,641171456,643395584])
java128p = np.array([4994976,4587136,5025920,5006464,5024128,
		5009088,5194112,5010560,5009152,5026528])
java256b = np.array([952716550,956027200,959036735,957873853,957785284,
		951490578,958315716,954655488,957776326,955068166])
java256p = np.array([3721549,3734483,3746245,3741696,3741351,
		3716766,3743423,3729122,3741315,3730740])

c64b = c64b.sum() / 10000000000.0
c64p = c64p.sum() / 10000000.0
c128b = c128b.sum() / 10000000000.0
c128p = c128p.sum() / 10000000.0
c512b = c512b.sum() / 10000000000.0
c512p = c512p.sum() / 10000000.0
c1024b = c1024b.sum() / 10000000000.0
c1024p = c1024p.sum() / 10000000.0
java64b = java64b.sum() / 10000000000.0
java64p = java64p.sum() / 10000000.0
java128b = java128b.sum() / 10000000000.0
java128p = java128p.sum() / 10000000.0
java256b = java256b.sum() / 10000000000.0
java256p = java256p.sum() / 10000000.0

N = 5

cbytes = [c64b, c128b, 0, c512b, c1024b]
cpackets = [c64p, c128p, 0, c512p, c1024p]

jbytes = [java64b,java128b,java256b, 0, 0]
jpackets = [java64p,java128p,java256p, 0, 0]

ind = np.arange(N)
width = 0.35

fig, ax = plt.subplots()
#ax2 = ax.twinx()
rects1 = ax.bar(ind, jpackets, width, color="r")
rects2 = ax.bar(ind+width, cpackets, width, color="b")

#ax.set_ylabel('Bytes per second (GigaBytes)')
ax.set_ylabel('Packets per second (millions)')
ax.set_xlabel('Packet size (Bytes)')
ax.set_xticks(ind + (width))
ax.set_xticklabels(["64", "128", "256", "512", "1024"])
ax.set_xlim(0,5)
ax.set_ylim(0,15)
#ax2.set_ylim(0,6)

ax.legend( (rects1[0], rects2[0]), ('Java', 'C') )

# plt.ylabel('packets per second (millions)')
# plt.xlabel('packet size (bytes)')
# plt.xticks(index + (bar_width/2), ["64", "128", "256", "512", "1024"])
# plt.yticks(np.arange(0, 15, 1))

plt.savefig("packets.png")
plt.show()



