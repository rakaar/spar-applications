# What Tokens Lead to Emergent Misalignment?

Project page: [SPAR project](https://sparai.org/projects/f26/recn72ZNYRMuOGcV4/)

Mentor: Gonçalo Paulo

Applicant name: Raghavendra Kaushik Archak

## Question 1

*What do you think is the thing most likely to be wrong or missing from the supplied paper [1]? Maximum 200 words.*

The paper nicely demonstrates the fact that all training examples are not equally harmful(Fig 3). While figure 5 tries to show the properties of examples that vary the degree of influence, it would be nice to see some representative examples in a each category, about what makes them so different and effective. A word cloud or may be low dimensional projection of embeddings of the samples might try to hint at the difference in the samples.

Another impressive fact about figure 3 is that the Wildguard curve and the EK-FAC curve produce a similar qualitative curve. One of them is white box method obtained by gradients of the OLMO model while the other is a black box method obtained from tuning the Mistral model [2]. The agreement deserves more study. More specifically, a scatter plot between Wildguard’s scoring of a prompt and EK-FAC score will establish the strength of the result.

Another possibly confounding result is the prompts used to evaluate misalignment are the same examples that were used to calculate the query attribution. But it would have been nice if only a subset of them were used to calculate metric while the rest to evaluate misalignment.

## Question 2

*What is the most likely reason for this project not to produce any relevant scientific knowledge? Maximum 100 words.*

The project may fail to produce new scientific knowledge if future work shows that the influential examples simply reinforce an existing misaligned persona. For example, the most influential examples might be those that express an already known harmful persona more strongly, or that have obvious semantic properties such as greater wrongness - “do not wear a seatbelt” versus “drink and drive.” The WildGuard curve in Figure 3 qualitatively resembling the EK-FAC curve may suggest that this is possible.

## Question 3

*If we establish that certain tokens are significantly more influential than others, how would you classify them or find patterns that describe them? Maximum 200 words.*

The first step would be to inspect representative examples from both categories. I would ask whether there is a pattern at the word level or at the semantic level. We can compare token frequency and position as a function of influence on emergent misalignment. A word cloud may provide a useful qualitative comparison. We can also examine a low-dimensional projection of contextual token embeddings to see whether low- and high-influence tokens form clear clusters.

If these experiments reveal no clear pattern, we can begin looking at the model's internal representations. Do the most influential examples align with an existing harmful-persona direction in the model? Could this explain why different models have different influential examples?

## References

[1] [Supplied project paper](https://drive.google.com/file/d/1BwUONlrJeTf1UmhLywXWFjM0I-xa3gtc/)

[2] Han et al., “WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs.” [arXiv](https://arxiv.org/abs/2406.18495)
