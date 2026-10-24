import pytest
from main import run_log_summary
import json


def test_run_log_summary(tmp_path):
    out = tmp_path / "s.json"
    f = tmp_path/ "ttt_test.log"
    f.write_text(
        "[INFO] a\n"
        "\n"                  
        "[ERROR] b\n"
        "hello\n"             
        "[INFO] c\n",
        encoding="utf-8",
        )
    run_log_summary(f,out)
    assert json.loads(out.read_text(encoding="utf-8"))["INFO"]==2
    assert json.loads(out.read_text(encoding="utf-8"))["ERROR"]==1