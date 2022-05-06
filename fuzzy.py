import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('diabetes.csv')

# Nowy plik, bo KNN mocno mieli, więc wolę testować osobno puszczając cały plik
# Instalacja bibliotek: w konsoli w ścieżce projektu wpisujecie 'pipenv install'
# piszcie jakby nie działało


# Klasa FuzzyClassifier zawierająca klasyfikator zbiorów rozmytych oraz metody pomocnicze
class FuzzyClassifier:
    """
    Normy:
    Pregnancies:
    -
    Glucose:
    - 70-99 prawidlowe
    - 100-125 ryzyko
    - 126+ cukrzyca
    BloodPressure:
    - <80 prawidlowe
    - 80-89 podwyzszone faza 1
    - >90 podwyszone faza 2
    SkinThickness:
    -
    Insulin:
    - <30
    Age:
    -
    """
    @staticmethod
    def whatever():
        print('Działa')
