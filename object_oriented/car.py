class Car:
    def __init__(self, model, year, color, for_sale):     # method가 필요하다
        self.model = model                                # car이 가지고 있을 만한 attributes
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")