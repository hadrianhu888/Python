import drive_by_wire as dbw 
import brake_system as bs
class VehicleDynamics:
    mass = 1000
    gravity = 9.81
    drag_coefficient = 0.4257
    frontal_area = 1.863
    rolling_resistance = 0.015
    wheel_radius = 0.318
    gear_ratio = 0.35
    final_drive_ratio = 3.42
    engine_speed = 0
    engine_torque = 0
    engine_power = 0
    wheel_speed = 0
    wheel_torque = 0
    wheel_power = 0
    acceleration = 0
    velocity = 0
    distance = 0
    time = 0
    def __init__(self):
        self.engine_speed = 0
        self.engine_torque = 0
        self.engine_power = 0
        self.wheel_speed = 0
        self.wheel_torque = 0
        self.wheel_power = 0
        self.acceleration = 0
        self.velocity = 0
        self.distance = 0
        self.time = 0
    def update(self, throttle, brake, gear, dt):
        """_summary_

        Args:
            throttle (_type_): _description_
            brake (_type_): _description_
            gear (_type_): _description_
            dt (_type_): _description_

        Returns:
            _type_: _description_
        """
        # TODO: make sure wheel speed is never zero! 
        try: 
            self.wheel_speed = self.velocity / self.wheel_radius
            self.engine_speed = self.wheel_speed * gear * self.final_drive_ratio * self.gear_ratio
            self.engine_torque = self.engine_speed * self.wheel_torque / self.wheel_speed
            self.engine_power = self.engine_torque * self.engine_speed / 9.5488

            if throttle > 0:
                self.wheel_torque = throttle * self.engine_torque
            elif brake > 0:
                self.wheel_torque = -brake * self.engine_torque
            else:
                self.wheel_torque = 0

            self.wheel_power = self.wheel_torque * self.wheel_speed / 9.5488
            self.acceleration = (self.wheel_torque * self.gear_ratio * self.final_drive_ratio - self.drag_coefficient * self.frontal_area * self.velocity ** 2 - self.rolling_resistance * self.mass * self.gravity) / self.mass
            self.velocity += self.acceleration * dt
            self.distance += self.velocity * dt
            self.time += dt
        except ZeroDivisionError:
            self.wheel_speed = 0
            self.engine_speed = 0
            self.engine_torque = 0
            self.engine_power = 0
            self.wheel_torque = 0
            self.wheel_power = 0
            self.acceleration = 0
            self.velocity = 0
            self.distance = 0
            self.time = 0
            print("Error: wheel speed is zero!")
            

        

        return self.velocity, self.distance, self.time

class DriveByWire:
    def __init__(self):
        self._engine = dbw.Engine()
        self._propulsion = dbw.Propulsion()
        self._steering = dbw.Steering()
        self._transmission = dbw.Transmission()
        self._gear = dbw.Gear()
        self._vehicle_dynamics = VehicleDynamics()
    def on(self):
        self._engine.on()
        self._propulsion.on()
    def off(self):
        self._engine.off()
        self._propulsion.off()
    def accelerate(self, throttle):
        self._engine.on()
        self._propulsion.on()
        self._propulsion.set_rotation_speed(throttle)
    def brake(self, brake):
        self._propulsion.brake(brake)
    def set_gear(self, gear):
        self._transmission.set_gear(gear)
    def set_angle(self, angle):
        self._steering.set_angle(angle)
    def get_status(self):
        return {
            'Engine Status': self._engine.get_status(),
            'Steering Angle': self._steering.get_angle(),
            'Transmission Gear': self._transmission.get_gear(),
            'Propulsion Status': self._propulsion.get_status(),
            'Gear Status': self._gear.get_gear()
        }
    def set_status(self):
        return {
            'Engine Status': self._engine.get_status(),
            'Steering Angle': self._steering.get_angle(),
            'Transmission Gear': self._transmission.get_gear(),
            'Propulsion Status': self._propulsion.get_status(),
            'Gear Status': self._gear.get_gear()
        }
    def get_gear(self):
        return self._transmission.get_gear()
    def get_rotation_speed(self):
        return self._propulsion.get_rotation_speed()
    def drive_brake(self):
        self._propulsion.brake()
    def update(self, throttle, brake, gear, dt):
        self._vehicle_dynamics.update(throttle, brake, gear, dt)
        return self._vehicle_dynamics.velocity, self._vehicle_dynamics.distance, self._vehicle_dynamics.time
class BrakeByWire: 
    def __init__(self):
        self._brake_control_module = bs.BrakeControlModule()
        self._engine_control_module = bs.EngineControlModule()
        self._throttle_control_module = bs.ThrottleControlModule()
        self._gearbox = bs.Gearbox()
        self._gear = 0
        self._wheels = bs.Wheels()
        self._vehicle_dynamics = VehicleDynamics()
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
    def brake(self):
        self._throttle_control_module.off()
        self._brake_control_module.on(self._wheels)
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
    def update(self, throttle, brake, gear, dt):
        self._vehicle_dynamics.update(throttle, brake, gear, dt)
        return self._vehicle_dynamics.velocity, self._vehicle_dynamics.distance, self._vehicle_dynamics.time
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
    def accelerate(self, throttle):
        self._drive_by_wire.accelerate(throttle)
        self._brake_by_wire.accelerate(throttle)
    def brake(self, brake):
        self._drive_by_wire.brake(brake)
        self._brake_by_wire.brake(brake)
    def set_gear(self, gear):
        self._drive_by_wire.set_gear(gear)
        self._brake_by_wire.set_gear(gear)
    def set_angle(self, angle):
        self._drive_by_wire.set_angle(angle)
    def get_status(self):
        return {
            'Drive By Wire': self._drive_by_wire.get_status(),
            'Brake By Wire': self._brake_by_wire.get_status()
        }
    def get_gear(self):
        return self._drive_by_wire.get_gear()
    def get_rotation_speed(self):
        return self._drive_by_wire.get_rotation_speed()
    def vehicle_brake(self):
        self._drive_by_wire.brake()
        self._brake_by_wire.brake()
    def update(self, throttle, brake, gear, dt):
        self._vehicle_dynamics.update(throttle, brake, gear, dt)
        return self._vehicle_dynamics.velocity, self._vehicle_dynamics.distance, self._vehicle_dynamics.time

def main():
    car = Vehicle()
    car.on()

    velocity, distance, time_elapsed = car.update(100, 0, 1, 0.1)
    print(f"Velocity: {velocity}, Distance: {distance}, Time: {time_elapsed}")

    car.set_gear(1)
    car.set_angle(10)

    status = car.get_status()
    print(f"Car Status: {status}")

    gear = car.get_gear()
    print(f"Current Gear: {gear}")

    rotation_speed = car.get_rotation_speed()
    print(f"Rotation Speed: {rotation_speed}")

    car.vehicle_brake()

    velocity, distance, time_elapsed = car.update(0, 100, 1, 0.1)
    print(f"After Brake - Velocity: {velocity}, Distance: {distance}, Time: {time_elapsed}")

    car.off()

    print(car)  # This will call the __str__ method of the Vehicle class

if __name__ == '__main__':
    main()
