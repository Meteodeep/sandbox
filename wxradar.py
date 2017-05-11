import webbrowser

new=2;

url="http://api.wunderground.com/api/8a861440afa5861d/radar/q/Ireland/Dublin.gif?newmaps=1width=300&height=300";

print("Welcome to Meteodeep Live Radar, Dublin Ireland")
wx=input("Type 'Yes' if you want to access the Radar")



if wx == "Yes":
    webbrowser.open(url,new=new);


else:
    print("ERROR")
