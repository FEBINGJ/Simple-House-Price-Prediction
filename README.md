# Beginner ML Model

This project demonstrates **linear regression**: a model learns a relationship from examples and uses it to make a prediction.

The example uses fictional house data:

- Input (feature): house size in square meters
- Output (target): house price in thousands of dollars

## Run it

From this folder, run:

```powershell
python house_price_model.py
```

`scikit-learn` is required. Install it if needed:

```powershell
python -m pip install scikit-learn
```

## What the code demonstrates

1. Split data into training and testing examples.
2. Train a `LinearRegression` model.
3. Evaluate predictions with average error and an R-squared score.
4. Predict the price of a new 155 m² house.

The data is intentionally tiny and made up for learning. Real models need larger, representative datasets and more careful validation.
