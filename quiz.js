const questions = [
    { q: "What is 2+2 ?", a:"4", options: ["3","4","5"]},
    { q: "What is the captial of france ?", a:"Paris", options: ["London","Paris","Berlin"]},
    { q: "What is the colour of the sky ?", a:"Blue", options: ["Green","Red","Blue"]},
];

const questionEl = document.getElementById("question");
const optionsEl = document.getElementById("options");
const messageEl = document.getElementById("message");
const nextBtn = document.getElementById("nextBtn");
const scoreEl = document.getElementById("score");
const restartBtn = document.getElementById("restartBtn");


let score = 0;
scoreEl.textContent = `Score: ${score}`;
let usedIndexes = [];
let currentQuestion;


function pickQuestion() {

    // STOP when all questions are used
    if (usedIndexes.length === questions.length) {
        questionEl.textContent = "Quiz finished!";
        optionsEl.innerHTML = ""; // removes options
        messageEl.textContent = `Final Score: ${score} / ${questions.length}`;
        nextBtn.disabled = true;
        return ;
        }


    let index ;
    do {
        index = Math.floor(Math.random() * questions.length);
    } while (usedIndexes.includes(index));
    
    usedIndexes.push(index);
    currentQuestion = questions[index];

    questionEl.textContent = currentQuestion.q;
    messageEl.textContent = ""
    optionsEl.innerHTML = ""

    const answers = [...currentQuestion.options];


    for (let i = answers.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [answers[i], answers[j]] = [answers[j],answers[i]];
    }

    answers.forEach( answer => {
        const btn = document.createElement("button");
        btn.textContent = answer;
        btn.addEventListener("click", () => checkAnswer(answer, btn));
        optionsEl.appendChild(btn);
    });
}


function checkAnswer(answer, clickedBtn) {
  const buttons = optionsEl.querySelectorAll("button");

  // disable all buttons
  buttons.forEach(btn => btn.disabled = true);

  if (answer === currentQuestion.a) {
    score++;
    scoreEl.textContent = `Score: ${score}`;
    messageEl.textContent = "Correct!";
    clickedBtn.classList.add("correct");
  } else {
    clickedBtn.classList.add("wrong");
    messageEl.textContent = `Wrong! The answer was ${currentQuestion.a}`;
  }
}


function restartQuiz() {
    score = 0;
    usedIndexes = [];
    nextBtn.disabled = false;

    scoreEl.textContent = `Score: ${score}`;
    messageEl.textContent = "";

    pickQuestion();
}
nextBtn.addEventListener("click",pickQuestion);
restartBtn.addEventListener("click", restartQuiz);

// start first question
pickQuestion();
scoreEl.textContent = `Score: ${score}`;
