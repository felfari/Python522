class WeightConverter:
    @staticmethod
    def kg_to_lb(kg):
        if not isinstance(kg, (int, float)):
            raise TypeError("Должно быть число")
        if kg < 0:
            raise ValueError("Вес не может быть отрицательным")
        return kg * 2.205

w1=12
w2=41

print(w1,f" кг = {WeightConverter.kg_to_lb(w1):.2f} фунтов")
print(w2,f" кг = {WeightConverter.kg_to_lb(w2):.3f} фунтов")