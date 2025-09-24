from items import ITEMS, Item

def reset_all(items: dict):
    """Reset demand before calculation"""
    for item in items.values():
        item.reset()

def propagate(item: Item, amount: float, items: dict):
    """递归更新需求"""
    item.demand += amount
    if not item.recipe:   # 无配方（原矿）
        return
    for child_name, qty in item.recipe.items():
        child_item = items[child_name]
        propagate(child_item, amount * qty, items)

def print_tree(item: Item, indent=0, items: dict = ITEMS):
    """打印需求树"""
    print("  " * indent + f"- {item.name}: {item.demand}/min   {item.machine_type}: {item.machine_num():.1f}")
    if not item.recipe:
        return
    for child_name, qty in item.recipe.items():
        child_item = items[child_name]
        print_tree(child_item, indent + 1, items)
