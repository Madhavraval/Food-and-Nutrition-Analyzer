🍽️ Food & Nutrition Analyzer

📌 Overview
The Food & Nutrition Analyzer is a Streamlit-based web application that allows users to upload images of their meals. Using **Google Gemini AI**, the app analyzes the food items and provides an estimated calorie count along with health suggestions.

🚀 Features
- Upload multiple food images (JPG, JPEG, PNG format).
- AI-powered food identification and calorie estimation.
- Structured meal breakdown with calorie details.
- Health suggestions for a balanced diet.
- User-friendly and interactive UI built with **Streamlit**.

🛠️ Technologies Used
- Python
- Streamlit - Web UI framework
- Google Generative AI (Gemini) - AI model for food analysis
- Pillow (PIL) - Image processing
- python-dotenv - Environment variable management
- LangChain, ChromaDB, FAISS (for potential future enhancements)

📂 Installation & Setup
1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/food-nutrition-analyzer.git
cd food-nutrition-analyzer
```

2️⃣ Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate     # On Windows
```

3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

4️⃣ Set Up API Key
Create a `.env` file in the project root and add your **Google API Key**:
```env
GOOGLE_API_KEY=your_api_key_here
```

5️⃣ Run the Application
```sh
streamlit run app.py
```

🖼️ Usage
1. Upload one or more images of your food.
2. (Optional) Enter any specific instructions in the text input.
3. Click **"🔍 Analyze Food & Calories"**.
4. View the meal breakdown, total estimated calories, and health suggestions.

📜 Example Output
```
🍽️ Meal Breakdown:
1. Chicken Burger - 500 kcal
2. French Fries - 300 kcal
---
🍎 Total Estimated Calories: 800 kcal
🥗 Health Suggestions: Consider adding a fresh salad for a balanced meal.
```
