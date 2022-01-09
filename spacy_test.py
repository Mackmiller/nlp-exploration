import spacy
nlp = spacy.load('en_core_web_sm')
# text = """spaCy is an open-source software library for advanced natural language processing, 
# written in the programming languages Python and Cython. The library is published under the MIT license
# and its main developers are Matthew Honnibal and Ines Montani, the founders of the software company Explosion."""
text = """Work on the React.js codebases supporting subscription experiences
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

# doc = nlp(text)
# assert doc.has_annotation("SENT_START")
# for sent in doc.sents:
#     print(sent.text)

# tokenization
doc = nlp(text)
# for token in doc:
#     print(token.text)

# relation to real world
print(doc.ents)
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)