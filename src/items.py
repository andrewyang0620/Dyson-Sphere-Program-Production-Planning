# items.py
from requests import options
from machine import MACHINES, Machine
from recipe import RECIPE, SELECTED_RECIPE

class Item:
    def __init__(self, name, base_rate = None, machine_type = None):
        self.name = name
        recipe_data = self._load_recipe()
        self.recipe= recipe_data.get("inputs", {})
        self.base_rate = base_rate or recipe_data.get("base_rate", 0)
        self.machine_type = machine_type or recipe_data.get("machine_type", "未知设备")
        self.actual_rate = self.base_rate * MACHINES[self.machine_type].multiplier
        self.demand = 0

    def _load_recipe(self):
        if self.name not in RECIPE:
            return {}
        options = RECIPE[self.name]
        idx = SELECTED_RECIPE.get(self.name, 0)
        return options[idx]
    
    def machine_num(self):
        return self.demand / self.actual_rate if self.actual_rate > 0 else 0
        
    def reset(self):
        self.demand = 0
        
    def __repr__(self):
        return f"item({self.name}, {self.machine_type}, rate={self.demand:.2f}/min)"

# define items

# raw materials
## 普通矿石
iron_ore = Item("铁矿", base_rate=60, machine_type="矿脉")
copper_ore = Item("铜矿", base_rate=60, machine_type="矿脉")
stone_ore = Item("石矿", base_rate=60, machine_type="矿脉")
coal_ore = Item("煤矿", base_rate=60, machine_type="矿脉")
sil_ore = Item("硅矿", base_rate=60, machine_type="矿脉")
tit_ore = Item ("钛矿", base_rate=60, machine_type="矿脉")
## 液体/气体
water = Item("水", base_rate=50, machine_type="抽水机")
oil_ore = Item("原油", base_rate=5.0*60, machine_type="原油站") # 真实的rate取决于矿脉
h_1_1 = Item("氢-轨道采集器-气巨", base_rate=0.90*60, machine_type="轨道采集器")
h_1_2 = Item("氢-轨道采集器-冰巨", base_rate=0.30*60, machine_type="轨道采集器")
hh_1 = Item("重氢-轨道采集器", base_rate=0.30*60, machine_type="轨道采集器")
light = Item("临界光子", base_rate=60, machine_type="射线接收站")
## 珍奇矿石
diamond_ore = Item("金伯利矿石", base_rate=60, machine_type="矿脉")
tran_sil_ore = Item("分形硅石", base_rate=60, machine_type="矿脉")
lightstone_ore = Item("光栅石", base_rate=60, machine_type="矿脉")
bamboo = Item("刺笋结晶", base_rate=60, machine_type="矿脉")
mag_ore = Item("单极磁石", base_rate=40, machine_type="矿脉")
ice_1 = Item("可燃冰-矿机", base_rate=60, machine_type="矿脉")
ice_2 = Item("可燃冰-轨道采集器", base_rate=0.64*60, machine_type="轨道采集器")
organic = Item("有机晶体", base_rate=60, machine_type="矿脉")


# basic materials
h_h = Item("反物质")
iron = Item("铁块")
mag_circle = Item("磁铁")
copper = Item("铜块")
stone_material = Item("石材")
pencil = Item("石墨")
sil = Item("硅块")
tit = Item("钛块")
oil_gas = Item("精炼油")
glass = Item("玻璃")
diamond = Item("钻石")
tran_sil = Item("晶格硅")
plastic = Item("塑料")
wire_circle = Item("线圈")
net = Item("石墨烯")
electron_board = Item("电路板")
motor = Item("马达")
electronic = Item("微晶原件")
tit_crystal = Item("钛晶石")
net_tube = Item("碳纳米管")
gear = Item("齿轮")
green_motor = Item("绿马达")

# high level materials
green_tube = Item("绿管")
gold_cpu = Item("金cpu")
purple_crystal = Item("卡西米尔晶体")
cpu_tube = Item("粒子宽带", base_rate=7.5)
tit_glass = Item("钛玻璃")
cpu_glass = Item("位面过滤器")
blue_cpu = Item("蓝cpu")
purple_tube = Item("紫管")
green_mirror = Item("引力透镜")
# sugars
blue_matrix = Item("蓝糖")
red_matrix = Item("红糖")
yellow_matrix = Item("黄糖")
purple_matrix = Item("紫糖")
green_matrix = Item("绿糖")
white_matrix = Item("白糖")
# dictionary for items
ITEMS = {
    "铁矿": iron_ore,
    "铜矿": copper_ore,
    "石矿": stone_ore,
    "煤矿": coal_ore,
    "硅矿": sil_ore,
    "钛矿": tit_ore,
    "水": water,
    "原油": oil_ore,
    "氢-轨道采集器-气巨": h_1_1,
    "氢-轨道采集器-冰巨": h_1_2,
    "重氢-轨道采集器": hh_1,
    "反物质": h_h,
    # "核心素": hgold,
    "临界光子": light,
    "金伯利矿石": diamond_ore,
    "分形硅石": tran_sil_ore,
    "光栅石": lightstone_ore,
    "刺笋结晶": bamboo,
    "单极磁石": mag_ore,
    "可燃冰-矿机": ice_1,
    "可燃冰-轨道采集器": ice_2,
    "铁块": iron,
    "铜块": copper,
    "石材": stone_material,
    "石墨": pencil,
    "硅块": sil,
    "钛块": tit,
    # "硫酸": h2so4,
    "精炼油": oil_gas,
    # "氢棒": h_container,
    # "氚棒": hh_container,
    # "反物质棒": h-h_container,
    # "奇异棒": hgold_container,
    "磁铁": mag_circle,
    "线圈": wire_circle,
    "玻璃": glass,
    "钻石": diamond,
    "晶格硅": tran_sil,
    # "钛合金": tit_metal,
    "塑料": plastic,
    "有机晶体": organic,
    "石墨烯": net,
    # "湮灭球": sunball,
    # "钢材": steel,
    "电路板": electron_board,
    # "棱镜": tran_mirror,
    "马达": motor,
    "微晶原件": electronic,
    "绿管": green_tube,
    "钛晶石": tit_crystal,
    "碳纳米管": net_tube,
    "粒子宽带": cpu_tube,
    "齿轮": gear,
    # "电浆管": white_tube,
    # "光子器": purple_red,
    "绿马达": green_motor,
    "金cpu": gold_cpu,
    "卡西米尔晶体": purple_crystal,
    "钛玻璃": tit_glass,
    "位面过滤器": cpu_glass,
    "蓝cpu": blue_cpu,
    # "引擎1": engine_1,
    # "引擎2": engine_2,
    # "引擎3": engine_3,
    # "磁场环": blue_engine,
    "紫管": purple_tube,
    # "地面机1": army_1,
    # "地面机2": army_2,
    # "地面机3": army_3,
    # "太空机1": air_force_1,
    # "太空机2": air_force_2,
    # "炮弹1": cannonball_1,
    # "炮弹2": cannonball_2,
    # "炮弹3": cannonball_3,
    # "等离子胶囊": green_ball,
    # "反物质胶囊": black_ball,
    # "电磁手雷1": elec_wep_1,
    # "电磁手雷2": elec_wep_2,
    # "mk1": mk_1,
    # "mk2": mk_2,
    # "mk3": mk_3,
    # "导弹1": missile_1,
    # "导弹2": missile_2,
    # "导弹3": missile_3,
    # "燃烧单元1": explosive_1,
    # "燃烧单元2": explosive_2, 
    # "燃烧单元3": explosive_3,
    # "子弹1": bullet_1,
    # "子弹2": bullet_2,
    # "子弹3": bullet_3,
    # "无人机": delivery_1,
    # "行星运输机": delivery_2,
    # "星际运输机": delivery_3,
    # "翘曲器": jumper,
    "引力透镜": green_mirror,
    # "地基": floor, 
    # "太阳帆": fan,
    # "框架材料": structural_material,
    # "框架节点": structural_base,
    # "小火箭": rocket,
    "蓝糖": blue_matrix,
    "红糖": red_matrix,
    "黄糖": yellow_matrix,
    "紫糖": purple_matrix,
    "绿糖": green_matrix,
    "白糖": white_matrix,
    # "黑雾糖": enemy_tube,
    # "黑雾碎片": enemy_0,
    # "黑雾1": enemy_1,
    # "黑雾2": enemy_2,
    # "黑雾3": enemy_3,
}