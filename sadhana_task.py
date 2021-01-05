import requests
import json
import csv
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


url = 'https://api.github.com/users'


#retrieves the entire user infomation
def list_of_users(): 
    user_info = requests.get(url).json()
    return user_info

# retrieves specified user informations
def organised_users(login): 
    user_info_1 = requests.get(url+f'/{login}').json()
    return user_info_1

# retrieves followers details
def followers_details(login): 
    followers_info = requests.get(url+f'/{login}/followers').json()
    return followers_info

#uploading file to the drive
def upload_to_drive(): 
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth() 
    drive = GoogleDrive(gauth)
    file = drive.CreateFile({"mimeType": "text/csv"})
    file.SetContentFile(r"final_users_list.csv")
    file.Upload()
    
    
final_users = list_of_users()
rows = []
for user in final_users:
    #fetching the user_id divisible by 10
    if user["id"] % 10 == 0:  
        single_user = organised_users(user["login"])
        list_of_followers = followers_details(single_user["login"])

        for followers in list_of_followers:
            rows.append([user["id"], user["login"], single_user["name"], followers["id"], followers['login']])



#csv conversion
with open("final_users_list.csv", 'w') as csvfile: 
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['UserId', 'UserLogin', 'UserName', 'FollowerId', 'FollowerLogin'])
    csvwriter.writerows(rows)
    
upload_to_drive()