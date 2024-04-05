# FRESH_PICKER

# Quality and Storage Monitoring with Reminders _inteloneAPI

## Description
 Embrace the innovation in product assessment with FreshPicker, where technology enhances freshness. Our groundbreaking application redefines the way you interact with fruits and vegetables, providing instant quality evaluations and freshness insights right at your fingertips. With our intuitive scan-and-identify feature, discover the health of your product through a simple upload click. Dive into a repository of preservation techniques and delicious recipes curated by our AI, tailored to the specific needs of your fruits and vegetables


## Execution Command

1.file directory


    /streamlit webapp
          ├── app.py             <-- main script
          └── streamlit environment   #mandatory create streamlitenv  
          └── models
                 └── xgmodel_without1api_job.pk1
                 └──100GPT
                    └── added_tokens.json
                    └── config.json
                    └── generation_config.json
                    └── merges.txt
                    └── special_tokens_map.json
                    └── tokenizer.json
                    └── tokenizer_config.json
                    └── training_args.bin
                    └── vocab.json
                    └── model.safetensors  # that is a large file so i have shared my drive link.
                
                   
                    
          

2.Install required packages into streamlit environment

3.Using this command to run our webapp
            
            "streamlit run app.py"

**Dataset Drive link**

            https://drive.google.com/drive/folders/18YIJhz7DfPHTS9pOgLojFKHWAWoMa4FE?usp=sharing


 **Some trained models and Dataset are too large. So, here I have shared my drive link .You can refer and download it.**

            https://drive.google.com/drive/folders/1kR-l7_63u6LWxUhMsXbFY43ik3hv3Sgu?usp=sharing

----------------------------------------------------------------------------------------------------------------------------------
## Problem Statement :
In the realm of food consumption, consumers struggle with assessing the freshness
and quality of fruits and vegetables, leading to wastage and sustainability setbacks.The lack of
efficient monitoring methods hampers inventory management, complicating the issue
further.Thus, there’s a growing need for an innovative solution, integrating Intel oneAPI toolkit
that provides reliable freshness detection and quality evaluation for fruits and vegetables,
empowering consumers to make informed decisions and reduce waste.

## Solution:
Our solution is a revolutionary web application designed to streamline the process of
assessing fruits and vegetable quality and freshness. Leveraging technologies such as the Intel
oneAPI toolkit and advanced image recognition algorithms, our application aims to transform
how consumers interact with products. Key features include:
+ Automated evaluation of scanned fruits and vegetables quality and freshness using
advanced image recognition and AI.
+ Personalized recommendations on product quality, including ripeness, freshness, and
condition, are provided.
+ The option to upload images for analysis ensures accuracy and flexibility in assessing a
wide range of products.
+ Interactive chatbot provides curated recipes and storage guidance tailored to scanned
products.
+ Effortless inventory management allows users to receive proactive reminders when
items are nearing expiration, minimizing food waste.

# Demonstration of the Project






            

## FreshPicker - Two Models
**1.Fruit and Vegetable quality prediction:**

This model represents a significant advancement in product evaluation,
leveraging Intel Extension for TensorFlow to redefine how we assess the freshness and
quality of fruits and vegetables. Notably, running this code in Google Colab exceeded 30
minutes, but leveraging Intel's GPU ensures completion in less than a minute. 

**2.Recipe Generator:**

This model represents a leap forward in culinary innovation,
harnessing the power of GPT and Intel Extension for PyTorch. This groundbreaking
model redefines culinary creativity by generating personalized recipes based on your
ingredients. Leveraging the cutting-edge capabilities of GPT and Intel's technology, our
model ensures seamless recipe generation. The process involves installing essential
dependencies, fine-tuning GPT with a custom dataset, and configuring the model for
recipe generation. 

## Usage of Intel Developer Cloud:

Utilizing the resources provided by Intel Developer Cloud has significantly
expedited our fruit quality prediction model's development and deployment processes.
Specifically, we harnessed the power of Intel's GPU through Intel Extension for
TensorFlow to accelerate critical components of our project: Fruits and Vegetables
Quality Prediction.

**Fruits and vegetables Quality Prediction Model Training:**
The Intel Developer Cloud's GPU capabilities, combined with Intel Extension for TensorFlow, played a crucial role in
reducing the training time of our Fruit Detection model. Leveraging Intel's
high-performance computing infrastructure, we achieved more efficient model training,
significantly cutting down the time required for optimization and experimentation.Notably,
a single epoch now takes only 2 seconds, a substantial improvement compared to other
environments, showcasing the remarkable speedup achieved with Intel's hardware
resources and optimized software stack.

**Recipe Generation Model:**
Leveraging Intel Extension for PyTorch, our recipe generator
model benefits from the accelerated development and deployment processes facilitated
by Intel Developer Cloud. By harnessing Intel's GPU capabilities, we've significantly
reduced training times, ensuring efficient model optimization and experimentation. This
collaborative approach has led to remarkable speedups, enhancing the overall
performance of our Recipe Generation model and streamlining the culinary creativity
process.
