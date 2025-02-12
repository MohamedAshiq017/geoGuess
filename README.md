# **GeoGuess** – Interactive State Guessing Game & Custom Map Creator  

GeoGuess is a **fun and educational** game that challenges players to guess states on a map. Play with **U.S. states** or **Indian states & UTs**, or **create your own custom map** using the built-in **Map Creator Tool**!  

 **Test your geography skills & build custom maps effortlessly!**  

---

## **Features**  

 Guess U.S. or Indian states and see them placed on the map.  
 Track correct guesses and highlight missed states in red.  
 Works with **any map** – easily add custom maps!  
 **Map Creator Tool** to create and save new maps dynamically.  
 **Interactive UI** with **real-time updates** using Python’s `turtle`.  

---

##  **How to Play**  

1️ **Run the game** (`usa.py` or `india.py`).  
2️ A map appears – **enter state names** in the pop-up box.  
3️ **Correct answers** are marked on the map.  
4️ Click "Exit" to finish and **see missed states** in red.  

**Want to create your own game for a different country/region?**  
Use **Map Creator (`map_creator.py`)** to mark locations and generate new datasets!  

---

##  **Installation & Setup**  

1️ **Clone the repository**  
```bash
git clone https://github.com/YourUsername/GeoGuess.git
cd GeoGuess
```

2️ **Install dependencies**  
```bash
pip install pandas pyperclip
```

3️ **Run a game**  
```bash
python usa.py
```
```bash
python india.py
```

4️ **Create a custom map**  
```bash
python map_creator.py
```

---

## **Customization**  

 Want to create a game for another country or region?  
Use `map_creator.py` to collect coordinates and generate a new dataset!  

1️ **Replace the map**  
- Change `usa.gif` or `india.gif` to your own map file (must be `.gif`).  

2️ **Run `map_creator.py`**  
- Click anywhere on the map and enter the location name.  
- Save the coordinates to a `.csv` file.  

3️ **Modify the game script**  
- Update the script to use your new `.csv` dataset.  

 **Now you have a fully customized GeoGuess game!**  

---

##  **Project Structure**  

 `usa.py` → U.S. state-guessing game  
 `india.py` → Indian state & UT guessing game  
 `map_creator.py` → Tool to create custom maps  
 `usa.gif` / `india.gif` → Map images used in the game  
 `usa.csv` / `india.csv` → Coordinate datasets  

---

##  **Technologies Used**  

 **Python** – Core programming language  
 **Turtle** – Graphical interface for interactive maps  
 **Pandas** – Data handling for state coordinates  
 **Pyperclip** – Clipboard integration for user input  

---

##  **Like this project?**  

If you enjoyed playing **GeoGuess**, please **star**  this repo and share it with others! 
