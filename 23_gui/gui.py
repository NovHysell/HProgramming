from nicegui import ui

ui.label("Welcome to nicegui!").style("color: blue; font-size: 20px")

# Create a greeting

def greet():
    name = input_field.value.strip()
    msg = f"Hello, {name}!"
    ui.notify(msg) # Create a popup

input_field = ui.input("Enter your name")
ui.button("Greet Me!", on_click=greet, color="green")

# Create a counter
class State:
    count = 0

count_label = ui.label("Count: 0")

def add_one():
    State.count += 1
    count_label.text = f"Count: {State.count}"
# TODO
# Create a Reset button which sets the counter to 0

ui.button("Add 1", on_click=add_one)

ui.run(title="Simple Greeting App")
