from flask import Flask, request,jsonify
import pickle
import pandas as pd

#from sympy import content

#initiation
app = Flask(__name__)

#open model
def open_model(model_path):
    """
    helper function for loading model
    """

    with open(model_path,'rb') as f:
        model = pickle.load(f)
    return model


model_airlines = open_model("final_pipe.pkl") #pandas dataframe


#inference airlines function
def inference_airlines(data,model):
    """
    input: pandas dataframe
    output: predicted class(idx,label)
    """
    LABEL = ["Satisfied","neutral or dissatisfied"]
    columns = ['flight_distance', 'age', 'inflight_wifi_service', 'online_boarding', 'inflight_entertainment', 'leg_room_service', 'seat_comfort', 'ease_of_online_booking', 'onboard_service', 'cleanliness', 'inflight_service', 'baggage_handling', 'checkin_service', 'food_and_drink', 'customer_class', 'type_of_travel', 'customer_type']
    data = pd.DataFrame([data], columns=columns)
    res = model.predict(data)
    return res[0], LABEL[res[0]]


#home page
@app.route("/") #menandakan homepage
def homepage():
    return "<h1> Home page of airlines satisfaction prediction </h1>"


# inference page for airlines
@app.route('/airlines_prediction', methods = ['POST'])
def airlines_predict():
    """
    content =
    {
        'flight_distance' : xx,
        'age' : xx,
        'inflight_wifi_service' : xx,
        'online_boarding' : xx,
        'inflight_entertainment' : xx,
        'leg_room_service' : xx,
        'seat_comfort' : xx,
        'ease_of_online_booking' : xx,
        'onboard_service' : xx,
        'cleanliness' : xx,
        'inflight_service' : xx,
        'baggage_handling' : xx,
        'checkin_service' : xx,
        'food_and_drink' : xx,
        'customer_class' : xx,
        'type_of_travel' : xx,
        'customer_type' : xx
    }
    """

    content = request.json
    newdata = [content['flight_distance'],
                content['age'],
                content['inflight_wifi_service'],
                content['online_boarding'],
                content['inflight_entertainment'],
                content['leg_room_service'],
                content['seat_comfort'],
                content['ease_of_online_booking'],
                content['onboard_service'],
                content['cleanliness'],
                content['inflight_service'],
                content['baggage_handling'],
                content['checkin_service'],
                content['food_and_drink'],
                content['customer_class'],
                content['type_of_travel'],
                content['customer_type']
                ]
    res_idx, res_label = inference_airlines(newdata,model_airlines)
    result = {
        'label_idx': str(res_idx),
        'label_name': res_label
    }
    response = jsonify(success = True,
                       result = result)
    return response, 200

#run app di local
#app.run(debug=True) #jika deploy diheroku maka harus di hapus atau dibuat comment