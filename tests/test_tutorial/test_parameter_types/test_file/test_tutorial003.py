import subprocess
from pathlib import Path

import typer
from typer.testing import CliRunner

from parameter_types.file import tutorial003 as mod

runner = CliRunner()

app = typer.Typer()
app.command()(mod.main)

binary_file = Path("./config.txt")


def test_main():
    binary_file.write_bytes(b"la cig\xc3\xbce\xc3\xb1a trae al ni\xc3\xb1o")
    result = runner.invoke(app, ["--file", f"{binary_file}"])
    binary_file.unlink()
    assert result.exit_code == 0
    assert "Processed bytes total:" in result.output


def test_script():
    result = subprocess.run(
        ["coverage", "run", mod.__file__, "--help"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
    )
    assert "Usage" in result.stdout
