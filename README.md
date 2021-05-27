# aviahackathon2021
Airport navigation system

### Run
Run the app:
```bash
python3 -m pip install -r requirements.txt
python3 main.py
```


AR microservice build:

Step 1: Build image
```bash
docker build -t ar-app .
```

Step 2: Run image
```bash
docker run -it -p 8081:4000 ar-app:latest
```

After this microservice will be available by address: 
```bash
https://your_server_ip:8081 
```


### Demo
Main map screen with generated route:
![Alt text](img/1.jpg?raw=true "Title")
Map is resizable and movable. 
Route page shows description of the route steps:

![Alt text](img/2.jpg?raw=true "Title")

Menu of the app allows to scan passenger ticket QR and build route right to the passenger's gate. 
Also user can use AR to navigate through the airport. Help button calls the airport service.

![Alt text](img/3.jpg?raw=true "Title")


### Contacts

- AR implementation: [@kekmarakek](https://t.me/kekmarakek)
- Navigation system: [@mommysskier](https://t.me/mommysskier)
- Cross-platform app: [@grit4in](https://t.me/grit4in)

[Up](#candydeliveryapi)
