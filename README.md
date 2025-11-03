# Numerical Methods CLI Calculator

Hey! This is a simple command-line calculator I built using Python. It's designed to handle some common numerical methods.

You can feed it data (like time vs. position), save your data sets, and then use it to figure things out like interpolation or differentiation. I originally built this for my **[Your Course Name Here, e.g., "Numerical Methods"]** class project.

## 📸 What it Looks Like (Demo)

*(Seriously, swap these placeholder images with your own screenshots! Show off your menu and the cool graphs it makes.)*

**The Main Menu:**
![Main Menu Screenshot](https://via.placeholder.com/600x300.png?text=REPLACE+ME:+Your+Main+Menu+Screenshot)

**Sample Calculation & Plot:**
![Sample Output and Graph](https://via.placeholder.com/600x300.png?text=REPLACE+ME:+Your+Calculation+Output+or+Graph)

## 🚀 Key Features

* **Lagrange Interpolation:** Finds the estimated **Position** at any given time `t`.
* **Numerical Differentiation:** Calculates the estimated **Velocity** (1st derivative) and **Acceleration** (2nd derivative) using the Central Difference method.
* **Data Management:**
    * You can save up to 5 different data sets in "slots".
    * It automatically saves your data to `data_simpan.csv` and loads it back up when you start the app.
* **Export & Plotting:**
    * Whip up a quick graph of your data using `matplotlib` and save it as a PNG.
    * Save your calculation results to a clean `.txt` file.

## 💻 Tech Stack

* **Python 3**
* **Numpy:** For all the heavy-duty math and array stuff.
* **Matplotlib:** For plotting those sweet, sweet graphs.

## 🚀 How to Get it Running

1.  **Clone this repo:**
    ```bash
    git clone [YOUR_GITHUB_REPO_URL]
    cd [YOUR_PROJECT_FOLDER_NAME]
    ```

2.  **(Good Practice!) Create and activate a virtual environment:**
    ```bash
    # Create the env
    python -m venv venv

    # Activate on Mac/Linux
    source venv/bin/activate

    # Activate on Windows (CMD)
    .\venv\Scripts\activate
    ```

3.  **Install the goodies:**
    *(Make sure you've created a `requirements.txt` file!)*
    ```bash
    pip install -r requirements.txt
    ```
    *(If you haven't, just install them manually: `pip install numpy matplotlib`)*

4.  **Run the program:**
    ```bash
    python "PROYEK KN.py"
    ```

5.  Just follow the on-screen menu!