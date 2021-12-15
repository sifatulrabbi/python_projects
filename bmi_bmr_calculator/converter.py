class Converter:
    def __init__(self) -> None:
        pass

    def inch_to_meter(self, val: float) -> float:
        cm = val * 2.54
        return self.cm_to_meter(cm)

    def cm_to_meter(self, val: float) -> float:
        return val / 100

    def lb_to_kg(self, val: float) -> float:
        return val / 2.21

    def inch_to_cm(self, val: float) -> float:
        return val * 2.54
