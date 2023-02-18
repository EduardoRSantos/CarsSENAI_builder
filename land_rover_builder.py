from body import Body
from car import Car
from builder import Builder
from engine import Engine
from wheel import Wheel


class LandRoberBuilder(Builder):
    def __init__(self):
        self.wheel = Wheel()
        self.engine = Engine()
        self.body = Body()
        
        self.wheel.size = 22
        self.engine.horsepower = 249
        self.body.shape = "SUV"

    def get_wheel(self) -> Wheel:
        return self.wheel

    def get_engine(self) -> Engine: 
        return self.engine

    def get_body(self) -> Body: 
        return self.body