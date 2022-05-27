class Fuzzy:
    def __init__(self):
        self.antecedent = []
        self.consequent = []
        self.rules = []

    @staticmethod
    def triangular_function(x, a, b, c):
        if x <= a:
            return 0
        if a < x <= b:
            return (x - a) / (b - a)
        if b < x <= c:
            return (c - x) / (c - b)
        if x > c:
            return 0

    def add_antecedent(self, parameter, linguisticValue, a, b, c):
        self.antecedent.append([parameter, linguisticValue, a, b, c])

    def add_rule(self, rule):
        self.rules.append(rule)

    def add_consequent(self, linguisticValue, parameters):
        self.consequent.append([linguisticValue, parameters])

    def compute(self, x):
        # rozmycie
        fuzzy_values = []
        for i in self.antecedent:
            fuzzy_values.append([i[0], i[1], self.triangular_function(x[i[0]], i[2], i[3], i[4])])

        # wnioskowanie
        rules_result = []
        for i in self.rules:
            tmp = 1
            for j in fuzzy_values:
                if i[j[0]] == j[1]:
                    tmp *= j[2]
            rules_result.append(tmp)
        print('rules_result:', rules_result)
        # wyostrzenie
        res = max(rules_result)
        decision = self.rules[rules_result.index(res)]['jakosc zycia']
        print("W miescie", sample['miasto'], "jakosc zycia jest", decision)
        print()


system = Fuzzy()
system.add_antecedent('naslonecznienie', 'zle', 0, 0, 0.4)
system.add_antecedent('naslonecznienie', 'srednie', 0.3, 0.4, 0.8)
system.add_antecedent('naslonecznienie', 'dobre', 0.7, 1, 1)

system.add_antecedent('skazenie', 'wysokie', 0, 0, 0.4)
system.add_antecedent('skazenie', 'srednie', 0.3, 0.4, 0.8)
system.add_antecedent('skazenie', 'niskie', 0.7, 1, 1)

system.add_consequent('jakosc zycia', [['zla', 0, 0, 0.4], ['srednia', 0.3, 0.6, 0.8], ['dobra', 0.7, 1, 1]])

# regul powinno byc 9
system.add_rule({'naslonecznienie': 'zle', 'skazenie': 'wysokie', 'jakosc zycia': 'zla'})
system.add_rule({'naslonecznienie': 'srednie', 'skazenie': 'wysokie', 'jakosc zycia': 'zla'})
system.add_rule({'naslonecznienie': 'zle', 'skazenie': 'srednie', 'jakosc zycia': 'zla'})
system.add_rule({'naslonecznienie': 'zle', 'skazenie': 'niskie', 'jakosc zycia': 'srednia'})
system.add_rule({'naslonecznienie': 'dobre', 'skazenie': 'wysokie', 'jakosc zycia': 'srednia'})
system.add_rule({'naslonecznienie': 'srednie', 'skazenie': 'srednie', 'jakosc zycia': 'srednia'})
system.add_rule({'naslonecznienie': 'srednie', 'skazenie': 'niskie', 'jakosc zycia': 'dobra'})
system.add_rule({'naslonecznienie': 'dobre', 'skazenie': 'srednie', 'jakosc zycia': 'dobra'})
system.add_rule({'naslonecznienie': 'dobre', 'skazenie': 'niskie', 'jakosc zycia': 'dobra'})

miasta = [{'naslonecznienie': 0.6, 'skazenie': 0.3, 'miasto': 'Warszawa'},
          {'naslonecznienie': 1.0, 'skazenie': 0.1, 'miasto': 'Krakow'}]

for sample in miasta:
    print(sample)
    system.compute(sample)
