# 列表的类型
# 列表最外层是中括号
# 列表中可存放任何数据类型的元素
# 列表是有顺序的、

# 定义一个列表
li = [1, "老孙", True, ["2","nice"]]
# 最外层中括号，中间会有很多个单独的元素，每个元素以逗号隔开。
# 列表可以从中取值。
# print(li[-1][-1])

# 列表也可以进行替换  替换的原则就是对于需要替换的位置，重新赋值。
# li[1] = "老赵"
# print(li[1][1])
# 取出ic
# print(li[-1][-1][1:3])


# 现有列表 ln = []
ln = ["2", "3", 2, ["老赵", "老孙"], "we", "['t']", 45, ["233"]]

# 取出老赵和老孙后，合并成 "老赵老孙"
# print(ln[3][0] + ln[3][1])
# print(f"{ln[3][0]}{ln[3][1]}")
# 计算列表中int类型的和
# print(ln[2] + ln[-2])
# 将233与3进行相乘。 int类型才能相乘。
# print(int(ln[-1][0]) * int(ln[1]))

# 输出wet 需要拼接列表中的元素
print(ln[4] + ln[5][2])
# 将老赵换成老王
ln[3][0] = "老王"
print(ln)
# 将233与45进行拼接变成23345
print(ln[-1][0] + str(ln[-2]))










