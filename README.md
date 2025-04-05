# 🎬 Movie Recommendation System

![App Preview](https://github.com/San7122/movies_recommendation/blob/main/app.png)

An interactive movie recommendation web app that suggests similar movies based on your selection. Built using **Python**, **Streamlit**, and **machine learning techniques**, the app fetches real-time movie posters using the **TMDB API** for an immersive UI experience.

---

## 📌 Overview

This project uses a **content-based filtering** approach to recommend similar movies by comparing their overview vectors. Movie posters are dynamically fetched from **The Movie Database (TMDB)** using their public API, while **cosine similarity** measures help determine closeness between selected titles.

---

## 🛠️ Tech Stack

| Tool       | Usage                              |
|------------|-------------------------------------|
| Python     | Core programming                   |
| Streamlit  | Web application development        |
| Pandas     | Data manipulation                  |
| Scikit-learn | Cosine similarity for recommendations |
| TMDB API   | Fetching movie posters dynamically |
| Pickle     | Loading pre-trained model          |

---

## 🧠 How It Works

1. **User selects a movie** from the dropdown.
2. The app loads a pre-computed **similarity matrix** using cosine similarity.
3. It identifies top 5 most similar movies.
4. **TMDB API** is used to fetch posters for those movies.
5. The recommendations are displayed beautifully using **Streamlit**.

---

## 🧪 Dataset

- Source: Preprocessed TMDB dataset
- Size: ~5,000 movies
- Features used: Movie title, overview (plot summary), poster path, and metadata

---

## 🚀 How to Run Locally

1. Clone this repository  
   `git clone https://github.com/San7122/movies_recommendation.git`

2. Navigate to the folder  
   `cd movies_recommendation`

3. Install dependencies  
   `pip install -r requirements.txt`

4. Run the app  
   `streamlit run app.py`

---

## 🔍 Sample Output

Here’s how it looks when you select a movie like **“Avatar”**:

![App Preview](https://github.com/San7122/movies_recommendation/blob/main/app.png)

---

## 📦 Files in this Repo

- `app.py` — Main Streamlit app logic
- `movies.pkl` — Serialized movie data
- `requirements.txt` — Python dependencies
- `README.md` — Project documentation

---

## 🌟 Features

- Intuitive user interface using Streamlit
- Clean layout with movie posters
- Live recommendations within seconds
- Accurate and scalable similarity algorithm

---

## 💡 Future Enhancements

- Add **collaborative filtering** based on user behavior
- Include genre-based or year-based filtering
- Improve UI with animations or transitions
- Add trailer preview functionality

---

## 🧠 Limitations

- Based only on content (movie descriptions)
- Doesn’t learn from user feedback
- Requires manual update of movie database

---

## 📬 Contact

- 📧 Email: sanjanathakur302@gmail.com  
- 🔗 [LinkedIn](https://linkedin.com/in/sanjana-thakur-b35459246)  
- 🔗 [Live App](https://san7122-ml-app-sanjanathakur.streamlit.app)

---

⭐ If you like this project, don’t forget to **star** this repo!  
