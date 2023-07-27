import streamlit as st
from PIL import Image 

ab_img = Image.open('20230331_181049.jpg')
an_img = Image.open('anirudh_2023_03_31.jpg')
dr_img = Image.open('IMG_20210318_074005.jpg')
papa_img = Image.open('20220410_155706_0000.png')
bingg_img = Image.open('IMG-20220819-WA0006.jpg')
var_img = Image.open('IMG_20220604_200315.jpg')
snv_img = Image.open('20230702_114424.jpg')

title = st.title("YOU ARE FAMOUS")
c1 , c2 = st.columns(2)

rn = st.number_input("Enter your roll_no ")

with c1:

    if rn == 30:
        st.header("_YOU ARE DHEERAJ_")
        st.write("You are from K.K.R.H.S")
        st.write("You fear ZOMBIES")
        st.write("You like Traffic Rider")
        st.subheader("Oopsuu")
        st.write("fav food : Biryani")

    if rn == 12:
        st.header("_YOU ARE ABHIRAM_")
        st.write("You fear your brother")
        st.write("You like mini militia")
        st.subheader("Abhi")
        st.write("fav food : Biryani")

    if rn == 23:
        st.header("_YOU ARE SAANVI_")
        st.write("You are from K.K.R.H.S")
        st.write("You fear lizard")
        st.write("You like Vlogs,tours")
        st.subheader("Milky")
        st.write("fav food : peanuts")

    if rn == 19:
        st.header("_YOU ARE ANIRUDH_")
        st.write("You fear Mom")
        st.write("You like making videos, indian bike racer")
        st.subheader("Anir,Chitri")
        st.write("fav food : Chicken")

    if rn == 8:
        st.header("_YOU ARE HARSHINI SAGAR IAS_")
        st.write("You are from K.K.R.P.S")
        st.write("You fear Nothing , universe extinction")
        st.write("You like Play games,Writing")
        st.subheader("Papa , Ramana , Mr , Nookayya , papuu , papaayya , pops")
        st.write("fav food : Egg")

    if rn == 26:
        st.header("_YOU ARE HARSHITH_")
        st.write("You are from K.K.R.P.S")
        st.write("You fear Varshith")
        st.write("You like Horror shows")
        st.subheader("Bingg")
        st.write("fav food : Aloo fry")

    if rn == 33:
        st.header("_YOU ARE VARSHITH_")
        st.write("You are from K.K.R.Pp.S")
        st.write("You fear Absolutely nothing")
        st.write("You like cycle")
        st.subheader("Siggo,Varshu,varshu kanna")
        st.write("fav food : chicken , mutton , talkay , boati")

    if rn == 29:
        st.title("_YOU ARE D CHARAN_")
        st.write("You are from K.K.R.H.S")
        st.write("Your pet's name is KIWI")
        st.write("Best friend : DHEERAJ")

    if rn == 13:
        st.title("_YOU ARE NAGA SANJANA_")
        st.write("You are from K.K.R.H.S")
        st.write("Best friend : SAANVI")

    if rn == 16:
        st.title("_YOU ARE RISHITHA_")
        st.write("You are from K.K.R.P.S")
        st.write("Your pet's name is KIWI")
        st.write("Best friend : HARSHINI")

#_____________________________________________Images____________________________
with c2:
    st.write("**_ _by Saathvik_**")
    if rn == 8:
        st.image(papa_img)

    if rn == 12:
        st.image(ab_img)

    if rn == 19:
        st.image(an_img)

    if rn == 30:
        st.image(dr_img)

    if rn == 33:
        st.image(var_img)

    if rn == 23:
        st.image(snv_img)
