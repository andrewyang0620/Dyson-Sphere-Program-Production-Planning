# machine.py

# the class of machine
class Machine:
    def __init__(self, name, multiplier=1.0):
        self.name = name
        self.multiplier = multiplier
        
    def __repr__(self):
        return f"Machine({self.name}, x{self.multiplier})"

# the instance of machine
# raw material mining
miner = Machine("矿机", multiplier=1.0)
well = Machine("抽水机", multiplier=1.0)
oil_well = Machine("原油站", multiplier=1.0)
electron_receiver = Machine("射线接收站", multiplier=1.0)

# smelting
stove_low = Machine("初级熔炉", multiplier=1.0)
stove_high = Machine("高级熔炉", multiplier=2.0)
stove_ultra = Machine("黑雾熔炉", multiplier=3.0)

# crafting
crafter_mk1 = Machine("mk1制造台", multiplier=0.75)
crafter_mk2 = Machine("mk2制造台", multiplier=1.0)
crafter_mk3 = Machine("mk3制造台", multiplier=1.5)
crafter_ultra = Machine("黑雾制造台", multiplier=3.0)

# oil processing
hh_tower = Machine("分馏塔", multiplier=1.0)
oil_processor = Machine("精炼厂", multiplier=1.0)
crasher = Machine("对撞机", multiplier=1.0)

# chemical plant
chem_low = Machine("初级化工厂", multiplier=1.0)
chem_high = Machine("高级化工厂", multiplier=2.0)

# research station
research_station = Machine("研究站", multiplier=1.0)
research_station_ultra = Machine("黑雾研究站", multiplier=3.0)

# the dictionary of machine
MACHINES = {
    "矿机": miner,
    "初级熔炉": stove_low,
    "高级熔炉": stove_high,
    "黑雾熔炉": stove_ultra,
    "mk1制造台": crafter_mk1,
    "mk2制造台": crafter_mk2,
    "mk3制造台": crafter_mk3,
    "黑雾制造台": crafter_ultra,
    "抽水机": well,
    "原油站": oil_well,
    "分馏塔": hh_tower,
    "精炼厂": oil_processor,
    "对撞机": crasher,
    "初级化工厂": chem_low,
    "高级化工厂": chem_high,
    "研究站": research_station,
    "黑雾研究站": research_station_ultra,
    "射线接收站": electron_receiver
}