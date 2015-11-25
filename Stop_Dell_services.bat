@echo off
sc stop dcpm-notify
::IF %ERRORLEVEL% NEQ 0 call 
echo stopped
sc stop  DellDataVault
::IF %ERRORLEVEL% NEQ 0 call 
echo stopped 
sc stop  DellDataVaultWiz
::IF %ERRORLEVEL% NEQ 0 call 
echo stopped 
sc stop  DellDigitalDelivery
::IF %ERRORLEVEL% NEQ 0 call 
echo stopped 
sc stop  Dell Foundation Services
::IF %ERRORLEVEL% NEQ 0 call 
echo stopped 
sc stop  SupportAssistAgent
::IF %ERRORLEVEL% NEQ 0 call 
echo stopped 
sc stop  Dell.CommandPowerManager.Service
::IF %ERRORLEVEL% NEQ 0 call 
echo stopped 

sc config dcpm-notify start=demand
::IF %ERRORLEVEL% NEQ 0 call 
echo stopped 
sc config  DellDataVault start=demand
::IF %ERRORLEVEL% NEQ 0 call 
echo stopped 
sc config  DellDataVaultWiz start=demand
::IF %ERRORLEVEL% NEQ 0 call 
echo stopped 
sc config  DellDigitalDelivery start=demand
::IF %ERRORLEVEL% NEQ 0 call 
echo stopped 
sc config  "Dell Foundation Services" start=demand
::IF %ERRORLEVEL% NEQ 0 call 
echo stopped 
sc config  SupportAssistAgent start=demand
::IF %ERRORLEVEL% NEQ 0 call 
echo stopped 
sc config  Dell.CommandPowerManager.Service start=demand
::IF %ERRORLEVEL% NEQ 0 call 
echo stopped 
echo done
pause
