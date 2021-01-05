# Sadhana_user_info
 
TASK 1
Fetch the user's  list from https://api.github.com/users.
Filter only the id that is divisible by 10
Iterate the results and get the user details and folloers detals from https://api.github.com/users/{login} and https://api.github.com/users/{login}/followers respectively.

list_of_users function gets the list of users.
organised_users gets the specific login details of the users.
followers_details gets the folloers list.
upload_to_drive loads into the drive
using for loop id's that are divisible by 10 are fetched.
finally convert the entire file to csv format using csvwriter.

