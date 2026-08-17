# Representation Diagnostics for LLM Safety

Project page: [SPAR project](https://sparai.org/projects/f26/rec4NRAGVuLATiWpd/)

Mentors: Sandy Tanwisuth and Mohan Gupta

Applicant name: Raghavendra Kaushik Archak

Track represented by the current draft: engineering / empirical diagnosis.

## Question 1 - Prior Work

*Link to one piece of work that best represents you as a researcher and collaborator. Explain your contribution, how your thinking or approach changed during the project, and what the work reveals about how you conduct research and would contribute to this project. Clearly distinguish your role in collaborative work, explain why you chose to undertake that prior project, and describe how your research practices would transfer to this project. Maximum 300 words.*

As an independent side project, I recently worked on Bau lab’s April challenge [1] which asks you to reverse engineer a toy transformer that can find a maximum of 5 numbers. I found that more attention matrices are recruited to tweak the maximum response, and that the model’s operations can be interpreted as a low dimensional computation. This project helped me exercise thinking about internal matrix operations in a transformer block.

My approach and how I conduct research:

These are the research skills that I learnt over my ~4 years of working in neuroscience

- Before I write code, I try to make things clear first on paper to get an intuition of how my outputs should be. For example, in this project, writing out each of the weight matrices, made it clear that it is enough to look only at the last row of attention matrices.
- Before testing out any immediate hypothesis, I try to look at raw data to get a sense of what is in the raw data. Like here, embedding and unembedding norms, individual weight matrices, seeing attention patterns for different groups of examples.
- The most valuable skill I learned in my lab is the process of hypothesis testing. Once I look at raw data, I start with the simplest hypothesis that I wish would be true. Check for correlative evidence first. If it exists, then test for causal manipulation. If it works, then test for as many alternate hypothesis as you can [2].

How I can contribute:

Alongside the scientific methodology, I have done a good amount of programming and maths in my past projects. From neuroscience, I have been habituated to think about computation in low dimensional spaces, which is closely related to the representations related to refusal or compliance in the model’s activity for this project.

## Question 2 - Engineering and Empirical Diagnosis

*You are replicating prior work on internal activation directions in LLMs. You successfully recover a published “refusal direction”: responses classified as refusal tend to have higher projections onto the direction than responses classified as compliance. However, when you evaluate a broader behavioral taxonomy, you find substantial overlap between refusal and several other policies, including clarification, safe help, hierarchy preservation, and source isolation. Before concluding that this direction mechanistically represents refusal, how would you investigate what information it encodes and whether it contains other behaviorally relevant structure? Describe what you would examine first, the main competing interpretations you would consider, and how different possible findings would change your interpretation of the direction. Maximum 500 words.*

The key problem is that the behavior underlying six behavioral taxonomies is not mutually exclusive. While compliance and refusal are clear opposites of each other, there can be confusion when you consider other labels. For example, if the model refuses to a question, is it because it thought it is unsafe or did the system prompt contained a explicit instruction to not answer such queries. If we want to look at representations inside the model, and we find a direction, is it for refusal or hierarchy preservation.

To test such cases, one would have to design prompts which can disambiguate. For example

- (a) Prompt saying answer in french. The model would happily respond(compliance)
- (b) Prompt with system instruction saying always respond in english even if asked to do in other languages. And user instructions says “answer in french”

In case of (b), if the model doesn’t answer in french, then we can find a direction that differentiates compliance and hierarchy preservation. Of course, there is a confounding factor that the direction could be French. But such problems can be dealt with by having counter balancing examples, where French and English can be interchanged. Also, averaging across many prompts should cancel out such detailed prompt related directions.

But the challenge is, one can come up with multiple such pairs. Another possibility could be to collect activations related to all behavioral taxonomies, and find a low dimensional subspace where the the activations can be separated maximally using multiclass-LDA. And then the obtained directions could be tested in the same way as [3]. - check activation correlation with prompt(figure 5) and use causal manipulative methods like direction ablation to see if the behavior separates the effects(figure 1)

Now, there could be a possibility that we may not be able to find a subspace that maximally can differentiate six taxonomies. But before concluding the representations for different behavioral taxonomies overlap, we also have to test with non-linear methods. Recent methods like J-space [4] also give a chance to look at model internals for individual examples, and give an insight at what intermediate computations led to the model's response.

## Process Note

- **I was initially confused by cases that seemed to fit more than one behavioral category, especially source isolation and hierarchy preservation.**
- **Both may result in the model continuing to follow the system prompt, but for different reasons: hierarchy preservation resolves a conflict between instructions at user level vs system level, whereas source isolation recognizes that the text inside retrieved documents is data rather than instruction.**
- **Both can be considered as a consequence of “respecting system prompt” above all else.**

## References

[1] Archak, “Reverse Engineering a Max-of-Five Transformer,” Bau Lab April Challenge. [Project results](https://rakaar.github.io/april-2026-max-of-list-mech-interp/main-results/)

[2] Gershman, “How to Never Be Wrong,” on auxiliary hypotheses and explaining away disconfirmation. [PubMed](https://pubmed.ncbi.nlm.nih.gov/29799092/)

[3] Arditi et al., “Refusal in Language Models Is Mediated by a Single Direction.” [arXiv](https://arxiv.org/abs/2406.11717)

[4] Lindsey et al., “Verbalizable Representations Form a Global Workspace in Language Models.” [Transformer Circuits](https://transformer-circuits.pub/2026/workspace/index.html)

[5] [SPAR 2026 Representation Diagnostics Mentee Questions](https://docs.google.com/document/d/1QSMaGd9ezmsSuw22GdsSfX-SztDumAQRoBtyz-G9daU/)
