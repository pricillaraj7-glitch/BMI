class BMI:
    def __init__(self, weight=0.0, height=0.0):
        self.weight = weight
        self.height = height

    @property
    def Weight(self):
        return self.weight

    @Weight.setter
    def Weight(self, value):
        self.weight = value

    @property
    def Height(self):
        return self.height

    @Height.setter
    def Height(self, value):
        self.height = value

    def BMI_Value(self):
        return self.weight / (self.height ** 2)   # let ZeroDivisionError occur if height=0

    def __eq__(self, other):
        if not isinstance(other, BMI):
            return False
        return self.Weight == other.Weight and self.Height == other.Height