# process.py
from items import ITEMS, Item

def reset_all(items: dict):
    for item in items.values():
        item.reset()

def propagate(item: Item, amount: float, items: dict):
    """全局累计，总机器数/资源用它"""
    item.demand += amount
    if not item.recipe:
        return
    for child_name, qty in item.recipe.items():
        child_item = items[child_name]
        propagate(child_item, amount * qty, items)

def print_tree_local(item: Item, flow: float, indent=0, items: dict = ITEMS):
    """逐层展示局部需求：这里不用 item.demand，而用 flow"""
    # 用 flow 来算本节点需要的机器数（该分支角度）
    machines_local = flow / item.actual_rate if item.actual_rate > 0 else 0.0
    print("  " * indent + f"- {item.name}: {flow}/min   {item.machine_type}: {machines_local:.1f}")

    if not item.recipe:
        return
    for child_name, qty in item.recipe.items():
        child_item = items[child_name]
        child_flow = flow * qty
        print_tree_local(child_item, child_flow, indent + 1, items)
