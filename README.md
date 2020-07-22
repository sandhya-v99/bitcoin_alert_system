# bitcoin alert system using telegram chatbot in python
<Strong> In this Project, the program alerts the user with an audible alert via a buzzer and a telegram chatbot when the bitcoin price exceeds the set threshold. </Strong> <br>
To build the Bitcoin Price Alerting system, we will require a method to find the current price of Bitcoin by writing a Python program. I have used the following website https://min-api.cryptocompare.com to get the price of Bitcoin. It is a very popular site that provides APIs using which you can fetch various cryptocurrency related data. <br>
The program does the following tasks:- <br>
1) Fetch the current price of Bitcoin every 30 seconds using the Single Symbol Price API in USD. <br>
2) Check if the current price returned by the API is greater than the selling price defined as a variable in the program. <br>
3) If the current price is greater than the selling price, the program should trigger the Bolt Cloud API to switch on the buzzer connected to the Bolt module for 5 seconds and then switches it off after 5 seconds and send a message to the telegram bot that the bitcoin price has exceeded the set threshold. <br>
4) The program repeats the steps 1,2,3 continuously every 30 seconds.
