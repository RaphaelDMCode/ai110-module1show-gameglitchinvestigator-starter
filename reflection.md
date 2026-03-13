# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

When I first loaded up the Game, the Side Panel shows that I was in the Normal Difficulty, and that the Attempts I'm allowed are 8. In the Game Panel, it shows that I have to guess a number between 1 and 100, and that the Attempts I had left are 7. I also noticed that the "Show hints" was toggled True, and that the Developer Debug Info is accessible which shouldn't be. When I tested the game, I noticed that the Hints were telling the Opposite, where my secret number was 6, and I typed in 54, the Hint told me to go higher instead of lower. I also noticed that once I guessed the correct secret number and tried to start a new game, it won't let me submit another guess, nor the attempts I had did not increase nor decrease.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used both ChatGPT, for asking simple questions about the clarifications regarding the steps, and Claude for fixing the Bugs and Core Logics of the Program. An example of where the suggestion was correct when I asked Claude to fix the opposite Hint popping out. I verified it when if my Guess was higher than the Secret, it shows "Lower". An example of where the suggestion was incorrect was when I asked Claude to fix the part where submitting the guess does not register the attempt. When submitting a guess, the attempt is registered where you can see the attempts you have left. Once I confirmed it decreases every guess, except for not an empty input, the Bug was fixed.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

Testing whether a Bug was fixed or not, I tested the app manually and input a guess and see whether or not the bug was fixed or not. One such test was the High/Low Bug. When I first thought I fixed it, it showed that the Hint was alternating between High and Low so I used Claude to fixed the pronlem. Nevertheless, mostly about ChatGPT AI helped me understand the function of the codes. Most of the times, the Git Bash Commands for Claude is difficult to understand.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The reason why the Secret Number kept changing is due to the function random.randint that ranges from the lowest to the highest set range. Regarding Streamlit, it basically is the thing that updates the app as someone is making changes from the code. Session States is where data stored like the guesses one made. A change I made for the secret number to be stable is how I make it sure it stays withing the range depending on the difficulty ranges so that the secret number matches the difficulty.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

A strategy I would want to reuse is testing the app first, finding bugs, then noting them out. After asking Claude to fix them, I would then test whether the bug is fixed, then repeat. At first, I thought that this course was about creating AIs, but after this project, I learned how AI is very helpful of creating codes but also put worries me how AI would replace many jobs. Nevertheless, sometimes the AI generated code can be confusing to understand, some AI chatbots provide different results and understanding.