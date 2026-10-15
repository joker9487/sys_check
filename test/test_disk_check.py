import pytest
from disk_check import check_disk

PATH = "."   

def test_回傳欄位():
    desk_test= check_disk(PATH,80)
    for key in ["path", "total", "used", "percent", "ok"]:
        assert key in desk_test 

def test_使用率範圍():
    desk_test =check_disk(PATH,80)
    assert 0<=desk_test["percent"]<=100

def test_上限判斷():
    desk_test = check_disk(PATH,101)
    assert(desk_test["ok"])
    desk_test = check_disk(PATH,0)
    assert not desk_test["ok"]

def test_路徑不存在():
    desk_test = check_disk("Z:/",80)
    assert desk_test is None