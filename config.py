import json
import logging
def load_config(path):
        try:
            with open(path,encoding="utf-8")as f :
                config = json.load(f)
                return config
        except FileNotFoundError:
            logging.error("找不到設定檔")
            return None
        except json.JSONDecodeError:
            logging.error("設定檔格式錯誤")
            return None