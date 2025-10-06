# main.py
from items import ITEMS
from process import reset_all, propagate, print_tree_local

if __name__ == "__main__":
    reset_all(ITEMS)

    target_item = ITEMS["白糖"]
    propagate(target_item, 360, ITEMS)   # THIS IS THE TARGET DEMAND

    print("=== Production Demand Tree ===")
    print_tree_local(target_item, 360, items=ITEMS)

print("\n=== Final Demands ===")
for name, item in ITEMS.items():
    if item.demand > 0:
        print(f"{name}: {item.demand:.1f}/min, Machines: {item.machine_num():.1f}")