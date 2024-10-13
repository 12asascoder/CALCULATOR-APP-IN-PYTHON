We first import the necessary module, tkinter, for the GUI.
We define two functions: calculate() to evaluate the expression in the display and clear() to clear the display.
Inside calculate(), we use the eval() function to evaluate the expression and handle any exceptions that may occur.
We create the GUI components, including the display field and buttons for numbers and operations.
We set the button's command to either insert the button's text into the display or call the calculate() function if the "=" button is clicked.
Finally, we start the GUI event loop with root.mainloop().
Note:
This code uses the eval() function to evaluate the expression, which can pose a security risk if used with untrusted input. You may want to consider using a safer alternative for more complex calculator apps.
