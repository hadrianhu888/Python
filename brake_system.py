import time

class BrakeSystem:
    def __init__(self):
        self._brake_control_module = BrakeControlModule()
        self._engine_control_module = EngineControlModule()
        self._gearbox = Gearbox()  # Added this line
        self._throttle_control_module = ThrottleControlModule()  # Added this line
        self.wheels = Wheels()

    def accelerate(self, target_speed):
        self._engine_control_module.on()  # Fixed this line
        self._gearbox.set_gear(1)  # Fixed this line
        self._throttle_control_module.on()  # Fixed this line
        for speed in range(1, target_speed, 10):
            self.wheels.set_rotation_speed(speed)
            time.sleep(0.1)
        self.wheels.set_rotation_speed(target_speed)

    def brake(self):
        self._throttle_control_module.off()  # Optionally add this line to turn off throttle when braking
        self._brake_control_module.on(self.wheels)

    def feedback(self):
        return self._brake_control_module.feedback()

    def set_gear(self, gear):
        self._gear = gear

class BrakeControlModule:
    def __init__(self):
        self._is_on = False

    def on(self, wheels):
        self._is_on = True
        initial_speed = wheels.get_rotation_speed()
        for brake_force in range(initial_speed, 0, -10):
            wheels.apply_brake_force(brake_force)
            time.sleep(0.1)
        self._is_on = False

    def feedback(self):
        return "Brake applied successfully" if not self._is_on else "Brake is being applied"

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

    def set_rotation_speed(self, rotation_speed):
        self._rotation_speed = rotation_speed

    def get_rotation_speed(self):
        return self._rotation_speed

    def apply_brake_force(self, brake_force):
        self._rotation_speed = max(0, self._rotation_speed - brake_force)
        
class Gearbox:
    def __init__(self):
        self._gear = 0

    def set_gear(self, gear):
        self._gear = gear
        
class ThrottleControlModule:
    def __init__(self):
        self._is_on = False

    def on(self):
        self._is_on = True

    def off(self):
        self._is_on = False

def main():
    brake_system = BrakeSystem()
    brake_system.accelerate(100)
    print(f"Current wheel speed: {brake_system.wheels.get_rotation_speed()}")
    brake_system.brake()
    print(f"Current wheel speed: {brake_system.wheels.get_rotation_speed()}")
    print(brake_system.feedback())
    brake_system.accelerate(90)
    print(f"Current wheel speed: {brake_system.wheels.get_rotation_speed()}")
    brake_system.brake()
    print(f"Current wheel speed: {brake_system.wheels.get_rotation_speed()}")
    print(brake_system.feedback())

if __name__ == "__main__":
    main()

