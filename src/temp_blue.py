# this is a temporary file for designing purposes, not part of the main program
eff0 = 0.75
eff1 = 1.0
eff2 = 1.5
eff3 = 3.0
n = 120


def creation_rate(product_name, machine_name, product_per_min, machine_per_min, efficiency):
    machine_actual = machine_per_min * efficiency
    machine_needed = product_per_min / machine_actual
    print(f"{product_name}/min: {product_per_min} {machine_name}需求: {machine_needed:.2f}")
    return machine_needed

#blue
creation_rate("蓝糖", "研究站", n, 20, eff3)

#red
creation_rate("红糖", "研究站", n, 10, eff3)

# yellow
creation_rate("黄糖", "研究站", n, 7.5, eff3)
print("\n")

# purple
creation_rate("紫糖", "研究站", n, 6, eff3)
creation_rate("黄色芯片", "黑雾制造台", n*2, 20, eff3)
creation_rate("粒子宽带", "黑雾制造台", n, 7.5, eff3)
creation_rate("塑料", "高级化工厂", n, 20, 2)