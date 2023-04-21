from task2.API import YDAPI


def run_YD_API():
    YDHandler = YDAPI()
    YDHandler.delete_folder()
    resultCode = YDHandler.create_folder()
    return resultCode