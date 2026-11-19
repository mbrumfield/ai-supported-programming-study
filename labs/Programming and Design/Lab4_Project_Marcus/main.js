const calculateBtn = document.getElementById("calculateBtn");
const resetBtn = document.getElementById("resetBtn");
const saveBtn = document.getElementById("saveBtn");

let currentData = null;

function validateInputs() {
    let valid = true;

    const course = document.getElementById("course");
    const courseError = document.getElementById("courseError");

    courseError.textContent = "";

    if (course.value === "") {
        courseError.textContent =
            "Please select a course.";
        valid = false;
    }

    const scoreInputs =
        document.querySelectorAll("#scores input");

    let validScores = 0;

    scoreInputs.forEach(input => {

        const errorSpan =
            input.nextElementSibling;

        errorSpan.textContent = "";
        input.classList.remove("invalid");

        if (input.value.trim() === "") {
            return;
        }

        const value = Number(input.value);

        if (isNaN(value) ||
            value < 0 ||
            value > 100) {

            input.classList.add("invalid");

            errorSpan.textContent =
                "Enter a value from 0-100.";

            valid = false;
        } else {
            validScores++;
        }
    });

    if (validScores === 0) {
        alert("Enter at least one valid score.");
        valid = false;
    }

    return valid;
}

function determineLetterGrade(avg) {

    if (avg >= 90) return "A";
    if (avg >= 80) return "B";
    if (avg >= 70) return "C";
    if (avg >= 60) return "D";

    return "F";
}

calculateBtn.addEventListener("click", () => {

    if (!validateInputs()) {
        return;
    }

    const course =
        document.getElementById("course").value;

    const scoreInputs =
        document.querySelectorAll("#scores input");

    const scores = [];

    scoreInputs.forEach(input => {
        if (input.value.trim() !== "") {
            scores.push(Number(input.value));
        }
    });

    const total =
        scores.reduce((sum, score) =>
            sum + score, 0);

    const average =
        Number((total / scores.length).toFixed(2));

    const grade =
        determineLetterGrade(average);

    document.getElementById(
        "displayCourse").textContent = course;

    document.getElementById(
        "displayAverage").textContent = average.toFixed(2);

    document.getElementById(
        "displayGrade").textContent = grade;

    currentData = {
        course,
        scores,
        average,
        grade
    };
});

resetBtn.addEventListener("click", () => {

    document.getElementById("course").value = "";

    document.querySelectorAll("input")
        .forEach(input => {
            input.value = "";
            input.classList.remove("invalid");
        });

    document.querySelectorAll(".error")
        .forEach(error => {
            error.textContent = "";
        });

    document.getElementById(
        "displayCourse").textContent = "-";

    document.getElementById(
        "displayAverage").textContent = "-";

    document.getElementById(
        "displayGrade").textContent = "-";

    currentData = null;
});

saveBtn.addEventListener("click", () => {

    if (!currentData) {
        alert(
            "Calculate the average before saving."
        );
        return;
    }

    const today =
        new Date().toISOString().split("T")[0];

    const courseName =
        currentData.course
            .split(" - ")[0]
            .replaceAll(" ", "");

    const fileName =
        `${today}_${courseName}.csv`;

    const row = [
        currentData.course,
        currentData.scores[0] ?? "",
        currentData.scores[1] ?? "",
        currentData.scores[2] ?? "",
        currentData.scores[3] ?? "",
        currentData.scores[4] ?? "",
        currentData.average,
        currentData.grade
    ];

    const csv =
`Course Name,Score 1,Score 2,Score 3,Score 4,Score 5,Average,Letter Grade
${row.join(",")}`;

    const blob =
        new Blob([csv], { type: "text/csv" });

    const url =
        URL.createObjectURL(blob);

    const link =
        document.createElement("a");

    link.href = url;
    link.download = fileName;

    document.body.appendChild(link);
    link.click();

    document.body.removeChild(link);

    URL.revokeObjectURL(url);
});