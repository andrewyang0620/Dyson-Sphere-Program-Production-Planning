# this is a temporary file for testing purposes
eff0 = 0.75
eff1 = 1.0
eff2 = 1.5
eff3 = 3.0

def creation_rate(product_name, machine_name, product_per_min, machine_per_min, efficiency):
    machine_actual = machine_per_min * efficiency
    machine_needed = product_per_min / machine_actual
    print(f"{product_name}/min: {product_per_min} {machine_name}需求: {machine_needed:.2f}")
    return machine_needed

# 终产物
print("\n==========终产物需求==========")
creation_rate("绿糖", "研究站", 60, 5, eff1)

# 1级产物
print("\n==========1级产物需求==========")
creation_rate("蓝色芯片", "mk3制造台", 30, 10, eff2)
creation_rate("绿豆", "mk3制造台", 30, 10, eff2)

# 2级产物
print("\n==========2级产物需求==========")
creation_rate("黄色芯片", "mk3制造台", 60, 20, eff2) # 2.1
creation_rate("过滤玻璃" , "黑雾制造台", 60, 5, eff3) # 2.2
creation_rate("金刚石", "mk3制造台", 120, 80, eff2) # 2.3 # ENDS
creation_rate("绿管子", "粒子对撞机", 30, 7.5, eff1) # 2.4

# 3级产物
print("\n==========3级产物需求==========")
# for 2.1
creation_rate("电路板", "mk2制造台", 120, 120, eff1) #3.1
creation_rate("微晶原件", "mk2制造台", 120, 30, eff1) # 3.2
# for 2.2
creation_rate("卡西米尔晶体", "mk2制造台", 60, 15, eff1) # 3.3
creation_rate("钢化玻璃", "mk2制造台", 120, 24, eff1) # 3.4
# for 2.4
creation_rate("紫管子", "mk2制造台", 60, 15, eff1) # 3.5
creation_rate("铁块", "高级熔炉", 60, 60, 2) # 3.6 # ENDS
#重氢直接采集

# 4级产物
print("\n==========4级产物需求==========")
# for 3.1
creation_rate("铁块", "高级熔炉", 120, 60, 2) #ENDS
creation_rate("铜块", "高级熔炉", 60, 60, 2) #ENDS
# for 3.2
creation_rate("硅块", "高级熔炉", 240, 30, 2) #ENDS
creation_rate("铜块", "高级熔炉", 120, 60, 2) #ENDS
# for 3.3
# 光栅石直接采集 480/min
creation_rate("石墨烯", "初级化工厂", 120, 40, 1) # 生成副产物氢气 
# 氢气直接采集 720/min, 可燃冰副产物60/min
# for 3.4
creation_rate("玻璃", "高级熔炉", 120, 30, 2)
creation_rate("钛块", "高级熔炉", 120, 30, 2) #ENDS
creation_rate("水", "抽水机", 120, 50, 1) #ENDS
# for 3.5
creation_rate("铜块", "高级熔炉", 120, 60, 2) #ENDS
# 单极磁石直接采集 600/min

# 基础矿物
print("\n==========基础矿物需求==========")
print(f"金伯利矿石: {60}/min")
print(f"铁矿石: {60+120}/min")
print(f"铜矿石: {120+120}/min")
print(f"硅矿石: {480}/min")
print(f"氢气: {660}/min")
print(f"重氢: {300}/min")
print(f"可燃冰: {120}/min")
print(f"光栅石: {480}/min")
print(f"石头: {240}/min")
print(f"钛矿石: {240}/min")
print(f"单极磁石: {600}/min")
print("铁块: 1.5; 铜块: 2.5; 硅块: 4; 钛块: 2")