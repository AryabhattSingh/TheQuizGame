# The Quiz Game

Welcome to **The Quiz Game**, a console-based project that tests your knowledge with a series of true or false questions. This game is designed to provide you with an interactive and fun quiz experience. Before we dive into the game, let's understand how it works.

## Features

- **ASCII Art**: The game starts with some cool ASCII art to set the mood.

- **Instructions**: Clear instructions are displayed to guide you on how to answer the questions.

- **Question Display**: Each question is displayed, and you are prompted to enter either "true" or "false" as your answer.

- **Correct Answers**: If your answer is correct, you'll receive a congratulatory message along with the right answer on the screen, and your score will increase.

- **Incorrect Answers**: If your answer is wrong, you'll receive an informative message along with the correct answer. In this case, your score remains unchanged.

- **Score Tracking**: The game keeps track of your score and the number of questions displayed as you progress.

- **Final Score**: When all the questions have been displayed, the program will show your final score.

## Data Storage

All the questions, along with their answers, are stored in the `data.py` file. This file contains a list with multiple dictionaries as its elements. Each dictionary represents a question with two key-value pairs: "text," which contains the question text, and "answer," which contains the correct answer.

## Code Structure

- **Question Model**: The `question_model.py` file defines a "Question" class, which outlines the structure and attributes of a question, including "text" and "answer."

- **QuizBrain Class**: The `QuizBrain` class outlines the structure of the quiz object, which contains multiple Question objects. The program iterates over these objects to display questions and update the score according to your answers.

- **Input Validation**: Input validation has been implemented to ensure that non-valid entries do not crash the program, providing a smooth and error-free experience.

## Getting Started

To start playing The Quiz Game, simply run the program. You'll be presented with a series of true or false questions, and your goal is to answer them correctly to increase your score. Enjoy the quiz and challenge yourself to achieve the highest score possible!

Have fun and test your knowledge with The Quiz Game!
