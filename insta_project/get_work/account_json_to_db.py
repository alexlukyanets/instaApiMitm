from AccountInfo import AccountInfo
from DbWorking import DbWorking
data = AccountInfo.get_from_json()

DbWorking.update_db(data)