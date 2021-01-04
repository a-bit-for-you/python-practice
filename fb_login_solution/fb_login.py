import requests
import re

user_name = 'sangem007@gmail.com'  # friend's account (Name Santosh)
password = 'Your password here'  
fb_url = 'https://www.facebook.com/'


def login(session, email, password):


    # Attempt to login to Facebook
    response = session.post('https://m.facebook.com/login.php', data={
        'email': email,
        'pass': password
    }, allow_redirects=False)  # disabling the redirections
    
    # handling response code 302
    assert response.status_code == 302
    assert 'c_user' in response.cookies
    return response.cookies


# session
session = requests.session()

# cookies
cookies = login(session, user_name, password)

# response
response = session.get(fb_url, cookies=cookies,allow_redirects=False)

# storing the output in html file
with open("file.html", "w",encoding='utf-8') as f:
    f.write(response.text)

assert response.text.find('Home') != -1
print(response)