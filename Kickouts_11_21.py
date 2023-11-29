import streamlit as st
import glob
import random
import json

st.header("Kickout Engine Testing - 11/29")

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

        # kickout_details = sample_kickout_details(call_type)

        # zone = kickout_details["zone"]
        # symptom = kickout_details["symptom"]

        
        st.write("Call Type: " + call_type)
        # link to call
        st.header("[CALL URL]({})".format(url))
        # st.write("Please portray the following symptom: " + symptom)
        # st.write("Please portray the following zone: " + zone)

