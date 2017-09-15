import webbrowser

f = open('wx.html','w')

message = """<html>
<head></head>
<body><h1>Meteodeep</h1><br><h2>Live Weather Radar</h2><br><a href='http://en.sat24.com/en' target='sat24'><image src='http://api.sat24.com/animated/GB/visual/1/GMT%20Standard%20Time/4551246' width=400 height=291></a></body>
</html>"""

f.write(message)
f.close()

webbrowser.open_new_tab('wx.html')
