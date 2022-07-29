import streamlit as st
import requests

st.title("Airlines Customer Satisfaction Prediction")
flightdist = st.number_input("flight distance")
age = flightdist = st.number_input("age")
wifi = st.radio("inflight wifi service (1-5 point)", [1, 2, 3, 4, 5])
oboard = st.radio("online boarding (1-5 point)", [1, 2, 3, 4, 5])
inentertainment = st.radio("inflight entertainment (1-5 point)", [1, 2, 3, 4, 5])
legroom = st.radio("leg room service (1-5 point)", [1, 2, 3, 4, 5])
seatcom = st.radio("seat comfort (1-5 point)", [1, 2, 3, 4, 5])
easebooking = st.radio("ease of online booking (1-5 point)", [1, 2, 3, 4, 5])
oservice = st.radio("onboard service (1-5 point)", [1, 2, 3, 4, 5])
cleanliness = st.radio("cleanliness (1-5 point)", [1, 2, 3, 4, 5])
iservice = st.radio("inflight service (1-5 point)", [1, 2, 3, 4, 5])
bhandling = st.radio("baggage handling (1-5 point)", [1, 2, 3, 4, 5])
cservice = st.radio("checkin service (1-5 point)", [1, 2, 3, 4, 5])
fdrink = st.radio("food and drink (1-5 point)", [1, 2, 3, 4, 5])
custclass = st.radio("customer class", ['Eco', 'Business', 'Eco Plus'])
traveltype = st.radio("type of travel", ['Business travel', 'Personal Travel'])
custtype = st.radio("customer type", ['disloyal Customer', 'Loyal Customer'])

# inference
data = {'flight_distance' : flightdist,
        'age' : age,
        'inflight_wifi_service' : wifi,
        'online_boarding' : oboard,
        'inflight_entertainment' : inentertainment,
        'leg_room_service' : legroom,
        'seat_comfort' : seatcom,
        'ease_of_online_booking' : easebooking,
        'onboard_service' : oservice,
        'cleanliness' : cleanliness,
        'inflight_service' : iservice,
        'baggage_handling' : bhandling,
        'checkin_service' : cservice,
        'food_and_drink' : fdrink,
        'customer_class' : custclass,
        'type_of_travel' : traveltype,
        'customer_type' : custtype}

#URL = "http://127.0.0.1:5000/airlines_prediction" # sebelum push backend
URL = "https://ml2p1-ftds12-gusti-ayu-dewi-p.herokuapp.com/airlines_prediction" #URL Heroku Backend

# komunikasi
r = requests.post(URL, json=data)
res = r.json()
if r.status_code == 200:
    st.title(res['result']['label_name'])
else:
    st.title("ERROR BOSS")
    st.write(res['message'])