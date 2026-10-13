import json
def load_config(path):
        try:
            with open(path,encoding="utf-8")as f :
                config = json.load(f)
                return config
        except FileNotFoundError:
            print("找不到設定檔")
            return None
        except json.JSONDecodeError:
            print("設定檔格式錯誤")
            return None