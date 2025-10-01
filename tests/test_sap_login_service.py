from pathlib import Path
from pytest_lazyfixture import lazy_fixture
from unittest.mock import patch, MagicMock
from sap_vault.services.sap_login_service import SAPLoginService

def test_find_sap_executable_in_path():
    service = SAPLoginService()
    fake_path = Path(r"C:\fake\saplgpad.exe")

    with patch("sap_vault.services.sap_login_service.shutil.which", return_value=str(fake_path)):
        exe = service.find_sap_executable()
        assert exe == fake_path

def test_build_sap_command_basic():
    service = SAPLoginService()
    fake_exe = Path(r"C:\fake\saplgpad.exe")

    with patch.object(service, 'find_sap_executable', return_value=fake_exe):
        command = service.build_sap_command("ED0", "100", "EN", "fabiojg", "pass")
        expected_command = [str(fake_exe), '/SHORTCUT=-sid="ED0" -clt="100" -language="EN" -user="fabiojg" -pw="pass" -maxgui']
        assert command == expected_command

def test_launch_sap_calls_popen():
    service = SAPLoginService()
    fake_command = ["C:\\fake\\saplgpad.exe", '/SHORTCUT=-sid="ED0" -clt="100" -language="EN" -user="fabiojg" -pw="pass" -maxgui']

    with patch("sap_vault.services.sap_login_service.subprocess.Popen") as mock_popen:
        service.launch_sap(fake_command)
        mock_popen.assert_called_once_with(fake_command)
