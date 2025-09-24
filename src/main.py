# main.py
from items import ITEMS
from process import reset_all, propagate, print_tree

if __name__ == "__main__":
    reset_all(ITEMS)

    target_item = ITEMS["线圈"]
    propagate(target_item, 60, ITEMS)   # want 60 iron blocks per minute

    print("=== Production Demand Tree ===")
    print_tree(target_item)

    print("\n=== Final Demands ===")
    for name, item in ITEMS.items():
        print(item)
