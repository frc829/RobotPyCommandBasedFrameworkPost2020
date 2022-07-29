from commands2 import CommandBase
from subsystems.ExampleSubsystem import ExampleSubsystem

class ExampleCommand(CommandBase):
    _subsystem : ExampleSubsystem
    
    def __init__(self, subsystem : ExampleSubsystem) -> None:
        self._subsystem = subsystem
        
        CommandBase.addRequirements(subsystem)
        
    def initialize(self) -> None:
        return super().initialize()
    
    def execute(self) -> None:
        return super().execute()
    
    def end(self, interrupted: bool) -> None:
        return super().end(interrupted)
    
    def isFinished(self) -> bool:
        return False
        