# WhatsApp Spy
**WhatsApp Spy** is a python script which allow their users to keep a track on the target's online status.
>Note: This script is for educational purposes only. Use it only to stalk your evil boss. Just kidding, be a good boy and use it justly.

## Prerequisite
* WhatsApp account 
* Python3
* Selenium
* Chrome Browser
* Chrome Driver

## Installation
Clone this repository:
```
git clone https://github.com/nirbhay-gaur/whatsapp-spy.git
cd whatsapp-spy
```
Download Chrome Driver: [Download](https://sites.google.com/a/chromium.org/chromedriver/downloads)<br />
> Note: Be sure to download the correct version of chrome driver which is same as the version of chrome browser installed.
Once downloaded, unzip the file and copy the content inside `whatsapp-spy` folder.<br />

Install requirements: `pip install -r requirements.txt`<br />

Run Script:
```
chmod +x script.py
./script.py -n "Your Boss Name"
```

> Note: The name should the contact name saved in your mobile phone.<br />
> Tip: Instead of name you can also enter saved contact number for more accurate results.

In case you need any help, run: `./script.py -h`

## TODO
Add Notification services to alert the user when target is online.
