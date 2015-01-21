Checking Common Data Cleaning & Transformations
================================================

[Data smells](https://source.opennews.org/en-US/learning/distrust-your-data/) and things we've run into before, during and after common data transformations and cleaning

### [Getting to Know Data](https://gist.github.com/auremoser/6d9475e02ea5cd5908e1)

This follows [Aurelia Moser's](https://github.com/auremoser) [work](https://gist.github.com/auremoser/6d9475e02ea5cd5908e1)

* **Who published?**
    * [ ] Just like the sources we interview have motivations, so too do data providers
    * [ ] Advocacy groups
    * [ ] Studies
    * [ ] Trade groups

* **What is the relevant date range?**

* **Is the information current? How often is it updated**

* **What does the data encompass?**

* **How was it compiled?**

* **Ask about the methodology and how calculations were made**
    * [ ] If receiving from a database, ask for a record layout or schema
    * [ ] Ask someone to walk you through the findings

* **What can the data tell you?**

* **What can't the data tell you?**
    * [ ] Spot check everything
    * [ ] Any strange of conflicting values present
    * [ ] Incorrect percentages and calculations
    * [ ] Multiple spellings of people, places and things
    * [ ] Can it be benchmarked against other data sets

* **Stats/Math**
    * [ ] How are numbers contextualized in the representation?
    * [ ] How is the reference point for visual read introduced
        * [ ] Baseline of 0 on charts?
        * [ ] Visual order of the image to suggest legibility
    * [ ] How is math done in the viz?
        * [ ] Are they explicit about % vs. abolute values and how faithfully the #s represent their images
    * [ ] How are outliers, anomalies, awk data points explained/handled?

### Geocoding

* [ ] Examine results for instances of centroids and illogical addresses

    * For instance

            Hollywood & Highland, North Highland Avenue & Hollywood Boulevard, Los Angeles, CA 90028, USA
            Los Angeles River, California, USA
            Los Angeles, CA, USA

### Averaging/Median

.....

### Peforming DB joins

.....