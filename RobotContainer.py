from commands2 import Command, button
from wpilib import XboxController
from commands.ExampleCommand import ExampleCommand
from subsystems.ExampleSubsystem import ExampleSubsystem

class RobotContainer:
    _exampleSubsystem : ExampleSubsystem
    _exampleCommand : ExampleCommand
    _coontrols0 : XboxController
    
    def __init__(self) -> None:                
        self.configureButtonBindings(self)
        
    def configureButtonBindings(self) -> None:
        button.JoystickButton(self._coontrols0, 0)
        
    def getAutonomousCommand(self) -> Command:
        return self._exampleCommand
        
        