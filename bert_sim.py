import torch
from transformers import BertTokenizer, BertModel
from scipy.spatial.distance import cosine

# Step 1: Load the pre-trained BERT model and tokenizer
model_name = 'bert-large-uncased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)


# Step 2: Tokenize the input texts (job description and CV)
def tokenize(text):
    tokens = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    return tokens


# Step 3: Get the embeddings (the last hidden state of the model)
def get_embeddings(tokens):
    with torch.no_grad():
        outputs = model(**tokens)
        embeddings = outputs.last_hidden_state.mean(dim=1)  # Averaging the token embeddings
    return embeddings.squeeze()


# Step 4: Calculate cosine similarity between two sets of embeddings
def calculate_similarity(cv_text, job_description_text):
    # Tokenize both texts
    cv_tokens = tokenize(cv_text)
    job_tokens = tokenize(job_description_text)

    # Get embeddings for both texts
    cv_embeddings = get_embeddings(cv_tokens)
    job_embeddings = get_embeddings(job_tokens)

    # Calculate cosine similarity
    similarity_score = 1 - cosine(cv_embeddings.numpy(), job_embeddings.numpy())
    return similarity_score


# Step 5: Sample input texts
cv_text = """Ivan Popovych Software Developer– Machine Learning & NLP Contact Information Darmstadt, Germany | popovytch.i@gmail.com | +49 151 64392179 | LinkedIn Professional Summary Motivated Computer Science student with hands-on experience in machine learning, NLP, and full-stack web development. Skilled in building and fine-tuning ML models, utilizing deep learning frameworks like TensorFlow and Hugging Face Transformers. Experienced in integrating APIs, creating responsive UIs with React, and deploying scalable backends. Known for strong problem-solving, adaptability, and teamwork. Education Experience • Student Assistant – ML / NLP • Fullstack Developer • Intern - IT Assistant Skills Hochschule Darmstadt | Darmstadt, Germany | Dec 2024 - Present Freelance | Remote | Jul 2024 - Present Uzhhorod City Council | Uzhhorod, Ukraine | Jan – Apr 2022 • Uzhhorod National University | Computer Science B.S. Uzhhorod, Ukraine / Online Sep 2022 – Jun 2026 • Hochschule Darmstadt (h_da) | Exchange Darmstadt, Germany Oct 2023 – Feb 2025 o Development of machine learning models for text classification. o Leveraged different NLP libraries using technologies such as SpaCy, NLTK, Tensorflow, Keras, Hugging Face Transformers, TextBlob for feature extraction and preprocessing. o Collaborated with academic staff to improve existing systems and datasets, processing 100,000+ text samples for model evaluation. o Designed and developed responsive web applications with React, TypeScript, MaterialUI and Tailwind, ensuring optimal UX across devices. o Integrated multiple third-party APIs for dynamic data retrieval. o Built a scalable backend with Node.js, Express.js, MongoDB and REST API, improving DB performance. o Collected and organized data for a future municipal database, analyzing information from 10+ organizations. o Managed and optimized content for 3+ social media platforms, increasing the number of followers by 30%. o Supported the development of digital tools, streamlining administrative workflows in a government setting. • Python: Flask, Numpy, Pandas, MatplotLib • Machine Learning: ScikitLearn, Tensorflow, CNNs, Deep Learning, Computer Vision, Feature Engineering • NLP: SpaCy, NLTK, Hugging Face, TextBlob • Frontend: HTML, CSS, JavaScript, TypeScript, React, MaterialUI, Tailwind • Backend: Node.js, Express.js, REST API • Databases: MongoDB, SQL, SPARQL • Tools: Docker, Git, GitLab CI/CD • Soft Skills: Quick learning, Problem Solving, Teamwork, Adaptability, Flexibility, Innovation Academic Projects • Brain Computer Interface ML Application • AI Movie Recommender • IForms | Web App with sentiment analysis • Dashly | Multi User Widgets Web App • Autonomous Parking System Languages Achievments Hochschule Darmstadt Hochschule Darmstadt Hochschule Darmstadt Hochschule Darmstadt Hochschule Darmstadt o Developed an ML model to detect eye blinks with ~90% accuracy using TensorFlow. o Analyzed and preprocessed brainwave datasets consisting of 30,000+ samples for model training. o Implemented a model that uses real time electrical brain impulses from a Brain Computer Interface. o Built a Flask-based web app that recommends movies using SPARQL queries and NLP techniques. o Enhanced user experience by analyzing text inputs, increasing recommendation accuracy by 15%. o Optimized data retrieval, reducing response time by 80% for better user experience. o Built a platform for creating and analyzing questionnaires using React, TS, MaterialUI (Frontend) and Express.js, Node.js, Natural (Backend). o Integrated sentiment analysis, improving actionable feedback accuracy by 20%. o Designed and implemented the backend for a multi-user web application for customizable dashboards with widgets (Weather, Calendar, RSS, GitHub Issues, etc.). o Developed a multi-user authentication system, reducing login time by 90% and improving overall user engagement. o Technologies Used: Node.js, TypeScript, Express.js, MongoDB, GitLab CI/CD o Developed and calibrated sensors for the RVR vehicle, improving locator precision by 20% and enhancing IMU accuracy. o Designed system architecture and Python-based interfaces to handle real-time data efficiently. o Authored comprehensive project documentation to support future development. • Ukrainian: Native • English: C1 | University of Central Lancashire Language Courses, UK • German: B2.1 | Intensive & Extensive courses, Hochschule Darmstadt • Italian: B1 • The 2023 ICPC Ukraine Western Contest • International Programming Proggy- Buggy Towel Contest • The 2022 ICPC Ukraine Western Contest • GoITeens Hakathon | HTML & CSS Website category • Codeforces 1600+ Solved Problems Sep 30th, 2023 May 25th, 2023 Oct 22th, 2022 Jun 18th – 19th, 2023"""
job_description_text = """Machine Learning Engineer, Intern (m/f/d) Praktikum/Werkstudium bei Maddox AI, Vollzeit · Tübingen/Berlin/Köln/Remote YOUR MISSION We are looking for a stellar intern in machine learning who is passionate about cutting-edge machine vision topics such as image-conditioned object detection, feature matching, semantic segmentation, uncertainty estimation, image registration, self-supervised learning, unsupervised domain adaptation, transformer architectures, graph neural networks, anomaly detection, etc. As part of our machine learning team, you will solve challenging computer vision problems with real-world datasets of manufacturers and develop innovative AI-based features for our product. You will work closely with experienced machine learning engineers and researchers, but you will also interact with customer success managers, software and hardware engineers, so that you learn about and contribute to the full process of bringing ML solutions to the factory floor. In short, your journey with us will lead you to: Research, prototype, and develop state-of-the-art deep learning models together with other machine learning engineers to create novel and innovative machine learning solutions that solve the manufacturing problems of our clients Train deployment-ready AI models available through our Maddox platform for our customers Create large, efficient and automated data processing and machine learning pipelines that scale across many customers and applications Test and develop new ML-based product features (together with our tech and business team) YOUR PROFILE Basic qualifications You are currently pursuing a Bachelor, Master or PhD degree in computer science or related technical field, or you have equivalent practical experience Solid understanding of Machine Learning and Deep Learning. Ability to implement, debug, and deploy deep learning models in PyTorch, either from scratch or inspired from public libraries or Github repositories. Preferred qualifications Industry experience developing enterprise or data products Experience or knowledge in manufacturing industry End-to-end experience of developing computer vision applications from scratch and continuously improving at production Experience with deploying models to edge computing platforms like Nvidia Jetson using ONNX, TensorRT, etc. Experience with modelling tabular data (neural networks, XGBoost, …) Experience with multi-partners research projects Note that preferred qualifications are just that: preferred. None of us started out with all boxes ticked. If some of these points apply to you, we definitely want to talk. WHY US? We work in flat hierarchies, value direct communication, learn a lot as a team and make important decisions together. At Maddox AI you can expect the following benefits: Independent work on projects in the field of artificial intelligence / Industry 4.0 Flat hierarchies, ownership, autonomy, a growth perspective and very good development opportunities A dynamic and motivated team with great colleagues (with experience from BCG, IBM, SAP, Cyber Valley, etc.) The possibility to work flexibly in Tübingen (preferred), Berlin, Cologne or remotely within Germany (relocating to Germany is needed for the duration of the internship). Regular team events Diversity is very important to us! We welcome all applications regardless of gender, nationality, social and ethnic origin, disability, sexual orientation and identity. ABOUT US Our product, Maddox AI, is an AI-based visual quality control solution, which can automate manually performed quality inspection for manufacturing companies. Maddox AI is an asset-light SaaS solution, which addresses those visual inspection tasks that are still performed manually, as conventional (=rule-based) computer vision methods fail. In product development, we closely collaborate with leading AI researchers from the Cyber Valley. Prof. Dr. Matthias Bethge, Prof. Dr. Alexander Ecker and Dr. Wieland Brendel have been researching in the field of machine learning and computer vision for years and are part of our founding team.Maddox AI is used by DAX-30 companies as well as by large medium-sized enterprises. Our team consists of scientists, former strategy consultants, mechanical engineers, and software developers. We know that Maddox AI's success is only made possible by our unique team. As we continue to grow, we want to convince the best and brightest minds of our mission to establish Maddox as the modern quality management platform."""

# Step 6: Calculate similarity
similarity_score = calculate_similarity(cv_text, job_description_text)
print(f"Compatibility Similarity: {similarity_score * 100:.2f}%")
