import pytest
from brake_system import BrakeSystem, BrakeControlModule, EngineControlModule, Wheels

# Test for brake function
def test_brake():
    brake_system = BrakeSystem()
    brake_system.brake()
    assert brake_system.feedback() == "Brake applied successfully"

# Test for feedback function
def test_feedback():
    brake_control_module = BrakeControlModule()
    assert brake_control_module.feedback() == "Brake applied successfully"

# Test for on function
def test_on():
    engine_control_module = EngineControlModule()
    engine_control_module.on()
    assert engine_control_module._is_on == True

# Test for off function 
def test_off():
    brake_system = BrakeSystem()
    brake_system.brake() # This will turn off the throttle
    assert brake_system._brake_control_module._is_on == False

# Test for apply_brake_force function
def test_apply_brake_force():
    wheels = Wheels()
    wheels.set_rotation_speed(100)  # Setting initial speed
    wheels.apply_brake_force(20)
    assert wheels.get_rotation_speed() == 80

# Test for set_rotation_speed function
def test_set_rotation_speed():
    wheels = Wheels()
    wheels.set_rotation_speed(100)
    assert wheels.get_rotation_speed() == 100

# Test for accelerate function
def test_accelerate():
    brake_system = BrakeSystem()
    brake_system.accelerate(100)
    assert brake_system.wheels.get_rotation_speed() == 100

# Test for init function
def test_init():
    brake_system = BrakeSystem()
    assert brake_system._brake_control_module._is_on == False
    assert brake_system._engine_control_module._is_on == False
    assert brake_system.wheels.get_rotation_speed() == 0
