import pytest
from unittest import mock

@pytest.fixture
def temp_dir(tmp_path):
    """Provides a temporary directory unique to the test invocation."""
    return tmp_path

@pytest.fixture
def mock_git_repo():
    """Mocks GitPython's Repo object."""
    with mock.patch("git.Repo") as mock_repo_cls:
        mock_repo = mock.Mock()
        mock_repo_cls.return_value = mock_repo
        yield mock_repo

@pytest.fixture(autouse=True)
def shared_setup_teardown():
    """Shared setup/teardown logic for all tests, including patching gh repo create."""
    import subprocess as sp
    from unittest import mock

    real_run = sp.run

    def fake_run(*args, **kwargs):
        # Support subprocess.run(args, **kwargs) where args can be list or str
        cmd = args[0] if args else kwargs.get("args")
        if isinstance(cmd, list) and len(cmd) >= 3:
            if cmd[0] == "gh" and cmd[1] == "repo" and cmd[2] == "create":
                # Simulate successful repo creation without creating a real repo
                return sp.CompletedProcess(cmd, 0, stdout="Simulated repo created\n", stderr="")
        # Otherwise, call the real subprocess.run
        return real_run(*args, **kwargs)

    with mock.patch("subprocess.run", side_effect=fake_run):
        yield