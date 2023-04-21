import requests
import configparser


class YDAPI:
    def __init__(self) -> None:
        self.folderName = 'dummy folder'
        self.baseUrl = 'https://cloud-api.yandex.net/v1/disk/'
        
        self.userConfig = configparser.ConfigParser()
        self.userConfig.read('./user_config.ini')
        self.headers = {"Content-Type": "application/json", 
                        "Authorization": "OAuth {token}".format(token=self.userConfig['YD']['token'])}

    def create_folder(self):
        requestUrl = self.baseUrl + 'resources'
        params = {'path':self.folderName}
        response = requests.put(requestUrl, headers=self.headers, params=params)

        return response.status_code
    
    def delete_folder(self):
        requestUrl = self.baseUrl + 'resources'
        params = {'path':self.folderName}
        response = requests.delete(requestUrl, headers=self.headers, params=params)

        return response.status_code
    

if __name__ == '__main__':
    YDHandler = YDAPI()
    resultCode = YDHandler.create_folder()
    print(resultCode)