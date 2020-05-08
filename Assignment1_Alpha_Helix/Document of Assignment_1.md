## Document of Assignment_1

#### 1. Generate unified_data_file:

> **Notice**: The "unified_data_file.json"  have been already generated and stored in the folder ".\Assignment1_Alpha_Helix\data".

Run **Generate_Unified_Data.py** in command prompt (of windows):

1. Step: Use command 'cd file_path' to go to the folder: "".\Assignment1_Alpha_Helix\code\" .

2. Step: Use the following command line to run the file "Generate_Unified_Data.py"

   \> python Generate_Unified_Data.py

After these two steps, the "unified_data_file.json" will be generated.

#### 2. Approach to compute the 10 most specific words of argument units

> **Notice:** There are three kinds of argument unit: major claim, claim and premise. Our approach is the same for the three sorts of argument unit.  

Firstly we define what a specific word of an argument unit is: 

**A word is called specific in an argument unit, if this word is only in this argument unit but not in others**

For example, we have two argument units:

1. $word_1\ \ word_2\ \ word_x$
2.  $word_y\ \ word_1\ \ word_2$

According to our definition: $word_x$ is the specific word of the first unit, and $word_y$ is the specific word of the second unit.

Secondly we define what specific-words-set  of argument units is:

**Specific-words-set is a set of words, it contains the words which are specific words of  argument units .**

For example, we have the same argument units mentioned above. The specific-words-set of this example is: $\{word_x,\ \  word_y\}$. 

**Description of Approach for one kind of Argument Units:** 

1. Step: Compute the specific-words-set of all argument units.

   After the first step we get a specific-words-set, it could contain a large number of words. We want to remain the words that more meet the essays' topics, so go to the second step.

2. Step: Extract all topics of essays and compute the specific-words-set of all topics.

3. Step: Computer the intersection set between specific-words-set of argument units and specific-words-set of topics. This intersection set is the candidate-set of most specific words of argument units.

4. Random 10 words from the candidate-set.