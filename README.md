# What is LDA (Latent-Dirichlet-Allocation) ?

---

* It is a technique used for topic modelling - viewing the documents collection as being *generated* through latent groups called topics.

* It is a **general statistical model**.

* Collection of topics -> Documents (Bag-Of-Words model).
* Collection of words -> Topics

### LDA ASSUMPTIONS :
> * The semantic content of a document is composed of one or more terms from one or more topics.
> * Terms are *ambiguous*, belonging to more than one topic, with different probability. However, inside a document, the surrounding **context-words** *specify* the exact topic the **target-word** is part of.
> * Most documents will contain only a relatively small number of topics. In the collection, individual topics will occur with different frequencies. That is, they have a probability distribution, so that a given document is more likely to contain some topics than others.
> * Within a topic, certain terms will be used much more frequently than the others. The terms within a topic will have their own probability distribution.