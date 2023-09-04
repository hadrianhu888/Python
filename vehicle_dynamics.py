
import time 

class Vehicle: 
    def __init__(self):
        self._drive_by_wire = DriveByWire()
        self._brake_by_wire = BrakeByWire()
        self._gear = 0
        self._vehicle_dynamics = VehicleDynamics()
    
    def __str__(self):
        return f"Vehicle: {self._drive_by_wire.get_status()}"
    
    def on(self):
        self._drive_by_wire.on()
        self._brake_by_wire.on()
        
    def off(self):
        self._drive_by_wire.off()
        self._brake_by_wire.off()
        
    def accessory(self):
        self._drive_by_wire.accessory()
        self._brake_by_wire.accessory()
        
    def crank(self):
        self._drive_by_wire.crank()
        self._brake_by_wire.crank()
    
    def accelerate(self, throttle):
        self._drive_by_wire.accelerate(throttle)
        self._brake_by_wire.accelerate(throttle)
        
    def brake(self, *args):
        self._drive_by_wire.brake(*args)
        self._brake_by_wire.brake(*args)
        
    def update(self):
        self._vehicle_dynamics.update()
        return self._vehicle_dynamics.velocity, self._vehicle_dynamics.distance, self._vehicle_dynamics.time

class VehicleDynamics:
    def __init__(self):
        self._engine_control_module = EngineControlModule()
        self._wheels = Wheels()
        self._gearbox = Gearbox()
        self._throttle_control_module = ThrottleControlModule()
        self._brake_control_module = BrakeControlModule()
        self._brake_by_wire = BrakeByWire()
        self._drive_by_wire = DriveByWire()
        self._power_train = PowerTrain()
        self._brake_system = BrakeSystem()
        self.engine_torque = 0
        self.time = 0
        self.distance = 0
        self.velocity = 0
        self.acceleration = 0
        
    def update(self, throttle, brake, gear, dt):
        self._vehicle_dynamics.update(throttle, brake, gear, dt)
        return self._vehicle_dynamics.velocity, self._vehicle_dynamics.distance, self._vehicle_dynamics.time
    
    def get_status(self):
        return {
            'Engine Status': self._engine_control_module.get_status(),
            'Transmission Gear': self._gearbox.get_gear(),
            'Propulsion Status': self._throttle_control_module.get_status(),
            'Gear Status': self._gear
        }
        
    def get_gear(self):
        return self._gear
    
    def __str__(self):
        return f"Vehicle: {self._drive_by_wire.get_status()}"
    
    def on(self):
        self._drive_by_wire.on()
        self._brake_by_wire.on()
    
    def off(self):
        self._drive_by_wire.off()
        self._brake_by_wire.off()
        
    def accelerate(self, throttle):
        self._engine_control_module.on()
        self._gearbox.set_gear(1)
        self._throttle_control_module.on()
        self._wheels.set_rotation_speed(throttle)
        
    def brake(self):
        self._throttle_control_module.off()
        self._brake_control_module.on(self._wheels)
        
    def set_gear(self, gear):
        self._gear = gear
    
    def get_rotation_speed(self):
        return self._wheels.get_rotation_speed()
    
    def wire_brake(self):
        self._brake_control_module.on(self._wheels)
    
        
class EngineControlModule: 
    def __init__(self):
        self._is_on = False
    
    def on(self):
        self._is_on = True
    
    def off(self):
        self._is_on = False
        
    def get_status(self):
        return self._is_on
    
    def mass_air_flow(self, airflow, speed):
        return airflow * speed
    
    def mass_air_pressure(self, airflow, pressure):
        return airflow * pressure
    
    def fuel_air_ratio(self, fuel, air):
        return fuel / air
    
    def mass_air_temperature(self, temperature):
        return temperature
    
class Wheels: 
    def __init__(self):
        self._rotation_speed = 0
        
    def set_rotation_speed(self, speed):
        self._rotation_speed = speed
        
    def get_rotation_speed(self):
        return self._rotation_speed
    
    def apply_brake_force(self, force):
        self._rotation_speed -= force

class Gearbox:
    def __init__(self):
        self._gear = 0
    
    def set_gear(self, gear):
        self._gear = gear
    
    def get_gear(self):
        return self._gear
    
class ThrottleControlModule:
    def __init__(self):
        self._is_on = False
    
    def on(self):
        self._is_on = True
    
    def off(self):
        self._is_on = False
        
    def get_status(self):
        return self._is_on
    
class BrakeControlModule:
    def __init__(self):
        self._is_on = False
    
    def on(self, wheels):
        self._is_on = True
        wheels.apply_brake_force(100)
    
    def off(self):
        self._is_on = False
        
    def get_status(self):
        return self._is_on
    
class DriveByWire:
    def __init__(self):
        self._engine = Engine()
        self._propulsion = Propulsion()
        self._transmission = Transmission()
        self._gear = 0
        
    def on(self):
        self._engine.on()
        self._transmission.set_gear(1)
        self._propulsion.on()
        
    def off(self):
        self._engine.off()
        self._transmission.set_gear(0)
        self._propulsion.off()
        
    def accelerate(self, throttle):
        self._engine.on()
        self._transmission.set_gear(1)
        self._propulsion.on()
        self._propulsion.set_rotation_speed(throttle)
    
    def brake(self, *args):  # Add *args to accept multiple arguments
        self._propulsion.off()
        if args:
            print(f"Braking with force: {args[0]}")
        else:
            print("Braking")
            
    def set_gear(self, gear):
        self._gear = gear
        
    def get_status(self):
        return {
            'Engine Status': self._engine.get_status(),
            'Transmission Gear': self._transmission.get_gear(),
            'Propulsion Status': self._propulsion.get_status(),
            'Gear Status': self._gear
        }
        
    def get_gear(self):
        return self._gear
    
    def get_rotation_speed(self):
        return self._propulsion.get_rotation_speed()
    
    def wire_brake(self):
        self._propulsion.brake()
        
    def accessory(self):
        self._engine.on()
        self._transmission.set_gear(1)
        self._propulsion.on()
        
    def crank(self):
        self._engine.on()
        self._transmission.set_gear(1)
        self._propulsion.on()
        
class BrakeByWire:
    def __init__(self):
        self._brake_control_module = BrakeControlModule()
        self._engine_control_module = EngineControlModule()
        self._throttle_control_module = ThrottleControlModule()
        self._gearbox = Gearbox()
        self._gear = 0
        self._wheels = Wheels()
        
    def on(self):
        self._engine_control_module.on()
        self._gearbox.set_gear(1)
        self._throttle_control_module.on()
        
    def off(self):
        self._engine_control_module.off()
        self._gearbox.set_gear(0)
        self._throttle_control_module.off()
        
    def accelerate(self, throttle):
        self._engine_control_module.on()
        self._gearbox.set_gear(1)
        self._throttle_control_module.on()
        self._wheels.set_rotation_speed(throttle)
        
    def brake(self, *args):  # Add *args to accept multiple arguments
        self._throttle_control_module.off()
        self._brake_control_module.on(self._wheels)
        if args:
            print(f"Braking with force: {args[0]}")
        else:
            print("Braking")
        
    def set_gear(self, gear):
        self._gear = gear
        
    def get_status(self):
        return {
            'Engine Status': self._engine_control_module.get_status(),
            'Transmission Gear': self._gearbox.get_gear(),
            'Propulsion Status': self._throttle_control_module.get_status(),
            'Gear Status': self._gear
        }
        
    def get_gear(self):
        return self._gear
    
    def get_rotation_speed(self):
        return self._wheels.get_rotation_speed()
    
    def wire_brake(self):
        self._brake_control_module.on(self._wheels)
        
    def accessory(self):
        self._engine_control_module.on()
        self._gearbox.set_gear(1)
        self._throttle_control_module.on()
        
    def crank(self):
        self._engine_control_module.on()
        self._gearbox.set_gear(1)
        self._throttle_control_module.on()
        
class BrakeSystem:
    def __init__(self):
        self._brake_control_module = BrakeControlModule()
        self._engine_control_module = EngineControlModule()
        self._gearbox = Gearbox()
        self._throttle_control_module = ThrottleControlModule()
        self.wheels = Wheels()
        
    def accelerate(self, target_speed):
        self._engine_control_module.on()
        self._gearbox.set_gear(1)
        self._throttle_control_module.on()
        for speed in range(1, target_speed, 10):
            self.wheels.set_rotation_speed(speed)
            time.sleep(0.1)
        self.wheels.set_rotation_speed(target_speed)
        
    def brake(self):
        self._throttle_control_module.off()
        self._brake_control_module.on(self.wheels)
        
    def feedback(self):
        return self._brake_control_module.feedback()
    
    def set_gear(self, gear):
        self._gear = gear
        
class PowerTrain:
    def __init__(self):
        self._engine = Engine()
        self._transmission = Transmission()
        self._propulsion = Propulsion()
        self._gear = 0
        
    def on(self):
        self._engine.on()
        self._transmission.set_gear(1)
        self._propulsion.on()
        
    def off(self):
        self._engine.off()
        self._transmission.set_gear(0)
        self._propulsion.off()
        
    def accelerate(self, throttle):
        self._engine.on()
        self._transmission.set_gear(1)
        self._propulsion.on()
        self._propulsion.set_rotation_speed(throttle)
        
    def brake(self):
        self._propulsion.off()
        
    def set_gear(self, gear):
        self._gear = gear
        
    def get_status(self):
        return {
            'Engine Status': self._engine.get_status(),
            'Transmission Gear': self._transmission.get_gear(),
            'Propulsion Status': self._propulsion.get_status(),
            'Gear Status': self._gear
        }
        
    def get_gear(self):
        return self._gear
    
    def get_rotation_speed(self):
        return self._propulsion.get_rotation_speed()
    
    def wire_brake(self):
        self._propulsion.brake()

class Engine:
    def __init__(self):
        self._is_on = False
        
    def on(self):
        self._is_on = True
        
    def off(self):
        self._is_on = False
        
    def get_status(self):
        return self._is_on
    
class Propulsion:
    def __init__(self):
        self._is_on = False
        self._wheels = Wheels()
        
    def on(self):
        self._is_on = True
        
    def off(self):
        self._is_on = False
        
    def set_rotation_speed(self, speed):
        self._wheels.set_rotation_speed(speed)
        
    def get_rotation_speed(self):
        return self._wheels.get_rotation_speed()
    
    def get_status(self):
        return self._is_on
    
    def brake(self, *args):
        return self._wheels.apply_brake_force(*args)
    
class Transmission:
    def __init__(self):
        self._gear = 0
        
    def set_gear(self, gear):
        self._gear = gear
        
    def get_gear(self):
        return self._gear
    
def main():
    vehicle = Vehicle()
    vehicle.on()
    vehicle.accelerate(100)
    vehicle.brake(100)
    vehicle.off()
    print(vehicle)
    
if __name__ == '__main__':
    main()