# 🌍 Leaders Data Collector (Dummy Version)
![WIKIPEDIA-SCRAPER](https://ibb.co/wZFnDHnj)
A simple Python project that simulates collecting historical leaders for multiple countries and exporting the data into a structured JSON file.

This version uses **dummy data instead of real APIs or web scraping**, making it perfect for learning, testing, and understanding the data flow without external dependencies.

---

## ✨ Features

* 📦 Clean and modular Python structure
* 🌐 Simulated country and leader data
* 🧠 Wikipedia paragraph fetching (mocked)
* ⏱️ Artificial delay to mimic real API requests
* 🗂️ JSON export with readable formatting
* 🧪 Perfect for practicing:

  * loops
  * functions
  * dictionaries
  * file handling
  * project structure

---

## 📁 Project Structure

```
.
├── main.py
└── leaders_data.json   # generated after running the script
```

---

## ⚙️ How It Works

1. A list of countries is loaded from dummy data.
2. Each country is processed one by one.
3. Leaders of that country are retrieved.
4. A simulated Wikipedia first paragraph is generated.
5. All data is stored in a dictionary.
6. The final result is exported as a JSON file.

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/leaders-data-project.git
cd leaders-data-project
```

### 2️⃣ Run the script

```bash
python main.py
```

---

## 🧾 Output

After running the script, a file named:

```
leaders_data.json
```

will be created.

Example output:

```json
{
    "us": [
        {
            "name": "George Washington",
            "start_date": "1789",
            "end_date": "1797",
            "wikipedia_first_paragraph": "This is a simulated first paragraph for https://en.wikipedia.org/wiki/George_Washington"
        }
    ]
}
```

---

## 🧠 Learning Goals

This project is ideal for practicing:

* Working with structured data
* Writing reusable functions
* Iterating through nested data
* Creating JSON files
* Building a real-world style data pipeline (without real APIs yet)

---

## 🔮 Future Improvements

You can upgrade this project by:

* 🌐 Replacing dummy data with a real API
* 🕷️ Implementing real Wikipedia scraping (BeautifulSoup / requests)
* ⚡ Adding async requests for performance
* 🧩 Converting the script into a class-based architecture
* 🖥️ Creating a simple CLI interface
* 🐳 Dockerizing the project

---

## 🛠️ Technologies Used

* Python 3
* json
* time

(No external libraries required)

---

## ▶️ Example Console Output

```
Fetching leaders for us...
  Fetching info for George Washington...
  Fetching info for Abraham Lincoln...
Fetching leaders for fr...
  Fetching info for Napoleon Bonaparte...
Fetching leaders for be...
  Fetching info for Leopold II of Belgium...
Done! 'leaders_data.json' has been created with dummy data.
```

---

## 🤝 Contributing

Pull requests are welcome.
For major changes, please open an issue first to discuss what you would like to change.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 💡 Author

Built as a learning project to practice Python data workflows and GitHub project structure.
