#!/usr/bin/env python
# coding: utf-8

# In[17]:


import nltk
import re
import pprint
from nltk import Tree


# In[18]:


patterns = """
    NP: {<JJ>*<NN>+}
    {<JJ>*<NN><CC>*<NN>+}
    """


# In[19]:


NPChunker = nltk.RegexpParser(patterns)


# In[35]:


sample_text = """Responsibilities

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

Experience with version control
"""


# In[22]:


etiquette_excerpt = """If you wish to make yourself agreeable to a lady, turn the conversation adroitly upon taste, or art, or books, or persons, or events of the day.
"""

etiquette_excerpt.split()


# In[23]:


nltk.sent_tokenize(etiquette_excerpt)


# In[24]:


tokenized_sentence = nltk.sent_tokenize(etiquette_excerpt)

[nltk.word_tokenize(sentence) for sentence in tokenized_sentence]


# In[25]:


tokenized_sentence = nltk.sent_tokenize(etiquette_excerpt)

tokenized_words = [nltk.word_tokenize(sentence) for sentence in tokenized_sentence]

[nltk.pos_tag(word) for word in tokenized_words]


# In[26]:


tokenized_sentence = nltk.sent_tokenize(etiquette_excerpt)
tokenized_words = [nltk.word_tokenize(sentence) for sentence in tokenized_sentence]
tagged_words = [nltk.pos_tag(word) for word in tokenized_words]
[NPChunker.parse(word) for word in tagged_words]


# In[27]:


def prepare_text(input):
    tokenized_sentence = nltk.sent_tokenize(input)  # Tokenize the text into sentences.
    tokenized_words = [nltk.word_tokenize(sentence) for sentence in tokenized_sentence]  # Tokenize words in sentences.
    tagged_words = [nltk.pos_tag(word) for word in tokenized_words]  # Tag words for POS in each sentence.
    word_tree = [NPChunker.parse(word) for word in tagged_words]  # Identify NP chunks
    return word_tree  # Return the tagged & chunked sentences.


# In[28]:


prepare_text(sample_text)


# In[29]:


new_patterns = """
    NP:    {<DT><WP><VBP>*<RB>*<VBN><IN><NN>}
           {<NN|NNS|NNP|NNPS><IN>*<NN|NNS|NNP|NNPS>+}
           {<JJ>*<NN|NNS|NNP|NNPS><CC>*<NN|NNS|NNP|NNPS>+}
           {<JJ>*<NN|NNS|NNP|NNPS>+}
           
    """

new_NPChunker = nltk.RegexpParser(new_patterns)

def prepare_text(input):
    tokenized_sentence = nltk.sent_tokenize(input)  # Tokenize the text into sentences.
    tokenized_words = [nltk.word_tokenize(sentence) for sentence in tokenized_sentence]  # Tokenize words in sentences.
    tagged_words = [nltk.pos_tag(word) for word in tokenized_words]  # Tag words for POS in each sentence.
    word_tree = [new_NPChunker.parse(word) for word in tagged_words]  # Identify NP chunks
    return word_tree  # Return the tagged & chunked sentences.


# In[39]:


prepare_text(sample_text)


# In[40]:


sentences = prepare_text(sample_text)

def return_a_list_of_NPs(sentences):
    nps = []  # an empty list in which to NPs will be stored.
    for sent in sentences:
        tree = NPChunker.parse(sent)
        for subtree in tree.subtrees():
            if subtree.label() == 'NP':
                t = subtree
                t = ' '.join(word for word, tag in t.leaves())
                nps.append(t)
    return nps


# In[41]:


return_a_list_of_NPs(sentences)


# In[ ]:




