#PUSHEEN
=====
The purpose of this web based application is to encourage users to read complex and lengthy documents.


##Document Format
To do so, the documentation owner is supposed to provide a easy-to-read, easy-to-write plain text for the document.
There are three parts(levels) of expected format:

###Title
A title should start with `'#'` notation. More than one title is allowed.

**Example**
```
#Title1
  ...
#Title2
  ...
```

###Sub-Title
A sub-title should start with increasing numbers (starting from 1).

**Example**
```
#Title1
  1. Subtitle 1-1
    ...
  2. Subtitle 1-2
    ...

#Title2
  3. Subtitle 2-1
    ...
```

####Highlight a subtitle
If all of the paragraphs in a sub-title region are important, use '**' notation to sandwish sub-title content.

**Example**
```
1. Normal Subtitle
  ...
2. **Important Subtitle**
  ...
```

###Content
Content is divided into several paragraphs. Each paragraph should start with '-' notation.

**Example**
```
#Title
  1. Subtitle
    - Paragraph1
      ...
    - Paragraph2
      ...
```

####Hightlight whole paragraph
If a paragraph is important, start the paragraph with '*' instead.

**Example**
```
- This is a normal paragraph.
* This is an importment paragraph.
```

####Highlight keywords
If a couple of words are important, they can be sandwiched by '**' notation.

**Example**
```
- This is a normal paragraph with a **keyword**.
- This is a normal paragraph with **some important terms**.
- This is a normal paragraph with **many keywords** and **several critical concepts**.
* This is an importment paragraph with a **keyword**.
```

###URL
URLs can be added on any text. Put target text in `[]` brackets, following target link in `()` parentheses.

**Example**
```
#Title with [link](http://my.url1)
  4. Subtitle with [link](http://my.url2)
    - Content with [link](http://my.url3) and illustartions.
``` 

###Escape notation
In the document, if a normal '*' or '\' character is used, escape them by '\' notation.

**Example**

If you want to present this sentense:
```
"I have * and \ in my document."
```

Use the following instead:
```
"I have \* and \\ in my document."
```

