import tkinter as tk
from tkinter import ttk

from GenerateWords import GenerateWords


def solve_puzzle():
	user_input = entry.get()
	if len(user_input) > 7:
		input_error.config(text="Letters Must not be greater than 7")
	elif not user_input:
		input_error.config(text="Please Enter Letters")
	else:
		input_error.config(text="")
		generated_words = GenerateWords()
		results = generated_words.main(letters=user_input)

		# Set state to "normal" to enable editing
		result_text.config(state="normal")
		# Clear the previous content in result_text
		result_text.delete("1.0", "end")
		# Display the formatted dictionary content
		for key, value in results.items():
			result_text.insert("end", f'{key}-letter words:\n')
			for word in value:
				result_text.insert("end", f'{word}\n')
			result_text.insert("end", '\n')

		# Set state to "disabled" to make it read-only
		result_text.config(state="disabled")


# tkinter widows
window = tk.Tk()
window.title("Puzzle Solver")
window.geometry("400x400")
window.resizable(0, 0)
window.iconphoto(False, tk.PhotoImage(file="assets/icon.png"))
label = tk.Label(
	window,
	text="Puzzle Solver",
	font=15,
	foreground="blue"
)
label.pack()

entry = tk.Entry(window, width=50)
input_error = tk.Label(window, text="", foreground="red")
entry.pack()
input_error.pack()
button = tk.Button(
	window,
	text="Get Words",
	command=solve_puzzle,
	background="green",
	foreground="white"
)
button.pack()

# Create a scrollable view for the result
scrollable_frame = ttk.Frame(window)
scrollable_frame.pack(fill="both", expand=True)

scrollbar = ttk.Scrollbar(scrollable_frame, orient="vertical")
scrollbar.pack(side="right", fill="y")

result_text = tk.Text(scrollable_frame, wrap="none", yscrollcommand=scrollbar.set, state="disabled")
result_text.pack(fill="both", expand=True)

scrollbar.config(command=result_text.yview)

window.mainloop()
