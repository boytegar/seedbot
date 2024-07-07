from datetime import datetime
import random
import socket
import requests
import time
import base64
import datetime
import socket
import urllib.parse
import json
import time
from datetime import datetime
# Load tokens from file
def main():
    with open('query_id.txt', 'r') as f:
        tokens = [line.strip() for line in f.readlines()]

    print("===========================| t.me/sansxgroup |==============================")
    print("1. Complete all task")
    print("2. Upgrade Tree")
    print("3. Upgrade Storage")
    print("4. Checkin Daily")
    print("5. Claim Daily")
    print("============================================================================")

    choice = input("Enter your choice: ")

    for i, token in enumerate(tokens):
        acc = i + 1
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Origin": "https://cf.seeddao.org",
            "Referer": "https://cf.seeddao.org/",
            "Telegram-Data": token,
            "Origin": "https://cf.seeddao.org"
        }

        if choice == "1":
            response = requests.get("https://elb.seeddao.org/api/v1/tasks/progresses", headers=headers)
            data = response.json()
            if response.status_code == 200:
                task_ids = [task["id"] for task in data["data"]]
                for task_id in task_ids:
                    response_task = requests.post(f"https://elb.seeddao.org/api/v1/tasks/{task_id}", headers=headers)
                    task_data = response_task.json()
                    response_notification = requests.get(f"https://elb.seeddao.org/api/v1/tasks/notification/{task_data['data']}", headers=headers)
                    notification_data = response_notification.json()

                    if response_notification == 200:
                        if notification_data["data"]["data"]["completed"] == "true":
                            print(f"Account {acc} => Reward: {notification_data['data']['data']['reward_amount'] / 1e9:.6f} SEED")
                    else:
                        print(f"Account {acc} => {response_notification.text}")
            else:
                print("query data expired")

        elif choice == "2":
            response = requests.post("https://elb.seeddao.org/api/v1/seed/mining-speed/upgrade", headers=headers)
            print(f"Account {acc} => {response.text}")
        
        elif choice == "3":
            response = requests.post("https://elb.seeddao.org/api/v1/seed/storage-size/upgrade", headers=headers)
            print(f"Account {acc} => {response.text}")
        
        elif choice == "4":
            try:
                response = requests.post("https://elb.seeddao.org/api/v1/login-bonuses", headers=headers)
        # Raise an exception for 4xx or 5xx status codes
                data = response.json()
                if response.status_code == 200:
                    print(f"Account {acc} => Success Checkin {data['data']['no']} Reward: {data['data']['amount'] / 1e9:.6f} SEED")
                else:
                    print(f"Account {acc} => {response.text}")
            except Exception as e:
                print(f"Error: {e}")
                print(f"Response code: {response.status_code}")
                print(f"Response text: {response.text}")      
        
        elif choice == "5":
            while True:
                for i, token in enumerate(tokens):
                    acc = i + 1
                    headers = {
                        "Accept": "application/json, text/plain, */*",
                        "Origin": "https://cf.seeddao.org",
                        "Referer": "https://cf.seeddao.org/",
                        "Telegram-Data": token,
                        "Origin": "https://cf.seeddao.org"
                    }

                    response_worm = requests.post("https://elb.seeddao.org/api/v1/worms/catch", headers=headers)
                    if response_worm.status_code == 200:
                        print("Worm caught")
                    else:
                        print(response_worm.text)

                    response_claim = requests.post("https://elb.seeddao.org/api/v1/seed/claim", headers=headers)
                    claim_data = response_claim.json()
                    response = requests.get("https://elb.seeddao.org/api/v1/profile/balance", headers=headers)
                    balance_data = response.json()
                    if response_claim.status_code == 200:
                        print(f"[[{time.strftime('%d-%m-%Y %H:%M:%S')}] Account {acc}: success claim {claim_data['data']['amount'] / 1e9:.6f} [SEED Balance: {balance_data['data'] / 1e9:.6f}] \033[0m")
                    else:
                        if response.status_code == 200:
                            print(f"[[{time.strftime('%d-%m-%Y %H:%M:%S')}] Account {acc}: {claim_data['message']} [SEED Balance: {balance_data['data'] / 1e9:.6f}][")

                delay = random.randint(4000, 5000)
                mins = delay / 60
                print(f"{time.strftime('%d-%m-%Y %H:%M:%S')} |Wait {mins:.2f} minutes")
                time.sleep(delay)
        
        else:
            exit()


####################################################################################################################################


def print_welcome_message(serial=None):
    print(r"""
              
            Created By Snail S4NS Group
    find new airdrop & bot here: t.me/sansxgroup
              
          """)
    print()
    if serial is not None:
        print(f"Copy, tag bot @SnailHelperBot and paste this key in discussion group t.me/sansxgroup")
        print(f"Your key : {serial}")

def read_serial_from_file(filename):
    serial_list = []
    with open(filename, 'r') as file:
        for line in file:
            serial_list.append(line.strip())
    return serial_list

serial_file = "serial.txt"
serial_list = read_serial_from_file(serial_file)


def read_initdata_from_file(filename):
    initdata_list = []
    with open(filename, 'r') as file:
        for line in file:
            initdata_list.append(line.strip())
    return initdata_list

def get_user_id_from_init_data(init_data):
    parsed_data = urllib.parse.parse_qs(init_data)
    if 'user' in parsed_data:
        user_data = parsed_data['user'][0]
        user_data_json = urllib.parse.unquote(user_data)
        user_data_dict = json.loads(user_data_json)
        if 'id' in user_data_dict:
            return user_data_dict['id']
    return None

def get_nama_from_init_data(init_data):
    parsed_data = urllib.parse.parse_qs(init_data)
    if 'user' in parsed_data:
        user_data = parsed_data['user'][0]
        data = ""
        user_data_json = urllib.parse.unquote(user_data)
        user_data_dict = json.loads(user_data_json)
        if 'first_name' in user_data_dict:
            data = user_data_dict['first_name']
        if 'last_name' in user_data_dict:
            data = data + " " + user_data_dict['last_name']
        if 'username' in user_data_dict :
            data = data + " " + f"({user_data_dict['username']})"
    return data


def get_serial(current_date, getpcname, name, status):
    formatted_current_date = current_date.strftime("%d-%m-%Y")
    # Encode each value using base64
    getpcname += "knjt"
    name    += "knjt"
    encoded_getpcname = base64.b64encode(getpcname.encode()).decode().replace("=", "")
    encoded_current_date = base64.b64encode(formatted_current_date.encode()).decode().replace("=", "")
    encoded_name = base64.b64encode(name.encode()).decode().replace("=", "")
    encoded_status = base64.b64encode(str(status).encode()).decode().replace("=", "")

    # Calculate the length of each encoded value
    getpcname_len = len(encoded_getpcname)
    current_date_len = len(encoded_current_date)
    name_len = len(encoded_name)
    status_len = len(encoded_status)

    # Concatenate the encoded values with their lengths
    serial = "S4NS-"
    serial += str(getpcname_len).zfill(2) + encoded_getpcname
    serial += str(current_date_len).zfill(2) + encoded_current_date
    serial += str(name_len).zfill(2) + encoded_name
    serial += str(status_len).zfill(2) + encoded_status
    return serial

def decode_pc(serial, getpcname, name, current_date):
    try:
        getpcname_len = int(serial[5:7])
        encoded_getpcname = serial[7:7+getpcname_len]
        current_date_len = int(serial[7+getpcname_len:9+getpcname_len])
        encoded_current_date = serial[9+getpcname_len:9+getpcname_len+current_date_len]
        name_len = int(serial[9+getpcname_len+current_date_len:11+getpcname_len+current_date_len])
        encoded_name = serial[11+getpcname_len+current_date_len:11+getpcname_len+current_date_len+name_len]
        status_len = int(serial[11+getpcname_len+current_date_len+name_len:13+getpcname_len+current_date_len+name_len])
        encoded_status = serial[13+getpcname_len+current_date_len+name_len:13+getpcname_len+current_date_len+name_len+status_len]

        # Decode each value using base64
        decoded_getpcname = base64.b64decode(encoded_getpcname + "==").decode()
        decoded_current_date = base64.b64decode(encoded_current_date + "==").decode()
        decoded_name = base64.b64decode(encoded_name + "==").decode()
        decoded_status = base64.b64decode(encoded_status + "==").decode()
        
        dates = compare_dates(decoded_current_date)

        if decoded_status != '1':
            print("Key Not Generated")
            return None
            
        elif decoded_getpcname.replace("knjt", "") != getpcname:
            print("Different devices registered")
            return None
        
        elif decoded_name.replace("knjt", "") != name:
            print("Different bot registered")
            return None
        
        elif dates < 0:
            print("Key Expired")
            return None
        else:
            print(f"            Key alive until : {decoded_current_date} ")
            return dates
    except Exception as e:
        print(f'Key Error : {e}')

def compare_dates(date_str):
    tanggal_compare_dt = datetime.strptime(date_str, '%d-%m-%Y')
    tanggal_now = datetime.now()
    perbedaan_hari = (tanggal_compare_dt - tanggal_now).days
    return perbedaan_hari

def started():
    getpcname = socket.gethostname()
    name = "SEED"
    current_date = datetime.now() # Get the current date
    status = '0'

    if len(serial_list) == 0:
        serial = get_serial(current_date, getpcname, name, status)
        print_welcome_message(serial)
    else:
        serial = serial_list[0]
        if serial == 'S4NS-XXWEWANTBYPASSXX':
            main()
        else:
            decodeds = decode_pc(serial, getpcname, name, current_date)
            if decodeds is not None:
                    print_welcome_message()
                    time.sleep(10)
                    main()         
            else:
                serial = get_serial(current_date, getpcname, name, status)
                print_welcome_message(serial)
                print("Please submit the key to bot for get new key")
            
if __name__ == "__main__":
    started()
