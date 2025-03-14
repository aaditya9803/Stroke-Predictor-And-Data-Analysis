import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pages.fake_data_generator import fake_data_generator

def show_information():

    filepath = './static/dataset-stroke.csv'

    st.title('Information about the dataset')

    train_data = pd.read_csv((filepath), sep=',', header=0)
    df = pd.DataFrame(train_data)
    df.drop(df[df['gender'] == 'Other'].index, inplace=True)#Since there is only 1 row with 'Other' value
    df['bmi']=df['bmi'].fillna(df['bmi'].mean())
    original_df = df
    df_stroke = df[df['stroke'] == 1]

    total_people_stroke = df_stroke.shape[0]
    df.dropna(inplace=True)
    # st.write(df_stroke.head())
##########################################################################
    st.header('1. Data Analysis on people who had a stroke')


    st.markdown(
        """
        <style>
        .stImage {
            display: flex;
            justify-content: flex-start;
            align-items: flex-start;
            width: 70%;
            margin-left: 160px;
            margin-top: -105px;
        }
        .custom-div {
            margin-top: 10px; 
            margin-left: -300px;
        }

        </style>
        """,
        unsafe_allow_html=True
        )












            # /* Adjust Specific Robot Button */
            # div[data-testid="stHorizontalBlock"] > div:nth-of-type(3) button {
            #     width: 40px !important;
            #     height: 40px !important;
            #     background-repeat: no-repeat !important;
            #     background-position: center !important;
            #     background-size: contain !important;
            #     border: none !important;
            #     border-radius: 50% !important;
            #     visibility: visible !important;
            # }
                  # .custom-div {
            #     display: flex;
            #     justify-content: flex-start;
            #     align-items: flex-start;
            #     width: 200%;
            #     margin-left: 0px; 
            #     margin-top: 100px; 
            # }  

                # div[data-testid="stImageContainer"]:nth-of-type(6) {
            #     display: flex;
            #     justify-content: flex-start;
            #     align-items: flex-start;
            #     width: 50%;
            #     margin-left: 160px;  /* Move chart to the right */
            #     margin-top: -105px;  /* Move chart upwards */
            # }    


    st.subheader('1.1. Gender')

    # Gender
    stroke_females = df_stroke[df_stroke['gender'] == 'Female'].shape[0]
    stroke_males = df_stroke[df_stroke['gender'] == 'Male'].shape[0]
    percent_females_stroke = (stroke_females / total_people_stroke) * 100
    percent_males_stroke = (stroke_males / total_people_stroke) * 100
    st.write(f"Gender of people who had a stroke")
    st.write(f"• Female:  {percent_females_stroke:.2f}%")
    st.write(f"• Male:  {percent_males_stroke:.2f}%")

    # Gender Pie Chart
    gender_labels = ['Female', 'Male']
    gender_sizes = [percent_females_stroke, percent_males_stroke]
    fig, ax = plt.subplots(figsize=(5, 5), dpi=300)  # Adjusted size and dpi for clarity
    ax.pie(gender_sizes, labels=gender_labels, autopct='%1.2f%%', colors=['pink', 'skyblue'], startangle=90, 
        textprops={'fontsize': 15})  # Adjusted font size for labels
    ax.axis('equal')
    st.pyplot(fig)


    st.subheader('1.2. Hypertension')

    # Hypertension
    stroke_no_hypertension = df_stroke[df_stroke['hypertension'] == 0].shape[0]
    stroke_with_hypertension = df_stroke[df_stroke['hypertension'] == 1].shape[0]
    percent_no_hypertension = (stroke_no_hypertension / total_people_stroke) * 100
    percent_with_hypertension = (stroke_with_hypertension / total_people_stroke) * 100
    st.write(f"Hypertension status of people who had a stroke:")
    st.write(f"• No Hypertension:  {percent_no_hypertension:.2f}%")
    st.write(f"• Hypertension:  {percent_with_hypertension:.2f}%")

    # Hypertension Pie Chart
    hypertension_labels = ['No Hypertension', 'Hypertension']
    hypertension_sizes = [percent_no_hypertension, percent_with_hypertension]
    fig, ax = plt.subplots(figsize=(5, 5), dpi=300)  # Adjusted size and dpi for clarity
    ax.pie(hypertension_sizes, labels=hypertension_labels, autopct='%1.2f%%', colors=['lightgreen', 'yellow'], startangle=90, 
        textprops={'fontsize': 15})  # Adjusted font size for labels
    ax.axis('equal')
    st.pyplot(fig)


    st.subheader('1.3. Marital Status')
    # Marital Status
    stroke_never_married = df_stroke[df_stroke['ever_married'] == 'No'].shape[0]
    stroke_married = df_stroke[df_stroke['ever_married'] == 'Yes'].shape[0]
    percent_never_married = (stroke_never_married / total_people_stroke) * 100
    percent_married = (stroke_married / total_people_stroke) * 100
    st.write(f"Marital Status of people who had a stroke:")
    st.write(f"• Never Married:  {percent_never_married:.2f}%")
    st.write(f"• Married:  {percent_married:.2f}%")

    # Marital Status Pie Chart
    marital_labels = ['Never Married', 'Married']
    marital_sizes = [percent_never_married, percent_married]
    fig, ax = plt.subplots(figsize=(5, 5), dpi=300)
    ax.pie(marital_sizes, labels=marital_labels, autopct='%1.2f%%', colors=['lightcoral', 'gold'], startangle=20, 
        textprops={'fontsize': 15})
    ax.axis('equal')
    st.pyplot(fig)

    st.subheader('1.4. Residence Type')
    # Residence Type
    stroke_rural = df_stroke[df_stroke['Residence_type'] == 'Rural'].shape[0]
    stroke_urban = df_stroke[df_stroke['Residence_type'] == 'Urban'].shape[0]
    percent_rural = (stroke_rural / total_people_stroke) * 100
    percent_urban = (stroke_urban / total_people_stroke) * 100
    st.write(f"Residence Type of people who had a stroke:")
    st.write(f"• Rural:  {percent_rural:.2f}%")
    st.write(f"• Urban:  {percent_urban:.2f}%")

    # Residence Type Pie Chart
    residence_labels = ['Rural', 'Urban']
    residence_sizes = [percent_rural, percent_urban]
    fig, ax = plt.subplots(figsize=(5, 5), dpi=300)
    ax.pie(residence_sizes, labels=residence_labels, autopct='%1.2f%%', colors=['lightgreen', 'grey'], startangle=90, 
        textprops={'fontsize': 15})
    ax.axis('equal')
    st.pyplot(fig)

    st.subheader('1.5. Heart Disease')
    # Heart Disease
    stroke_no_heart_disease = df_stroke[df_stroke['heart_disease'] == 0].shape[0]
    stroke_with_heart_disease = df_stroke[df_stroke['heart_disease'] == 1].shape[0]
    percent_no_heart_disease = (stroke_no_heart_disease / total_people_stroke) * 100
    percent_with_heart_disease = (stroke_with_heart_disease / total_people_stroke) * 100
    st.write(f"Heart condition of people who had a stroke:")
    st.write(f"• No Heart Disease:  {percent_no_heart_disease:.0f}%")
    st.write(f"• Heart Disease:  {percent_with_heart_disease:.2f}%")

    # Heart Disease Pie Chart
    heart_disease_labels = ['No Heart Disease', 'Heart Disease']
    heart_disease_sizes = [percent_no_heart_disease, percent_with_heart_disease]
    fig, ax = plt.subplots(figsize=(5, 5), dpi=300)
    ax.pie(heart_disease_sizes, labels=heart_disease_labels, autopct='%1.2f%%', colors=['lightpink', 'salmon'], startangle=90, 
        textprops={'fontsize': 15})
    ax.axis('equal')
    st.pyplot(fig)


    st.subheader('1.6. Work Type')
    # Work Type
    stroke_govt_job = df_stroke[df_stroke['work_type'] == 'Govt_job'].shape[0]
    stroke_never_worked = df_stroke[df_stroke['work_type'] == 'Never_worked'].shape[0]
    stroke_private = df_stroke[df_stroke['work_type'] == 'Private'].shape[0]
    stroke_self_employed = df_stroke[df_stroke['work_type'] == 'Self-employed'].shape[0]
    stroke_have_children = df_stroke[df_stroke['work_type'] == 'children'].shape[0]
    percent_govt_job = (stroke_govt_job / total_people_stroke) * 100
    percent_never_worked = (stroke_never_worked / total_people_stroke) * 100
    percent_private = (stroke_private / total_people_stroke) * 100
    percent_self_employed = (stroke_self_employed / total_people_stroke) * 100
    percent_have_children = (stroke_have_children / total_people_stroke) * 100
    st.write(f"Work Type of people who had a stroke:")
    st.write(f"• Government Job:  {percent_govt_job:.2f}%")
    st.write(f"• Never Worked:  {percent_never_worked:.2f}%")
    st.write(f"• Private:  {percent_private:.2f}%")
    st.write(f"• Self-employed:  {percent_self_employed:.2f}%")
    st.write(f"• Have children:  {percent_have_children:.2f}%")

    # Work Type Pie Chart
    work_type_labels = ['Government Job', 'Never Worked', 'Private', 'Self-employed', 'Have children']
    work_type_sizes = [percent_govt_job, percent_never_worked, percent_private, percent_self_employed, percent_have_children]
    fig, ax = plt.subplots(figsize=(5, 5), dpi=300)
    ax.pie(work_type_sizes, labels=work_type_labels, autopct='%1.2f%%', startangle=90, 
        colors=['lightgreen', 'pink', 'lightblue', 'yellow', 'green'], textprops={'fontsize': 15})
    ax.axis('equal')
    st.pyplot(fig)



    st.subheader('1.7. Smoking Status')
        # Smoking Status
    stroke_unknown = df_stroke[df_stroke['smoking_status'] == 'Unknown'].shape[0]
    stroke_formerly_smoked = df_stroke[df_stroke['smoking_status'] == 'formerly smoked'].shape[0]
    stroke_never_smoked = df_stroke[df_stroke['smoking_status'] == 'never smoked'].shape[0]
    stroke_smokes = df_stroke[df_stroke['smoking_status'] == 'smokes'].shape[0]
    percent_unknown = (stroke_unknown / total_people_stroke) * 100
    percent_formerly_smoked = (stroke_formerly_smoked / total_people_stroke) * 100
    percent_never_smoked = (stroke_never_smoked / total_people_stroke) * 100
    percent_smokes = (stroke_smokes / total_people_stroke) * 100
    st.write(f"Smoking Status of people who had a stroke:")
    st.write(f"• Unknown:  {percent_unknown:.2f}%")
    st.write(f"• Formerly Smoked:  {percent_formerly_smoked:.2f}%")
    st.write(f"• Never Smoked:  {percent_never_smoked:.2f}%")
    st.write(f"• Smokes:  {percent_smokes:.2f}%")

    # Smoking Status Pie Chart
    smoking_status_labels = ['Unknown', 'Formerly Smoked', 'Never Smoked', 'Smokes']
    smoking_status_sizes = [percent_unknown, percent_formerly_smoked, percent_never_smoked, percent_smokes]
    fig, ax = plt.subplots(figsize=(5, 5), dpi=300)
    ax.pie(smoking_status_sizes, labels=smoking_status_labels, autopct='%1.2f%%', startangle=90, 
        colors=['gray', 'lightblue', 'lightgreen', 'orange'], textprops={'fontsize': 15})
    ax.axis('equal')
    st.pyplot(fig)


    # 1.8. BMI Distribution
    st.subheader('1.8. BMI Distribution')
    st.write(f"BMI of people who had a stroke:")
    st.write(f"• Average BMI:  {df_stroke['bmi'].mean():.2f}")
    st.write(f"• Highest BMI:  {df_stroke['bmi'].max():.2f}")
    st.write(f"• Lowest BMI:  {df_stroke['bmi'].min():.2f}")
    st.markdown('<div class="custom-div">', unsafe_allow_html=True)

    #Histogram
    fig, ax = plt.subplots(figsize=(20, 6))
    sns.histplot(df_stroke['bmi'], kde=True, ax=ax)
    ax.set_title('Distribution of BMI', fontsize=30)
    ax.set_xlabel('BMI', fontsize=30)
    ax.set_ylabel('Frequency', fontsize=30)
    ax.tick_params(axis='both', which='major', labelsize=20)  
    st.pyplot(fig)
    st.markdown('</div>', unsafe_allow_html=True)



    # 1.9. Age Distribution
    st.subheader('1.9. Age Distribution')
    st.write(f"Age of people who had a stroke:")
    st.write(f"• Average Age:  {df_stroke['age'].mean():.2f}")
    st.write(f"• Highest Age:  {df_stroke['age'].max():.2f}")
    st.write(f"• Lowest Age:  {df_stroke['age'].min():.2f}")
    st.markdown('<div class="custom-div">', unsafe_allow_html=True)

    #Histogram
    fig, ax = plt.subplots(figsize=(20, 6))
    sns.histplot(df_stroke['age'], kde=True, ax=ax)
    ax.set_xlabel('Age', fontsize=30)
    ax.set_ylabel('Frequency', fontsize=30)
    ax.tick_params(axis='both', which='major', labelsize=20) 
    st.pyplot(fig)
    st.markdown('</div>', unsafe_allow_html=True)

    # 1.10. Glucose Level Distribution
    st.subheader('1.10. Average Gulcose Level Distribution')
    st.write(f"Average Gulcose Level of people who had a stroke:")
    st.write(f"• Average Level:  {df_stroke['avg_glucose_level'].mean():.2f}")
    st.write(f"• Highest Level:  {df_stroke['avg_glucose_level'].max():.2f}")
    st.write(f"• Lowest Level:  {df_stroke['avg_glucose_level'].min():.2f}")
    st.markdown('<div class="custom-div">', unsafe_allow_html=True)

    #Histogram
    fig, ax = plt.subplots(figsize=(20, 6))
    sns.histplot(df_stroke['avg_glucose_level'], kde=True, ax=ax)
    ax.set_xlabel('Average Glucose Level', fontsize=30)
    ax.set_ylabel('Frequency', fontsize=30)
    ax.tick_params(axis='both', which='major', labelsize=20) 
    st.pyplot(fig)
    st.markdown('</div>', unsafe_allow_html=True)

    st.header(" ")
##########################################################################
    st.header('2. Comparison between people who had a stroke and those who did not')



    columns = ['gender', 'hypertension', 'ever_married', 'work_type', 'Residence_type', 'smoking_status', 'heart_disease']
    label_mappings = {
        'gender': ['Female', 'Male'],
        'hypertension': ['No', 'Yes'],
        'ever_married': ['No', 'Yes'],
        'work_type': ['Government Job', 'Never Worked', 'Private', 'Self-employed', 'Have children'],
        'Residence_type': ['Rural', 'Urban'],
        'smoking_status': ['Unknown', 'Formerly Smoked', 'Never Smoked', 'Smokes'],
        'heart_disease': ['No', 'Yes']
    }

    i=0
    for col in range(len(columns)):
        i=i+1
        st.header(" ")
        st.subheader(f'2.{i}. {columns[col].replace("_", " ").capitalize()}')
        st.header(" ")
        st.subheader(" ")
        fig, ax = plt.subplots(figsize=(12, 8))
        sns.countplot(x=df[columns[col]], hue=df['stroke'], palette=['skyblue', 'black'], ax=ax)
        ax.set_xticks(range(len(label_mappings[columns[col]])))
        ax.set_xticklabels(label_mappings[columns[col]], rotation=30, fontsize=12)
        ax.set_xlabel(columns[col].replace('_', ' ').capitalize(), fontsize=14)
        ax.set_ylabel('', fontsize=14)
        ax.legend(title="Stroke", labels=['No', 'Yes'], fontsize=12)
        st.pyplot(fig)



    continuous_columns = ['age', 'avg_glucose_level', 'bmi']
    for i,col in enumerate(continuous_columns, start=8):
        st.header(" ")
        st.subheader(f'2.{i}. {col.replace("_", " ").capitalize()}')
        st.header(" ")
        st.subheader(" ")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(
            data=df,
            x=col,
            hue='stroke',
            kde=False,
            palette=['skyblue', 'black'],
            bins=20,
            multiple='dodge',
            ax=ax
        )
        ax.set_xlabel(col.replace('_', ' ').capitalize(), fontsize=14)
        ax.set_ylabel('Frequency', fontsize=14)
        ax.legend(title='Stroke', labels=['No Stroke', 'Stroke'], fontsize=12)
        st.pyplot(fig)




### Generating Fake Data ###
###############################
#Analysis with 30% fake dat
    st.header(" ")
    st.header("""3. Analysis with 30% fake data""")

#Fake data
    df_fakedata = fake_data_generator(1500)
    df_mix = pd.concat([original_df, df_fakedata], ignore_index=True)

# Mapping the Columns for to use in plot
    columns = ['gender', 'hypertension', 'ever_married', 'work_type', 'Residence_type', 'smoking_status', 'heart_disease']
    label_mappings = {
        'gender': ['Female', 'Male'],
        'hypertension': ['No', 'Yes'],
        'ever_married': ['No', 'Yes'],
        'work_type': ['Government Job', 'Never Worked', 'Private', 'Self-employed', 'Have children'],
        'Residence_type': ['Rural', 'Urban'],
        'smoking_status': ['Unknown', 'Formerly Smoked', 'Never Smoked', 'Smokes'],
        'heart_disease': ['No', 'Yes']
    }

#Plotting The Discrete variables of data frame with fake data

    i=0
    for col in range(len(columns)):
        i=i+1
        st.header(" ")
        st.subheader(f'3.{i}. {columns[col].replace("_", " ").capitalize()}')
        st.header(" ")
        st.subheader(" ")
        fig, ax = plt.subplots(figsize=(12, 8))
        sns.countplot(x=df_mix[columns[col]], hue=df['stroke'], palette=['lightgreen', 'black'], ax=ax)
        ax.set_xticks(range(len(label_mappings[columns[col]])))
        ax.set_xticklabels(label_mappings[columns[col]], rotation=30, fontsize=12)
        ax.set_xlabel(columns[col].replace('_', ' ').capitalize(), fontsize=14)
        ax.set_ylabel('', fontsize=14)
        ax.legend(title="Stroke", labels=['No', 'Yes'], fontsize=12)
        st.pyplot(fig)


#Plotting The continious variables of data frame with fake data
    continuous_columns = ['age', 'avg_glucose_level', 'bmi']
    for i,col in enumerate(continuous_columns, start=8):
        st.header(" ")
        st.subheader(f'3.{i}. {col.replace("_", " ").capitalize()}')
        st.header(" ")
        st.subheader(" ")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(
            data=df_mix,
            x=col,
            hue='stroke',
            kde=False,
            palette=['lightgreen', 'black'],
            bins=20,
            multiple='dodge',
            ax=ax
        )
        ax.set_xlabel(col.replace('_', ' ').capitalize(), fontsize=14)
        ax.set_ylabel('Frequency', fontsize=14)
        ax.legend(title='Stroke', labels=['No Stroke', 'Stroke'], fontsize=12)
        st.pyplot(fig)





#Comparion of dataframe after adding Fake data
    st.header(" ")
    st.header("4. Dataframe after adding Fake data")
    st.subheader(" ")
    label_mappings = label_mappings or {}
    
    def calculate_percentage_distribution(df, column):
        return df[column].value_counts(normalize=True) * 100
    for column in original_df.columns:
        if original_df[column].dtype == 'object' or original_df[column].nunique() < 10:  # Compare categorical or low-cardinality columns
            original_dist = calculate_percentage_distribution(original_df, column)
            mix_dist = calculate_percentage_distribution(df_mix, column)
            st.write(f"Column: {column}")
            for value in original_dist.index:
                original_percent = original_dist[value]
                mix_percent = mix_dist.get(value, 0)  # Use 0 if value not present in mix_df
                st.markdown(f"<div style='margin-left: 100px;'> • '{value}' class changed by {abs(original_percent-mix_percent):.2f}%</div>", unsafe_allow_html=True)
            st.markdown("###### ")
    st.write("The percentage difference tells us that the random values used to create Fake-Data Dataset weren't biased and was uniformly distributed to each class ")
    st.write("Approach used to compare the differences:")
    st.code("| Class Percentage From Original Dataset - Class Percentage From Fake-Data Dataset |" )
