
"""Generate a python script to simulate the vehicle power train 
"""
import sys

from vehicle_dynamics import *
from drive_by_wire import *
from brake_by_wire import *

class PowerTrain:
    def __init__(self):
        self._engine = Engine()
        self._propulsion = Propulsion()
        self._transmission = Transmission()
        self._gear = Gear()
        self._brake_control_module = BrakeControlModule()
        self._engine_control_module = EngineControlModule()
        self._throttle_control_module = ThrottleControlModule()
        self._wheels = Wheels()
        self._vehicle_dynamics = VehicleDynamics()
        self._steering = Steering()
        self._brake = BrakeSystem()
        self._state = 0
        
    def on(self):
        self._engine.on()
        self._propulsion.on()
        
    def off(self):
        self._engine.off()
        self._propulsion.off()
        
    def acc(self):
        self._engine.on()
        self._propulsion.on()
        self._throttle_control_module.on()
        
    def crank(self):
        self._engine.on()
        self._propulsion.on()
        self._throttle_control_module.on()
        self._engine_control_module.on()
        
    def accelerate(self, throttle):
        self._engine.on()
        self._propulsion.on()
        self._propulsion.set_rotation_speed(throttle)
        
    def brake(self, *args):
        if len(args) == 1:
            self._propulsion.brake(args[0])
        else:
            self._propulsion.brake()
    
    def set_gear(self, gear):
        self._gear = gear
        
    def get_status(self):
        return {
            'Engine Status': self._engine.get_status(),
            'Transmission Gear': self._transmission.get_gear(),
            'Propulsion Status': self._propulsion.get_status(),
            'Gear Status': self._gear.get_gear()
        }
        
    def get_gear(self):
        return self._transmission.get_gear()
    
    def get_power(self):
        return self._engine.get_power()
    
    def get_speed(self):
        return self._propulsion.get_speed()
    
    def get_torque(self):
        return self._engine.get_torque()
    
    def get_rpm(self):
        return self._engine.get_rpm()
        
    def get_throttle(self):
        return self._throttle_control_module.get_throttle()
    
    def get_brake(self):
        return self._brake.get_brake()
    
    def get_clutch(self):
        return self._transmission.get_clutch()
    
    def get_engine_temp(self):
        return self._engine.get_engine_temp()
    
    def get_oil_temp(self):
        return self._engine.get_oil_temp()
    
    def get_oil_pressure(self):
        return self._engine.get_oil_pressure()
    
    def get_fuel_pressure(self):
        return self._engine.get_fuel_pressure()
    
    def get_fuel_level(self):
        return self._engine.get_fuel_level()
    
    def get_rotation_speed(self):
        return self._propulsion.get_rotation_speed()
    
    def drive_brake(self):
        self._propulsion.brake()
        
    def wire_brake(self):
        self._brake_control_module.on(self._wheels)
        
    def update(self, throttle, brake, gear, dt):
        self._vehicle_dynamics.update(throttle, brake, gear, dt)
        return self._vehicle_dynamics.velocity, self._vehicle_dynamics.distance, self._vehicle_dynamics.time
    
    def set_angle(self, angle):
        self._steering.set_angle(angle)
        
    def get_angle(self):
        return self._steering.get_angle()
    
    def set_rotation_speed(self, speed):
        self._propulsion.set_rotation_speed(speed)
        
    def system_power_mode_state_flow(self,state):
        # use match case in Python 3.10
        # https://docs.python.org/3.10/whatsnew/3.10.html#pep-634-structural-pattern-matching
        match state:
            case 0:
                self.off()
                self.state = 0                
            case 1:
                self.acc()
                self.state = 1
            case 2:
                self.on()
                self.state = 2
            case 3:
                self.crank()
                self.state = 3
            case _: 
                self.off()
                self.state = 0
        return self.state
    
def main():
    print(sys.version)
    """test out the power train program"""
    new_power_train = PowerTrain()
    new_power_train.system_power_mode_state_flow(0)
    print(new_power_train.get_status())
    new_power_train.system_power_mode_state_flow(1)
    print(new_power_train.get_status())
    new_power_train.system_power_mode_state_flow(2)
    print(new_power_train.get_status())
    new_power_train.system_power_mode_state_flow(3)
    print(new_power_train.get_status())
    print('Testing texts')

if __name__ == '__main__':
	main()

