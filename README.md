# Product-Review-Analyzer

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/)
[![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-DeepSeek--Prover-yellow)](https://huggingface.co/deepseek-ai/DeepSeek-Prover-V2-671B)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

## 📋 Overview

Product-Review-Analyzer is a powerful tool that leverages the DeepSeek-Prover-V2-671B model to analyze product reviews. The application processes review text and extracts pros, cons, provides a concise summary, and determines the overall sentiment.

## ✨ Features

- **Comprehensive Analysis**: Extract pros, cons, summary, and sentiment from product reviews
- **User-Friendly Interface**: Simple and intuitive Streamlit web application
- **Structured Output**: Results provided in clean JSON format
- **High-Quality Insights**: Powered by the advanced DeepSeek-Prover-V2-671B model

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- A Hugging Face API token

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Nirikshan95/Product-Review-Analyzer.git
   cd Product-Review-Analyzer
   ```

2. Create virtual environment and activate 
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory with your Hugging Face API token:
   ```
   HUGGINGFACE_API_TOKEN=your_token_here
   ```

## 🚀 Usage

1. Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Access the application in your browser (typically at `http://localhost:8501`).

3. Enter a product review in the text area and click "Analyze".

4. View the structured analysis results including pros, cons, summary, and sentiment.

### Example Input

```
I've been using this wireless mouse for about a month now. The battery life is impressive, lasting 3 weeks on a single charge. The ergonomic design fits comfortably in my hand, and the precision is spot on. However, the clicking sound is quite loud which can be annoying in quiet environments. Also, the Bluetooth connection occasionally drops when used with multiple devices. Overall, it's a solid product for the price point.
```

### Example Output

```json
{
  "pros": ["Impressive battery life (3 weeks on single charge)", "Ergonomic design", "Comfortable fit", "Precise tracking", "Good value for money"],
  "cons": ["Loud clicking sound", "Occasional Bluetooth connection drops with multiple devices"],
  "summary": "A reliable wireless mouse with excellent battery life and ergonomics, though with minor issues regarding noise and connectivity.",
  "sentiment": "Positive"
}
```

## ⚙️ How It Works

1. **User Input**: The user enters a product review through the Streamlit interface.
2. **Processing Pipeline**:
   - The review is formatted using predefined prompt templates in `prompt_template.py`
   - `llm_interface.py` sends the formatted prompt to the DeepSeek-Prover model via Hugging Face API
   - `output_parser.py` processes the model's response into structured JSON
   - `pipeline.py` orchestrates the entire workflow
3. **Output**: The processed results are displayed in the Streamlit app, showing pros, cons, summary, and sentiment analysis.

## 📁 Project Structure

```
Product-Review-Analyzer/
├── configs/
│   └── settings.py         # Configuration settings
├── src/
│   ├── llm_interface.py    # Interface to Hugging Face API
│   ├── output_parser.py    # Processes model output to JSON
│   ├── pipeline.py         # Main processing pipeline
│   └── prompt_template.py  # Templates for model prompts
├── app.py                  # Streamlit application
├── .env                    # Environment variables
├── LICENSE                 # MIT License
├── README.md               # This file
└── requirements.txt        # Project dependencies
```

## 📋 Requirements

Key dependencies include:
- langchain_huggingface
- streamlit
- langchain

For a complete list, see `requirements.txt`.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.