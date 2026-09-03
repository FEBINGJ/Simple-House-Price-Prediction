# House Price Prediction: A Beginner ML Project

This mini project demonstrates **machine learning with linear regression**. The model studies examples of house sizes and prices, learns a simple relationship between them, and predicts the price of a new house.

The project is intentionally small so that a beginner can read the complete workflow in one file.

## Project Files

| File | Purpose |
| --- | --- |
| `house_price_model.py` | Creates the data, trains the model, evaluates it, and makes a prediction |
| `requirements.txt` | Lists the Python package needed to run the project |
| `README.md` | Project documentation |

## How It Works

The model uses one input, called a **feature**:

- House size in square meters

It learns one output, called the **target**:

- House price in thousands of dollars

The program follows these steps:

1. Stores a small fictional dataset of house sizes and prices.
2. Splits the examples into training data and test data.
3. Trains a `LinearRegression` model with the training data.
4. Uses the test data to measure how well the model performs on examples it did not train on.
5. Predicts the price of a new 155 m² house.

Linear regression tries to find a line that best describes the data:

```text
predicted price = slope * house size + intercept
```

## Requirements

- Python 3.10 or newer
- `scikit-learn`

## Installation

Open a terminal in this project folder and run:

```powershell
python -m pip install -r requirements.txt
```

## Run the Model

```powershell
python house_price_model.py
```

Example output:

```text
House Price Prediction
----------------------
Model slope: $2.02k per square meter
Model intercept: $22.09k
Average test error: $1.18k
R-squared score: 1.00
Predicted price for a 155 m² house: $335.14k
```

The exact test result depends on the data and the fixed `random_state` used when splitting the dataset.

## Understanding the Evaluation

- **Average test error (MAE):** the average difference between the predicted and actual prices. Lower is better.
- **R-squared score:** how well the model explains the variation in the target values. A score closer to `1.0` generally indicates a better fit.

## Try It Yourself

Open `house_price_model.py` and change the value of `new_house_size`, for example:

```python
new_house_size = [[180]]
```

Run the program again to see the prediction for a different house size. You can also add more fictional examples to the dataset and observe how the learned slope changes.

## Important Limitation

This is an educational example, not a real house valuation system. The dataset is tiny, fictional, and uses only house size. Real predictions would need much more data and other factors such as location, age, number of rooms, condition, and market changes.
