# Smart House System using OOP

class Device:
    """
    Base class for all devices in the Smart Home.
    Each device has a name and status (ON or OFF).
    """
    def __init__(self, name):
        """
        Initializes the device with a given name and sets the status to OFF.
        """
        self.name = name
        self.status = "OFF"

    def turn_on(self):
        """
        Turns the device ON and sets its status to ON.
        """
        self.status = "ON"
        print(f"{self.name} is now ON.")

    def turn_off(self):
        """
        Turns the device OFF and sets its status to OFF.
        """
        self.status = "OFF"
        print(f"{self.name} is now OFF.")

    def get_status(self):
        """
        Returns the current status of the device.
        """
        return f"{self.name} status: {self.status}"


class Light(Device):
    """
    Light class, represents a light in the house.
    Inherits from the Device class.
    """
    def __init__(self, location):
        """
        Initializes the Light with a location.
        """
        super().__init__(f"{location} Light")


class Fan(Device):
    """
    Fan class, represents a fan in the house.
    Inherits from the Device class.
    """
    def __init__(self, location):
        """
        Initializes the Fan with a location.
        """
        super().__init__(f"{location} Fan")


class AirConditioner(Device):
    """
    AirConditioner class, represents an air conditioner.
    Inherits from the Device class.
    Also allows setting the temperature.
    """
    def __init__(self, location, temperature=24):
        """
        Initializes the AirConditioner with a location and an optional temperature.
        Default temperature is 24°C.
        """
        super().__init__(f"{location} Air Conditioner")
        self.temperature = temperature

    def set_temperature(self, temp):
        """
        Sets the air conditioner's temperature.
        """
        self.temperature = temp
        print(f"{self.name} temperature set to {self.temperature}°C")


class SecuritySystem(Device):
    """
    SecuritySystem class, represents a security system for the house.
    Inherits from the Device class.
    Allows the system to be activated or deactivated.
    """
    def __init__(self):
        """
        Initializes the Security System.
        """
        super().__init__("Security System")

    def activate(self):
        """
        Activates the security system and sets its status to ARMED.
        """
        self.status = "ARMED"
        print("Security System is now ARMED.")

    def deactivate(self):
        """
        Deactivates the security system and sets its status to DISARMED.
        """
        self.status = "DISARMED"
        print("Security System is now DISARMED.")


class SmartHome:
    """
    SmartHome class, represents the central system managing all devices in the house.
    """
    def __init__(self):
        """
        Initializes the SmartHome with an empty list of devices.
        """
        self.devices = []

    def add_device(self, device):
        """
        Adds a device to the SmartHome system.
        """
        self.devices.append(device)

    def show_all_statuses(self):
        """
        Displays the status of all devices in the SmartHome system.
        """
        print("\nSmart Home Device Status:")
        for device in self.devices:
            print(device.get_status())


# Example usage of the Smart Home system
if __name__ == "__main__":
    # Create smart devices
    living_light = Light("Living Room")
    bedroom_fan = Fan("Bedroom")
    ac = AirConditioner("Living Room")
    security = SecuritySystem()

    # Create the Smart Home system and add devices
    home = SmartHome()
    home.add_device(living_light)
    home.add_device(bedroom_fan)
    home.add_device(ac)
    home.add_device(security)

    # Use devices: turning them on, setting temperature, and activating security
    living_light.turn_on()
    bedroom_fan.turn_on()
    ac.turn_on()
    ac.set_temperature(22)  # Set the air conditioner to 22°C
    security.activate()

    # Display the status of all devices
    home.show_all_statuses()

    # Example of turning off a device
    bedroom_fan.turn_off()
    home.show_all_statuses()
