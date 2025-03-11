# PubMed Research Fetcher

This project is designed to fetch research papers from **PubMed** based on search terms provided by the user. The fetched data is then saved into a **CSV file** containing relevant information such as **Title, Authors, Abstract, and Publication Date.**

## 🚀 Features
- ✅ Fetch research papers from **PubMed** using user-defined search terms.
- ✅ Save the fetched research papers in a **CSV file**.
- ✅ Handle HTTP requests using Python's `requests` library.
- ✅ Simple and easy to use.

## 📂 Project Structure
```
PubMedResearchFetcher
│
├── .gitignore
├── main.py
├── poetry.lock
├── pyproject.toml
└── README.md
```

## 💻 Requirements
This project requires **Python 3.10+** and the following libraries:
- **requests** - For making HTTP requests to PubMed.
- **pandas** - For handling and saving data to CSV.

All dependencies are managed using **Poetry**.

## 📜 Installation

1. **Clone the repository**:
```bash
git clone https://github.com/PujithaDhoragolla/PubMedResearchFetcher.git
cd PubMedResearchFetcher
```

2. **Install Poetry** (if not installed):
```bash
pip install poetry
```

3. **Install dependencies**:
```bash
poetry install
```

4. **Activate the virtual environment**:
```bash
poetry shell
```

## 🏃‍♀️ Running the Project

To run the project, simply execute:
```bash
poetry run python main.py
```

You will be prompted to enter a search term (like `Cancer Research`). The script will then fetch related research papers from PubMed and save them as a **CSV file** in your directory.

## 💾 Output
The fetched data will be saved as a CSV file named:
```
research_results.csv
```
This file will contain the following columns:
- **Title** - Research paper title.
- **Authors** - Authors of the research paper.
- **Abstract** - Abstract of the paper.
- **Publication Date** - Date of publication.

## 📊 Example Output
| Title | Authors | Abstract | Publication Date |
|-------|---------|----------|------------------|
| Cancer Research in 2025 | John Doe, Jane Smith | This paper discusses... | 2025-03-10 |
| AI in Healthcare | Alex Johnson | This study explores... | 2025-03-11 |

## 📤 Contributing
Contributions are welcome! If you'd like to contribute, please:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## 💌 Contact
If you have any questions, feel free to reach out to me on **GitHub**:
- **GitHub Profile:** [PujithaDhoragolla](https://github.com/PujithaDhoragolla)

## 📝 License
This project is licensed under the **MIT License** - see the LICENSE file for details.

