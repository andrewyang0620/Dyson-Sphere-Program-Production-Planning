# recipe.py
from machine import MACHINES
RECIPE = {
    "反物质": {
        0: {
            "inputs": {"临界光子": 1},
            "base_rate": 60,
            "machine_type": "对撞机"
            }
    },
    "铁块": {
        0: {
            "inputs": {"铁矿": 1},
            "base_rate": 60,
            "machine_type": "黑雾熔炉"
            }
    },
    "铜块": {
        0: {
            "inputs": {"铜矿": 1},
            "base_rate": 60,
            "machine_type": "黑雾熔炉"
        },
    },
    "石材":{
        0: {
            "inputs": {"石矿": 1},
            "base_rate": 60,
            "machine_type": "黑雾熔炉"
        }
    },
    "石墨": {
        0: {
            "inputs": {"煤矿": 2},
            "base_rate": 30,
            "machine_type": "黑雾熔炉"
        }
    },
    "硅块": {
        0: {
            "inputs": {"硅矿": 2},
            "base_rate": 30,
            "machine_type": "黑雾熔炉"
        }
    },
    "钛块": {
        0: {
            "inputs": {"钛矿": 2},
            "base_rate": 30,
            "machine_type": "黑雾熔炉"
        }
    },
    "精炼油": {
        0: {
            "inputs": {"原油": 1},
            "base_rate": 30,
            "machine_type": "精炼厂"
        }
    },
    "磁铁": {
        0: {
            "inputs": {"铁矿": 1},
            "base_rate": 40,
            "machine_type": "黑雾熔炉"
        }
    },
    "线圈": {
        0: {
            "inputs": {"铜块": 1, "磁铁": 2},
            "base_rate": 120,
            "machine_type": "黑雾制造台"
        }
    },
    "玻璃": {
        0: {
            "inputs": {"石材": 2},
            "base_rate": 30,
            "machine_type": "黑雾熔炉"
        }
    },
    "钻石": {
        0: {
            "inputs": {"金伯利矿石": 0.5},
            "base_rate": 80,
            "machine_type": "黑雾熔炉"
        }
    },
    "晶格硅": {
        0: {
            "inputs": {"硅块": 1},
            "base_rate": 30,
            "machine_type": "黑雾熔炉"
        }
    },
    "塑料": {
        0: {
            "inputs": {"精炼油": 2, "石墨": 1},
            "base_rate": 20,
            "machine_type": "高级化工厂"
        }
    },
    "石墨烯": {
        0: {
            "inputs": {"可燃冰-矿机": 1},
            "base_rate": 60,
            "machine_type": "高级化工厂"
        }
    },
    "电路板": {
        0: {
            "inputs": {"铜块": 0.5, "铁块": 1},
            "base_rate": 120,
            "machine_type": "黑雾制造台"
        }
    },
    "马达": {
        0: {
            "inputs": {"铁块": 2, "齿轮": 1, "线圈": 1},
            "base_rate": 30,
            "machine_type": "黑雾制造台"
        }
    },
    "微晶原件": {
        0: {
            "inputs": {"铜块": 1, "硅块": 2},
            "base_rate": 30,
            "machine_type": "黑雾制造台"
        }
    },
    "绿管": {
        0: {
            "inputs": {"紫管": 2, "铁块": 2, "重氢-轨道采集器": 10},
            "base_rate": 7.5,
            "machine_type": "对撞机"
        }
    },
    "钛晶石": {
        0: {
            "inputs": {"钛块": 3, "有机晶体": 1},
            "base_rate": 15,
            "machine_type": "黑雾制造台"
        }
    },
    "碳纳米管": {
        0: {
            "inputs": {"钛块": 0.5, "石墨烯": 1.5},
            "base_rate": 30,
            "machine_type": "高级化工厂"
        }
    },
    "粒子宽带": {
        0: {
            "inputs": {"碳纳米管": 2, "晶格硅": 2, "塑料": 1},
            "base_rate": 7.5,
            "machine_type": "黑雾制造台"
        }
    },
    "齿轮": {
        0: {
            "inputs": {"铁块": 1},
            "base_rate": 60,
            "machine_type": "黑雾制造台"
        }
    },
    "绿马达": {
        0: {
            "inputs": {"马达": 2, "线圈": 2},
            "base_rate": 30,
            "machine_type": "黑雾制造台"
        }
    },
    "金cpu": {
        0: {
            "inputs": {"电路板": 2, "微晶原件": 2},
            "base_rate": 20,
            "machine_type": "黑雾制造台"
        }
    },
    "卡西米尔晶体": {
        0: {
            "inputs": {"钛晶石": 1, "石墨烯": 2, "氢-轨道采集器-气巨": 12},
            "base_rate": 15,
            "machine_type": "黑雾制造台"
        },
        1: {
            "inputs": {"光栅石": 8, "石墨烯": 2, "氢-轨道采集器-气巨": 12},
            "base_rate": 15,
            "machine_type": "黑雾制造台"
        }
    },
    "钛玻璃": {
        0: {
            "inputs": {"玻璃": 1, "钛块": 1, "水": 1},
            "base_rate": 24,
            "machine_type": "黑雾制造台"
        }
    },
    "位面过滤器": {
        0: {
            "inputs": {"卡西米尔晶体": 1, "钛玻璃": 2},
            "base_rate": 5,
            "machine_type": "黑雾制造台"
        }
    },
    "蓝cpu": {
        0: {
            "inputs": {"金cpu": 2, "位面过滤器": 2},
            "base_rate": 10,
            "machine_type": "黑雾制造台"
        }
    },
    "紫管": {
        0: {
            "inputs": {"绿马达": 2, "铜块": 2, "石墨烯": 2},
            "base_rate": 15,
            "machine_type": "黑雾制造台"
        }
    },
    "引力透镜": {
        0: {
            "inputs": {"钻石": 4, "绿管": 1},
            "base_rate": 10,
            "machine_type": "黑雾制造台"
        }
    },
    "蓝糖": {
        0: {
            "inputs": {"线圈": 1, "电路板": 1},
            "base_rate": 20,
            "machine_type": "黑雾研究站"
        }
    },
    "红糖": {
        0:{
            "inputs": {"氢-轨道采集器-气巨": 2, "石墨": 2},
            "base_rate": 10,
            "machine_type": "黑雾研究站"
        }
    },
    "黄糖": {
        0: {
            "inputs": {"钻石": 1, "钛晶石": 1},
            "base_rate": 7.5,
            "machine_type": "黑雾研究站"
        }
    },
    "紫糖": {
        0: {
            "inputs": {"粒子宽带": 1, "金cpu": 2},
            "base_rate": 6,
            "machine_type": "黑雾研究站"
        }
    },
    "绿糖": {
        0: {
            "inputs": {"引力透镜": 0.5, "蓝cpu": 0.5},
            "base_rate": 5,
            "machine_type": "黑雾研究站"
        }
    },
    "白糖": {
        0: {
            "inputs": {"蓝糖": 1, "红糖": 1, "黄糖": 1, "紫糖": 1, "绿糖": 1, "反物质": 1},
            "base_rate": 4,
            "machine_type": "黑雾研究站"
        }
    }
}
SELECTED_RECIPE = {
    "反物质": 0,
    "铁块": 0,
    "铜块": 0,
    "石材": 0,
    "石墨": 0,
    "硅块": 0,
    "钛块": 0,
    "精炼油": 0,
    "磁铁": 0,
    "线圈": 0,
    "玻璃": 0,
    "钻石": 0,
    "晶格硅": 0,
    "塑料": 0,
    "石墨烯": 0,
    "电路板": 0,
    "马达": 0,
    "微晶原件": 0,
    "绿管": 0,
    "钛晶石": 0,
    "碳纳米管": 0,
    "粒子宽带": 0,
    "齿轮": 0,
    "绿马达": 0,
    "金cpu": 0,
    "卡西米尔晶体": 0,
    "钛玻璃": 0,
    "位面过滤器": 0,
    "蓝cpu": 0,
    "紫管": 0,
    "引力透镜": 0,
    "蓝糖": 0,
    "红糖": 0,
    "黄糖": 0,
    "紫糖": 0,
    "绿糖": 0,
    "白糖": 0,
}