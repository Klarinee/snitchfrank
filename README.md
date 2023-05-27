# snitchfrank
### **Tool's brief history**
Snitch Frank is a tool that takes advantage of the online service called Franklin Fueling System TS-550. This exploit was firstly found by [Parsa Rezaie Khiabanloo](https://www.exploit-db.com/?author=11857) and posted on [Exploit DB](https://www.exploit-db.com/exploits/51321) on 2023.04.07. This exploit was later adapted by me, Klarine, to become automated and much less time consuming so you can spend your time finding vulnerable servers instead of just following the same boring process of finding vulnerable servers, adpating the payload and sending it only to find out that the server is not vulnerable, and repeat the process all over again.

### **What does this tool do?**
Snitch Frank basically sends a payload asking the vulnerable server for its configurations. If the server is vulnerable, it returns hashed default passwords that can be easily broken using [John](https://www.github.com/openwall/john).

### **Requirements**
> Requests, Python 3

### **Compatible platforms**
> Windows, Linux, MacOS, WSL

## **This tool does not require sudo**
### **Usage**
Snitch frank has 4 parameters.
- u  | url (-u | --url) Required;
- p  | port (-p | --port) Optional; Default is 10001
- ua | user-agent (-ua | --user-agent) Optional; If no user agent is set by user, a random user agent will be picked.
- v  | verbose (-v | --verbose) Optional; This option prints the progress on screen
```
python3 snitchfrank -u <URL> -v
```
![](https://media.discordapp.net/attachments/1105259252135768207/1111864328652607549/image.png)
