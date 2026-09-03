"""A tiny beginner-friendly machine learning example.

The model learns the relationship between house size and house price.
The data is intentionally small and fictional so the workflow is easy to see.
"""

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

# Feature: house size in square meters.
house_sizes = [[50], [60], [75], [85], [100], [120], [140], [160], [180], [200]]

# Target: price in thousands of dollars.
house_prices = [120, 145, 175, 195, 225, 265, 305, 345, 385, 425]

# Keep some examples aside so we can test the model on unseen data.
X_train, X_test, y_train, y_test = train_test_split(
    house_sizes,
    house_prices,
    test_size=0.2,
    random_state=42,
)

# Create and train the model.
model = LinearRegression()
model.fit(X_train, y_train)

# Measure how close the predictions are to the real test prices.
test_predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, test_predictions)
r_squared = r2_score(y_test, test_predictions)

# Use the trained model to predict a new house price.
new_house_size = [[155]]
predicted_price = model.predict(new_house_size)[0]

print("House Price Prediction")
print("----------------------")
print(f"Model slope: ${model.coef_[0]:.2f}k per square meter")
print(f"Model intercept: ${model.intercept_:.2f}k")
print(f"Average test error: ${mae:.2f}k")
print(f"R-squared score: {r_squared:.2f}")
print(f"Predicted price for a 155 m² house: ${predicted_price:.2f}k")

# Try changing 155 above and run the file again to see a new prediction.
