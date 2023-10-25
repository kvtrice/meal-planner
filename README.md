# Meal Planner Terminal App

## Links
* [Github Repository](https://github.com/kvtrice/meal-planner)
* [Slide Deck](https://www.canva.com/design/DAFyJ9mJGM8/k-JMQ6WurNEl9qWDLk6k7g/view?utm_content=DAFyJ9mJGM8&utm_campaign=designshare&utm_medium=link&utm_source=editor)
* [Development Plan (Linear)](https://linear.app/kats-workspace/join/88596d7e69b639b4a651783417b35e23?s=4)
* [Code Style Guide (Pep8)](https://peps.python.org/pep-0008/#documentation-strings)

# Table of Contents
* [Purpose and Overview](#purpose-and-overview)
* [Features](#features)
* [Development Plan](#development-plan)
* [Installation and Help Docs](#help-and-installation-instructions)
* [References](#references)

## 📖 Purpose and Overview
Meal Planner is a terminal application that helps make meal planning easy. As a user, you're able to define what your daily calorie target is (e.g. 1800 calories) and from there the program will randomly generate a meal plan that's within an acceptable range to the target the user has set. 

The meal plan will consist of 5 meals (Breakfast, Lunch, Dinner and 2 snacks) and the meals are chosen from a CSV list of recipes, that the user is able to both view and add to.

This application has allowed me to demonstrate my ability to effectively accept user input and interact with file systems, alongside the broader ability to design and implement a commandline application complete with the utilisation of multiple pakages and unit testing.

## ✨ Features
There are a number of key features of my application, with each outlined at a high level below:

### 1. Add a new recipe

The user is able to add a new recipe to the recipe list in two ways:
* Via the user menu within the application
* Via a command line script outside of the application

In each case, the user is required to enter the recipe `title`, the `ingredients` and the `calories` (for 1 serving). Once provided, the application appends this new entry to the existing CSV file of recipes (which comes pre-loaded with over 200 recipes).

### 2. Choose how many days the user wants a meal plan for

Initially I began implementing the ability to create a meal plan for a single day. Once this was working successfully I then created a secondary option, re-using much of the functionality from the single day option, to then enable the user the ability to choose a custom number of days to create meal plans for (e.g. for 5 days). This is improved upon from my initial idea of creating a _weekly_ meal plan - where I ran into concerns around what happens if a user doesn't need the full 7 days (such as if they have dinner plans one night). So landed on a custom option that was much more versatile. 

This also led me to the realisation that using the custom number of days also actually covers the use case of a single meal plan, as the user can simply choose to create a meal plan for 1 day. This led to a refactor that removed the single day option and improved upon the functionality of the custom number of days option. 

### 3. Generate (and optionally regenerate) a meal plan

The core functionality of this application is in generating a meal plan for the user. At the beginning of the user journey, the user is prompted to provide a calorie target for each day (e.g. 1800 calories). Once this is entered, the application will take that target number and based on some pre-defined ranges, will determine roughly what the calories for each meal should be in order to hit close to the users calorie target.

As an example, if the users goal is 1800 calories, then given there will be 5 meals provided to the user for the day, I wanted to have a rough range of calories as a guide for each meal, such as:

```
If calorie target is between 1701 - 2000 then:

Meal 1 (Breakfast): 400 Calories
Meal 2 (Lunch): 400 Calories
Meal 3 (Dinner): 600 Calories
Meal 4 (Snack 1): 300 Calories
Meal 5 (Snack 2): 200 Calories
```

For each range I allowed a variation of `+- 75` each side

The program then iterates through the recipe csv, searching for meals that adequately fill the calorie target defined; shuffling the recipe list each time and removing it so that the options are randomised and the user doesn't get duplicate meals.

Finally, at the end of each day the calories for each meal are summed together and the total is compared to the calorie target that the user set - if it's within `+-100` of the target; then the meal is considered complete for that day. Otherwise, the loop repeats until a meal plan within an acceptable range is created.

Additionally, once the user is shown their meal plan, they're given the option to manually regenerate it if they want to (e.g. if they don't like the meals). They can also optionally choose to change their calorie target upon regeneration or keep the orginal target they set.


### 4. Save a meal plan

Finally, once the user is happy with their plan, the plan is displayed to them on screen, complete with numbered days and semantic meal names. Once the user is happy with their meal they can save it, and upon doing so they are prompted to enter a `filename`. The meal plan is then saved to a file with this filename in the source directory for access later. The data & time of the meal plan is included so if multiple meal plans are savevd, the user can distinguish between them.

## 📋 Help and Installation Instructions
These steps are for MacOS, steps may differ for Windows and other operating systems.
It is also assumed that Python 3.11 or higher is already installed on your PC. Alternatively, for instructions on how to do that [head over here](https://wiki.python.org/moin/BeginnersGuide/Download).

### Steps to install the application
#### 1. Clone the application

Within your terminal, navigate to the folder where you would like to save the program. For example:

```bash
cd projects/python
```

Once inside the directory where you would like the program to be stored, clone the application using the following command:

```bash
git clone https://github.com/kvtrice/meal-planner.git
```

#### 2. Run the executable file
Once the application has been cloned, navigate into the application directory by using the following:

```bash
cd meal-planner
```

Finally, copy and run the script below, this will automatically create and activate a virtual python environment for you, install all dependencies and run the python file:

```bash
./setup.sh
```
---

### How to use the application

#### 1. Add a new recipe via the terminal
To add a new recipe to the application from the commandline, enter into the folder where the application is located, for example:

```bash
cd projects/python/meal-planner
```

Run the following command, replacing the `title`, `ingredients` and `calories` with your own recipes details.

All recipes added assume a serving size of 1. Both the title and the ingredients are *strings*, calories is an *integer*

```python
python3 main.py --title "Spaghetti Bolognese" --ingredients "2 Tomatoes, 500g Beef Mince, Spaghetti" --calories 540
```

#### 2. Add a new recipe within the application

To add a new recipe from the application, if not already done so, navigate to the project source directory, e.g:

```bash
cd projects/python/meal-planner
```

Run the following script to start the application 
(Note: In this step it is assumed all dependencies have been installed, if not please refer to [cloning the application](#1-clone-the-application)):

```bash
./run.sh
```

From the user menu, simply enter the letter `a` to add a new recipe, and follow the prompts


#### 3. View all recipes (printed to screen)

* With the application running, to view all recipes simply enter the letter `v` to have all recipes printed to the screen (Note: This might be a long list!)

#### 4. Start a new meal plan

* With the application running, enter the letter `n` to start a new meal plan. 
* When prompted, enter in the number of days you would like a meal plan for (an integer between 1 and 14)
* When prompted, enter in your daily calorie target (an integer between 1400 and 3000)
* Review the meal plans presented to you on screen
    * If you'd like to regenerate the meal plans, hit `n` and follow the prompts
    * If you'd like to save the meal plan, hit `s` and follow the prompts

* Once your meal plan is saved, you can access your meal plan directly file from the source directory, for example:

```bash
cd projects/python/meal-planner/your-file.txt
```

Or alternatively, in terminal navigate to the source directory of the project, for example: 

```bash
cd projects/python/meal-planner
```

Run following script which will prompt you for the name of your saved file:

```bash
./open.sh
```
Enter the exact name of your file (must be an exact match), including the .txt extension:

![open_file_bash](/docs/help_docs/bash_open_script.jpg)

Your saved meal plan will automatically open in the default program (e.g. TextEdit on Mac):

![example_meal_plan](/docs/help_docs/saved_meal_plan_example.jpg)



### System and Hardware Requirements
The following minimum hardware requirements are required to run the application (equivalent to the minimum hardware requirements for running Python)
* MacOS 10.11 or later
* Miniumum 4GB RAM (but 8-16GB is highly recommended)
* x86 64-bit CPU
* Minimum 5GB free disk space

### Dependencies
As also found in requirements.txt
```
beautifulsoup4==4.12.2
certifi==2023.7.22
charset-normalizer==3.3.0
extruct==0.16.0
html-text==0.5.2
html5lib==1.1
idna==3.4
iniconfig==2.0.0
isodate==0.6.1
jstyleson==0.0.2
lxml==4.9.3
mf2py==1.1.3
packaging==23.2
pluggy==1.3.0
pyparsing==3.1.1
pyRdfa3==3.5.3
pytest==7.4.2
rdflib==7.0.0
requests==2.31.0
six==1.16.0
soupsieve==2.5
urllib3==2.0.7
w3lib==2.1.2
webencodings==0.5.1
```

## 💻 Development Plan

### Prioritisation Approach

[Link to development plan (Linear)](https://linear.app/kats-workspace/join/88596d7e69b639b4a651783417b35e23?s=4)

I started out by getting all my ideas for the application out on the development board. I realised quickly that I had more ideas that what would likely be feasible in the amount of time I had so I prioritised things baed on what was a must-have, or `MVP` vs. what was a `nice-to-have` (if time permits).

MVP features were features that were critical to the core functionality of my application (creating a meal plan, adding a recipe), where as the nice-to-have's were features that whilst they could potentially enhance the user experience, they wouldn't utlimately make or break the experience. Each ticket was also estimated using t-shirt sizing (S, M, L etc.), and based on this I was able to prioritize my time and attention.

I also labelled each card with the title of the feature that it was related to, and built out sub-issues under each main issue to outline the steps required in order to implement it - at least, my best attempt at what I thought was the best solution at the time... many of my initial approaches changed or were tweaked as I built out the project and learnt more and more.

Ultimately, a few `nice-to-have` features were cancelled based on their priority. Given more time, these would be great enhancements to build onto the applications functionality in the future. The overview of these can be seen below:

#### MVP Features
* Feature 1: Add a new recipe - `implemented`
    * Import pre-populated list of recipes - `implemented`
    * View recipe list - `implemented`
* Feature 2: Create a meal plan based on users calorie target - `implemented`
* Feature 3: Create a meal plan for specified number of days - `implemented`
    * Ability to re-roll the meal plan - `implemented`

#### Nice-to-have Features
* Feature 4: Print meal plan to a CSV - `changed`
    * Requirement changed to instead print to a text file - `implemented`   
* Feature 5: Remove a recipe from the recipe list - `cancelled`
* Feature 6: Allow user to set dietary requirements for their meal plan - `cancelled`
* Feature 7: Allow user to set custom calories per meal - `cancelled`

### Guide to Linear Boards

![linear_overview](docs/development_plan/linear_overview.jpg)

**Day 1**

![day_1](docs/development_plan/day_1/day_1.jpg)
![add_recipes](docs/development_plan/day_1/add_recipes.jpg)
![calorie_ranges](docs/development_plan/day_1/calorie_ranges.jpg)
![new_recipe_user_input](docs/development_plan/day_1/new_recipe_user_input.jpg)

**Day 2**

![day_2](docs/development_plan/day_2/day_2.jpg)
![meal_plans](docs/development_plan/day_2/meal_plans.jpg)
![recipe_list](docs/development_plan/day_2/recipe_list.jpg)

**Day 3**

Day start:
![day_3_start](docs/development_plan/day_3/day_start/day_3_start.jpg)
![display_meals](docs/development_plan/day_3/day_start/display_meals.jpg)
![regenerate_meals](docs/development_plan/day_3/day_start/regenerate_meal_plan.jpg)
![user_entry](docs/development_plan/day_3/day_start/user_entry.jpg)

Day end:
![day_3_end](docs/development_plan/day_3/day_end/day_3_end.jpg)
![custom_num_days](docs/development_plan/day_3/day_end/custom_num_days.jpg)
![multi_regenerate](docs/development_plan/day_3/day_end/multi_regenerate.jpg)
![num_days_prompt](docs/development_plan/day_3/day_end/num_days_prompt.jpg)
![display_multi_meals](docs/development_plan/day_3/day_end/display_multi_meals.jpg)

**Day 4**

Day start:
![day_4_start](docs/development_plan/day_4/day_start/day_4_start.jpg)
![exceptions](docs/development_plan/day_4/day_start/exceptions.jpg)

Day mid:
![day_4_mid](docs/development_plan/day_4/day_start/day_4_mid.jpg)

Day end:
![day_4_end](docs/development_plan/day_4/day_end/day_4_end.jpg)
![recipes_bug](docs/development_plan/day_4/day_end/recipes_bug.jpg)

**Day 5**

![day_5](docs/development_plan/day_5/day_5.jpg)

**Final Day**

![final_day](docs/development_plan/day_6/final_day_board.jpg)

**Feature Checklists**

![new_recipe](docs/development_plan/feature_checklists/new_recipe.jpg)
![calorie_target](docs/development_plan/feature_checklists/calorie_target.jpg)
![multiple_days](docs/development_plan/feature_checklists/multiple_days.jpg)

## References

Apple Support. (n.d.). _Intro to Shell Scripts in Terminal on Mac._ [online] Available at: https://support.apple.com/en-au/guide/terminal/apd53500956-7c5b-496b-a362-2845f2aab4bc/mac.

Apple Support. (n.d.). _Make a File Executable in Terminal on Mac._ [online] Available at: https://support.apple.com/en-au/guide/terminal/apdd100908f-06b3-4e63-8a87-32e71241bab4/2.14/mac/14.0.

GeeksforGeeks. (2019). _Writing CSV files in Python._ [online] Available at: https://www.geeksforgeeks.org/writing-csv-files-in-python/.

March, J. (2020). _Enthought Python Minimum Hardware Requirements._ [online] Enthought Knowledge Base. Available at: https://support.enthought.com/hc/en-us/articles/204273874-Enthought-Python-Minimum-Hardware-Requirements.

Official Python Documentation. (n.d.). _Argparse Tutorial — Python 3.9.5 Documentation._ [online] Available at: https://docs.python.org/3/howto/argparse.html.

Official Python Documentation. (n.d.). _PEP 8 – Style Guide for Python Code | peps.python.org_. [online] Available at: https://peps.python.org/pep-0008/#documentation-strings.

Python Software Foundation (2020). _Csv — CSV File Reading and Writing — Python 3.8.1 Documentation._ [online] Python.org. Available at: https://docs.python.org/3/library/csv.html.

realpython.com. (n.d.). _Build Command-Line Interfaces With Python’s argparse – Real Python._ [online] Available at: https://realpython.com/command-line-interfaces-python-argparse/.
