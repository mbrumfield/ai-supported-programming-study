import csv
from datetime import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class CourseAverageCalculator:

    def __init__(self, root):
        self.root = root
        self.root.title("Course Average Calculator")
        self.root.geometry("600x550")

        self.course_var = tk.StringVar()
        self.score_vars = [tk.StringVar() for _ in range(5)]

        self.average = None
        self.grade = None

        self.create_widgets()

    def create_widgets(self):

        title = tk.Label(
            self.root,
            text="Course Average Calculator",
            font=("Arial", 16, "bold")
        )
        title.pack(pady=10)

        # Course Selection
        course_frame = tk.Frame(self.root)
        course_frame.pack(fill="x", padx=20, pady=10)

        tk.Label(
            course_frame,
            text="Course:"
        ).pack(anchor="w")

        self.course_dropdown = ttk.Combobox(
            course_frame,
            textvariable=self.course_var,
            state="readonly"
        )

        self.course_dropdown["values"] = (
            "CSC 221 - Fundamental Programming I",
            "MAT 131 - College Algebra",
            "BIO 111 - General Biology"
        )

        self.course_dropdown.pack(fill="x")
        self.course_dropdown.set("Select a Course")

        # Score Inputs
        self.score_entries = []

        scores_frame = tk.Frame(self.root)
        scores_frame.pack(fill="x", padx=20)

        for i in range(5):

            row = tk.Frame(scores_frame)
            row.pack(fill="x", pady=5)

            tk.Label(
                row,
                text=f"Score {i + 1}:",
                width=10
            ).pack(side="left")

            entry = tk.Entry(
                row,
                textvariable=self.score_vars[i]
            )

            entry.pack(
                side="left",
                fill="x",
                expand=True
            )

            self.score_entries.append(entry)

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)

        tk.Button(
            button_frame,
            text="Calculate Average",
            command=self.calculate_average
        ).pack(side="left", padx=5)

        tk.Button(
            button_frame,
            text="Reset",
            command=self.reset_form
        ).pack(side="left", padx=5)

        tk.Button(
            button_frame,
            text="Save To CSV",
            command=self.save_to_csv
        ).pack(side="left", padx=5)

        # Results
        result_frame = tk.LabelFrame(
            self.root,
            text="Results"
        )

        result_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        self.course_result = tk.Label(
            result_frame,
            text="Course: -"
        )
        self.course_result.pack(anchor="w", padx=10, pady=5)

        self.average_result = tk.Label(
            result_frame,
            text="Average: -"
        )
        self.average_result.pack(anchor="w", padx=10, pady=5)

        self.grade_result = tk.Label(
            result_frame,
            text="Letter Grade: -"
        )
        self.grade_result.pack(anchor="w", padx=10, pady=5)

    def validate_inputs(self):

        course = self.course_var.get()

        if course == "Select a Course":
            messagebox.showerror(
                "Validation Error",
                "Please select a course."
            )
            return None

        scores = []

        for i, score_var in enumerate(self.score_vars):

            value = score_var.get().strip()

            if value == "":
                continue

            try:
                score = float(value)

            except ValueError:
                messagebox.showerror(
                    "Validation Error",
                    f"Score {i + 1} must be numeric."
                )
                return None

            if score < 0 or score > 100:
                messagebox.showerror(
                    "Validation Error",
                    f"Score {i + 1} must be between 0 and 100."
                )
                return None

            scores.append(score)

        if len(scores) == 0:
            messagebox.showerror(
                "Validation Error",
                "Enter at least one valid score."
            )
            return None

        return scores

    def determine_letter_grade(self, average):

        if average >= 90:
            return "A"

        if average >= 80:
            return "B"

        if average >= 70:
            return "C"

        if average >= 60:
            return "D"

        return "F"

    def calculate_average(self):

        scores = self.validate_inputs()

        if scores is None:
            return

        self.average = round(sum(scores) / len(scores), 2)

        self.grade = self.determine_letter_grade(
            self.average
        )

        self.course_result.config(
            text=f"Course: {self.course_var.get()}"
        )

        self.average_result.config(
            text=f"Average: {self.average:.2f}"
        )

        self.grade_result.config(
            text=f"Letter Grade: {self.grade}"
        )

    def save_to_csv(self):

        if self.average is None:
            messagebox.showwarning(
                "Save Error",
                "Calculate the average first."
            )
            return

        today = datetime.now().strftime(
            "%Y-%m-%d"
        )

        course_code = (
            self.course_var.get()
            .split(" - ")[0]
            .replace(" ", "")
        )

        filename = (
            f"{today}_{course_code}.csv"
        )

        row = [self.course_var.get()]

        for score_var in self.score_vars:
            row.append(score_var.get())

        row.extend([
            f"{self.average:.2f}",
            self.grade
        ])

        with open(
            filename,
            "w",
            newline=""
        ) as csvfile:

            writer = csv.writer(csvfile)

            writer.writerow([
                "Course Name",
                "Score 1",
                "Score 2",
                "Score 3",
                "Score 4",
                "Score 5",
                "Average",
                "Letter Grade"
            ])

            writer.writerow(row)

        messagebox.showinfo(
            "Success",
            f"File saved:\n{filename}"
        )

    def reset_form(self):

        self.course_dropdown.set(
            "Select a Course"
        )

        for score_var in self.score_vars:
            score_var.set("")

        self.average = None
        self.grade = None

        self.course_result.config(
            text="Course: -"
        )

        self.average_result.config(
            text="Average: -"
        )

        self.grade_result.config(
            text="Letter Grade: -"
        )


def main():

    root = tk.Tk()

    app = CourseAverageCalculator(root)

    root.mainloop()


if __name__ == "__main__":
    main()