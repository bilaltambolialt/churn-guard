# ChurnGuard: E-Commerce Customer Churn Predictor

ChurnGuard estimates the likelihood that an e-commerce customer will stop
using a platform based on their tenure, order behavior, satisfaction, and
other customer attributes. It combines an exploratory machine-learning
notebook, a saved Random Forest model, a reusable prediction function, and a
small Flask web application.

## Project highlights

- Explores churn patterns in customer behavior and order history.
- Compares Logistic Regression with Random Forest.
- Serves a churn probability through an interactive web form.
- Uses recall alongside accuracy and precision to assess performance on an
  imbalanced churn target.

## Model results

On the reported held-out test set, the selected Random Forest achieved:

| Metric | Logistic Regression | Random Forest |
| --- | ---: | ---: |
| Accuracy | 88.8% | 94.0% |
| Precision | 74.7% | 86.6% |
| Recall | 48.1% | 75.2% |

Recall measures how many actual churners the model identifies. The Random
Forest improved recall by about 27 percentage points over the Logistic
Regression baseline. These figures come from this project's notebook and are
not a guarantee of performance on new data.

## Run the web app locally

Python 3.10 or later is recommended. From the project root, create and activate
a virtual environment, then install the dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Start the app:

```powershell
python app\main.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) and enter customer details
to get a churn probability. To run the sample prediction checks:

```powershell
python src\test_predictions.py
```

The app loads the serialized model and scaler in `models/`. Since these files
are serialized Python objects, use a compatible scikit-learn version when
loading them; retrain the model from the notebook if compatibility issues
occur.

## Project structure

```text
app/                  Flask app and web form
data/                 Source customer churn dataset
docs/                 Project overview and methodology
models/               Saved model and feature scaler
notebooks/            Data exploration and model training
src/                  Prediction function and sample checks
requirements.txt      Python dependencies
```

## Dataset

The project uses the [E-Commerce Customer Churn dataset on Kaggle](https://www.kaggle.com/datasets/samuelsemaya/e-commerce-customer-churn/data)
by samuelsemaya. It contains 3,941 customer records and 11 columns; `Churn` is
the target. The target is imbalanced, with roughly 15% churners. Please review
the dataset source for its license and terms of use.

## Limitations

This is a portfolio demonstration based on one dataset and one held-out split.
Predicted probabilities should not be treated as calibrated business
forecasts, and the reported metrics may not generalize to other customers or
businesses.
