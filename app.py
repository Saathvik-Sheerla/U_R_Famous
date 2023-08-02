import streamlit as st
from PIL import Image 

mb2_img = Image.open('Mahesh-Babu-Super-HD-Stills-from-Maharshi-5.webp')
aa_img = Image.open('0df61656b7e76ab5cecaf3e6be991edc.jpg')

ab_img = Image.open('20230331_181049.jpg')
an_img = Image.open('anirudh_2023_03_31.jpg')
dr_img = Image.open('IMG_20210318_074005.jpg')
papa_img = Image.open('20220410_155706_0000.png')
bingg_img = Image.open('IMG-20220819-WA0006.jpg')
var_img = Image.open('IMG_20220604_200315.jpg')
snv_img = Image.open('20230702_114424.jpg')
hr_img = Image.open('IMG-20220819-WA0006.jpg')

abrm_img = Image.open('Photo from Saathvik S (1).jpg')
aj_img = Image.open('SmartSelect_20230125_081617_Instagram.jpg')
kr_img = Image.open('SmartSelect_20220921-133231_WhatsApp.jpg')
sr_img = Image.open('IMG-20220803-WA0010.jpg')
bt_img = Image.open('SmartSelect_20230723_211519_WhatsApp.jpg')
pnd_img = Image.open('Photo from Saathvik S.jpg')
lkt_img = Image.open('Likith _ kmit.png')

title = st.title("YOU ARE FAMOUS")
c1 , c2 = st.columns(2)

rn = st.number_input("roll.no or phone no of min 5 digits")


with c1:

    if rn == 1:
        st.header("YOU ARE MAHESH BABU")
        st.write("You are from Guntur")
        st.write("You like your family")
        st.subheader("Prince , Super Star")
        st.write("fav food : Hyderabad Biryani")
        st.subheader("Best work : DOOKUDU ")

    if rn == 2:
        st.header("YOU ARE ALLU ARJUN")
        st.write("You are from Tollywood")
        st.write("You like your family")
        st.subheader("Bunny , Icon Star")
        st.write("fav food : Biryani")
        st.subheader("Best work : JULAYI")

    if rn == 6:
        st.header("YOU ARE AASHRITHA")
        st.write("You are from sri chaitanya")
        st.write("You like instagram")
        st.subheader("Aashu")
        st.write("fav food : Egg")

    if rn == 79896:
        st.header("_YOU ARE SURYATEJA_")
        st.write("You are from K.K.R.H.S")
        st.write("You like sweets , pets")
        st.subheader("Sunny")

        st.write("fav food: gulab jamoon")

    if rn == 99481:
        st.header("_YOU ARE AJAY_")
        st.write("You are from Kothakota")
        st.write("You like watching movies")
        st.subheader("Gibbs , bro")
        st.write("fav food : Talkay")

    if rn == 79936 :
        st.header("_YOU ARE LIKITH_")
        st.write("You are from KMIT")
        st.write("You like Photography , Cars")
        st.subheader("member of TOL")
        st.write("Fav food : unknown!")


    if rn == 0:
        st.header("_YOU ARE SRIKANTH_")
        st.header("_Happy birthday Baa_ 🎂🎉😍")
        #st.write("You are from Kothakota")
        st.write("You like Talking, foodie , So have them ")
        st.subheader("It's your day ")
        st.write("fav food : Mandi , go have it")

    if rn == 96402:
        st.header("_YOU ARE KIRAN_")
        st.write("You are from Telkapally")
        st.write("You like Meenakshi , Hemanth ")
        st.subheader("Chintu")
        st.write("fav food : Biryani")

    if rn == 87905:
        st.header("_YOU ARE NITHIN_")
        st.write("You are from Kothakota")
        st.write("You like BGMI , Friends")
        st.subheader("Banti")
        st.write("fav food : Mandi")

    if rn == 93900:
        st.header("_YOU ARE SATHYA SHEELA REDDY_")
        st.write("You are from Kothakota")
        st.write("You like BGMI , Reels")
        st.subheader("Pandu")
        st.write("fav food : Biryani")

    if rn == 77026:
        st.header("_YOU ARE ABHIRAM_")
        st.write("You are from KMIT")
        st.write("You like watching anime")
        st.subheader("Abhi")
        st.write("fav food : biryani ?")


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

    if rn == 99481:
        st.image(aj_img)

    if rn == 0:
        st.image(sr_img)

    if rn == 96402:
        st.image(kr_img)

    if rn == 87905:
        st.image(bt_img)

    if rn == 93900:
        st.image(pnd_img)

    if rn == 77026:
        st.image(abrm_img)

    if rn == 26:
        st.image(hr_img)

    if rn == 79936:
        st.image(lkt_img)

    if rn == 1:
        st.image(mb2_img)

    if rn == 2:
        st.image(aa_img)


















st_style = """
                <style>
                #MainMenu{visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden}
                </style>
                """

st.markdown(st_style , unsafe_allow_html=True)
