import requests

def fetch_from_api():
    response = requests.get('https://api.freeapi.app/api/v1/public/randomusers/user/random')
    data = response.json()


    if(data["success"]  and "data" in data):
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    
    else:
        raise Exception ("Failed to get data from api")
    
    


def main():
    try:
        username, country = fetch_from_api()
        print(f"{username} {country}")

    except Exception as e:
        print(str(e))   
        
         
if __name__ == "__main__":
    main()
