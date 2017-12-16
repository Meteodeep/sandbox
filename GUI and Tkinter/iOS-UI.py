import ui

def button_tapped(sender):
    sender.title = 'Hello'

view = ui.View()                                      # [1]
view.name = 'Demo'                                    # [2]
view.background_color = 'white'                       # [3]
button = ui.Button(title='Tap me!')                   # [4]
button.center = (view.width * 0.5, view.height * 0.5) # [5]
button.flex = 'LRTB'                                  # [6]
button.action = button_tapped                         # [7]
view.add_subview(button)                              # [8]
view.present('sheet')                                 # [9]
