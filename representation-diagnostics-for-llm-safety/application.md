# Representation Diagnostics for LLM Safety

Project page: [SPAR project](https://sparai.org/projects/f26/rec4NRAGVuLATiWpd/)

Track represented by the current draft: engineering / empirical diagnosis.

## Question 1 - Prior Work

*Link to one piece of work that best represents you as a researcher and collaborator. Explain your contribution, how your thinking or approach changed during the project, and what the work reveals about how you conduct research and would contribute to this project. Clearly distinguish your role in collaborative work, explain why you chose to undertake that prior project, and describe how your research practices would transfer to this project. Maximum 300 words.*

As an independent side project, I recently worked on Bau Lab's April Challenge [1], which asks you to reverse engineer a toy transformer that can find the maximum of five numbers. I found that more attention matrices are recruited to tweak the maximum response, and that the model's operations can be interpreted as a low-dimensional computation. This project helped me exercise thinking about internal matrix operations in a transformer block.

My approach and how I conduct research:

These are the research skills that I learnt over my approximately four years of working in neuroscience:

- Before I write code, I try to make things clear first on paper to get an intuition of what my outputs should be. For example, in this project, writing out each of the weight matrices made it clear that it is enough to look only at the last row of the attention matrices.
- Before testing any immediate hypothesis, I try to look at raw data to get a sense of what is in it. Here, that included embedding and unembedding norms, individual weight matrices, and attention patterns for different groups of examples.
- The most valuable skill I learned in my lab is the process of hypothesis testing. Once I look at raw data, I start with the simplest hypothesis that I wish would be true. I check for correlative evidence first [2]. If it exists, I test a causal manipulation. If it works, I test as many alternative hypotheses as I can [3].

How I can contribute:

Alongside the scientific methodology, I have done a good amount of programming and maths in my past projects. From neuroscience, I have been habituated to think about computation in low-dimensional spaces, which is closely related to representations of refusal or compliance in the model's activity for this project.

## Question 2 - Engineering and Empirical Diagnosis

*You are replicating prior work on internal activation directions in LLMs. You successfully recover a published “refusal direction”: responses classified as refusal tend to have higher projections onto the direction than responses classified as compliance. However, when you evaluate a broader behavioral taxonomy, you find substantial overlap between refusal and several other policies, including clarification, safe help, hierarchy preservation, and source isolation. Before concluding that this direction mechanistically represents refusal, how would you investigate what information it encodes and whether it contains other behaviorally relevant structure? Describe what you would examine first, the main competing interpretations you would consider, and how different possible findings would change your interpretation of the direction. Maximum 500 words.*

The key problem is that the behaviors underlying the six behavioral taxonomies are not mutually exclusive. While compliance and refusal are clear opposites, there can be confusion when considering other labels. For example, if the model refuses a question, is it because it thought the request was unsafe, or because the system prompt contained an explicit instruction not to answer such queries? If we look at representations inside the model and find a direction, is it a direction for refusal or for hierarchy preservation?

To test such cases, one would have to design prompts that disambiguate the possibilities. For example:

- A prompt says “answer in French.” The model would happily respond, demonstrating compliance.
- A system instruction says always respond in English even if asked to use another language, while the user instruction says “answer in French.”

In the second case, if the model does not answer in French, we can find a direction that differentiates compliance from hierarchy preservation. There is a confound that the direction could instead encode French. This can be addressed with counterbalanced examples in which French and English are interchanged. Averaging across many prompts should also cancel out detailed prompt-related directions.

The challenge is that one can construct many such pairs. Another possibility is to collect activations related to all behavioral taxonomies and find a low-dimensional subspace in which the activations can be separated maximally using multiclass LDA. The obtained directions could then be tested in the same way as the published refusal direction [4]: check activation correlation with the prompt and use causal manipulations such as directional ablation to see whether the behavioral effects separate.

It may be impossible to find a subspace that maximally differentiates all six taxonomies. Before concluding that the representations overlap, however, we should also test nonlinear methods. Recent methods such as J-space [5] offer a way to inspect model internals for individual examples and may reveal which intermediate computations led to the model's response.

## Question 3 - Causal Abstraction (Optional Alternative Track)

*Using Beyond Refusal and the framework of causal abstraction from Geiger et al., propose a high-level mechanistic account in which prompt context changes behavior by changing the safety task the model selects; a substantively different account that could produce the same observed behavior without representing task selection in that way; and one interchange intervention that could distinguish the accounts. Specify the source and base conditions, what internal state you would intervene on, and the result predicted by each account. Maximum 500 words.*

**Draft status:** The source response tab contains only `XXXXXX`. No substantive answer has been drafted.

## Process Note

**Draft status:** The application instructions require a short process note describing one uncertainty or change of mind. This note was not present in the source document.

## References

[1] Bau Lab April Challenge project or work sample. **Link needed.**

[2] Source supporting the correlational-to-causal research workflow. **Link needed.**

[3] Source supporting systematic testing of alternative hypotheses. **Link needed.**

[4] Arditi et al., “Refusal Is Mediated by a Single Direction.” [Available project-context link](https://www.lesswrong.com/posts/jGuXSZgv6qfdhMCuJ/refusal-in-llms-is-mediated-by-a-single-direction)

[5] J-space / Jacobian-lens source. **Link needed.**

[6] [SPAR 2026 Representation Diagnostics Mentee Questions](https://docs.google.com/document/d/1QSMaGd9ezmsSuw22GdsSfX-SztDumAQRoBtyz-G9daU/)
