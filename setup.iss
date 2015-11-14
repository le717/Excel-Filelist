#define MyAppName "Excel Filelist"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "Caleb Ely"
#define MyAppURL "https://github.com/le717/Excel-Filelist"
#define MyAppExeName "ExcelFilelist.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
AppId={{66B90F83-87B7-4508-9B38-E9FC7CDC3D80}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
DefaultDirName={localappdata}\ExcelFilelist
OutputDir=Output
DefaultGroupName={#MyAppName}
DisableDirPage=yes
DisableProgramGroupPage=yes
DisableFinishedPage=yes
DisableStartupPrompt=yes
DisableReadyPage=yes
DisableReadyMemo=yes
DisableWelcomePage=yes
OutputBaseFilename=ExcelFilelist
Compression=lzma2/max
SolidCompression=yes
Uninstallable=no
CreateUninstallRegKey=no
PrivilegesRequired=lowest

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "src\blacklist.cfg"; DestDir: "{app}"; Flags: ignoreversion
Source: "bin\ExcelFilelist.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "bin\library.zip"; DestDir: "{app}"; Flags: ignoreversion
Source: "bin\_bz2.pyd"; DestDir: "{app}"; Flags: onlyifdoesntexist
Source: "bin\_decimal.pyd"; DestDir: "{app}"; Flags: onlyifdoesntexist
Source: "bin\_elementtree.pyd"; DestDir: "{app}"; Flags: onlyifdoesntexist
Source: "bin\_hashlib.pyd"; DestDir: "{app}"; Flags: onlyifdoesntexist
Source: "bin\_lzma.pyd"; DestDir: "{app}"; Flags: onlyifdoesntexist
Source: "bin\_socket.pyd"; DestDir: "{app}"; Flags: onlyifdoesntexist
Source: "bin\PIL._imaging.pyd"; DestDir: "{app}"; Flags: onlyifdoesntexist
Source: "bin\pyexpat.pyd"; DestDir: "{app}"; Flags: onlyifdoesntexist
Source: "bin\select.pyd"; DestDir: "{app}"; Flags: onlyifdoesntexist
Source: "bin\unicodedata.pyd"; DestDir: "{app}"; Flags: onlyifdoesntexist
Source: "bin\win32api.pyd"; DestDir: "{app}"; Flags: onlyifdoesntexist
Source: "bin\python34.dll"; DestDir: "{app}"; Flags: onlyifdoesntexist
Source: "bin\pywintypes34.dll"; DestDir: "{app}"; Flags: onlyifdoesntexist

[Run]
Filename: "{app}\ExcelFilelist.exe"; Parameters: "{src}"

[Code]
// Sourced from http://stackoverflow.com/a/22184880
const
  BN_CLICKED = 0;
  WM_COMMAND = $0111;
  CN_BASE = $BC00;
  CN_COMMAND = CN_BASE + WM_COMMAND;

procedure CurPageChanged(CurPageID: Integer);
var
  Param: Longint;
begin
  // if we are on the ready page, then...
  if CurPageID = wpReady then
  begin
    // the result of this is 0, just to be precise...
    Param := 0 or BN_CLICKED shl 16;
    // post the click notification message to the next button
    PostMessage(WizardForm.NextButton.Handle, CN_COMMAND, Param, 0);
  end;
end;
