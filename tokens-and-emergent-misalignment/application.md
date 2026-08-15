# What Tokens Lead to Emergent Misalignment?

Project page: [SPAR project](https://sparai.org/projects/f26/recn72ZNYRMuOGcV4/)

## Question 1

*What do you think is the thing most likely to be wrong or missing from the supplied paper [1]? Maximum 200 words.*

The paper nicely demonstrates that not all training examples are equally harmful in Figure 3. While Figure 5 tries to show the properties of examples that vary in their degree of influence, it would be useful to see representative examples from each category and understand what makes them so different and effective. A word cloud or a low-dimensional projection of the sample embeddings might hint at the differences between the samples.

Another impressive fact about Figure 3 is that the WildGuard and EK-FAC curves have similar qualitative shapes. One is a white-box method based on gradients of the OLMo model, while the other is a black-box method based on tuning the Mistral model [2]. The agreement deserves more study. More specifically, a scatter plot comparing WildGuard's score for a prompt with its EK-FAC score would establish the strength of the relationship.

Another possible confound is that the prompts used to evaluate misalignment are the same examples used to calculate query attribution. It would have been better to use only a subset to calculate the metric and reserve the rest for evaluating misalignment.

## Question 2

*What is the most likely reason for this project not to produce any relevant scientific knowledge? Maximum 100 words.*

The project may fail to produce new scientific knowledge if future work shows that the influential examples simply reinforce an existing misaligned persona. For example, the most influential examples might be those that express an already known harmful persona more strongly, or that have obvious semantic properties such as greater wrongness - “do not wear a seatbelt” versus “drink and drive.” The WildGuard curve in Figure 3 qualitatively resembling the EK-FAC curve may suggest that this is possible.

## Question 3

*If we establish that certain tokens are significantly more influential than others, how would you classify them or find patterns that describe them? Maximum 200 words.*

The first step would be to inspect representative examples from both categories. I would ask whether there is a pattern at the word level or at the semantic level. We can compare token frequency and position as a function of influence on emergent misalignment. A word cloud may provide a useful qualitative comparison. We can also examine a low-dimensional projection of contextual token embeddings to see whether low- and high-influence tokens form clear clusters.

If these experiments reveal no clear pattern, we can begin looking at the model's internal representations. Do the most influential examples align with an existing harmful-persona direction in the model? Could this explain why different models have different influential examples?

## References

[1] [Supplied project paper](https://drive.google.com/file/d/1BwUONlrJeTf1UmhLywXWFjM0I-xa3gtc/)

[2] Exact WildGuard paper/source intended by the draft. **Link needed.**

[3] Exact EK-FAC attribution source, if cited separately from the supplied project paper. **Link needed.**
