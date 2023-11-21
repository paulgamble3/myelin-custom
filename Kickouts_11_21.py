import streamlit as st
import glob
import random
import json

st.header("Kickout Engine Testing - 11/21")

def sample_kickout_details():
    zones = ["Red", "Yellow", "Green", "White"]
    zone = random.choice(zones)
    symptoms = [
        "HEADACHE",
        "ABDOMINAL_PAIN",
        "PILLOWS",
        "CHEST_PAIN",
        "RASH",
        "COUGH",
        "CLOTHING_TIGHT",
    ]
    symptom = random.choice(symptoms)
    return {
        "zone": zone,
        "symptom": symptom,
    }


def sample_url():
    configs = glob.glob("call_configs/*.json")
    config = random.choice(configs)
    with open(config) as f:
        config = json.load(f)
    c = random.choice(config)
    url = c["url"]
    return url


with st.form("generate-call-url"):

    submitted = st.form_submit_button("Generate Call URL")

    if submitted:
        kickout_details = sample_kickout_details()

        zone = kickout_details["zone"]
        symptom = kickout_details["symptom"]

        url = sample_url()

        # link to call
        st.header("[CALL URL]({})".format(url))
        st.write("Please portray the following symptom: " + symptom)
        st.write("Please portray the following zone: " + zone)

