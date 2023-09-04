
import time 
class DriveByWire:
    MAX_SPEED = 1000  # Assuming maximum limit is 400
    
    def __init__(self):
        self._steering = Steering()
        self._engine = Engine()
        self._propulsion = Propulsion()
        self._transmission = Transmission()
        self._gear = Gear()
    
    def accelerate(self, target_speed):
        self._engine.on()
        self._transmission.set_gear(1)
        self._propulsion.on()
        current_speed = self.get_rotation_speed()
        new_speed = min(current_speed + target_speed, self.MAX_SPEED)
        for speed in range(current_speed + 1, new_speed, 10):
            self._propulsion.set_rotation_speed(speed)
            time.sleep(0.1)
        self._propulsion.set_rotation_speed(new_speed)
    
    def steer(self, angle):
        if -45 <= angle <= 45:
            self._steering.set_angle(angle)
            gear_to_set = max(int(abs(angle) / 9), 1)  # Making the gear setting dynamic
            self._transmission.set_gear(gear_to_set)
        else:
            print("Invalid angle. Must be between -45 and 45.")

    def on(self):
        self._engine.on()
        self._propulsion.on()
        
    def off(self):
        self._engine.off()
        self._propulsion.off()
    
    def feedback(self):
        return {
            'Engine Status': self._engine.get_status(),
            'Steering Angle': self._steering.get_angle(),
            'Transmission Gear': self._transmission.get_gear(),
            'Propulsion Status': self._propulsion.get_status(),
            'Gear Status': self._gear.get_gear()
        }
    
    def get_status(self):
        return self._engine.get_status() and self._propulsion.get_status()
    
    def get_gear(self):
        return self._transmission.get_gear()
    
    def get_rotation_speed(self):
        return self._propulsion.get_rotation_speed()
    
    def brake(self):
        self._propulsion.brake()
class Steering:
    def __init__(self):
        self._angle = 0
    
    def set_angle(self, angle):
        self._angle = angle
    
    def get_angle(self):
        return self._angle

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
        if len(args) == 0:
            # Code for default braking behavior
            print("Default braking.")
        elif len(args) == 1:
            # Code for braking with a specified force
            print(f"Applying brake with force {args[0]}.")
        else:
            print("Invalid number of arguments.")
        return self._wheels.brake()
    
        
    def feedback(self):
        return "Brake applied successfully" if self._wheels.get_rotation_speed() == 0 else "Brake is being applied"

class Wheels:
    def __init__(self):
        self._rotation_speed = 0
    
    def set_rotation_speed(self, speed):
        self._rotation_speed = speed
    
    def get_rotation_speed(self):
        return self._rotation_speed
    
    def brake(self):
        self._rotation_speed = 0
    
    def feedback(self):
        return "Brake applied successfully" if self._rotation_speed == 0 else "Brake is being applied"

class Transmission:
    def __init__(self):
        self._gear = 0
    
    def set_gear(self, gear):
        self._gear = gear
    
    def get_gear(self):
        return self._gear

class Gear:
    def __init__(self):
        self._gear = 0
    
    def set_gear(self, gear):
        self._gear = gear
    
    def get_gear(self):
        return self._gear

def main():
    drive_by_wire = DriveByWire()
    drive_by_wire.steer(10)
    drive_by_wire.accelerate(100)
    drive_by_wire.brake()
    print(drive_by_wire.feedback())

if __name__ == "__main__":
    main()
