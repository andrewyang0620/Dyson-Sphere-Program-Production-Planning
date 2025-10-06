# process.py
from items import ITEMS, Item

def reset_all(items: dict):
    for item in items.values():
        item.reset()

def propagate(item: Item, amount: float, items: dict):
    # 累计需求
    item.demand += amount
    if not item.recipe:
        return
    for child_name, qty in item.recipe.items():
        child_item = items[child_name]
        propagate(child_item, amount * qty, items)

def print_tree_local(item: Item, flow: float, indent=0, items: dict = ITEMS):
    # 分支需求
    machines_local = flow / item.actual_rate if item.actual_rate > 0 else 0.0
    if machines_local.is_integer():
        machines_display = int(machines_local)
    else:
        machines_display = round(machines_local, 1)
    print("  " * indent + f"- {item.name}: {flow}/min   {item.machine_type}: {machines_display}")

    if not item.recipe:
        return
    for child_name, qty in item.recipe.items():
        child_item = items[child_name]
        child_flow = flow * qty
        print_tree_local(child_item, child_flow, indent + 1, items)
