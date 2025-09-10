class WordGame{
    constructor(config){
        this.config = config;
        this.maxGuesses = config.maxGuesses || 6;
        this.currentGuess = 0;
        this.winStreak = 0;
        this.answer = "";
        this.allowedWords = [];
        this.possibleAnswers = [];
        this.isQwertyLayout = true;
        this.previousButtonStates = {};

        this.soundFiles = {
            pop: "pop.wav",
            hint: "hint.wav",
            win: "win.wav",
            lose: "lose.wav",
            submit: "submit.wav",
            correct: "correct.wav",
            correctish: "correctish.wav",
            incorrect: "incorrect.wav"
        }

        this.sounds = {};
        this.preloadSounds();

        this.gameBoard = document.getElementById("game-board");
        this.guessHistory = document.getElementById("guess-history");
        this.guessField = document.getElementById("guess-field");
        this.submitGuessButton = document.getElementById("submit-guess-button");
        this.clearButton = document.getElementById("clear-button");
        this.toggleLayoutButton = document.getElementById("toggle-layout-button");
        this.deleteButton = document.getElementById("delete-button");
        this.changeGuessesButton = document.getElementById("change-guesses-button");

        this.init();
    }

    async init(){
        await this.loadWordLists();
        this.createQwertyKeyboard();
        this.addEventListeners();
        this.initGuessRows();
    }

    async loadWordLists(){
        try{
            const allowedResponse = await fetch(`${this.config.resources}/allowed.txt`);
            const allowedText = await allowedResponse.text();
            this.allowedWords = allowedText.split('\n').map(w => w.trim().toUpperCase());

            const answerResponse = await fetch(`${this.config.resources}/wordlist.txt`);
            const answerText = await answerResponse.text();
            this.possibleAnswers = answerText.split('\n').map(w => w.trim().toUpperCase());

            this.answer = this.possibleAnswers[Math.floor(Math.random() * this.possibleAnswers.length)];
            this.submitGuessButton.disabled = false;
        } catch(err){
            console.error("Error loading word lists: ", err);
        }
    }

    preloadSounds(){
        for (let key in this.soundFiles){
            this.sounds[key] = new Audio(`${this.config.resources}/soundeffects/${this.soundFiles[key]}`);
        }
    }

    playSound(effect){
        if(this.sounds[effect]) {
            this.sounds[effect]. currentTime = 0;
            this.sounds[effect].play();
        }
    }

    createQwertyKeyboard() {
        const qwertyRows = [
            ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
            ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
            ["Z", "X", "C", "V", "B", "N", "M"]
        ];//Specified the rows each letter should be on. hopefully this fixes its appearance on mobile
        qwertyRows.forEach(rowLetters => {
            const rowDiv = document.createElement("div");
            rowDiv.classList.add("row");
            //rowDiv.style.flexWrap = "nowrap";
            //rowDiv.style.justifyContent = "center";
            //rowDiv.style.width = "100%";
            rowLetters.forEach(letter => {
                rowDiv.appendChild(this.createLetterButton(letter));
            });
            this.gameBoard.appendChild(rowDiv);
        });
    }

    createAZKeyboard() {
        const abcdefRows = [
            ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
            ["K", "L", "M", "N", "O", "P", "Q", "R", "S"],
            ["T", "U", "V", "W", "X", "Y", "Z"]
        ];//Specified the rows each letter should be on. hopefully this fixes its appearance on mobile
        abcdefRows.forEach(rowLetters => {
            const rowDiv = document.createElement("div");
            rowDiv.classList.add("row");
            //rowDiv.style.flexWrap = "nowrap";
            //rowDiv.style.justifyContent = "center";
            //rowDiv.style.width = "100%";
            rowLetters.forEach(letter => {
                rowDiv.appendChild(this.createLetterButton(letter));
            });
            this.gameBoard.appendChild(rowDiv);
        });
    }

    createLetterButton(letter) {
        const button = document.createElement("button");
        button.classList.add("letter-button");
        button.textContent = letter;
        button.onclick = () => {
            if (this.guessField.value.length < 5) {
                this.guessField.value += letter;
                this.playSound('pop');
            }
        };
        return button;
    }

    initGuessRows(){
        this.guessHistory.innerHTML = "";
        for (let i=0;i<this.maxGuesses;i++){
            const guessRow = document.createElement("div");
            guessRow.classList.add("guess-row");
            for(let j=0; j<5; j++){
                const letterSlot = document.createElement("span");
                letterSlot.classList.add("letter-slot");
                letterSlot.textContent = " ";
                guessRow.appendChild(letterSlot);
            }

            this.guessHistory.appendChild(guessRow);
        }
    }

    addEventListeners(){
        this.submitGuessButton.addEventListener("click", () => this.submitGuess());
        this.guessField.addEventListener("keydown", e => {
            if (e.key === "Enter") this.submitGuess();
        });
        this.clearButton.addEventListener("click", () => {
            this.guessField.value = "";
            this.playSound('pop');
        });
        this.deleteButton.addEventListener("click", () => {
            this.guessField.value = this.guessField.value.slice(0,-1);
            this.playSound('pop');
        });
    }

    submitGuess() {
        const guess = this.guessField.value.trim().toUpperCase();
        if (guess.length === 5) {
            if (!this.allowedWords.includes(guess) && !this.possibleAnswers.includes(guess)) {
                this.playSound('hint');
                alert("This is not a valid word.");
                return;
            }

            //update the guess history row
            const guessRow = this.guessHistory.children[this.currentGuess];
            for (let i = 0; i < 5; i++) {
                const letterSlot = guessRow.children[i];
                //set a delay for each letter to reveal in sequence
                setTimeout(() => {
                    letterSlot.textContent = guess[i];
                    letterSlot.classList.add("animate");
                    setTimeout(() => {
                        letterSlot.classList.remove("animate");
                    }, 500);
                    
                    if (guess[i] === this.answer[i]) {
                        letterSlot.style.backgroundColor = "green";
                        this.updateLetterBoard(guess[i], "green");
                        this.playSound('correct');
                    } else if (this.answer.includes(guess[i])) {
                        letterSlot.style.backgroundColor = "yellow";
                        this.updateLetterBoard(guess[i], "yellow");
                        this.playSound('correctish');
                    } else {
                        letterSlot.style.backgroundColor = "red";
                        this.updateLetterBoard(guess[i], "red");
                        this.playSound('incorrect');
                    }
                }, i * 300); //delay of 300ms between each letter reveal
            }
            this.currentGuess++;
            this.playSound('submit');
            this.guessField.value = "";
                    //check if the player has won or lost after all animations have played
            setTimeout(() => {
                if (guess === this.answer) {
                    this.winStreak++;
                    //update the win streak display regardless of the count
                    if (this.winStreak >= 3) {
                        document.getElementById('winstreak-display').innerHTML = `🔥 You're on a ${this.winStreak} word streak! 🔥`;
                    }
                    confetti({
                        particleCount: 100,      //number of confetti particles
                        spread: 70,              //spread of the confetti
                        origin: { y: 0.6 }       //position where the confetti starts
                    });
                    setTimeout(() => {
                        this.playSound('win');
                        alert("Congrats! You guessed " + this.answer + "!");
                        document.getElementById('winstreak-display').innerHTML = "";
                        this.resetGame();
                    }, 100); //slight delay before showing the alert
                } else if (this.currentGuess >= this.maxGuesses) {
                    this.winStreak = 0;
                    setTimeout(() => {
                        this.playSound('lose');
                        alert("Game Over! The correct word was: " + this.answer + ". Better luck next time!");
                        document.getElementById('winstreak-display').innerHTML = "";
                        this.resetGame();
                    }, 100); //slight delay before showing the alert
                }
            }, 1700); //total delay to ensure all animations finish (4 letters * 300ms + 500ms for last animation)
        } else {
            alert("Please enter a 5-letter word.");
            this.playSound('hint');
        }
    }

    updateLetterBoard(letter, color) {
        const buttons = document.getElementsByClassName("letter-button");
        for (let button of buttons) {
            if (button.textContent === letter) {
                if (color === "red") {
                    button.style.backgroundColor = color;
                } else if (color === "green" || (button.style.backgroundColor !== "green" && button.style.backgroundColor !== "red")) {
                    button.style.backgroundColor = color;
                }
            }
        }
    }

    resetGame() {
        this.currentGuess = 0;
        this.initGuessRows();
        this.guessField.value = "";

        const buttons = document.getElementsByClassName("letter-button");
        for (let button of buttons) {
            button.style.backgroundColor = this.config.defaultButtonColor || "#ccc";
        }

        this.answer = this.possibleAnswers[Math.floor(Math.random() * this.possibleAnswers.length)];
    }

}