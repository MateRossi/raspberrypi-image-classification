def classificar(model, features):
    predicted_class = model.predict([features])  # Use the trained model to predict the class for the image
    return predicted_class[0]
