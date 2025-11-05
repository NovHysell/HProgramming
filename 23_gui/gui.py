from nicegui import ui

# Create a greeting

# --- GREETINGS --- #
def greet():
    name = input_field.value.strip()
    msg = f"Hello, {name}!"
    ui.notify(msg) # Create a popup


# Create a counter
# --- COUNTER --- #
class State:
    count = 0

def add_one():
    State.count += 1
    count_label.text = f"Count: {State.count}"
# TODO
# Create a Reset button which sets the counter to 0
def reset():
    State.count = 0
    count_label.text = f"Count: {State.count}"

# --- LAYOUT --- #

ui.label("Welcome to nicegui!").style("color: blue; font-size: 20px")
input_field = ui.input("Enter your name")
ui.button("Greet Me!", on_click=greet, color="green")


count_label = ui.label("Count: 0").classes("font-mono-text-ig")
with ui.row():
    ui.button("Add 1", on_click=add_one)
    ui.button("Reset", on_click=reset, color = "red")

ui.run(title="Simple Greeting App")

# ui.columm() puts labels under it on the y-axis, ui.row() puts labels under it on the x-axis
# ui.columm():
#   ui.label("label 1")
