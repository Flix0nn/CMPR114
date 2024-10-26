class Insect:
    def __init__(self, name, legs):
        self._name = name
        self._legs = legs

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_legs(self):
        return self._legs

    def set_legs(self, legs):
        self._legs = legs


class Bumblebee(Insect):
    def __init__(self, name, legs, can_sting, honey_production):
        super().__init__(name, legs)
        self._can_sting = can_sting
        self._honey_production = honey_production

    def get_can_sting(self):
        return self._can_sting

    def set_can_sting(self, can_sting):
        self._can_sting = can_sting

    def get_honey_production(self):
        return self._honey_production

    def set_honey_production(self, honey_production):
        self._honey_production = honey_production

    def display_characteristics(self):
        print(f"{self.get_name()} has {self.get_legs()} legs.")
        print(f"Can sting: {self.get_can_sting()}")
        print(f"Honey production: {self.get_honey_production()} kg/year")


class Grasshopper(Insect):
    def __init__(self, name, legs, can_jump, chirp_sound):
        super().__init__(name, legs)
        self._can_jump = can_jump
        self._chirp_sound = chirp_sound

    def get_can_jump(self):
        return self._can_jump

    def set_can_jump(self, can_jump):
        self._can_jump = can_jump

    def get_chirp_sound(self):
        return self._chirp_sound

    def set_chirp_sound(self, chirp_sound):
        self._chirp_sound = chirp_sound

    def display_characteristics(self):
        print(f"{self.get_name()} has {self.get_legs()} legs.")
        print(f"Can jump: {self.get_can_jump()}")
        print(f"Chirp sound: {self.get_chirp_sound()}")

bumblebee = Bumblebee("Bumblebee", 6, True, 10)
grasshopper = Grasshopper("Grasshopper", 6, True, "Loud")

print("Bumblebee characteristics:")
bumblebee.display_characteristics()

print("\nGrasshopper characteristics:")
grasshopper.display_characteristics()
