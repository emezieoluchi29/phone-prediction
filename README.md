** Mobile Phone Price Range Prediction**

** Overview**
This project focuses on predicting the price range of mobile phones based on their features. The aim is to provide a tool that can assist users in understanding the expected price range of a mobile phone given its specifications. 

**Dataset**
The dataset used for this project consists of various features of mobile phones along with their corresponding price ranges. The columns used in this project are:
- `ram`: Random Access Memory (RAM) in megabytes.
- `battery_power`: Battery power in mAh.
- `px_height`: Pixel resolution height.
- `px_width`: Pixel resolution width.
- `mobile_wt`: Weight of the mobile phone.
- `int_memory`: Internal memory in gigabytes.
- `pc`: Primary camera mega pixels.
- `price_range`: Price range of the mobile phone (target variable).

**Model**
The model employed for predicting the price range is a machine learning model trained on the provided dataset. Various algorithms such as decision trees, random forests, and gradient boosting were experimented with to find the best-performing model.

**Deployment**
The model has been deployed using Streamlit, a Python library for building interactive web applications. Users can input the features of a mobile phone through the web interface, and the deployed model will predict the price range based on those features.

**Performance**
The model has achieved an accuracy of 89% on the test dataset. This level of accuracy was achieved through rigorous experimentation with feature engineering, model selection, hyperparameter tuning, and cross-validation techniques.

**Repository Structure**
- `app.py`: Python script containing the Streamlit web application for deploying the model.
- `model.py`: Python script containing the code for training and evaluating the machine learning model.
- `requirements.txt`: List of Python dependencies required for running the project.
- `data/`: Directory containing the dataset used for training the model.
- `README.md`: This file providing an overview of the project.

**Usage**
To run the Streamlit web application locally, follow these steps:
1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Run the Streamlit app using.
5. Access the web application in your browser at the provided URL.

**Future Work**
- Experiment with more advanced machine learning techniques such as neural networks to further improve prediction accuracy.
- Incorporate additional features or data sources to enhance the model's performance.
- Optimize the deployed application for scalability and efficiency.

**Contributors**
- [EMEZIE OLUCHI](https://github.com/emezieoluchi29)

**License**
This project is licensed under the [pluracodeacademy].
