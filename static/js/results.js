document.addEventListener("DOMContentLoaded", function() {
    const predictionText = document.getElementById("prediction-text");
    const outcomeCard = document.getElementById("outcome-card");
    const outcome = predictionText.textContent.trim().toLowerCase();

    const survivesSound = document.getElementById("survives-sound");
    const diesSound = document.getElementById("dies-sound");

    // Change card background color and play sound based on outcome
    if (outcome.includes("survives")) {
        outcomeCard.classList.add("survive-card");
        survivesSound.play();
    } else if (outcome.includes("dead")) {
        outcomeCard.classList.add("die-card");
        diesSound.play();
    }
});
