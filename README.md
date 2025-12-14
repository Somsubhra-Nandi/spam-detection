# Spam SMS Detection using Machine Learning

This project classifies SMS messages as **Spam** or **Not Spam** using
Naive Bayes algorithms.

## Dataset
- SMS Spam Collection dataset
- Stored in `data/spam.csv`
- Encoded in UTF-8

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

## Future Improvements
- Web app deployment
- API support
