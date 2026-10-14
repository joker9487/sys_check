import pytest
from log_summary import LogSummary

@pytest.mark.parametrize("line,expected", [
    ("[INFO] start", "INFO"),
    ("[ERROR] disk full", "ERROR"),
    ("[WARN]no space", "WARN"),
    ("[TEST]TEST", "TEST"),
    ("[123]456", "123"),
])

def test_取等級(line, expected):
    s = LogSummary()
    s.add(line)
    assert s.counts == {expected: 1}

def test_格式錯誤會跳過():
    s= LogSummary()
    s.add("hello world")
    assert not s.counts 
    assert s.skipped==1

def test_total():
    s= LogSummary()
    s.add("[INFO] start")
    s.add("[ERROR] disk full")
    s.add("[WARN]no space")
    assert s.total()==3

def test_讀檔統計(tmp_path):
    f = tmp_path/ "ttt_test.log"
    f.write_text(
        "[INFO] a\n"
        "\n"                  # 空行（read_lines 會跳過，不算 skipped）
        "[ERROR] b\n"
        "hello\n"             # 格式錯（算 skipped）
        "[INFO] c\n",
        encoding="utf-8",
    )
    s=LogSummary()
    s.add_files(str(f))
    assert s.counts=={"INFO": 2, "ERROR": 1}
    assert s.skipped==1

def test_讀檔不存在 (tmp_path):
    s=LogSummary()
    f = tmp_path/ "ttt_test.log"
    s.add_files(f)
    assert s.counts == {}

