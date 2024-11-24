# **Word Safari** :tiger:
Word Safari is a fun and interactive word-guessing game designed for educational purposes! It challenges players to guess a hidden five-letter word in five attempts, providing feedback on each guess to help players refine their word-solving skills.

It is intended to be used on desktop, but can work on mobile with varying results. Its initial use-case was to be used on a Smart Board.

- [Features](#features-memo) 
- [How to Play](#how-to-play-video_game)
- [Getting Started](#getting-started-rocket)
- [Educational Purpose](#educational-purpose-books)
- [Technologies Used](#technologies-used-test_tube)
- [Future Plans](#future-plans-hourglass)
- [Disclaimer](#disclaimer-heavy_exclamation_mark)
- [License](#license-scroll)

# **Features** :memo:
- Educational Focus: The game uses a curated list of common words suitable for young learners.
- Interactive Keyboard: Includes an on-screen keyboard with QWERTY and A-Z layout options for accessibility.
- Color-Coded Feedback: Helps players learn letter positions and refine their guesses.
- Sound Effects: Fun audio cues to make gameplay more engaging.
- Non-Commercial Purpose: This project is for educational use only.

# **How to Play** :video_game:
- You have ***5 chances*** to guess the secret 5-letter word.
- After each guess:
    - Letters in the correct spot are marked green (Note, there can be repeat letters)
    - Letters in the word, but in the wrong location are marked yellow
    - Letters not in the word are marked red (Note, they can still be used)
- Use the feedback given to make your next guess and try to solve the word!

# **Getting Started** :rocket:
### *Option 1 (Playing via the Web)* :globe_with_meridians:
- Simply go to the [GitHub page](https://jasonburas.github.io/WordSafari/) for Word Safari.

### *Option 2 (Clone the repo and play locally)* :house:
> For a full tutorial on cloning repos, please visit the [official GitHub "Cloning a repository" guide.(https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
- *Clone the Repository*
    > Navigate to the directory you'd like to clone the repo to and paste:
    >    ```bash
    >   git clone https://github.com/jasonBuras/WordSafari.git
    >    ```
    > into the terminal.

- Open `./docs/index.html` using a web browser (Firefox, Chrome, Edge, etc.)
    - This will open the webpage locally (no internet connection required)

### *Option 3 (Download the raw files)* :file_folder:
- If you don't feel like creating a GitHub account and setting up GitBash, simply [Download the repo as a zip file](https://github.com/jasonBuras/WordSafari/archive/refs/heads/main.zip)
    - You can click the hyperlink provided or: 
        1. Go to https://github.com/jasonBuras/WordSafari
        2. Click `<> Code v`
        3. Click "Download ZIP"
        4. Extract at your desired location.
    - Open `./docs/index.html` using a web browser (Firefox, Chrome, Edge, etc.)
        - This will open the webpage locally (no internet connection required)

### *Langniappe (Mod the game)* :cookie:
> If you mess around with the source code, please feel free to share what you've come up with. See [Future Plans](#future-plans)
- If you have the raw files, you have the ability to start messing around with the word lists.
    - Navigate to `./resources/wordlist.txt`
        - Add/remove possible answers :book:
    - `./resources/soundeffects/`
        - Change sound effects :musical_note:
    
# **Educational Purpose** :books:
- Word Safari is designed with the following educational goals in mind:
    - Vocabulary Building: Introduces children to new words in a fun, interactive way.
    - Logical Thinking: Encourages deductive reasoning based on feedback.
    - Keyboard Familiarity: Helps players familiarize themselves with the QWERTY and alphabetical layouts.
    - Confidence in Language Skills: Positive reinforcement through engaging audio and visual feedback.

# **Technologies Used** :test_tube:
- HTML: For structuring the game and creating the user interface.
- CSS: For styling the game.
- JavaScript: For game logic, interactivity, and handling user inputs.

# **Future Plans** :hourglass:
- Dynamic word lengths
    - Current format is 1 guess/letter, so there would be dynamic guess counts
- Allow users to import their own .txt files for a list of possible answers.
    - This is already technically implemented, but requires you to clone/download the repo in order to edit the files.
    - This may require hosting a server/database and having an account system to store the wordlists per user.
    - This would work with Dynamic Word lengths to allow instructors to curate wordlists relevant to their current lesson plans.
- Make the game more mobile friendly
    - It *technically* works on mobile currently, but isn't exactly a great experience.

# **Disclaimer** :heavy_exclamation_mark:
> [!IMPORTANT]
> Word Safari is an original creation for educational purposes. While inspired by games like Wordle, all code, word lists, and design elements are unique to this project. This game is not affiliated with, endorsed by, or sponsored by Wordle or its creators.

# **License** :scroll:
> [!NOTE] 
> This project is licensed under the [MIT License](https://mit-license.org). Feel free to use and modify the code for educational and non-commercial purposes.