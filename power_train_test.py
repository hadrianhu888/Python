import pytest
from power_train import PowerTrain

# Using pytest fixture to share powerTrain instance across tests
@pytest.fixture(scope="module")
def powerTrain():
    return PowerTrain()

# Testing initial state of PowerTrain
def test_power_train_initial_state(powerTrain):
    assert powerTrain.get_power() == 0
    assert powerTrain.get_speed() == 0
    assert powerTrain.get_torque() == 0
    assert powerTrain.get_gear() == 0
    assert powerTrain.get_rpm() == 0
    assert powerTrain.get_throttle() == 0
    assert powerTrain.get_brake() == 0
    assert powerTrain.get_clutch() == 0
    assert powerTrain.get_engine_temp() == 0
    assert powerTrain.get_oil_temp() == 0
    assert powerTrain.get_oil_pressure() == 0
    assert powerTrain.get_fuel_pressure() == "Empty"

# Testing the on() method
def test_power_train_on(powerTrain):
    powerTrain.on()
    assert powerTrain.get_status()['Engine Status'] == True

# Testing the off() method
def test_power_train_off(powerTrain):
    powerTrain.off()
    assert powerTrain.get_status()['Engine Status'] == False

# Testing brake method with and without arguments
def test_power_train_brake(powerTrain):
    powerTrain.brake()
    assert powerTrain.get_brake() == False  # Assuming brake method without args sets brake to 0

def test_power_train_brake_with_arg(powerTrain):
    powerTrain.brake(1)
    assert powerTrain.get_brake() == True  # Assuming brake method with arg sets brake to 1

# Testing set_gear() method
def test_power_train_set_gear(powerTrain):
    powerTrain.set_gear(1)
    assert powerTrain.get_gear() == 1

# Testing get_status() method
def test_power_train_get_status(powerTrain):
    assert powerTrain.get_status() == {
        'Engine Status': False,
        'Transmission Gear': 0,
        'Propulsion Status': False,
        'Gear Status': 1  # Gear was set to 1 in the previous test
    }

# ... Add other test cases as needed

def test_power_train_accelerate(powerTrain):
    powerTrain.accelerate(1)
    assert powerTrain.get_speed() == 1
    
def test_power_train_velocity(powerTrain):
    powerTrain.accelerate(1)
    assert powerTrain.get_speed() == 1
    
def main():
    powerTrain = PowerTrain()
    test_power_train_initial_state(powerTrain)
    test_power_train_on(powerTrain)
    test_power_train_off(powerTrain)
    test_power_train_brake(powerTrain)
    test_power_train_brake_with_arg(powerTrain)
    test_power_train_set_gear(powerTrain)
    test_power_train_get_status(powerTrain)
    test_power_train_accelerate(powerTrain)
    test_power_train_velocity(powerTrain)
    
if __name__ == "__main__":
    main()

    

    
