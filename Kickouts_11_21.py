import streamlit as st
import glob
import random
import json

st.header("Kickout Engine Testing - 11/22")

def sample_kickout_details(call_type):

    colonoscopy_custom = {
        "Refusing take bowel prep medication":["White", "Orange"],
        "did not have their bowel prep medication":["Orange"],
        "started bowel prep medication too early":["Green"], 
        "started bowel prep too late":["Yellow", "Green"],
        "eating clear liquid food with red, blue, or purple foods":["Yellow", "Green"],
    }

    base_symptoms = {
        "painful urination":["Orange", "Yellow"],
        "increased urination":["Orange"],
        "blood in urine":["Orange", "Yellow"],
        "unable to urinate":["Orange", "Yellow"],
        "Shortness of Breath":["Yellow"],
    }

    call_type_symptoms = {
        "CHF_discharge": {
            "symptoms": dict(base_symptoms),
        },
        "CHF": {
            "symptoms": dict(base_symptoms),
            },
        "CKD": {
            "symptoms": dict(base_symptoms),
            },
        "Colonoscopy": {
            "symptoms": dict(base_symptoms),
        },
        "TKR": {
            "symptoms": dict(base_symptoms),
        },
    }

    call_type_symptoms["Colonoscopy"]["symptoms"].update(colonoscopy_custom)

    symptom = random.choice(list(call_type_symptoms[call_type]["symptoms"].keys()))
    zone = random.choice(call_type_symptoms[call_type]["symptoms"][symptom])
    
    return {
        "zone": zone,
        "symptom": symptom,
    }


def sample_url():
    configs = glob.glob("call_configs/*.json")
    config_fn = random.choice(configs)
    call_type = config_fn.split("/")[-1].split(".")[0]
    with open(config_fn) as f:
        config = json.load(f)
    c = random.choice(config)
    url = c["url"]
    return {
        "url": url,
        "call_type": call_type,
    }


with st.form("generate-call-url"):

    submitted = st.form_submit_button("Generate Call URL")

    if submitted:

        zz = sample_url()
        url = zz["url"]
        call_type = zz["call_type"]

        kickout_details = sample_kickout_details(call_type)

        zone = kickout_details["zone"]
        symptom = kickout_details["symptom"]

        
        st.write("Call Type: " + call_type)
        # link to call
        st.header("[CALL URL]({})".format(url))
        st.write("Please portray the following symptom: " + symptom)
        st.write("Please portray the following zone: " + zone)

