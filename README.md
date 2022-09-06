# PySpam
>Python OTP Spammer for Iran Numbers (+98)

# Educational purposes only                  
This tool is for educational purposes only to show you how it works, or how to make one!!                           

# How to create one ?                                    
So the question is how I can create new spammer with new APIs?                                       
How can I find these headers or post url                                              
>Here is how to do that:                                                   

**1**: Find your website or web application                                                       
**2**: Navigate to** Registeration** page                                                             
**3**: Hit **f12** and open developer tools                                      
**4**: Go to **Network** section                                               
**5**: Then register to the website                                                      
**6**: After that, you will see the requests in **Network** section                                                  
**7**: Search for **post** request and find the request you just sent!                                               
**8**: If you click on the request, you wiil see some data and information                                             

**Header**: You can find your request header in **headers** section, turn on the **row** option and copy your header and create a variable for that
```
myHeader = {
    your header here    # you need to edit your header and change it to dictionary
}
```

**URL**: In the **Headers** section, at the top, you will see a **post url**, that is your url, copy it and create a variable for that                     
```
myURL = "your url here"
```

**Data**: In the **request** section, you can see your **Json** data, turn on the **row** option and copy your json and create a variable for that
```
myData = {
    your data here
}
```

**Make request**: The final step is making a post request
```
import requests

myHeader = {
    your header here    # you need to edit your header and change it to dictionary
}

myURL = "your url here"

myData = {
    your data here
}

response = requests.post(myURL, headers=myHeader, json=myData)  # you can also use proxy
print(response)
```
**Sorry for bad English**


# Installation
**apt:**                                  
**[1]** `sudo apt install python3 git python-pip`                               
**[2]** `git clone https://github.com/SlavPH/PySpam`                             
**[3]** `cd PySpam`               
**[4]** `chmod +x *`                  
**[5]** `./spam.py`                                            

**pacman:**                             
**[1]** `sudo pacman -S python3 git python-pip`                               
**[2]** `git clone https://github.com/SlavPH/PySpam`                             
**[3]** `cd PySpam`               
**[4]** `chmod +x *`                  
**[5]** `./spam.py`                                            
                            

**Termux:**                    
**[1]** `pkg install python3 git`                               
**[2]** `git clone https://github.com/SlavPH/PySpam`                             
**[3]** `cd PySpam`               
**[4]** `chmod +x *`                  
**[5]** `./spam.py`                                            


# Social Media
[Instagram](https://instagram.com/theslavph)                                                
[Telegram](https://telegram.me/theslavph)

# Educational purposes noly                 
> Use this tool only for fun with permission                  



> Thanks 
