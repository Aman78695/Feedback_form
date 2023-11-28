import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
@anvil.server.callable
def feedback(name,email,feedback):
  app_tables.feedback_table.add_row(name=name,email=email,feedback=feedback,created_on=datetime.now())
  anvil.email.send(from_name = "My App Support", 
                 to = email,
                 subject = "Welcome",
                 text = "Welcome to My App!")