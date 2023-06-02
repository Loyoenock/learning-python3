def make_sandwish(*items):
    """List for making sand wish"""
    print("\nMaking sand wish with the follwing items")
    for item in items:
        print(f"- {item}")



make_sandwish('Baking flour')
make_sandwish('Butter', 'salt', 'green pepper')
