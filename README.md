# Spam SMS Detection using Machine Learning

This project classifies SMS messages as **Spam** or **Not Spam** using
Naive Bayes algorithms.

## Dataset
- SMS Spam Collection dataset
- Stored in `data/spam.csv`
- Encoded in UTF-8

## 📊 Dataset Update & Model Improvement

Originally, this project used a standard Kaggle SMS spam dataset.
While it performed well on promotional spam, recall was poor on
modern scam patterns such as:

- account security alerts
- fake delivery messages
- job and investment scams
- invoice and refund phishing

To address this, a custom dataset was generated containing modern
spam and scam patterns.

## Models Used
- Gaussian Naive Bayes
- Multinomial Naive Bayes (selected for deployment)
- Bernoulli Naive Bayes

## Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib

## Project Structure
```
spam-detection/
├── spam_sms_detection.ipynb
├── data/
│   └── spam.csv
├── models/
│   ├── mnb.pkl
│   └── vectorizer.pkl
└── requirements.txt
```

## How to Run
1. Install dependencies  
   `pip install -r requirements.txt`
2. Open the notebook  
   `spam_sms_detection.ipynb`
3. Run all cells

## NLTK Setup
This project uses NLTK for tokenization.
If you face errors related to tokenizers, run:

```python
import nltk
nltk.download('punkt')


### Results
- Recall improved from ~74% → ~99.6%
- Precision remains ~99%
- Model now generalizes better to real-world scam messages

### Note on Limitations
This is a text-only model. Certain messages such as neutral security
alerts or charity requests may still be ambiguous without metadata
(sender, headers, links).

## Future Improvements
- Web app deployment
- API support

