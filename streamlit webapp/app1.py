
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
from transformers import pipeline
import pandas as pd
import time
import yagmail
import datetime


#----------------------------------------------------------------------------------------------------------


intel=st.sidebar.selectbox('intel',["with oneAPI","without oneAPI"])
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page",["Home","Monitoring","Chatbot"])



#----------------------------------------------------------------------------------------------------------

#model loading 

model1=load_model('model\modelintel80.h5')
model2=load_model('model\modelintel80.h5')
#-----------------------------------------------------------------------------------------------------
#function
labels=['Bad Quality Carrot',
 'Bad Quality Potato',
 'Bad Quality Tomato',
 'Fresh Apple',
 'Fresh Banana',
 'Fresh Bellpepper',
 'Fresh Carrot',
 'Fresh Cucumber',
 'Fresh Mango',
 'Fresh Orange',
 'Fresh Potato',
 'Fresh Strawberry',
 'Fresh Tomato',
 'Good Quality Carrot',
 'Good Quality Potato',
 'Good Quality Tomato',
 'Rotten Apple',
 'Rotten Banana',
 'Rotten Bellpepper',
 'Rotten Carrot',
 'Rotten Cucumber',
 'Rotten Mango',
 'Rotten Orange',
 'Rotten Potato',
 'Rotten Tomato',
 'Tomato_Unripe',
 'ripe apple',
 'ripe banana',
 'ripe dragon',
 'ripe grapes',
 'ripe lemon',
 'ripe mango',
 'ripe orange',
 'ripe papaya',
 'ripe pineapple',
 'ripe pomegranate',
 'ripe strawberry',
 'unripe apple',
 'unripe banana',
 'unripe dragon',
 'unripe grapes',
 'unripe lemon',
 'unripe mango',
 'unripe orange',
 'unripe papaya',
 'unripe pineapple']


storage_suggestions = {
    'Bad Quality Carrot': 'Dispose',
    'Bad Quality Potato': 'Dispose',
    'Bad Quality Tomato': 'Dispose',
    'Fresh Apple': 'Refrigerate',
    'Fresh Banana': 'Room Temperature',
    'Fresh Bellpepper': 'Refrigerate',
    'Fresh Carrot': 'Refrigerate',
    'Fresh Cucumber': 'Refrigerate',
    'Fresh Mango': 'Refrigerate',
    'Fresh Orange': 'Room Temperature',
    'Fresh Potato': 'Room Temperature',
    'Fresh Strawberry': 'Refrigerate',
    'Fresh Tomato': 'Room Temperature',
    'Good Quality Carrot': 'Refrigerate',
    'Good Quality Potato': 'Room Temperature',
    'Good Quality Tomato': 'Room Temperature',
    'Rotten Apple': 'Dispose',
    'Rotten Banana': 'Dispose',
    'Rotten Bellpepper': 'Dispose',
    'Rotten Carrot': 'Dispose',
    'Rotten Cucumber': 'Dispose',
    'Rotten Mango': 'Dispose',
    'Rotten Orange': 'Dispose',
    'Rotten Potato': 'Dispose',
    'Rotten Tomato': 'Dispose',
    'Tomato_Unripe': 'Room Temperature',
    'ripe apple': 'Refrigerate',
    'ripe banana': 'Refrigerate',
    'ripe dragon': 'Refrigerate',
    'ripe grapes': 'Refrigerate',
    'ripe lemon': 'Room Temperature',
    'ripe mango': 'Refrigerate',
    'ripe orange': 'Room Temperature',
    'ripe papaya': 'Room Temperature',
    'ripe pineapple': 'Room Temperature',
    'ripe pomegranate': 'Room Temperature',
    'ripe strawberry': 'Refrigerate',
    'unripe apple': 'Room Temperature',
    'unripe banana': 'Room Temperature',
    'unripe dragon': 'Room Temperature',
    'unripe grapes': 'Room Temperature',
    'unripe lemon': 'Room Temperature',
    'unripe mango': 'Room Temperature',
    'unripe orange': 'Room Temperature',
    'unripe papaya': 'Room Temperature',
    'unripe pineapple': 'Room Temperature'
}

days_to_use = {
    'Bad Quality Carrot': 3,
    'Bad Quality Potato': 5,
    'Bad Quality Tomato': 4,
    'Fresh Apple': 7,
    'Fresh Banana': 5,
    'Fresh Bellpepper': 7,
    'Fresh Carrot': 7,
    'Fresh Cucumber': 5,
    'Fresh Mango': 5,
    'Fresh Orange': 7,
    'Fresh Potato': 7,
    'Fresh Strawberry': 5,
    'Fresh Tomato': 4,
    'Good Quality Carrot': 10,
    'Good Quality Potato': 10,
    'Good Quality Tomato': 7,
    'Rotten Apple': 0,
    'Rotten Banana': 0,
    'Rotten Bellpepper': 0,
    'Rotten Carrot': 0,
    'Rotten Cucumber': 0,
    'Rotten Mango': 0,
    'Rotten Orange': 0,
    'Rotten Potato': 0,
    'Rotten Tomato': 0,
    'Tomato_Unripe': 5,
    'ripe apple': 7,
    'ripe banana': 5,
    'ripe dragon': 3,
    'ripe grapes': 5,
    'ripe lemon': 7,
    'ripe mango': 5,
    'ripe orange': 7,
    'ripe papaya': 5,
    'ripe pineapple': 3,
    'ripe pomegranate': 7,
    'ripe strawberry': 5,
    'unripe apple': 7,
    'unripe banana': 5,
    'unripe dragon': 3,
    'unripe grapes': 5,
    'unripe lemon': 7,
    'unripe mango': 5,
    'unripe orange': 7,
    'unripe papaya': 5,
    'unripe pineapple': 3
}






#--------------------------------------------------------------------------------

# Function to make predictions
def predict(image):
    
    img = image.resize((64, 64))
    img_array = np.asarray(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # Normalize
    if intel=="with oneAPI":
        prediction = model1.predict(img_array)
    else:
        prediction = model1.predict(img_array)    


    # Get the predicted class
    predicted_class = np.argmax(prediction)
    return labels[predicted_class]


#-----------------------------------------------------------------------------------------------------------
#Main Page
if(app_mode=="Home"):
    html_temp="""
<div style="background-color:lightblue;padding:1px">
<h2 style="color:white;text-align:center;">FRESH PICKER 
</h2>
</div>
"""
    st.markdown(html_temp, unsafe_allow_html=True)
    html_temp="""
<div style="background-color:white;padding:0.5px">
<h5 style="color:black;text-align:center;">POWERED BY intel oneAPI 
</h5>
</div>
"""
    st.markdown(html_temp, unsafe_allow_html=True)


#lottie
    def load_lottieurl(url):
        r=requests.get(url)
        if r.status_code !=200:
            return None
        return r.json()

    lottie_coding=load_lottieurl("https://lottie.host/efdf9ec0-c752-46da-aa4f-cf2a64f0a6e6/c4xCzifIQk.json")
    st_lottie(lottie_coding,height=200,key="coding")



#------------------------------------------


    

    def main():
        st.title("SCAN -BUY Goodone")

    # File uploader to get image from the user
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

        if uploaded_file is not None:
        # Display the image
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image.', use_column_width=True,)

        # Make a prediction
            prediction = predict(image)

        
            st.write("")
            st.subheader("NAME AND QUALITY OF THE PRODUCT")
            st.write(prediction)
            st.subheader("STORAGE SUGGESTION")
            st.write(storage_suggestions[prediction])
            st.subheader("use days")
            if days_to_use[prediction]==0:
                st.info("DON'T BUY ")
            else:
                st.info(days_to_use[prediction])
           


    if __name__ == '__main__':
        main()

#---------------------------------------------------------------------------------------------------------------------------
#Monitor
if(app_mode=="Monitoring"):
    def send_email(email, days,vege):

    # Compose email
        subject = "Reminder: Your vegetable & fruit monitor "
        contents = f"Your {vege} is expried in one days."

    # Send email
        yag = yagmail.SMTP('noornishai21cb@psnacet.edu.in', 'psnapsna')  # Update with your email credentials
        yag.send(to=email, subject=subject, contents=contents)
        st.success("Email sent successfully!")
    def main():

        
        html_temp="""
<div style="background-color:lightblue;padding:1px">
<h2 style="color:white;text-align:center;">Monitoring 
</h2>
</div>
"""
        st.markdown(html_temp, unsafe_allow_html=True)

        #lottie
        def load_lottieurl(url):
            r=requests.get(url)
            if r.status_code !=200:
                return None
            return r.json()

        lottie_coding=load_lottieurl("https://lottie.host/515363f8-843e-4ae7-85ea-8779c65f81bf/D4rkps71HW.json")
        st_lottie(lottie_coding,height=200,key="coding")

        email = st.text_input("Enter your email address:")
        alarms = []        
    
    # Initialize session state
        session_state = get_session_state()
    
    # Notification button
        #button_text = "Notification enabled" if session_state["notification_enabled"] else "Notification"
        #if st.button(button_text, key="notification_button"):
            #toggle_notification(session_state)
    
    # Upload image
        uploaded_image = st.file_uploader("Upload fruit or vegetable image", type=["jpg", "jpeg", "png"])
    
    # Display uploaded image with reduced size
        if uploaded_image is not None:
        # Create a container to hold the image and input boxes in a row
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image(uploaded_image, caption="Uploaded Image", width=150)
            with col2:
            # Add text input boxes for name and days in a single line
                image = Image.open(uploaded_image)
                prediction = predict(image)
                name, days = st.columns([1, 1])
                with name:
                    name_input = st.subheader(prediction)
                    name_input=prediction
                with days:
                    days_input = st.subheader(days_to_use[prediction])
                    days_input=days_to_use[prediction]
            # Add button
                if st.button("Add"):
                    if name_input and days_input and email:
                # Process the information when button is clicked
                        session_state["items"].append({"Name": name_input, "Days": days_input })
                        alarms.append({"Name": name_input,"Email": email, "Days": days_input * 24 * 3600})
                    else:
                        st.error("Please fill in both fields.")    
    
    # Display list of items as a table
        if session_state["items"]:
            st.write("\n### Items List:")
            df = pd.DataFrame(session_state["items"])
            df.index = range(1, len(df) + 1) # Start index from 1
            df = df.rename_axis("Item No.") # Rename index column
        
        # Convert index to a DataFrame column
            df.reset_index(inplace=True)
        
        # Style the DataFrame with HTML to adjust alignment of item numbers and increase table size
            st.write(df.to_html(index=False, classes=["styled-table", "large-table"], justify="center"), unsafe_allow_html=True)
        
        # Add CSS style
            st.markdown(
            """
            <style>
            /* CSS code to increase table size */
            .large-table {
                width: 100%; /* Set width to 100% to fill the available space */
                font-size: 16px; /* Adjust font size as needed */
                text-align: center;
                /* Add any other styling properties you want to customize the table */
            }
            </style>
            """,
            unsafe_allow_html=True
        )
            # Check for alarms
        if alarms:
            #st.header("List of Alarms")
            for alarm in alarms:
                #st.write(f"Alarm for {alarm['Email']}:")
                timer_text = st.empty()
                while alarm["Days"] > 0:
                    remaining_days = alarm["Days"] // (24 * 3600)
                    remaining_hours = (alarm["Days"] % (24 * 3600)) // 3600
                    remaining_minutes = (alarm["Days"] % 3600) // 60
                    remaining_seconds = alarm["Days"] % 60
                    timer_text.write(f"Time Remaining: {int(remaining_days)} days, {int(remaining_hours)} hours, {int(remaining_minutes)} minutes, {int(remaining_seconds)} seconds", key=f"timer_{email}")
                    time.sleep(1)
                    alarm["Days"] -= 1
                send_email(alarm["Email"], alarm["Days"],alarm["name_input"])
                alarms.remove(alarm)  # Remove alarm after sending email
    def toggle_notification(session_state):
        session_state["notification_enabled"] = not session_state["notification_enabled"]

    def get_session_state():
        if "items" not in st.session_state:
            st.session_state["items"] = []
        if "notification_enabled" not in st.session_state:
            st.session_state["notification_enabled"] = False
        return st.session_state

    if __name__ == "__main__":
        main()

#-------------------------------------------------------------------------------------------------------------------------------------
if(app_mode=="Chatbot"):
    if intel=="with oneAPI":
       pl = pipeline(task='text-generation',model='model/100GPT')
    else:
        pl = pipeline(task='text-generation',model='model/100gpt_without intel')
    def create_prompt(ingredients):
        ingredients = ','.join([x.strip().lower() for x in ingredients.split(',')])
        ingredients = ingredients.strip().replace(',','\n')
        s = f"<|startoftext|>Ingredients:\n{ingredients}\n"
        return s



# Sidebar title
    st.sidebar.title("Chatbot")

# Main page options
    page_options = ["Recipe Generator", "Storage"]
    selected_option = st.sidebar.selectbox("Select Option", page_options)



    def create_prompt(ingredients):
        ingredients = ','.join([x.strip().lower() for x in ingredients.split(',')])
        ingredients = ingredients.strip().replace(',','\n')
        s = f"<|100gpt|>Ingredients:\n{ingredients}\n"
        return s

# Function to suggest storage
    def suggest_storage(item):
        dict={'spinach ripe': 'Blanch and freeze spinach leaves for long-term storage.\t5-7 days', 'spinach unripe': 'Store unripe spinach in the refrigerator wrapped in damp paper towels to maintain freshness 7-10 days', 'tomato highly riped': 'Make tomato sauce and can it for long-term storage.\t5-7 days', 'tomato unripe': 'Place unripe tomatoes in a paper bag with a ripe banana to hasten ripening.\t3-5 days', 'carrot ripe': 'Store ripe carrots in the refrigerator in a plastic bag with damp paper towels to retain moisture.\t"3-4 weeks', 'carrot unripe': 'Keep unripe carrots in the refrigerator in a plastic bag to slow down ripening.\t1-2 weeks', 'broccoli ripe': 'Blanch broccoli florets and freeze them for later use.\t7-10 days', 'broccoli unripe': 'Store unripe broccoli in the refrigerator in a perforated plastic bag to maintain freshness.\t5-7 days', 'apple ripe': 'Make applesauce and can it for long-term storage.\t3-4 weeks', 'apple unripe': 'Place unripe apples in a cool, dark place to ripen gradually.1-2 weeks', 'banana ripe': 'Peel ripe bananas, slice, and freeze for smoothies or baking.\t2-3 days', 'banana unripe': 'Keep unripe bananas at room temperature until they ripen.\t3-7 days', 'potato ripe': 'Cure ripe potatoes in a cool, dark place for several weeks before storing in a cool, dry location.\t3-5 weeks', 'potato unripe': 'Store unripe potatoes in a well-ventilated area away from direct sunlight.\t1-2 weeks', 'lettuce ripe': 'Wrap ripe lettuce in paper towels and store it in a perforated plastic bag in the \t5-7 days', 'lettuce unripe': 'Keep unripe lettuce in the refrigerator wrapped in damp paper towels to maintain crispness.\t7-10 days', 'bell pepper ripe': 'Slice ripe bell peppers and freeze them for later use in recipes.\t7-10 days', 'bell pepper unripe': 'Store unripe bell peppers in the refrigerator in a plastic bag to slow down ripening.\t1-2 weeks'}
        return dict[item]

# Main page content based on selected option
    if selected_option == "Recipe Generator":
        st.header("Recipe Generator")
        #lottie
        def load_lottieurl(url):
            r=requests.get(url)
            if r.status_code !=200:
                return None
            return r.json()

        lottie_coding=load_lottieurl("https://lottie.host/b9de0b71-e9ac-46ad-acb8-a2f883a12193/ntQ1NiR11u.json")
        st_lottie(lottie_coding,height=200,key="coding")

        ingredients = st.text_input("Enter Your Ingredients (comma-separated)", "")
    
        if st.button("Generate Recipe"):
            if ingredients:
                s=['"'+ingredients+'"']
                for ing in s:
                    prompt = create_prompt(ing)
                    recipe = pl(prompt,max_new_tokens=512,penalty_alpha=0.6,top_k=4,pad_token_id=50259)[0]['generated_text']
                    st.subheader(recipe)
            else:
                st.warning("Please enter some ingredients.")

    elif selected_option == "Storage":
        st.header("Storage Suggestions")
        item = st.selectbox('intel',['Bad Quality Carrot',
 'Bad Quality Potato',
 'Bad Quality Tomato',
 'Fresh Apple',
 'Fresh Banana',
 'Fresh Bellpepper',
 'Fresh Carrot',
 'Fresh Cucumber',
 'Fresh Mango',
 'Fresh Orange',
 'Fresh Potato',
 'Fresh Strawberry',
 'Fresh Tomato',
 'Good Quality Carrot',
 'Good Quality Potato',
 'Good Quality Tomato',
 'Rotten Apple',
 'Rotten Banana',
 'Rotten Bellpepper',
 'Rotten Carrot',
 'Rotten Cucumber',
 'Rotten Mango',
 'Rotten Orange',
 'Rotten Potato',
 'Rotten Tomato',
 'Tomato_Unripe',
 'ripe apple',
 'ripe banana',
 'ripe dragon',
 'ripe grapes',
 'ripe lemon',
 'ripe mango',
 'ripe orange',
 'ripe papaya',
 'ripe pineapple',
 'ripe pomegranate',
 'ripe strawberry',
 'unripe apple',
 'unripe banana',
 'unripe dragon',
 'unripe grapes',
 'unripe lemon',
 'unripe mango',
 'unripe orange',
 'unripe papaya',
 'unripe pineapple'])
        if st.button("Apply"):
            if item:
                storage_suggestion = storage_suggestions(item)
                st.success(storage_suggestion)
            else:
                st.warning("Please enter a vegetable or fruit name.")














          