price_kg_vegetables = float(input())
price_kg_fruits = float(input())
total_kg_vegetables = int(input())
total_kg_fruits = int(input())
total_leva = price_kg_vegetables * total_kg_vegetables + price_kg_fruits * total_kg_fruits
total_eur = total_leva / 1.94
print(f"{total_eur:.2f}")