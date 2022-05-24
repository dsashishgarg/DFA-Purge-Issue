# DFA-Purge-Issue
Durable Function App: 
It contains two Python based Function App one is in DFA code folder, which is a normal durable function app to send/receive request. It is saving the request payload as a output to Storage Account Tables named TaskHubInstance.
Another Time Triggered Function App is in Purge folder, to purge the request sent by the first App, which is actually failing.
