; datalogger.nsi

;--------------------------------

!ifdef HAVE_UPX
!packhdr tmp.dat "upx\upx -9 tmp.dat"
!endif

!ifdef NOCOMPRESS
SetCompress off
!endif

;--------------------------------

Name "Hermes-Datalogger"
Caption "Instal·lació del Datalogger 2.1"
Icon "${NSISDIR}\Contrib\Graphics\Icons\box-install.ico"
OutFile "hermes_datalogger21.exe"

SetDateSave on
SetDatablockOptimize on
CRCCheck on
SilentInstall normal
BGGradient 000000 FFFFFF FFFFFF 
InstallColors FF8080 000030
XPStyle on

InstallDir "$PROGRAMFILES\Datalogger"
;InstallDirRegKey HKLM "Software\NSISTest\BigNSISTest" ""

CheckBitmap "${NSISDIR}\Contrib\Graphics\Checks\classic-cross.bmp"

;LicenseText "A test text, make sure it's all there"
;LicenseData "llicencia.txt"

;--------------------------------

;Page license
;Page components
Page directory
Page instfiles

UninstPage uninstConfirm
UninstPage instfiles

;--------------------------------

;!ifndef NOINSTTYPES ; only if not defined
;  InstType "Most"
;  InstType "Full"
;  InstType "More"
;  InstType "Base"
  ;InstType /NOCUSTOM
  ;InstType /COMPONENTSONLYONCUSTOM
;!endif

AutoCloseWindow false
ShowInstDetails show

;--------------------------------

Section ""

  SetOutPath $INSTDIR
  
  File /a "datalogger.exe"
  File /a "bz2.pyd"
  File /a "library.zip"
  File /a "mingwm10.dll"
  File /a "MSVCR71.dll"
  File /a "python24.dll"
  File /a "pywintypes24.dll"
  File /a "QtCore4.dll"
  File /a "QtCore.pyd"
  File /a "QtGui4.dll"
  File /a "QtGui.pyd"
  File /a "select.pyd"
  File /a "sip.pyd"
  File /a "unicodedata.pyd"
  File /a "w9xpopen.exe"
  File /a "win32event.pyd"
  File /a "win32file.pyd"
  File /a "zlib.pyd"
 
  WriteUninstaller "datalogger-uninst.exe"
   
  SetShellVarContext All
  CreateDirectory "$SMPROGRAMS\Hermes Datalogger 2.1"
  CreateShortCut "$SMPROGRAMS\Hermes Datalogger 2.1\Datalogger.lnk" "$INSTDIR\datalogger.exe" 
  CreateShortCut "$SMPROGRAMS\Hermes Datalogger 2.1\Uninstall.lnk" "$INSTDIR\datalogger-uninst.exe"
SectionEnd

UninstallText "This will uninstall Datalogger. Hit next to continue."
UninstallIcon "${NSISDIR}\Contrib\Graphics\Icons\box-uninstall.ico"

Section "Uninstall"

  Delete "$INSTDIR\datalogger.exe"
  Delete "$INSTDIR\bz2.pyd"
  Delete "$INSTDIR\datalogger-uninst.exe"
  Delete "$INSTDIR\library.zip"
  Delete "$INSTDIR\library.zip"
  Delete "$INSTDIR\mingwm10.dll"
  Delete "$INSTDIR\MSVCR71.dll"
  Delete "$INSTDIR\python24.dll"
  Delete "$INSTDIR\pywintypes24.dll"
  Delete "$INSTDIR\QtCore4.dll"
  Delete "$INSTDIR\QtCore.pyd"
  Delete "$INSTDIR\QtGui4.dll"
  Delete "$INSTDIR\QtGui.pyd"
  Delete "$INSTDIR\select.pyd"
  Delete "$INSTDIR\sip.pyd"
  Delete "$INSTDIR\unicodedata.pyd"
  Delete "$INSTDIR\w9xpopen.exe"
  Delete "$INSTDIR\win32event.pyd"
  Delete "$INSTDIR\win32file.pyd"
  Delete "$INSTDIR\zlib.pyd"
  
  RMDir "$INSTDIR"
  
  SetShellVarContext All
  RMDir "$SMPROGRAMS\Hermes Datalogger 2.1"

  IfFileExists "$INSTDIR" 0 NoErrorMsg
    MessageBox MB_OK "Note: $INSTDIR could not be removed!" IDOK 0 ; skipped if file doesn't exist
  NoErrorMsg:

SectionEnd
