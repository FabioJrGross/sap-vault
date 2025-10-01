# Responsible for managing SAP login process and session
import os
import shutil
import subprocess
from pathlib import Path

try:
    import winreg
except Exception:
    winreg = None

COMMON_SUBPATHS = [
    r"\\SAP\\FrontEnd\\SapGui\\saplgpad.exe",
    r"\\SAP\\FrontEnd\\SapGui\\saplogon.exe"
]

class SAPLoginService:
        def find_sap_executable(self) -> Path | None:
            # Try to find the SAP Logon executable in common installation paths
            #1. Check PATH
            exe = shutil.which("saplgpad.exe") or shutil.which("saplogon.exe")
            if exe:
                return Path(exe)
            
            #2. Check registry (Windows only)
            if winreg is not None:
                for hive, arch_flag in ((winreg.HKEY_LOCAL_MACHINE, 0),):
                    try:
                        with winreg.OpenKey(hive, r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\saplgpad.exe") as key:
                            val, _ = winreg.QueryValueEx(key, "")
                            if val and Path(val).exists():
                                return Path(val)
                            
                        with winreg.OpenKey(hive, r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\saplogon.exe") as key:
                            val, _ = winreg.QueryValueEx(key, "")
                            if val and Path(val).exists():
                                return Path(val)
                            
                    except OSError:
                        pass
            
            #3. Get windows variable PROGRAMFILES and PROGRAMFILES(X86)
            env_candidates = [
                os.environ.get("ProgramFiles(x86)"),
                os.environ.get("ProgramW6432"),
                os.environ.get("ProgramFiles")                
            ]

            env_candidates = [Path(p) for p in env_candidates if p]

            for base in env_candidates:
                base_path = Path(base)
                for sub in COMMON_SUBPATHS:
                    candidate = base_path.joinpath(*Path(sub).parts[1:])
                    if candidate.exists():
                        return candidate
                    
            #4. Search in common paths
            possible_roots = [
                Path(r"C:\Program Files (x86)"),
                Path(r"C:\Program Files"),
                Path(r"C:\Arquivos de Programas (x86)"),
                Path(r"C:\Arquivos de Programas"),
            ]

            for root in possible_roots:
                for sub in COMMON_SUBPATHS:
                    candidate = root.joinpath(*Path(sub).parts[1:])
                    if candidate.exists():
                        return candidate
                    
            #5. Not found
            return None
        
        def build_sap_command(self, sid: str, client: str, language: str, login: str, password: str) -> list[str]:
            #Get SAP executable path
            exe = self.find_sap_executable()
            if exe is None:
                raise FileNotFoundError("SAP Logon executable not found.")
            
            if not language:
                language = "PT"

            #Build executable command
            shortcut = f'-sid="{sid}" -clt="{client}" -language="{language}" -user="{login}" -pw="{password}" -maxgui'
            return [str(exe), f'/SHORTCUT={shortcut}']
        
        def launch_sap(self, command: str):
            subprocess.Popen(command)