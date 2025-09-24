# process.py
from items import ITEMS, Item

def reset_all(items: dict):
    """Reset demand before calculation"""
    for item in items.values():
        item.reset()


def propagate(item: Item, amount: float, items: dict):
    """Recursive propagation of demand"""
    item.demand += amount
    if not item.recipe:  # no children
        return
    for child_name, qty in item.recipe.items():
        child_item = items[child_name]
        propagate(child_item, amount * qty, items)


def print_tree(item: Item, indent=0, items: dict = ITEMS):
    """Pretty-print demand tree"""
    print("  " * indent + f"- {item.name}: {item.demand}/min")
    for child_name, qty in item.recipe.items():
        child_item = items[child_name]
        print_tree(child_item, indent + 1, items)
