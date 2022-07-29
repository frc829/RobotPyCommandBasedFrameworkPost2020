from commands2 import CommandScheduler
from commands2 import Command
from wpilib import TimedRobot
from RobotContainer import RobotContainer

class robot(TimedRobot):
    _autonomousCommand : Command
    
    _robotContainer : RobotContainer
    
    def robotInit(self) -> None:
        self._robotContainer = RobotContainer()
    
    def robotPeriodic(self) -> None:
        CommandScheduler.getInstance().run()
        
    def disabledInit(self) -> None:
        return super().disabledInit()
    
    def autonomousInit(self) -> None:
        self._autonomousCommand = self._robotContainer.getAutonomousCommand()
        
        if(self._autonomousCommand != None):
            self._autonomousCommand.schedule()
        
    def autonomousPeriodic(self) -> None:
        return super().autonomousPeriodic()
    
    def teleopInit(self) -> None:
        if(self._autonomousCommand != None):
            self._autonomousCommand.cancel()
            
    def teleopPeriodic(self) -> None:
        return super().teleopPeriodic()
    
    def testInit(self) -> None:
        CommandScheduler.getInstance().cancelAll()
        
    def testPeriodic(self) -> None:
        return super().testPeriodic()
    
    def _simulationInit(self) -> None:
        return super()._simulationInit()
    
    def _simulationPeriodic(self) -> None:
        return super()._simulationPeriodic()
    
    
            
    
    
            
        
            
    
    
    
    