import tkinter

MILES_TO_KM_RATIO = 1.609344

# window setup
window = tkinter.Tk()
window.title("Miles to Km")
window.config(padx=10, pady=10)

# row 0 ***************************************************

# input setup
entry = tkinter.Entry(width=10)
entry.grid(column=1, row=0, padx=(10, 5), pady=(10, 5))

# "Miles" label setup
label_miles = tkinter.Label(text="Miles")
label_miles.grid(column=2, row=0, padx=(5, 10), pady=(10, 5))

# row 1 ***************************************************

# "is equal to" label setup
label_equal = tkinter.Label(text="is equal to")
label_equal.grid(column=0, row=1, padx=(10, 5), pady=(5, 5))

# converted unit label setup
label_converted = tkinter.Label(text="0")
label_converted.grid(column=1, row=1, padx=(5, 5), pady=(5, 5))

# converted unit label setup
label_km = tkinter.Label(text="Km")
label_km.grid(column=2, row=1, padx=(5, 10), pady=(5, 5))

# row 2 ***************************************************


def convert():
    miles = float(entry.get())
    kilometers = miles * MILES_TO_KM_RATIO
    label_converted.config(text=f"{kilometers}")


# calls convert() when pressed
button = tkinter.Button(text="Calculate", command=convert)
button.grid(column=1, row=2, padx=(5, 5), pady=(5, 5))

# maintain window until user closes app
window.mainloop()
