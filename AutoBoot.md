# Auto-Start a fullscreen Chrome webpage on Raspbian (Jessie)

1 Install Chromium

2 Create a file called ~/.config/autostart/chromium.desktop with the following contents:

<code>[Desktop Entry]
Encoding=UTF-8
Name=Connect
Comment=Checks internet connectivity
Exec=/usr/bin/chromium-browser -incognito --kiosk YOUR_WEB_ADDRESS</code>

3. Reboot!
