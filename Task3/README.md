# CODEWAY
## Password Generator

### Overview
This Python script serves as a versatile password generator that allows users to create strong and secure passwords based on their preferences. The script prompts the user to choose the length of the password and select character sets, such as digits, letters, and special characters, to be included in the generated password.

### Features
1. **Customizable Passwords:** Users can specify the length of the password and choose character sets according to their security requirements.
   
2. **Randomization:** The script uses the `random` module to ensure that each password generated is unique and unpredictable.

3. **Character Sets:**
    - Digits: `0123456789`
    - Letters: `abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`
    - Special Characters: `@#$!^&:?.|~*`

4. **Interactive User Interface:** The script provides an interactive command-line interface where users can easily navigate and input their preferences.

5. **Validation:** The script includes input validation to ensure that users provide valid input, preventing unexpected errors.

### How to Use
1. **Run the Script:**
    - Execute the script by running the `password_generator.py` file.

2. **User Interaction:**
    - Respond to prompts asking whether to generate a password.
    - Specify the desired password length and choose character sets.

3. **Generated Password:**
    - A secure password is generated based on the user's preferences and displayed.

4. **Exit:**
    - Users can exit the script at any time by entering 'N/n' when prompted.

### Integrated Libraries and Algorithms
- **Random Module:** Utilized for selecting random characters and shuffling the characters in the generated password.
  
- **String Module:** Used for accessing pre-defined character sets for digits, letters, and special characters.

- **Array Module:** Employed to convert and shuffle the temporary password as an array.

### IDE and API
- **IDE:** The code was developed using a Python-friendly Integrated Development Environment (IDE), Spyder.

- **APIs:** The script relies on the standard Python libraries, making it easily portable and runnable on any system with Python installed.

### License
This script is open-source and available under the [MIT License](LICENSE.md).
Feel free to contribute, report issues, or suggest improvements!
