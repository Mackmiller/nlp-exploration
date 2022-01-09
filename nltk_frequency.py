#!/usr/bin/env python
# coding: utf-8

# In[2]:


# grab all input types and install natural language toolkit
get_ipython().system('pip install nltk')


# In[4]:


# get ready for sentence tokenization (breaking paragraph into sentences)
from nltk.tokenize import sent_tokenize
import nltk
nltk.download('punkt')

# add sample copy/paste job description text
text = """Responsibilities

NBCUniversal’s News Group Digital is creating the digital future for one of the world’s best-known and most-trusted news organizations. Our Digital Technology organization is at the center of building and improving a suite of digital products including user experiences across web, mobile apps, OTT devices, storytelling tools including CMS and curation systems, and a platform to distribute that content to hundreds of millions of users. Our brands include NBC News, Today, MSNBC, CNBC, E! News, and Telemundo Noticias.

We are hiring with remote flexibility in multiple locations where our teams are based: New York, NY; Seattle, WA; Englewood Cliffs, NJ; Universal City, CA.

Position Overview

This is an opportunity to play a critical role in the digital evolution of the NBCUniversal News Group across our entire news portfolio.

As a Software Engineer, you will partner with the Product, Operations, Design, and Editorial teams to bring NBC News Digital content to life. You will be a significant influence on our product roadmap, bringing a technical and strategic perspective. You will work alongside fellow inspired developers in a fast-paced environment using technologies like Sass, React.js and GraphQL to help shape the future of digital news.

This role will report into the Manager of Engineering, Platform Partnerships.

Responsibilities

Work on the React.js codebases supporting subscription experiences
Build out GraphQL queries to consume data for all web properties
Implement beautiful UX for engaging news storytelling
Optimize sites across an array of web-capable devices, browsers and experiences
Automate front end testing to ship the highest quality experience for our audience
Write code and tests that are understandable and maintainable
Debug effectively within their primary area to help find root cause
Provide helpful, timely code reviews
Collaborate professionally with teammates and peers
Communicate with engineering precision, escalating blockers quickly, clarifying requirements and sharing assumptions
Seek understanding of how users interact with product/service
Exhibit a growth mindset and make investments in your growth and teammates’ growth

Qualifications/Requirements

Qualifications/Requirements

3+ years’ experience in software development or related

field(s)

1+ years recent experience with a modern JavaScript

framework (e.g. React.js, Vue.js, Aurelia)

B.S. in Computer Science, Computer Information

Systems, or equivalent industry experience

Strong proficiency in either CSS/Sass development or a

server-side programming language (e.g. Node.js, Go,

Java) in the context of a website

Experience implementing responsive designs using

HTML and a CSS preprocessor (SASS, PostCSS, LESS)

Experience using modular JavaScript, async patterns,

and DOM manipulation

Understanding of bundlers, transpilers and

preprocessors (Webpack, Babel, SASS)

Strong problem-solving skills, logical and creative

thinking

Experience with version control"""

# assign tokenized sentences to variable 
tokenized_text = sent_tokenize(text)

# show tokenized text
print(tokenized_text)


# In[5]:


# get ready for word tokenization 
from nltk.tokenize import word_tokenize

# assign tokenized words to variable
tokenized_word = word_tokenize(text)
print(tokenized_word)


# In[6]:


# prepare for frequency distribution
from nltk.probability import FreqDist

# set frequency distribution of words to new variable
fdist = FreqDist(tokenized_word)

# print count
print(fdist)

# show words with the highest frequency, based on integer included the method
fdist.most_common(30)


# In[39]:


# prepare for stopword removal 
from nltk.corpus import stopwords
nltk.download('stopwords')


# In[54]:


stop_words = stopwords.words("english")
stop_words2 = ['.',',','(',')',';','’']

# add punctuation to stopwords
stop_words.extend(stop_words2)

# print list of predetermined stopwords from nltk
print(stop_words)


# In[61]:


# stopword removal from text input
filtered_sent = []

for w in tokenized_word:
    # MIGHT ADD ADDITIONAL WORDSTOP SCRIPT TO BE CALLED HERE
    if w not in stop_words:
        filtered_sent.append(w)

fdist = FreqDist(filtered_sent)

top_words = fdist.most_common(40)
print(top_words)


# In[68]:


# TEST FOR PULLING OUT NOUNS
import nltk
input_lines = """Responsibilities

NBCUniversal’s News Group Digital is creating the digital future for one of the world’s best-known and most-trusted news organizations. Our Digital Technology organization is at the center of building and improving a suite of digital products including user experiences across web, mobile apps, OTT devices, storytelling tools including CMS and curation systems, and a platform to distribute that content to hundreds of millions of users. Our brands include NBC News, Today, MSNBC, CNBC, E! News, and Telemundo Noticias.

We are hiring with remote flexibility in multiple locations where our teams are based: New York, NY; Seattle, WA; Englewood Cliffs, NJ; Universal City, CA.

Position Overview

This is an opportunity to play a critical role in the digital evolution of the NBCUniversal News Group across our entire news portfolio.

As a Software Engineer, you will partner with the Product, Operations, Design, and Editorial teams to bring NBC News Digital content to life. You will be a significant influence on our product roadmap, bringing a technical and strategic perspective. You will work alongside fellow inspired developers in a fast-paced environment using technologies like Sass, React.js and GraphQL to help shape the future of digital news.

This role will report into the Manager of Engineering, Platform Partnerships.

Responsibilities

Work on the React.js codebases supporting subscription experiences
Build out GraphQL queries to consume data for all web properties
Implement beautiful UX for engaging news storytelling
Optimize sites across an array of web-capable devices, browsers and experiences
Automate front end testing to ship the highest quality experience for our audience
Write code and tests that are understandable and maintainable
Debug effectively within their primary area to help find root cause
Provide helpful, timely code reviews
Collaborate professionally with teammates and peers
Communicate with engineering precision, escalating blockers quickly, clarifying requirements and sharing assumptions
Seek understanding of how users interact with product/service
Exhibit a growth mindset and make investments in your growth and teammates’ growth

Qualifications/Requirements

Qualifications/Requirements

3+ years’ experience in software development or related

field(s)

1+ years recent experience with a modern JavaScript

framework (e.g. React.js, Vue.js, Aurelia)

B.S. in Computer Science, Computer Information

Systems, or equivalent industry experience

Strong proficiency in either CSS/Sass development or a

server-side programming language (e.g. Node.js, Go,

Java) in the context of a website

Experience implementing responsive designs using

HTML and a CSS preprocessor (SASS, PostCSS, LESS)

Experience using modular JavaScript, async patterns,

and DOM manipulation

Understanding of bundlers, transpilers and

preprocessors (Webpack, Babel, SASS)

Strong problem-solving skills, logical and creative

thinking

Experience with version control"""
tokenized = nltk.word_tokenize(input_lines)
# print(tokenized)
is_noun = lambda pos: 'NN' in pos[:2]
pos_tagged = [ word.lower() for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos) ]
print(pos_tagged)


# In[69]:


# frequency of nouns
fdist = FreqDist(pos_tagged)

top_words = fdist.most_common(20)
print(top_words)


# In[ ]:




