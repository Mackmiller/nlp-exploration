# Exploration into Natural Language Processing in Python

Gain a better understanding of the capabilities of the Python [Natural Language Toolkit]() library, as well as additional NLP libraries [spaCy](https://spacy.io/), [YAKE](https://pypi.org/project/yake/) and [Rake-Nltk](https://pypi.org/project/rake-nltk/)

## Tech stack

- Python, nltk, spaCy, YAKE, Rake-Nltk

## Summary of findings

- Overall, I ended up being just as happy with the end product of a modified nltk script (see nltk_chunking.py) as I was with the final products from my scripts for the other libraries. My end goal was extracting a list of noun-driven phrases from a technology-focused text input. While I was amazed by the methods of each library, none of them worked as well as I anticipated: My list of phrases had about 60% relevant and logical phrases and 40% nonlogical groupings. This could also partially have to do with my text input specifically pertaining to technology terms. 

## Thoughts on the specific libraries used

- spaCy has superb documentation and many different models to choose from. The medical/science community seems like the primary target audience, but the library also has models based on non-medical articles and posts.

- YAKE had really cool custom features, such as individual keyword size (word count), deduplication threshold, and maximum number of keywords extracted. I really enjoyed seeing how each of these customizations affected the end result.

- Rake-nltk was very similar to SpaCy in terms of performance. I primarily explored .get_ranked_phrases() as a method.

## Sample input

This was the text block I used for my samples. It was a copy/pasted job description from LinkedIn.

```sh
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
```

## Sample output

Based on the above text, desired output of noun groupings generally looked like this across the different libraries:

```sh
(3+ years, 1+ years, JavaScript, Aurelia, B.S., Computer Science, Computer Information

Systems, Node.js, Java, PostCSS, JavaScript, DOM, Webpack, Babel)
```

## Moving forward

- For my specific project idea, with enough time and research, a custom model would need to be created. [this](https://github.com/shivahari/identify-tech-words) was also a cool implimentation of what I was interested in exploring.

## Local deployment

```sh
git clone https://github.com/Mackmiller/nlp-exploration.git
```

- Navigate to the repo folder

```sh
cd nlp-exploration
```

- make sure latest version of Python is installed

```sh
brew install python3
```

- verify that pip3, a Python3 package installer, is installed and up-to-date

```sh
pip3 --version
```

- install iPython

```sh
pip3 install ipython
```

- verify the installation

```sh
ipython --version
```

- Note: libraries imported into each script need to be downloaded into your local environment before use. Each of the library sites listed above include import instructions.

- Once everything has been installed, script can be run via terminal within the local directory by running 

```sh
python3 <file name here>
```