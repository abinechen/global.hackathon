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
`#Title1`
  ...
`#Title2`
...
```

###Sub-Title
A sub-title should start with numbers (starting from 1).

**Example**
```
`#Title1`
  `1. Subtitle1`
    ...
  `2. Subtitle2`
    ...

`#Title2`
  `1. Subtitle1`
    ...
```

###Content
Content is divided into several paragraphs. Each paragraph should start with '-' notation.

**Example**
```
`#Title`
  `1. Subtitle1`
    `- Paragraph1`
    `- Paragraph2`
    ...
```
-----

In addition to the above, we provide two types of highlight notation.

##Hightlight whole paragraph
  - If a paragraph is important, start the paragraph with '*' instead.

  **Example**
  ```
  `- This is a normal paragraph.`
  `* This is an importment paragraph.`
  ```

  - If a couple of words are important, they can be sandwiched by '**' notation.

  **Example**
  ```
  `- This is a normal paragraph with a **keyword**.`
  `- This is a normal paragraph with **some important terms**.`
  `- This is a normal paragraph with **many keywords** and **several critical concepts**.`
  `* This is an importment paragraph with a **keyword**.`
  ```

##Escape notation
In the document, if a normal '*' or '\' character is used, escape them by '\' notation.

**Example**
If you want to present this sentense:
"There is a * and \ in my document."

Use the following instead:
"There is a \* and \\ in my document."

